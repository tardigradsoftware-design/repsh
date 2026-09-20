# Performans: Font ve Resim Optimizasyonu

## Font

- Kendin host et; Google Fonts'u `<link>` ile eklemek 3. parti kaynak maliyeti doğurur.
  Next/Font kendi host eder ve `next/font` ile kolay kullanılır.
- `display: 'swap'` (FOIT yerine FOUT'u tercih et).
- Alt küme: `latin,latin-ext` (Türkçe karakterleri de içerir). İhtiyaç varsa `cyrillic` vb. ekle.
- Preconnect: `<link rel="preconnect" href="https://fonts.googleapis.com">` kendi hostunda
  kullanıyorsan gerek yok.
- Çok fazla font yükleme (tek başına 3–4 weight yeterli: 400, 500, 600, 700).
- Dosya boyutu için `woff2` kullan; woff/ttf yükleme.
- `size-adjust`, `ascent-override`, `descent-override` ile CLS azalt (next/font bunu ayarlıyor).

## Resim

- Modern format: **AVIF** en iyi sıkıştırma; desteklenmeyen tarayıcıda WebP veya JPEG düşer.
- Next.js `<Image>` component kullan (veya Cloudflare/Imgix gibi CDN dönüşümü).
- Her resim için width/height veya aspect-ratio belirle → CLS düşer.
- `srcset` ile farklı boyutlar üret; küçük ekrana büyük resim indirme.
- Hero resmi: `fetchpriority="high"`; üst katman resim `loading="eager"` diğerleri `loading="lazy"`.
- Lazy-load resimler için üstündeki boşluğu aspect-ratio ile rezerve et (yer tutucu).
- Kullanıcı yüklediği içerik (avatar, ürün) için kesinlikle aynı işlem; medya depolamadan
  (S3/R2) sonra CDN ile varyasyon sun.
- Alt metin: bilgi veren resimler için açıklayıcı; dekoratif resimler için `alt=""`.
- Arka plan görselinde CSS `image-set` ile 1x/2x alternatif.
- Çok büyük orijinal fotoğrafları (ör. 4000×3000) doğru boyuta düşür; en fazla ekranın gerektirdiği
  pikseli sun.

## 3. parti scriptler

- Analytics, chat, pixel, AB scriptlerini `async` veya `defer` ile yükle.
- Kullanıcı etkileşimi sonrası yükleme (`requestIdleCallback`/lazy init) ilk yüklemeyi rahatlatır.
- Her eklediğin script'in LCP/INP üzerindeki etkisini Lighthouse ile ölç; gereksizse kaldır.

## Ölçüm

- Lighthouse Performance skoru ve Web Vitals (LCP, INP, CLS).
- Chrome DevTools Network: JS/CSS/Resim/Font toplam bayt ve sayı.
- `@next/bundle-analyzer` ile JS bundle'ı parçala ve ağır kütüphaneleri dynamic import ile böl.

## Hedefler
- LCP < 2.5s (mobil, 75p)
- INP < 200ms
- CLS < 0.1
- İlk JS gz bundle < 200KB
- Kritik yol resim < 200KB
