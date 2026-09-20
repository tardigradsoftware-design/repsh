---
name: browser-testing
version: 1.0.0
description: "Playwright ile E2E, gorsel regresyon, etkilesim, erisilebilirlik, responsive, performans, SEO, guvenlik, tarayici uyumu testlerini otomatiklestirme."
category: testing
status: curated
confidence: high
requires: []
tags: [testing, playwright, e2e, visual-regression, cross-browser, regression, screenshot, a11y]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

Kodun gerçek tarayıcıda çalıştığını, görsel olarak bozulmadığını, erişilebilir ve responsive
olduğunu makine tarafından tekrarlanabilir şekilde test etmek.

# Ne zaman kullan

- Her yeni özellik sonrası
- Yayın öncesi son kontrol
- Tasarım/tema değişikliklerinde görsel regresyon
- Kritik akışlarda (auth, ödeme, form) sürekli

# Hazırlık

- Playwright yükle (`@playwright/test` + browserlar).
- Proje dizini: `e2e/` veya `tests/e2e/`.
- Config: `playwright.config.ts`; 3 tarayıcı (chromium, firefox, webkit); viewport'lar mobil/tablet/desktop.
- `baseURL` ayarla; auth state storageState kullan (testler giriş yapmak için tekrar tekrar login olmasın).
- Visual regression için toMatchScreenshot (veya Percy/Chromatic/Lost Pixel).

# Test Matrisi

Testleri şu kategorilerde yaz:

1. **Functional (işlevsel):** Kritik akışlar. Kullanıcı kaydı, giriş, ürün gezme, sepete ekleme,
   ödeme, admin paneli işlemleri. Happy path + 1–2 hata durumu (boş form, hatalı kart).
2. **Visual (görsel):** Ana sayfalar için screenshot karşılaştırma (laptop ve mobil viewport).
   Her PR'da çalışır; fark %0.2 üzeri veya diff piksel belli ise fail.
3. **Responsive:** 390/768/1280/1536px'de layout kontrolü; taşma yok, etkileşim çalışıyor.
4. **Accessibility:** axe-core Playwright ile otomatik tarama; critical/serious violation sıfır.
5. **Performance:** Lighthouse CI (isteğe bağlı) ile belirlenen eşiklerin altında kalma.
6. **SEO:** SSR ile üretilen sayfada meta/title/h1/canonical var mı; response HTML kontrol.
7. **Security (temel):** Basit XSS denemesi (input'a `<script>alert(1)</script>`), auth korumalı
   sayfanın login olmadan yönlendirdiği, API CSRF kontrolleri.
8. **Cross-browser:** Chromium + Firefox + WebKit ana akışlar. (Tarayıcıya özel bilinen farklar için ayrı not.)

# İş Akışı (PLAN → CODE → RUN → FIX → CI → MAINTAIN)

## 1. PLAN — Test edilecek senaryoları listele

Her kritik kullanıcı akışı için 1 senaryo; 20–30 senaryo sağlıklı projeler için yeterlidir.
Çok fazla sürdürülemez; güvenilmez (flaky) testler güveni yok eder.

## 2. CODE — Testleri yaz

- `test.describe` ile sayfa bazlı grupla.
- `beforeEach` ile ortak setup; testler birbirine bağımlı olmasın (izolasyon).
- Selector'ları kararlı seç: `data-testid` veya role/getByRole; kırılgan CSS sınıfı veya `nth-child` kullanma.
- Assertion'ları açıkça yaz: görünür, metin var, yönlendirme, network başarılı.
- Web first assertion'lar kullan (`toBeVisible`, `toHaveText`, `toHaveURL`).
- Network isteklerini mock'lamayın gerçek entegrasyon testinde; ama 3. parti (iyzico, Stripe) için test ortamı veya mock webhook kullan.
- Görsel testlerde `fullPage: true` ve tutarlı zaman (animasyonları kapat, belirli veri seed et).

## 3. RUN — Çalıştır ve değerlendir

- `pnpm test:e2e` tekrar çalışır.
- Flaky (kimi zaman geçip kimi zaman kalan) testleri hemen işaretle; stabilize etmeden merge etme.
- Trace viewer ile hata inceleyebilmek için hata anında trace otomatik alın.

## 4. FIX — Hataları düzelt

Test bulunca: önce kök nedeni düzelt, sonra testi bekletmeye alma (`test.skip`) veya gevşetme.
Görsel diff kasıtlıysa screenshot'ı onayla (`--update-snapshots`).

## 5. CI — Sürekli entegrasyon

- Her PR'da chromium + 1 viewport hızlı smoke test.
- Merge öncesi tam matris (3 tarayıcı + 3 viewport).
- Nightly görsel regresyon + accessibility raporu.

## 6. MAINTAIN — Bakım

- Her yeni özellikle birlikte test ekle.
- Bozulan seçici veya değişen akışı hemen güncelle.
- Testler çok yavaşsa paralel çalıştır ve sharding yap.
- Test verilerini seed script ile oluştur; birbirinden bağımsız.

# Kalite Kontrol Listesi

- [ ] Playwright kurulu ve config'i mevcut
- [ ] Kod tabanında kritik akışlar için E2E test var
- [ ] Auth state storageState kullanılıyor
- [ ] Selector'lar kararlı (role/testid)
- [ ] Visual regression en az ana sayfalar için
- [ ] Axe ile a11y taraması
- [ ] 390/768/1280 viewport'ları test matrisinde
- [ ] Flaky testler işaretlenmiş ve azaltılmış
- [ ] Trace ve screenshot hata anında alınıyor
- [ ] CI'da her PR'da çalışıyor

# Yaygın Hatalar

- Snapshotları güncellemeden görsel değişiklik yapmak.
- Gerçek backend yerine tamamen mock kullanmak (gerçek kırıkları kaçırır).
- Aşırı kapsamlı selector (`.class1 .class2 div:nth-child(3)`) → küçük değişiklikte kırılır.
- Testleri birbirine bağımlı yazmak (sonraki test öncekinin sonucuna güveniyor).
- Auth'u her testte tekrar yapmak → yavaş ve çift yük biniyor.
- Animasyon ve yükleme sürelerini `waitForTimeout(5000)` ile sabit beklemek → flaky. Yerine web first assertion veya belirli state bekle.
- Cross-browser farklılık (özellikle Safari'de tarih/input/scroll) için özel düzeltme yapmadan testi ignore etmek.

# Referanslar

- Playwright: https://playwright.dev/
- axe-core/playwright: https://github.com/abhinaba-ghosh/axe-playwright
- Best Practices: https://playwright.dev/docs/best-practices
- Lost Pixel / Chromatic / Percy (görsel regresyon servisleri)

# İlgili Skill'ler

- `accessibility-audit`
- `performance-audit`
- `seo-audit`
- `security-audit`
- `debugging`
