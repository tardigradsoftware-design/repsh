#!/usr/bin/env node
// Temel doğrulama: YAML parse, skill frontmatter zorunlu alanlar, kırık dosya referansı, kaba secret kontrolü.
const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

const ROOT = path.resolve(__dirname, '../..');
const errors = [];
const warnings = [];

function addError(msg, loc) { errors.push(`ERROR [${loc}]: ${msg}`); }
function addWarn(msg, loc) { warnings.push(`WARN [${loc}]: ${msg}`); }

// 1. Her skill için SKILL.md ve test-cases.md var mı, frontmatter parse oluyor mu, zorunlu alanlar tam mı?
const skillsDir = path.join(ROOT, 'skills');
if (fs.existsSync(skillsDir)) {
  const skillReq = ['name','version','description','category','status','confidence','updated'];
  for (const n of fs.readdirSync(skillsDir)) {
    const dir = path.join(skillsDir, n);
    if (!fs.statSync(dir).isDirectory()) continue;
    const sk = path.join(dir, 'SKILL.md');
    const tc = path.join(dir, 'tests', 'test-cases.md');
    if (!fs.existsSync(sk)) addError('SKILL.md eksik', n);
    if (!fs.existsSync(tc)) addError('tests/test-cases.md eksik', n);
    if (fs.existsSync(sk)) {
      const content = fs.readFileSync(sk, 'utf8');
      const m = content.match(/^---\n([\s\S]*?)\n---/);
      if (!m) { addError('Frontmatter yok', n); continue; }
      try {
        const fm = yaml.load(m[1]);
        for (const k of skillReq) if (!(k in fm)) addError(`frontmatter alanı eksik: ${k}`, n);
        if (fm.name && fm.name !== n) addError(`frontmatter name "${fm.name}" klasör adı "${n}" ile uyuşmuyor`, n);
      } catch(e) { addError('frontmatter YAML parse hatası: '+e.message, n); }
    }
  }
}

// 2. Registry YAML dosyaları parse oluyor mu?
['repositories.yaml','sources.yaml','frameworks.yaml','tools.yaml','papers.yaml','mcp-servers.yaml']
  .forEach(f => {
    const p = path.join(ROOT, 'registry', f);
    if (!fs.existsSync(p)) return addError(`${f} yok`, 'registry');
    try {
      const data = yaml.load(fs.readFileSync(p,'utf8'));
      if (!Array.isArray(data)) addError('Array bekleniyor', f);
      else {
        const ids = new Set();
        for (const e of data) {
          for (const k of ['id','title','type','url','status','summary','verified_at']) {
            if (!(k in e)) addError(`alan eksik: ${k} (id=${e.id || '?'})`, f);
          }
          if (ids.has(e.id)) addError(`duplicate id: ${e.id}`, f);
          ids.add(e.id);
        }
      }
    } catch(e) { addError('YAML parse hatası: '+e.message, f); }
  });

// 3. Kaba secret taraması (basit pattern)
const SECRET_PATTERNS = [
  { name: 'Supabase Service Role Key', re: /(supabase[\w_-]*service[\w_-]*role[\w_-]*key|eyJ[a-zA-Z0-9_-]{60,})/i },
  { name: 'OpenAI/benzer API key', re: /sk-[a-zA-Z0-9]{32,}/ },
  { name: 'AWS access key', re: /AKIA[0-9A-Z]{16}/ },
  { name: 'Generic secret pair', re: /(?:password|secret|token|apikey|api_key)\s*[:=]\s*['"][^'"\s]{8,}['"]/i },
];
function walk(d, ignore = ['node_modules','.git','.next','dist']) {
  const results = [];
  for (const n of fs.readdirSync(d)) {
    if (ignore.includes(n)) continue;
    const p = path.join(d, n);
    const stat = fs.statSync(p);
    if (stat.isDirectory()) results.push(...walk(p, ignore));
    else if (/\.(js|ts|jsx|tsx|json|md|env|yaml|yml|sh)$/i.test(n)) results.push(p);
  }
  return results;
}
// Sadece son commit'lerde eklenen dosyalarda kabaca tara (zaman kısıtlı: tüm dosyayı değil son commit'teki değişiklikleri)
// Burada basitlik için proje içindeki source dosyaları tarıyoruz ama .env hariç
for (const f of walk(ROOT)) {
  const rel = path.relative(ROOT, f);
  if (rel.startsWith('.git') || rel.startsWith('.next') || rel.includes('node_modules')) continue;
  const c = fs.readFileSync(f, 'utf8');
  for (const pat of SECRET_PATTERNS) {
    if (pat.re.test(c)) {
      // .env.example ve dokümantasyondaki örnekler için yalancı pozitif filtre
      if (f.endsWith('.env.example') || rel.includes('README') || rel.includes('SECURITY.md') ||
          rel.includes('validate.js') || rel.includes('patterns/') || rel.includes('anti-patterns/')) continue;
      addWarn(`Potansiyel secret (${pat.name})`, rel);
    }
  }
}

// Sonuç
console.log(`\n=== Validation results ===`);
console.log(`Errors: ${errors.length}, Warnings: ${warnings.length}`);
errors.forEach(e => console.log(e));
warnings.slice(0,20).forEach(w => console.log(w));
if (warnings.length > 20) console.log(`... ve ${warnings.length-20} ek uyarı`);
process.exit(errors.length ? 1 : 0);
