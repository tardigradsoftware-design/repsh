#!/usr/bin/env node
// scripts/update/refresh-metadata.js
// GitHub API kullanarak registry kayıtlarının yıldız, son commit, lisans, archived
// ve release bilgilerini günceller. Çalıştırmadan önce GH_TOKEN tanımlı olmalı.
//
// Kullanım: node scripts/update/refresh-metadata.js [--dry-run] [--expired-only]
//
// Not: Bu script dosyayı yerinde günceller; öncesinde commit'li olun.
const fs = require('fs');
const path = require('path');
const https = require('https');
const yaml = require('js-yaml');

const ROOT = path.resolve(__dirname, '../..');
const args = new Set(process.argv.slice(2));
const DRY_RUN = args.has('--dry-run');
const EXPIRED_ONLY = args.has('--expired-only');
const TODAY = new Date().toISOString().slice(0, 10);

function ghApi(urlPath) {
  return new Promise((resolve, reject) => {
    const req = https.request({
      hostname: 'api.github.com',
      path: urlPath,
      headers: { 'User-Agent': 'repsh-kb/1.0', ...(process.env.GH_TOKEN ? { Authorization: `token ${process.env.GH_TOKEN}` } : {}) }
    }, res => {
      let body = '';
      res.on('data', c => body += c);
      res.on('end', () => {
        if (res.statusCode === 403 && res.headers['x-ratelimit-remaining'] === '0') {
          const reset = new Date(Number(res.headers['x-ratelimit-reset']) * 1000);
          return reject(new Error(`Rate limited; reset at ${reset}`);
        }
        if (res.statusCode !== 200) return reject(new Error(`HTTP ${res.statusCode} for ${urlPath}`));
        try { resolve(JSON.parse(body)); } catch(e) { reject(e); }
      });
    });
    req.on('error', reject);
    req.end();
  });
}

async function fetchRepo(repo) {
  const [owner, name] = repo.split('/');
  const data = await ghApi(`/repos/${owner}/${name}`);
  let release = null;
  try { release = await ghApi(`/repos/${owner}/${name}/releases/latest`); } catch {}
  return {
    stars: data.stargazers_count,
    archived: data.archived,
    pushed_at: data.pushed_at,
    license: (data.license && data.license.spdx_id) || 'no-license',
    latest_release: release ? release.tag_name : null,
    latest_release_at: release ? release.published_at : null,
  };
}

function parseRepoFromUrl(url) {
  if (!url) return null;
  const m = url.match(/^https:\/\/github\.com\/([^/]+\/[^/#?]+)/);
  if (!m) return null;
  let repo = m[1].replace(/\.git$/, '');
  if (repo.endsWith('/')) repo = repo.slice(0, -1);
  return repo;
}

function listExpired(entries) {
  const out = [];
  for (const e of entries) {
    if (!e.expires_at) continue;
    if (new Date(e.expires_at) < new Date(TODAY)) out.push(e.id);
  }
  return out;
}

async function processFile(relPath) {
  const fp = path.join(ROOT, relPath);
  const src = fs.readFileSync(fp, 'utf8');
  const data = yaml.load(src);
  if (!Array.isArray(data)) return { file: relPath, updated: 0 };
  let updated = 0;
  for (const entry of data) {
    if (EXPIRED_ONLY && entry.expires_at && new Date(entry.expires_at) >= new Date(TODAY)) continue;
    const repo = parseRepoFromUrl(entry.url);
    if (!repo) continue;
    try {
      const meta = await fetchRepo(repo);
      entry.stars = meta.stars;
      entry.stars_checked_at = TODAY;
      entry.last_commit = meta.pushed_at ? meta.pushed_at.slice(0,10) : entry.last_commit;
      entry.license = meta.license === 'NOASSERTION' ? entry.license || 'no-license' : meta.license;
      if (meta.latest_release) entry.latest_release = meta.latest_release;
      if (meta.latest_release_at) entry.latest_release_at = meta.latest_release_at;
      if (meta.archived && entry.status !== 'ARCHIVED') entry.status = 'ARCHIVED';
      entry.verified_at = TODAY;
      updated++;
      console.log(`  ✓ ${entry.id}: ⭐${meta.stars} pushed=${meta.pushed_at.slice(0,10)}`);
    } catch(e) {
      console.log(`  ✗ ${entry.id}: ${e.message}`);
    }
    await new Promise(r => setTimeout(r, 300));  // rate limit nezaket
  }
  if (!DRY_RUN && updated) {
    fs.writeFileSync(fp, yaml.dump(data, { lineWidth: 120, noRefs: true }) );
  }
  return { file: relPath, updated };
}

(async () => {
  const files = ['registry/repositories.yaml'];
  for (const f of files) {
    console.log(`Processing ${f} (dryRun=${DRY_RUN}, expiredOnly=${EXPIRED_ONLY})`);
    const r = await processFile(f);
    console.log(`  → ${r.updated} kayıt güncellendi\n`);
  }
  // Ek olarak expires_at geçen kayıtların listesini göster
  console.log('\n=== Süresi geçmiş kayıtlar ===');
  for (const f of ['repositories','sources','frameworks','tools','papers','mcp-servers']) {
    const data = yaml.load(fs.readFileSync(path.join(ROOT,'registry',f+'.yaml'),'utf8'));
    const ex = listExpired(data);
    if (ex.length) console.log(`${f}: ${ex.length} adet → ${ex.join(', ')}`);
  }
})().catch(err => { console.error(err); process.exit(1); });
