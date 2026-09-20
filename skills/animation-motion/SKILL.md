---
name: animation-motion
version: 1.0.0
description: "Hareket ve animasyonun ne zaman faydali ne zaman zararli oldugunu ayirt etme; reduced-motion destegi, performans, mobil fallback; amaca hizmet eden, olculu animasyon."
category: frontend
status: curated
confidence: high
requires: [frontend-design]
tags: [motion, animation, reduced-motion, performance, transition]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

Gereksiz, dikkat dağıtıcı ve performans düşüren animasyonları önlemek; amaca hizmet eden
hareketleri ölçülü kullanmak. Her animasyon "niçin?" sorusuna cevap vermeli.

# Ne zaman kullan

- Durum değişikliklerini görünür kılmak (açılır/kapanır, eklenir/silinir)
- Konum veya bağlam değişimini aktarmak (sayfa geçişi, liste sıralaması)
- Mikro-geribildirim (buton basıldı, kopyalandı, kaydedildi)
- Dikkat çekilmesi gereken ama rahatsız etmeyecek yoğunlukta işaretler

# Ne zaman kullanma

- Süs için (sayfa kaydırdıkça her bölüm yukarı kayması, gereksiz parallax, büyük animasyonlu arka plan)
- Dikkati dağıtıcı, eğlendirmekten başka işlevi yoksa
- Kullanıcı bir işi yapmaya çalışırken (form doldururken kayan animasyonlar)
- Kritik veri sunumunda (grafik animasyonu veriyi geciktiriyorsa)

# İş Akışı (PURPOSE → CHOICE → DURATION → PERF → A11Y → VALIDATE)

## 1. PURPOSE — Amacı belirle

Animasyonsuz versiyonda kullanıcı neyi kaçırıyor?
- Açılır menü nereden geliyor? → Amaç: bağlam.
- Butona bastım işlendi mi? → Amaç: feedback.
- Yeni öğe eklendi, nerede? → Amaç: dikkat.
- Sıradaki ekrana geçiyorum → Amaç: yön/yönelim.

Amacı yoksa animasyonu kaldır.

## 2. CHOICE — Animasyon türünü seç

- **Transform (translate/scale/rotate)** + **opacity** kullan; layout (width/height/top/left) ve
  renk (color/background-color) animasyonlarından kaçın. Maliyet ve GPU hızlandırma farkı var.
- Kullanım yerine göre:
  - Açılır/kapanır: opacity + translateY 8px; 200ms ease-out.
  - Liste öğesi eklenir/silinir: yumuşak fade + 12-20px kayma; exit animasyonu (AnimatePresence).
  - Buton basımı: scale 0.98 + hafif renk koyulaşması; 120ms.
  - Sayfa geçişi: basit fade-in veya 8-16px giriş; 200ms.
  - Sayım/metrik: isteğe bağlı sayı animasyonu 600ms; çok gösterişli değil.

## 3. DURATION & EASING — Süre ve eğri

- Hızlı geri bildirim: 100–200 ms (buton, link, focus)
- Orta: 200–350 ms (açılır/kapanır, kart)
- Yavaş (dikkat çekme): 400–600 ms (modal, panel); çok kullanmaktan kaçın.

Easing:
- `cubic-bezier(0.2, 0, 0, 1)` (ease-out): eleman ekrana gelirken doğal his.
- `cubic-bezier(0.4, 0, 0.2, 1)` (material ease): standart.
- `linear`: sadece sürekli/tekrarlayan animasyonlar (spinner, shimmer).

## 4. PERF — Performans

- Sadece `transform` ve `opacity` animate et.
- `will-change: transform` dikkatli kullan; sadece animasyon esnasında.
- Büyük ağaçta layout thrashing'e sebep olma (her kare layout ölçümü yapma).
- Ana thread'i bloklamaması için `requestAnimationFrame` / CSS transition; React'te Framer Motion
  kullan, ama her öğeye `motion.*` ekleme.
- GPU katmanı taşmasına dikkat (çok fazla `translateZ` veya `will-change` hafıza şişirir).
- Mobilde 60 FPS hedefle; 30 FPS'yi geçmeyen ağır animasyonlar için ya basitleştir ya da kaldır.

## 5. A11Y — Reduced motion

- `prefers-reduced-motion: reduce` varsayılanında tüm dönme/solma/sıçrama animasyonlarını kaldır;
  sadece opaklık geçişlerini (ve onları bile çok kısa) veya tamamen statik bırak.
- Otomatik oynayan video/animasyon (5 saniyeyi geçen) durdurma/kontrol düğmesi olmalı.
- Parlak ışık yanıp sönmesi (flashing) erişilebilirlik riskidir; kaçının.

## 6. VALIDATE

- Animasyon açıkken FPS ölç (Chrome devtools Performance).
- Reduced-motion açıkken test et: rahatsız edici hareket kalmamalı.
- İşlem bitti mi? (spinner dönmeye devam etmemeli, unmount sonrası temizlenmeli).
- Klavye ile gezinirken animasyon focus'u takip ediyor mu (focus ring hemen görünmeli, animasyon arkasına gizlenmemeli).

# Kalite Kontrol Listesi

- [ ] Her animasyonun bir nedeni var; süs için yok
- [ ] Süre 100–600 ms arasında
- [ ] Transform/opacity ile animasyon yapılıyor; layout animasyonu kaçınılmış
- [ ] Reduced-motion destekleniyor
- [ ] Mobilde 60 FPS korunuyor
- [ ] Otomatik-dönen/sonsuz animasyonlar kontrol edilebiliyor
- [ ] Yanıp sönen/parlak öğe yok
- [ ] Sayfa açılırken 1'den fazla zincir animasyon yok
- [ ] Hover scale %5'ten fazla değil ve shadow ile destekleniyor (ya da hiç yok)

# Yaygın Hatalar

- **Hata:** Her bölüm scroll'da yukarı kayarak geliyor (Framer Motion fade-up).
  **Düzeltme:** Sadece ilk ekran ve gerçekten dikkat çekilecek bölümlerde kullan; tercihen hiç yok.
- **Hata:** Sürekli dönen 3D nesne / gradient arka plan (dikkat dağıtıcı, GPU yiyor).
- **Hata:** Reduced-motion'u desteklememek.
  **Düzeltme:** Global CSS'de `@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } }` benzeri bir reset.
- **Hata:** Hover'da her karta `scale-105` ve parlak glow.
  **Düzeltme:** Hafif gölge veya yukarı 2-3px kayma, düşük süre (150 ms).
- **Hata:** Modal 600ms bounce ile açılıyor (yavaş ve "yapay AI" hissi).
  **Düzeltme:** 200ms ease-out, basit yumuşak giriş.

# Referanslar

- Material Motion: https://m2.material.io/design/motion/understanding-motion.html
- IBM Carbon Motion: https://carbondesignsystem.com/guidelines/motion/principles/
- Linear motion (ölçülü referans): https://linear.app/
- Bu KB: `patterns/transitions.md`, `anti-patterns/excessive-motion.md`

# İlgili Skill'ler

- `frontend-design`
- `ai-slop-detection`
- `performance-audit`
- `accessibility-audit`
