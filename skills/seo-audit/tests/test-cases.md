# Test Senaryoları — seo-audit

## Test 1: Site yayını öncesi denetim

**Girdi:** Yeni açılmış Next.js 15 pazarlama sitesi; ana sayfa ve 10 hizmet sayfası var. Hosting Vercel.

**Beklenen kontroller (en az):**
- `<html lang="tr">`
- Her sayfa için benzersiz title/description metadata.
- `robots.ts` ve `sitemap.ts` (Next.js App Router ile) doğru; production'da `noindex` yok.
- `vercel.json` veya yönlendirmeler www/non-www ve http→https tekilleştiriyor.
- `og:image` ve Twitter card meta'ları var.
- Breadcrumb ve WebSite schema JSON-LD.
- Hizmet sayfalarında Service veya Article JSON-LD.
- Görseller webp/avif, `alt` dolu.
- Lighthouse SEO skoru 90+.
- Search Console ve GA4 izleme kodları doğru (staging'de çalışmıyor).
- KVKK/Gizlilik/Çerez sayfaları var.

## Test 2: Staging noindex sızıntısı

**Girdi:** Production'daki yeni ürün sayfasında response header veya `<meta name="robots" content="noindex">` görünüyor.

**Beklenen:**
- CRITICAL olarak işaretler; nedenini arar (env tabanlı `robots.ts`, yanlış env var, deployment branch).
- Düzeltme: production ortamında noindex kaldırılır; staging environment korumalı (password veya IP kısıtı).
- Düzeltme sonrası Search Console URL Inspection ile doğrulama yapılması not edilir.
