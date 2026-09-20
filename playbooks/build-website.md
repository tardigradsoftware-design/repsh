# Playbook: build-website (Pazarlama/Kurumsal/Küçük Site)

Bu playbook fikir aşamasından yayına kadar bir web sitesi (pazarlama, hizmet, kurumsal tanıtım,
küçük ürün landing) inşa etmek için uçtan uca akışı tanımlar.

## Önkoşul

- `research-before-code` skill çalıştırılmış olmalı.
- Stack kararı `stacks/marketing-site.md` veya `stacks/corporate-site.md`'den alınmış olmalı.
- Marka ve içerik (metin, görseller) en azından taslak seviyesinde hazır olmalı.

## Faz Akışı

### 1. Fikir ve Araştırma (1–2 gün)

1. Proje amacı: ana mesaj, hedef kitle, CTA (iletişim formu, satın alma, demo, başvuru).
2. Rakip ve referans incelemesi (3–5 site): Linear/Stripe/Vercel gibi iyi örnekler kadar
   sektördeki yerel rakipler de dahil; renklerini kopyalama, hiyerarşi ve ritim ilkesi çıkar.
3. Domain, hosting, içerik dili, çoklu dil ihtiyacı varsa plan.
4. Anahtar sayfa listesi: Ana sayfa, Hakkımızda, Hizmetler/Ürün, Referanslar, SSS, Blog, İletişim,
   Gizlilik/KVKK, Çerez, Mesafeli Satış (varsa e-ticaret).
5. Stack seçimi ve repo kurulumu (`stacks/` ile).

### 2. Tasarım Sistemi (0.5–1 gün)

1. `design-system` skill uygula: renk (1 ana marka rengi), tipografi (1 aile, modüler ölçek), spacing, radius, shadow.
2. Token'ları CSS değişkeni + Tailwind config'e dök.
3. Temel bileşen seti: Button, Card, Input, Badge, Section, Container, Navbar, Footer.
4. Dark mode karar ver (çoğu pazarlama sitesi için ilk sürümde opsiyonel).

### 3. Mimari ve İskelet (0.5 gün)

1. Next.js App Router ile klasör yapısı kur (app/, components/, lib/, public/).
2. Layout: navbar + main + footer; metadata (title template, description, og).
3. Navbar: logo, ana linkler, CTA; mobil drawer.
4. Footer: logo, kısa açıklama, link grupları, sosyal, yasal linkler.

### 4. Sayfaları yaz (3–5 gün)

Her sayfa için:
1. İçerik metni (doğal Türkçe, jenerik "Build faster" yok).
2. Hiyerarşi: başlık, alt başlık, CTA, destekleyici görsel/illüstrasyon.
3. `frontend-design` skill uygula: 8px ızgara, ölçülü boşluk, 1 ana renk.
4. Görseller: Unsplash yerine özgün illüstrasyon/gerçek fotoğraflar; Next/Image, modern format, lazy.
5. Formlar (iletişim, bülten): react-hook-form + zod; sunucu tarafı doğrulama, spam koruması (Turnstile/reCAPTCHA v3, honeypot).

### 5. Animasyon (0.5 gün)

- `animation-motion` skill: ölçülü geçişler; hero haricinde scroll-triggerlı animasyon yok denecek kadar az.
- Reduced-motion desteği mutlaka.

### 6. Responsive (0.5–1 gün)

- `responsive-mobile`: 390/768/1024/1440 kırılımları; dokunma hedefleri; mobil menü.

### 7. Erişilebilirlik (0.5 gün)

- `accessibility-audit`: axe taraması, klavye gezinme, kontrast, dil özniteliği, alt metin.

### 8. Performans (0.5 gün)

- `performance-audit`: LCP, INP, CLS; resimler, font, 3. parti scriptler (analytics, chat).
- Lighthouse hedef 90+.

### 9. SEO ve Analytics (0.5 gün)

- `seo-audit`: title/description/og, sitemap, robots, Schema.org (Organization, WebSite, Breadcrumb, Service).
- GA4 ve/veya Plausible; Search Console doğrulaması.
- Türkiye'ye özel: `lang="tr"`, `hreflang`, iletişim bilgileri, KVKK/çerez metinleri.

### 10. Test (0.5–1 gün)

- `browser-testing`: Playwright ile ana akış (navbar dolaşım, form gönderimi, 3 dil/kırılım).
- Cross-browser (Chrome, Safari, Firefox) temel akışlar.
- Formun gerçekten e-posta/API çağrısı yaptığını doğrula.

### 11. Deploy (0.5 gün)

- `deployment`: Preview → canlı; domain bağlama, HTTPS, CDN, güvenlik header'ları.
- DNS, SPF/DKIM/DMARC (e-posta gönderiliyorsa).
- Canlı smoke test; izleme araçları.

### 12. Son denetim

- `website-quality-review` çalıştır. Skor 80+ ise canlı.
- CRITICAL/HIGH maddeler kapat; MEDIUM not al, sonraki sprinta taşı.

## Çıkış kriteri

- Ana sayfa ve 5+ içerik sayfası yayında
- HTTPS, responsive, erişilebilir, Lighthouse 90+
- İletişim/form çalışıyor
- Analytics/Search Console bağlı
- Yasal sayfalar mevcut
- Son kalite skoru 80+

## İlgili skill'ler

`research-before-code`, `design-system`, `frontend-design`, `responsive-mobile`,
`accessibility-audit`, `performance-audit`, `seo-audit`, `browser-testing`,
`deployment`, `website-quality-review`, `ai-slop-detection`.
