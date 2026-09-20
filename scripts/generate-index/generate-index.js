#!/usr/bin/env node
// index.json ve index.md üretir. Çalıştırmak: `npm run index` veya `node scripts/generate-index/generate-index.js`
const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

const ROOT = path.resolve(__dirname, '../..');

function findSkills() {
  const dir = path.join(ROOT, 'skills');
  return fs.readdirSync(dir).filter(n => {
    const p = path.join(dir, n, 'SKILL.md');
    return fs.existsSync(p);
  }).map(n => {
    const content = fs.readFileSync(path.join(dir, n, 'SKILL.md'), 'utf8');
    const fm = content.match(/^---\n([\s\S]*?)\n---/);
    let meta = {};
    if (fm) {
      fm[1].split('\n').forEach(line => {
        const m = line.match(/^([\w-]+):\s*(.*)$/);
        if (m) {
          let val = m[2].trim();
          if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
            val = val.slice(1, -1);
          }
          meta[m[1]] = val;
        }
      });
    }
    return { id: n, title: n, category: meta.category, status: meta.status, description: meta.description };
  });
}

function findMarkdowns(dirName) {
  const dir = path.join(ROOT, dirName);
  if (!fs.existsSync(dir)) return [];
  const out = [];
  function walk(d, prefix = '') {
    for (const n of fs.readdirSync(d)) {
      const p = path.join(d, n);
      const stat = fs.statSync(p);
      const rel = prefix + n;
      if (stat.isDirectory()) walk(p, rel + '/');
      else if (n.endsWith('.md')) out.push({ id: rel.replace(/\.md$/, ''), path: dirName + '/' + rel });
    }
  }
  walk(dir);
  return out;
}

const data = {
  generated_at: new Date().toISOString(),
  skills: findSkills(),
  playbooks: findMarkdowns('playbooks'),
  patterns: findMarkdowns('patterns'),
  anti_patterns: findMarkdowns('anti-patterns'),
  decisions: findMarkdowns('decisions'),
  stacks: findMarkdowns('stacks'),
};

fs.mkdirSync(path.join(ROOT, 'indexes'), { recursive: true });
fs.writeFileSync(path.join(ROOT, 'indexes/index.json'), JSON.stringify(data, null, 2));

// index.md
const md = [];
md.push('# Index\n');
md.push(`_Generated: ${data.generated_at}_\n`);
md.push('## Skills\n');
for (const s of data.skills) md.push(`- **${s.id}** [${s.category || '-'} / ${s.status || '-'}] — ${s.description || ''}`);
md.push('\n## Playbooks\n');
for (const p of data.playbooks) md.push(`- [${p.id}](${p.path})`);
md.push('\n## Patterns\n');
for (const p of data.patterns) md.push(`- [${p.id}](${p.path})`);
md.push('\n## Anti-patterns\n');
for (const p of data.anti_patterns) md.push(`- [${p.id}](${p.path})`);
md.push('\n## Decisions\n');
for (const p of data.decisions) md.push(`- [${p.id}](${p.path})`);
md.push('\n## Stacks\n');
for (const p of data.stacks) md.push(`- [${p.id}](${p.path})`);

fs.writeFileSync(path.join(ROOT, 'indexes/index.md'), md.join('\n') + '\n');
console.log(`Wrote indexes/index.json and indexes/index.md (${data.skills.length} skills, ${data.playbooks.length} playbooks)`);
