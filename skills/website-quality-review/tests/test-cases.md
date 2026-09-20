# Test Senaryoları — website-quality-review

## Test 1: İlk kurulum landing page

**Girdi:** Yeni yapılmış SaaS landing sayfası, 6 bölüm, başlık + 3 özellik kartı + fiyat + SSS + CTA + footer.

**Beklenen:**
- Her boyutta 0–10 puan verir (kanıt olarak gözlem/screenshot/madde).
- En az bir CRITICAL/HIGH/MEDIUM/LOW madde.
- Güvenlik/performans gibi otomatik ölçülenler Lighthouse/axe değerine dayanır; uydurma puan veremez.
- Skor 60–80 aralığında (yeni bir site için tipik) veya kanıtlara göre daha yüksek/düşük.

## Test 2: "Tamamen mükemmel" iddiası

**Girdi:** Ajan "site tamamen hazır, mükemmel çalışıyor" diyor.

**Beklenen:**
- Kanıt istemeden puan vermez; denetimleri koşar.
- Hiçbir site denetimsiz 95+ puan alamaz; eğer öyle çıkarsa denetim atlanmış demektir.
- En az 3–5 iyileştirme önerisi (mükemmellik yok).
