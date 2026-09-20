#!/usr/bin/env node
// scripts/validate/check-links.js
// Markdown dosyalarındaki http/https linklerini kontrol eder. 3 tekrar deneme ile
// false-positive azaltır. Kırık linkleri raporlar.
//
// Kullanım: node scripts/validate/check-links.js [--json]
const fs = require('fs');
const path = require('path');
const https = require('https');
const http = require('http');

const ROOT = path.resolve(__dirname, '../..');
const args = new Set(process.argv.slice(2));
const JSON_OUT = args.has('--json');
const RETRIES = 2;
const TIMEOUT_MS = 8000;
const ALLOW_REDIRECTS = true;
const CONCURRENCY = 8;

const SKIP = [
  /^https?:\/\/localhost/i,
  /^https?:\/\/127\./,
  /^https?:\/\/0\.0\.0\.0/,
  /example\.com/,
  /acme\.com/i,
];

function walk(dir, exts, ignore = ['node_modules','.git','.next','dist','build']) {
  const out = [];
  for (const n of fs.readdirSync(dir)) {
    if (ignore.includes(n)) continue;
    const p = path.join(dir, n);
    const s = fs.statSync(p);
    if (s.isDirectory()) out.push(...walk(p, exts, ignore));
    else if (exts.some(e => n.endsWith(e))) out.push(p);
  }
  return out;
}

function extractLinks(md) {
  // [text](url) ve doğrudan http://... yakalar; kapanan parantez/boşlukları ayıklar.
  const links = new Set();
  const re = /\[[^\]]*\]\((https?:\/\/[^)\s]+)\)|(?:^|\s)(https?:\/\/[^\s)]+)/g;
  let m;
  while ((m = re.exec(md))) {
    const url = (m[1] || m[2]).replace(/[.,;!?]$/, '');
    if (SKIP.some(r => r.test(url))) continue;
    links.add(url);
  }
  return [...links];
}

function checkOne(url, attempt = 0) {
  return new Promise(resolve => {
    const lib = url.startsWith('https://') ? https : http;
    const req = lib.get(url, {
      timeout: TIMEOUT_MS,
      headers: { 'User-Agent': 'repsh-link-checker/1.0', Accept: 'text/html,*/*' },
      followRedirects: ALLOW_REDIRECTS,
    }, res => {
      // 2xx/3xx başarı; 429 rate limit, 5xx geçici hata → tekrar dene
      const s = res.statusCode;
      res.resume();
      if (s >= 200 && s < 400) return resolve({ url, ok: true, status: s });
      if ((s === 429 || s >= 500) && attempt < RETRIES) {
        return setTimeout(() => checkOne(url, attempt+1).then(resolve), 1500*(attempt+1));
      }
      resolve({ url, ok: false, status: s });
    });
    req.on('error', () => {
      if (attempt < RETRIES) return setTimeout(() => checkOne(url, attempt+1).then(resolve), 1500*(attempt+1));
      resolve({ url, ok: false, status: 'ERR' });
    });
    req.on('timeout', () => { req.destroy(); });
  });
}

async function pool(items, worker, concurrency) {
  const results = [];
  let idx = 0;
  const workers = Array.from({length: Math.min(concurrency, items.length)}, async () => {
    while (idx < items.length) {
      const i = idx++;
      results[i] = await worker(items[i]);
    }
  });
  await Promise.all(workers);
  return results;
}

(async () => {
  const files = walk(ROOT, ['.md','.yaml','.yml']);
  const all = new Map();
  const fileLinkMap = new Map();
  for (const f of files) {
    const rel = path.relative(ROOT, f);
    const src = fs.readFileSync(f,'utf8');
    const links = extractLinks(src);
    fileLinkMap.set(rel, links);
    for (const l of links) all.set(l, (all.get(l)||[]).concat(rel));
  }
  const urls = [...all.keys()];
  console.log(`Toplam ${urls.length} eşsiz link, ${files.length} dosya...\n`);
  const results = await pool(urls, checkOne, CONCURRENCY);
  const broken = results.filter(r => !r.ok);
  if (JSON_OUT) {
    console.log(JSON.stringify({ total: urls.length, broken }, null, 2));
  } else {
    console.log(`\n=== Sonuç: ${urls.length-broken.length}/${urls.length} geçerli ===`);
    for (const r of broken) {
      console.log(`HATA [${r.status}] ${r.url}`);
      for (const file of all.get(r.url)) console.log(`   ↳ ${file}`);
    }
  }
  process.exit(broken.length > 10 ? 1 : 0);   // Çok kırık var ise hata; tekil 403 için kırılgan olma
})();
