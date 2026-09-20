---
name: accessibility-audit
version: 1.0.0
description: "Web sitelerini WCAG 2.2 AA hedefiyle erisilebilirlik denetiminden gecirme; otomatik ve manuel kontrol listesi; klavye, ekran okuyucu, kontrast, odak, form, ARIA denetimi."
category: accessibility
status: curated
confidence: high
requires: [browser-testing]
tags: [accessibility, a11y, wcag, screen-reader, keyboard, contrast, aria]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

WCAG 2.2 AA hedefiyle sitenin herkes tarafından kullanılabilir olmasını (görme, işitme, motor,
bilişsel engelli kullanıcılar dahil) sağlamak. Otomatik test + manuel kontrol birleşimi.

# Ne zaman kullan

- Her PR / her yeni sayfa sonrası
- Kabul testlerinde son adım
- Kurumsal/kamu projesi tesliminden önce (yasal yükümlülük)

# İş Akışı (AUTOMATED → KEYBOARD → SCREEN-READER → VISUAL → COGNITIVE → FIX → REPORT)

## 1. AUTOMATED — Otomatik tarama

- Playwright ile `@axe-core/playwright` çalıştır; violation'ları listele.
- Lighthouse "Accessibility" kategorisini çalıştır.
- HTML doğrulayıcıdan geçir (bozuk sözdizimi, kapanmamış etiket).
- Renk kontrastı otomatik olarak kontrol et (4.5:1 normal metin, 3:1 büyük metin ve grafik).

## 2. KEYBOARD — Klavye testi

- Sayfaya gir; Tab ile tüm etkileşimli öğelere ulaşılıyor mu?
- Odak hiçbir zaman kaybolmuyor/gizlenmiyor mu?
- Focus ring kaldırılmış mı? (focus-visible kullanmak koşulu ile outline kaldırılabilir.)
- Shift+Tab ile geri dönülebiliyor mu?
- Enter/Space tuşu button/link'te çalışıyor mu?
- Escape dialog/menu'yu kapatıyor mu?
- Trap focus (modal açıldığında dışına çıkılmamalı).
- Atla link (skip to content) var mı?

## 3. SCREEN-READER — Ekran okuyucu

- NVDA (Windows), VoiceOver (macOS/iOS) temel test.
- Sayfa yapısı: tek bir `<h1>`, mantıksal `h2-h3` akışı, landmark'lar (`<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`).
- Resim `alt` metni: bilgi veren resimlerde açıklama; dekoratif resimlerde `alt=""`.
- Formlarda her input'un `<label>` ile bağlı olması; hata mesajlarının `aria-describedby` ile duyurulması.
- ARIA yanlış kullanılmamalı: gereksiz `role` (doğal semantik varken), yanlış `aria-selected/aria-expanded`.
- Canlı bölgeler (`aria-live`) dinamik içerik için (toast, arama sonucu sayısı).

## 4. VISUAL — Görsel ve işitsel

- %200 zoom kaydırmasız çalışıyor mu?
- %400 zoom'da (WCAG Reflow 1.4.10) içerik 320px genişlikte okunuyor mu, iki yönlü kayma yok mu?
- Renk körü simülasyonu (protanopia/deuteranopia): sadece renkle kodlanmış bilgi (örn. "kırmızı hatalı"
  "yeşil doğru") ikon/metin ile desteklenmiş mi?
- Otomatik oynayan video 5 saniyeden uzunsa durdurma düğmesi var mı?

## 5. COGNITIVE — Bilişsel

- Açık ve tutarlı dil; jargonsuz, gereksiz karmaşık yapı yok.
- Hata mesajları sorunu açıklıyor ve nasıl düzeltileceğini söylüyor.
- Süre sınırı varsa uzatma imkanı.
- Animasyonlar kapatılabiliyor (reduced motion).
- Tutarlı navigasyon ve sayfa yapısı.

## 6. FIX → REPORT

Hataları şiddete göre sınıflandır: CRITICAL (engelli kullanıcı tamamen bloke) / HIGH / MEDIUM / LOW.
Her hata için: etkilenen WCAG kriteri, neden sorunlu, nasıl düzeltilir.

# Çıktı

- Axe/Lighthouse skorları
- Madde madde CRITICAL/HIGH/MEDIUM/LOW listesi
- Düzeltme önerileri
- Test edilen ekran görüntüleri/screen reader kayıtları (mümkünse)

# Kalite Kontrol Listesi

- [ ] axe-core ile otomatik tarandı
- [ ] Klavye ile tam gezinme testi yapıldı
- [ ] En az bir ekran okuyucu (VoiceOver/NVDA) ile test edildi
- [ ] Kontrast tüm metinlerde 4.5:1 (büyük 3:1)
- [ ] Sayfa yapısı (headings, landmark) doğru
- [ ] Form label ve hata duyurusu var
- [ ] Alt metin ve dekoratif `alt=""` doğru
- [ ] Focus ring görünür ve tutarlı
- [ ] %200 ve %400 zoom testi yapıldı
- [ ] Reduced-motion destekleniyor
- [ ] Tuzağa düşüren otomatik odak/ses yok

# Yaygın Hatalar

- Div/span'i buton yapmak (`<div onClick>` yerine `<button>`); klavye erişimi ve ARIA yok.
- Görseli sadece renkle kodlamak (kırmızı/yeşil durum rozeti).
- Placeholder'ı etiket olarak kullanmak.
- `outline: none` ile focus'u kaldırmak.
- Modal açıldığında focus'u trap etmemek (dış öğelere tab ile gidilir).
- `aria-label`'ı Türkçe ekran okuyucu testi yapmadan sadece İngilizce bırakmak.

# Referanslar

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- axe-core: https://github.com/dequelabs/axe-core
- WAI ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/

# İlgili Skill'ler

- `browser-testing`
- `frontend-design`
- `responsive-mobile`
- `animation-motion`
