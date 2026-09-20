# Test Senaryoları — performance-audit

## Test 1: Büyük kütüphanenin ilk sayfaya yüklenmesi

**Girdi:** Landing sayfasında bir anket formunda ReCaptcha + React Markdown + Chart.js hepsi static import ile yükleniyor.
Sayfa ilk JS bundle'ı 540KB gzipped; LCP 4.2s; Lighthouse perf 52.

**Beklenen:**
- Chart.js sadece dashboard sayfasında olduğundan veya dinamik olarak lazy import edilmesi gerektiğini not eder.
- React Markdown anket sorularında sadece varsa dynamic import edilir.
- ReCaptcha form görünümüne yaklaşınca inject edilmeli (görünüm uzakta veya kullanıcı form alanına dokunduğunda).
- Hero resimleri fetchpriority="high" + Image ile.
- Düzenleme sonrası LCP <2.5s, JS bundle <200KB gz, Lighthouse 90+ hedefi.

## Test 2: CLS'e sebep olan layout shift

**Girdi:** Ürün listesinde resimler JS yüklenmeden sonra geliyor ve öğeler aşağı itiliyor. CLS 0.35.

**Beklenen:**
- Resimlerde `width/height` veya `aspect-ratio` kullanarak yer rezerve edilmesini önerir.
- Font yüklemesi için `size-adjust` veya `font-display: optional` ile shift'i azaltma.
- Cookie banner / reklam / chat widget için sabit yükseklik veya yer rezerve etme.
- Düzeltme sonrası CLS < 0.1.
