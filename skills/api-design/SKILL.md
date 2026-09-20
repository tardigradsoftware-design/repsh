---
name: api-design
version: 1.0.0
description: "REST/Server Action/RPC API tasarimi: tutarli rota yapisi, hata yonetimi, surumlama, dogrulama, rate limit, versiyonlama, idempotency, guvenlik."
category: backend
status: curated
confidence: high
requires: [security-audit, database-design]
tags: [api, rest, http, server-actions, rpc, openapi, pagination, idempotency]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

Tutarlı, güvenli, bakımı kolay API'ler (REST route'ları, Next.js Server Actions, veya RPC) tasarlamak.

# Ne zaman kullan

- Yeni endpoint/action eklerken
- Hatalı/tutarsız API'yi düzeltirken
- Client-server arasındaki sözleşmeyi tanımlarken

# İş Akışı (SPEC → CONTRACT → VALIDATE → ERROR → AUTH → PERF → DOC → TEST)

## 1. SPEC — Sözleşme

- Ne dönecek? Hangi method (GET/POST/PUT/PATCH/DELETE)?
- Route yapısı: kaynak odaklı (`/api/orders`, `/api/orders/:id/items`).
- Server Action: `app/**/actions.ts` içinde tanımlı, "use server" belirtilmiş.
- Girdi ve çıktı şekli net: JSON şeması (zod ile).
- Sayfalama: `?page=2&limit=20`, imza (cursor) veya offset; yanıtta meta (total, pages).
- Filtre/sıralama: `?status=active&sort=-created_at`.
- Başarılı cevap: 200/201/204; standart şekil `{ data, meta?, error? }` veya doğrudan veri.

## 2. VALIDATE

- Tüm girdi (body, query, param, header) zod şeması ile doğrulanır.
- Doğrulama hatasında 400 + alan bazlı hata mesajı.
- Asla istemcinin sunduğu ID'ye güvenme; yetkiyi doğrula.

## 3. ERROR — Hata yönetimi

- Tutarlı hata cevabı: `{ error: { code, message, details? } }`.
- HTTP kodu anlamlı: 400 (bad req), 401 (unauth), 403 (forbidden), 404 (not found), 409 (conflict),
  422 (validation), 429 (rate limit), 500 (server).
- Hata mesajı kullanıcıya dost; ama iç detay (stack, DB hatası) dönmüyorsun.
- Her hata loglanır; correlation id ile takip.

## 4. AUTH/GUARD

- Her endpoint auth durumunu açıkça belirtir (public / authenticated / role gerekli).
- Middleware/guard ile tek noktadan kontrol.
- Rate limit: giriş/ödeme/arama gibi endpointlerde.
- Idempotency key: ödeme ve yazma işlemlerinde; tekrar gönderimde aynı sipariş/sonuç dönmeli.
- CSRF koruması; cookie session kullanıldığında doğrulama.

## 5. PERF

- N+1 sorgu önle; gerekli join/data loader.
- Ağır işlemler kuyruğa alınır (async worker, queue); HTTP isteğinde 30sn+ işlemler kullanıcıyı bekletmez.
- Cache: GET istekleri uygun TTL ile cache'lenebilir.
- Pagination büyük listelerde zorunlu; 1000+ kayıt imleç (cursor) tabanlı.
- Büyük payload'lar sıkıştır (compression); gereksiz alan döndürme (projection).

## 6. DOC

- OpenAPI/Swagger (eğer 3. parti kullanım varsa) veya en azından kodda JSDoc.
- Server Action'lar için her action'un ne yaptığı, hangi rol gerektirdiği, ne döndürdüğü yorumlanmış.

## 7. TEST

- Her endpoint için mutlu yol + 2 hata durumu (auth yok, yetki yok, validation).
- E2E testte akıştan geçir.

# Kalite Kontrol Listesi

- [ ] Route/action isimlendirme tutarlı ve kaynak odaklı
- [ ] Zod ile input doğrulaması
- [ ] Auth/guard kontrolü
- [ ] Tutarlı hata cevabı ve HTTP kodu
- [ ] Sayfalama (büyük liste)
- [ ] Rate limit kritik yerde
- [ ] Idempotency (ödeme/yazma)
- [ ] N+1 sorgu kontrolü
- [ ] Server action'larda "use server" ve input doğrulama
- [ ] Testler yazılmış
- [ ] Sır saklamıyor (stack trace, DB hatı döndürmüyor)

# Yaygın Hatalar

- Route'ları fiil odaklı yapmak (`/api/getOrders`, `/api/createOrder`) → REST kaynak odaklı olmalı.
- Sırf "kolay" diye tüm veriyi döndürmek (kullanıcıya ait hassas alanları da).
- 500 hatasında stack trace dönmek.
- Aynı endpoint'te 5 farklı iş yapmak (büyük switch/case handler).
- Rate limit koymamak (brute force / DoS riski).
- İstemcinin gönderdiği `isAdmin` alanını güvenmek.
- Server action'ı `"use server"` eklemeden yazmak veya client'ta DB çağırmak.

# İlgili Skill'ler

- `security-audit`
- `database-design`
- `deployment`
