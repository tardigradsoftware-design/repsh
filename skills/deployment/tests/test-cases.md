# Test Senaryoları — deployment

## Test 1: Env eksik production

**Girdi:** Deploy sonrası 500; log'da `NEXT_PUBLIC_SUPABASE_URL is undefined`.

**Beklenen:**
- Preview aşamasında env'leri eksiksiz tanımlamayı önerir (post-deploy smoke test bunu yakalamalı).
- Uygulama başlangıçta gerekli env var olup olmadığını kontrol etmeli; anlaşılır hata vermeli.
- Tüm env'ler bir checklist ile dokümante edilmeli (ör. `ENV.md`).

## Test 2: Migration geri alınamıyor

**Girdi:** Production'a `ALTER TABLE orders ADD COLUMN total_new numeric NOT NULL;` migrasyonu çalıştırıldı ama kod henüz bu kolonu yazmıyor; eski kod NULL constraint yüzünden insert yapamıyor.

**Beklenen:**
- Migration'ların backward compatible olması gerektiğini belirtir: yeni NOT NULL kolonlar önce DEFAULT/nullable eklenir; kod güncellendikten sonra constraint eklenir.
- Rollback ve strateji: geniş pencerelerde bakım modu; veya feature flag ile geçiş.
