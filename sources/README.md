# Sources

Provenance layer. Raw GitHub API snapshots: `../metadata/raw/`. Repo records: `../repositories/` (each cites its API snapshot date). Papers/blogs/discussions get records here as they're ingested (schema: schemas/source.schema.json).

## Research archive convention

Timestamped research outputs (comparison notes, verification runs, eval snapshots) may live in `sources/research/YYYY/MM/`:
- One file per research session: `YYYY-MM-DD-topic.md`
- Frontmatter: question, method, sources consulted (with verification dates), conclusion + confidence
- Findings that graduate to permanent knowledge get promoted into `knowledge/` (deduplicated, with backlinks) — the archive is the raw trail, knowledge/ is the curated layer
- Old archive entries are never deleted (provenance), only linked forward when superseded
