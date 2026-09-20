---
name: performance-audit
version: 1.0.0
description: "Web sitesi performansini Core Web Vitals, bundle boyutu, ag cagrilari, render metrikleri uzerinden denetleme ve somut iyilestirme onerileri."
category: performance
status: curated
confidence: high
requires: [browser-testing]
tags: [performance, core-web-vitals, lcp, inp, cls, lighthouse, bundle-size, web-vitals]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

Sitenin hızlı, hafif ve kullanıcıda "ağır uygulama" hissi vermemesini sağlamak. Core Web Vitals
hedeflerini tutturmadan yayına çıkmak hem SEO hem dönüşüm kaybı demektir.

# Ne zaman kullan

- Yayın öncesi
- Her önemli deploy sonrası
- Sayfa şişkinleştiğinde veya kullanıcı şikayeti olduğunda
- Animasyon/resim/yoğun liste eklerken

# İş Akışı (MEASURE → ANALYZE → FIX → VERIFY)

## 1. MEASURE — Ölç

- **Lighthouse** (laboratuvar): Performance, Accessibility, Best Practices, SEO, PWA.
- **Web Vitals (alan verisi)** = gerçek kullanıcı: LCP, INP, CLS; `web-vitals` kütüphanesi ile topla.
- **Bundle analizi:** `@next/bundle-analyzer` veya `rollup-plugin-visualizer` ile her sayfanın JS boyutu.
- **Ağ sayısı ve boyut:** devtools Network; ilk yükleme istek sayısı, toplam KB (JS+CSS+resim+font).
- **Render:** React DevTools Profiler; gereksiz re-render; büyük component tree.
- **Veritabanı ve API:** yavaş sorgular (n+1), waterfall, büyük payload.

## 2. ANALYZE — Hedefler ve sorun

Hedefler (75p yüzdesi / kullanıcıların %75'i):
- **LCP** < 2.5 saniye (iyi) → 2.5–4 "geliştirilmeli", >4 kötü.
- **INP** < 200 ms (iyi) → 200–500 geliştirilmeli, >500 kötü.
- **CLS** < 0.1 (iyi) → 0.1–0.25 geliştirilmeli, >0.25 kötü.
- **TTFB** < 800 ms.
- **FCP** < 1.8s.
- İlk JS bundle 200 KB gzipped altı hedef.

## 3. FIX — Yaygın iyileştirmeler

- **Resim:** Next.js `<Image>` veya uygun `srcset`, AVIF/WebP, boyut belirtmek (CLS düşürür), lazy-load, `fetchpriority="high"` (LCP resmi), hero resim CDN ile sıkıştırılsın.
- **Font:** `font-display: swap`, subset (latin + latin-ext), preconnect; kendi hostunda barındır.
- **JS:** büyük kütüphaneleri (chart, rich editor, markdown) dinamik `import()` ile ilk ekranda yükleme.
- **Tree shaking:** yanlış import yapma (`import * as`), yan etkisiz paketler.
- **React:** `useMemo/useCallback` abartma; client component'leri sınırla; RSC kullan; `window`-bağımlı kodları lazy et.
- **CSS:** critical CSS inline; gereksiz Tailwind sınıfı değil ama kodu sil; kullanılmayan CSS.
- **Server:** SSG/ISR ile önbellekle; uzun süren API'ler için cache/revalidate; redirect zincirlerini kır.
- **Ağ:** HTTP/2 veya HTTP/3, CDN, gzip/brotli sıkıştırma, keep-alive; 3. parti scriptleri (analytics, chat) async/defer ile yükle.
- **INP:** ana thread bloklayan ağır JS; büyük listeleri sanallaştır; debounce hızlı input'ları.
- **CLS:** resim/video için `aspect-ratio` veya `width/height`; font yükleme geçişini `size-adjust` kullanarak minimize et; reklam/widget yerlerini sabit ayır.

## 4. VERIFY

- İyileştirme sonrası tekrar Lighthouse ve Web Vitals ölç.
- Gerçek cihaz/mobil testi (3G simülasyonu ile).
- CI içine Lighthouse bütçesi koy (her PR'da 90+ kalıcılığı).

# Kalite Kontrol Listesi

- [ ] LCP/INP/CLS hedefte
- [ ] İlk JS bundle bütçesi (200KB gz altı)
- [ ] Resimler optimize + boyut belirli + modern format
- [ ] Font subset + swap + preconnect
- [ ] Ağır kütüphaneler lazy/dynamic import
- [ ] Server cache (ISR/SSR/CDN) ayarlı
- [ ] 3. parti scriptler gecikmeli
- [ ] Yönlendirme zinciri yok
- [ ] 404/500 oranları düşük
- [ ] Lighthouse perf skoru 90+
- [ ] Analytics/gerçek kullanıcı ölçümü kurulu

# Yaygın Hatalar

- Hero resmi `loading="lazy"` yapmak → LCP yavaşlatır.
- Büyük chart/markdown kütüphanesini tüm sayfalara yüklemek.
- Hero'da otomatik oynayan yüksek boyutlu video.
- React'te state'i yukarı taşıyıp tüm sayfayı re-render ettirmek.
- CSS'de yanlış `size-adjust` ayarı veya font yüklemesiyle layout shift.
- N+1 veri çekme (SSR'da her ürün için ayrı sorgu).

# Referanslar

- web.dev: https://web.dev/
- Next.js Performance: https://nextjs.org/docs/app/building-your-application/optimizing
- Web Vitals: https://web.dev/vitals/
- Bundle Analyzer: @next/bundle-analyzer

# İlgili Skill'ler

- `browser-testing`
- `seo-audit`
- `deployment`
