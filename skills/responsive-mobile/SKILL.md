---
name: responsive-mobile
version: 1.0.0
description: "Responsive ve mobil oncelikli tasarim; kirilim noktalarinda (390/768/1024/1440) duzenin bozulmamasini, dokunma hedeflerinin buyuklugunu, mobil UX kalibini saglar."
category: frontend
status: curated
confidence: high
requires: [frontend-design, design-system]
tags: [responsive, mobile, touch, breakpoints, media-queries, mobile-first]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

Mobil cihazlarda kullanılabilir, hızlı, okunabilir arayüz üretmek. Desktop-tasarla-mobilde-sıkıştır
tuzağından kaçınmak; mobile-first yaklaşımı.

# Ne zaman kullan

Her UI bileşen/sayfa yazımında (her zaman).

# İş Akışı (MOBILE-FIRST → BREAKPOINTS → TOUCH → PERF → VALIDATE)

## 1. MOBILE-FIRST — Önce mobil

- Önce en dar (390px) viewport'ta çalışır halde yaz; sonra daha geniş ekranlara aç.
- Tek kolon temel akış; başlık + CTA, içerik bölümleri dikey.
- Yazı boyutu en az 16px (iOS'ta input zoom'unu önlemek için).
- Başlıklar mobilde 24–36px; desktop'tan daha kısa ve öz.

## 2. BREAKPOINTS — Kırılımlar

Standart kırılımlar:
- `sm` 640px (büyük telefon)
- `md` 768px (tablet dikey)
- `lg` 1024px (tablet yatay / küçük dizüstü)
- `xl` 1280px (dizüstü)
- `2xl` 1536px (büyük ekran)

Her kırılımda:
- Grid kolon sayısı artar (1 → 2 → 3 → 4).
- Yazı ve boşluk büyür; ama orantılı.
- Yatay kaydırma gerekiyorsa tablo/grafik için ayrı scrollable alan.
- Sidebar desktop'ta sabit, mobilde drawer.

## 3. TOUCH — Dokunma

- Tıklanabilir hedef minimum **44×44px** (WCAG 2.5.5).
- Dokunma hedefleri arası boşluk en az 8px.
- Hover durumları mobilde yok; kritik etkileşim hover'a bağlı olmamalı.
- `touch-action` ile yanlış kaydırma engellenmeli (carousel, harita).
- Sabit header/footer fazla yer kaplamamalı.

## 4. PERF — Performans

- İlk ekran kritik CSS inline veya küçük; ilk resimler `fetchpriority="high"`.
- Alt ekran resimleri `loading="lazy"`; `decoding="async"`.
- Büyük resimlerde responsive `srcset` ve modern format (AVIF/WebP).
- Yazı tipi: `font-display: swap`; alt kümele (subset=latin,latin-ext) Türkçe karakterler dahil.
- JS bundle; ağ yavaşken işlevsellik kısıtlanmasın (progressive enhancement).

## 5. VALIDATE

- Playwright ile 390/768/1024/1440'da screenshot.
- 400% zoom testi (erişilebilirlik).
- Dokunma alanları: axe/playwright ile denetle.
- Cihaz emülasyonu (iOS Safari ve Chrome Android) — sticky, vh birimi, safe-area-inset.
- Çentik/güvenli alan: `env(safe-area-inset-bottom)` ile sabit alt barlar çentiğe binmesin.
- Yatay kayma (horizontal scroll) olmamalı.

# Kalite Kontrol Listesi

- [ ] Mobile-first yazıldı; tüm kırılımlarda test edildi
- [ ] Tüm butonlar/linkler 44×44px'den küçük değil
- [ ] Hover'a bağlı etkileşim yok
- [ ] 16px altı input yok
- [ ] Resimler lazy + srcset + modern format
- [ ] Yazı tipi swap + Türkçe subset
- [ ] Safe-area-inset ayarlandı
- [ ] Yatay kayma yok
- [ ] Sticky header fazla yer kaplamıyor
- [ ] Açılır menüler dokunma ile rahat kullanılıyor

# Yaygın Hatalar

- Desktop'ta tasarlayıp mobilde yığmak (sığmayan taşan kartlar, yanlamasına tablo).
- Hover ile açılan dropdown mobilde erişilemez.
- Küçük butonlar (28px × 28px çarpı ikonu).
- 12px-14px form input (iOS otomatik zoom).
- 100vh kullanımı mobil toolbar'ı kapatıyor → `min-height: 100dvh` kullan.

# İlgili Skill'ler

- `frontend-design`
- `design-system`
- `accessibility-audit`
- `performance-audit`
- `browser-testing`
