---
title: Paper Records
updated: 2026-09-20
---

# Paper Records

One file per paper when a paper earns a dedicated record (otherwise the topic-level knowledge notes cover them). Schema: `schemas/source.schema.json`. Paper→code→dataset relations are MANDATORY edges (also mirror into `metadata/relations.json`).

## Template (per paper)
```yaml
title:
authors: [ ]            # et al. acceptable
institution:
date: YYYY-MM-DD        # published
url:                    # arXiv/DOI
arxiv:
code:                   # official implementation repo (or null)
dataset:                # (or null)
benchmark:              # evaluated-on (or null)
reproducibility: high | medium | low | unknown   # code+data+detail sufficiency
license:
summary:                # 3-5 sentences, your words
key_contribution:
limitations:
related_papers: [ ]
verified_at: YYYY-MM-DD
expires_at: YYYY-MM-DD  # 180-365d per freshness policy
```

## Rules
- Summary/key contribution/limitations in YOUR words — never a copied abstract (copy-policy).
- `reproducibility: low` papers may still be recorded — graded honestly.
- No paper claiming to contain leaked/private model internals gets a record (SECURITY.md hard limit).
