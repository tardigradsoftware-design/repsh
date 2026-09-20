---
title: RAG Pipeline Notes
category: data-engineering
confidence: medium
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [rag, retrieval, data]
---

# RAG Pipeline Notes

## Pipeline stages (each is a failure surface)
ingestion → chunking → embedding → indexing → retrieval → rerank → generation

## Chunking
Semantic boundaries (headings/sections) over fixed windows; 200-500 tokens typical with overlap; preserve headings as metadata (retrievability!). This repo's own docs are chunked this way (see standards note).

## Retrieval
Hybrid (BM25 + vectors) beats pure vector for exact terms (error codes, IDs); rerank top-k (cross-encoder) for precision; MMR for diversity.

## Generation
Cite-or-refuse policy: answer only from retrieved context with citations; "not in the docs" is a valid output. Provenance strings (source+date) flow into the prompt (see context-engineering/context-packing.md).

## Evaluation
Retrieval: hit@k / MRR on labeled queries. End-to-end: faithfulness + answer-relevance on a fixed QA set (ragas-class or hand-built). Change one stage at a time; measure.
