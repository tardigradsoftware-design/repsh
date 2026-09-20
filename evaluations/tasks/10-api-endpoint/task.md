# Görev 10: Sipariş API Endpoint
## Açıklama
`GET /api/orders/:id` ve `PATCH /api/orders/:id` endpoint'leri yaz (Next.js Route Handler veya Server Action).
## Başarı
- Zod ile input doğrulaması
- Auth zorunlu; kullanıcı kendi siparişini görebiliyor/düzenleyebiliyor (IDOR yok)
- Düzgün HTTP kodu (200/400/401/403/404/422/429)
- Hata yanıtı standart formatta ({ error: { code, message } }), stack trace yok
- PATCH kısıtlı alanları kabul ediyor (kullanıcı sipariş toplamını değiştiremez)
- Rate limit (en az 30dk'da 60 istek)
- Idempotency PATCH için (aynı istek tekrar işlenmez)
