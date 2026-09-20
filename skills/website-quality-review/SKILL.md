---
name: website-quality-review
version: 1.0.0
description: "Teslim oncesi butunlesik kalite denetimi: gorsel, UX, mimari, performans, erisilebilirlik, responsive, animasyon, metin, SEO, guvenlik. SKOR + CRITICAL/HIGH/MEDIUM/LOW + Oneriler."
category: quality
status: curated
confidence: high
requires: [ai-slop-detection, frontend-design, accessibility-audit, seo-audit, performance-audit, security-audit, responsive-mobile, browser-testing]
tags: [quality, review, audit, final-check, acceptance, score]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

Herhangi bir web sitesini/dashboard'u teslimden önce bütüncül kalite denetiminden geçirmek.
Diğer audit skill'lerinin çıktısını birleştirerek tek bir skor ve öncelikli eylem listesi vermek.

# Ne zaman kullan

- Her demo/milestone öncesi
- Müşteri/müdür tesliminde "bitti" demeden önce
- AI ajan "bitti" dediğinde

# İş Akışı (RUN-AUDITS → SCORE → PRIORITIZE → REPORT)

## 1. Bireysel denetimleri sırayla çalıştır

Her ilgili skill'i tetikle ve sonuçlarını topla:

1. **AI-slop detection:** Görsel jeneriklik, kopya kalite, animasyon ölçüsü.
2. **Frontend/Design:** Hiyerarşi, renk/tipografi/spacing tutarlılığı, tasarım sistemine uyum.
3. **Responsive:** 390/768/1024/1440 px kırılımları, dokunma hedefleri.
4. **Accessibility:** WCAG 2.2 AA (axe + klavye + ekran okuyucu).
5. **Performance:** Core Web Vitals, bundle boyutu, Lighthouse.
6. **SEO:** Teknik SEO, meta, structured data, TR yerelleştirme.
7. **Security:** Header/secret/RLS/auth/XSS hızlı tarama.
8. **Animasyon/motion:** Ölçülü hareket, reduced-motion.
9. **Metin/Kopya:** Türkçe doğallık, çeviri hataları, jenerik CEA ("Get started" kalıntıları), sahte metrik.
10. **Mimari/Kod:** TypeScript katı, any yok, tekrar yok, veri akışı tutarlı, test var.
11. **Browser/Çalışma:** Chrome, Safari, Firefox temel akış testi.
12. **İçerik/Yasal:** KVKK, Mesafeli Satış, çerez politikası, iletişim bilgileri (e-ticaret/kurumsal).

## 2. SKOR hesapla

Her boyut 0–10 puan. Ağırlıklı ortalama toplam 0–100:

| Boyut | Ağırlık |
|------|--------|
| Görsel kalite (slop + design) | 15 |
| Erişilebilirlik | 12 |
| Performans (CWV) | 12 |
| Responsive/Mobil | 10 |
| SEO | 8 |
| Güvenlik | 15 |
| Metin/Kopya | 8 |
| Mimari/Kod | 10 |
| Animasyon/Ölçü | 5 |
| Yasal/İçerik uygunluğu | 5 |

- 90–100: Üretim hazır, çok iyi.
- 75–89: İyi, küçük iyileştirmelerle çıkabilir.
- 60–74: Kabul edilebilir ama HIGH maddeleri düzeltmeden çıkmamalı.
- 40–59: Önemli sorunlar var; teslim ertelenmeli.
- <40: Kabul edilemez; yeniden gözden geçir.

## 3. Öncelikli maddeleri grupla

- **CRITICAL:** Yayın engelleyici; güvenlik açığı, bozuk sayfa, kontrast 0, kırık checkout, beyaz ekran, secret sızıntısı.
- **HIGH:** Belirgin sorun; a11y ciddi ihlal, CWV kırmızı, mobil bozuk, AI-slop 40 altında.
- **MEDIUM:** İyileştirme alanı; metin doğallığı, küçük UX, animasyon ayarı.
- **LOW:** Rötuş; küçük spacing, ikon değişimi, mikro-kopya.

## 4. Raporla

Şablon:

```
## WEB SİTESİ KALİTE RAPORU
URL / sürüm / tarih

GENEL SKOR: XX/100 (derece)

---
### SKORLAR
- Görsel kalite: X/10
- Erişilebilirlik: X/10
- Performans: X/10
- Responsive: X/10
- SEO: X/10
- Güvenlik: X/10
- Metin/Kopya: X/10
- Mimari/Kod: X/10
- Animasyon: X/10
- Yasal: X/10

---
### CRITICAL (hemen düzelt)
- ...
### HIGH
- ...
### MEDIUM
- ...
### LOW
- ...

---
### ÖNERİLER (somut)
- ...
```

# Çıktı

- Yukarıdaki formatta rapor
- Varsa screenshot ve Playwright kaydı referansları
- Öncelik sıralı düzeltme listesi

# Kalite Kontrol Listesi

- [ ] Tüm alt denetimler uygulandı
- [ ] Skor her boyutta dolduruldu
- [ ] Önceliklendirme net (CRITICAL/HIGH/MEDIUM/LOW)
- [ ] Her öneri somut (renk kodu, piksel, düzeltme yolu)
- [ ] Hiçbir "bence" kanıtsız kalmadı
- [ ] Çözüm sonrası aynı denetim tekrar çalıştırılacak şekilde not alınmış

# Yaygın Hatalar

- Sadece yüzeysel bakıp "iyi görünüyor" demek (a11y/güvenlik/SEO kontrol edilmemiş).
- Ağırlıkları ters vermek (güvenlik düşük ama görsel yüksek).
- Skoru yüksek verip CRITICAL madde bırakmak.
- Önerilerin muğlak olması ("daha iyi olabilir", "biraz geliştir").
- Duygusal/öznel yorumlar yerine kanıta dayalı olmamak.

# İlgili Skill'ler

- Bu skill diğer tüm denetim skill'lerini koordine eden bir "üst denetim"dir.
