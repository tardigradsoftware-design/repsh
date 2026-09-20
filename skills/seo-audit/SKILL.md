---
name: seo-audit
version: 1.0.0
description: "Teknik SEO, Core Web Vitals, yapilandirilmis veri, Turkce/yerel SEO; meta, sitemap, robots, hreflang, canonical, indexleme, icerik optimizasyonu icin denetim."
category: seo
status: curated
confidence: high
requires: [performance-audit]
tags: [seo, technical-seo, core-web-vitals, structured-data, sitemap, turkish-seo, local-seo, lighthouse]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

Sitelerin arama motorları tarafından doğru taranması, indekslenmesi ve Türkiye odaklı içeriğin
hedef kullanıcıya ulaşması. Teknik SEO (tarama, hız, mobil), içerik SEO (başlık/meta/açıklama)
ve yapılandırılmış veri (Schema.org).

# Ne zaman kullan

- Site yayın öncesi zorunlu denetim
- Mevcut site trafiği düşükse
- Yeni sayfa/ürün/kategori eklerken
- Yeniden tasarım / migration sonrası (URL değişiklikleri)

# İş Akışı (CRAWL → INDEX → TECHNICAL → CONTENT → STRUCTURED → LOCAL → PERF → REPORT)

## 1. CRAWL — Taranabilirlik

- `robots.txt` istemci ve arama motorlarının erişebildiği/erişemediği yolları doğru tanımlıyor mu?
- `sitemap.xml` güncel ve Search Console'a gönderilmiş mi? İçerik 50.000 URL / 50MB sınırı dahilinde.
- Kırık linkler (4xx/5xx) var mı? Screaming Frog / Playwright taraması ile tespit.
- Tarama derinliği: önemli sayfalar ana sayfadan 3 tıktan daha uzakta olmamalı.
- Yumuşak 404 (200 dönüp "sayfa yok" diyen), sonsuz yönlendirme (redirect chain) yok.

## 2. INDEX — İndeksleme

- Her sayfada canonical doğru mu?
- `noindex` yanlışlıkla production sayfalarında bırakılmış mı? (development'tan sızma riski)
- Pagination için `rel=next/prev`; varyantlar için `hreflang` (tr-TR, en vb.).
- www/non-www, http/https tekil protokole yönlenmeli (301).
- URL yapısı temiz, kısa, Türkçe karakterler normalized (slug, ı→i, ş→s gibi veya Unicode URL uygunsa kalabilir ama tutarlı).

## 3. TECHNICAL — Teknik SEO

- `head` içinde `<title>` (her sayfada benzersiz, 50–60 karakter), `<meta name="description">` (150–160).
- Open Graph ve Twitter Card meta etiketleri (sosyal paylaşım için).
- Tek H1; mantıksal H2-H3 akışı.
- HTML dili: `<html lang="tr">`.
- LCP/FID/INP/CLS (Core Web Vitals) — mobile ilk 2.5 saniyede LCP; INP <200ms; CLS <0.1.
- Mobil uyumlu (viewport meta, mobil testi).
- HTTPS zorunlu.
- Yeni sayfa için prerender/SSG/ISR/SSR seçimi doğru mu? (Dinamik ama sık değişmeyen sayfalar ISR.)

## 4. CONTENT — İçerik

- Başlık etiketinde ve H1'de anahtar kelime doğal olarak geçiyor; aşırı doldurma yok.
- Ürün/kategori sayfaları benzersiz açıklama; üretici açıklamasını kopyala-yapıştır yapmamak (duplicate content).
- Dahili bağlantı (internal linking); benzer/ilgili ürün/makale linkleri.
- Görsellerde dosya adı anlamlı ve `alt` metni var; resim boyutları uygun.
- Türkçe imla ve dilbilgisi (AI ile yazıldıysa özellikle kontrol et).

## 5. STRUCTURED — Yapılandırılmış veri (Schema.org)

- Organizasyon/Logo
- WebSite (arama kutusu)
- BreadcrumbList
- Product (isim, açıklama, resim, fiyat, stok, rating)
- Article/BlogPosting
- FAQ (sıkça sorulanlar)
- LocalBusiness (konum, telefon, çalışma saatleri, harita)
- Yorum/yıldız varsa AggregateRating.

JSON-LD formatında; test aracı ile doğrula (Google Rich Results Test).

## 6. LOCAL TR — Türkiye'ye özel

- `lang="tr"`, `hreflang="tr-TR"`.
- Para birimi TRY, fiyatlar KDV dahil (Türkiye'de etiketlerde KDV dahil fiyat zorunlu).
- Adres/telefon formatı Türkiye formatı; LocalBusiness içinde `addressRegion` iller (İstanbul, Ankara).
- Google Business Profile (eski Google Benim İşletmem) kaydı; harita entegrasyonu.
- Yasal sayfalar: Mesafeli Satış Sözleşmesi, KVKK/Gizlilik, Gizlilik Politikası, Çerez Politikası, İptal/İade Koşulları.
- Çerez onayı (KVKK/KVK kapsamında, özellikle AB ziyaretçi olmasa bile en iyi pratik).

## 7. PERF — Performans ve Core Web Vitals

bkz. `performance-audit` skill'i.

## 8. REPORT

- Google Search Console, Analytics (GA4) kurulu ve izleme doğru.
- Lighthouse SEO skoru 90+ hedefi.
- Rapor: kırık link, eksik meta, canonical hatası, yapılandırılmış veri hatası, düşük CWV.

# Kalite Kontrol Listesi

- [ ] robots.txt + sitemap.xml + Search Console
- [ ] Title/description her sayfada benzersiz
- [ ] Canonical + hreflang + yönlendirmeler doğru
- [ ] `lang="tr"`
- [ ] Tek H1 ve mantıksal heading akışı
- [ ] HTTPS zorunlu
- [ ] Core Web Vitals hedefler içinde
- [ ] Schema.org JSON-LD ve doğrulaması geçiyor
- [ ] Görsellerde alt metin ve uygun boyut
- [ ] Kırık link/4xx düzeltilmiş
- [ ] Yasal sayfalar (KVKK, sözleşme, çerez) var
- [ ] Google Business Profile (yerel işletmeyse)

# Yaygın Hatalar

- Next.js'de App Router ile `metadata` nesnesi atlanıp her sayfada aynı title kullanmak.
- Staging'deki `noindex` production'a sızmak.
- Ürünlerde üreticiden kopya açıklama kullanmak (duplicate content).
- Canonical yanlış URL'yi işaret etmek.
- `lang` özniteliği yanlış veya unutmak.
- Türkçe karakterleri URL'ye yanlış kodlamak veya slug'da keyfi kesmek.
- Yapılandırılmış veriyi yanlış tipte kullanmak (Organization yerine Person).

# Referanslar

- Google Search Central: https://developers.google.com/search
- Rich Results Test: https://search.google.com/test/rich-results
- web.dev: https://web.dev/
- Lighthouse: https://github.com/GoogleChrome/lighthouse
- Schema.org: https://schema.org/

# İlgili Skill'ler

- `performance-audit`
- `accessibility-audit`
- `deployment`
- `browser-testing`
