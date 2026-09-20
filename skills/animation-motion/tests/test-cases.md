# Test Senaryoları — animation-motion

## Test 1: Aşırı scroll animasyonu

**Girdi:** Ajan landing page'de 6 ayrı bölüme `initial="hidden" animate="visible" whileInView` ile
bölümü kaydırdıkça fade-up uyguluyor.

**Beklenen:**
- Bunu gereksiz olarak tespit eder; sadece hero ve CTA bölümü gibi 1–2 kritik yerde bırakır,
  diğerlerinde kaldırır veya sadece hafif opacity geçişi (150ms) ile sınırlar.
- `prefers-reduced-motion` medya sorgusu ekler.
- Performans etkisini değerlendirir (6 bölümlük zincir animasyon 60 FPS'i bozmuyor mu?).

## Test 2: Hover'ın aşırı kullanımı

**Girdi:**
```css
.card:hover { transform: scale(1.10); box-shadow: 0 25px 50px -12px rgba(0,0,0,.25); transition: all 600ms; }
```

**Beklenen:**
- `scale(1.02-1.05)`e çeker, süreyi 150-200 ms'e düşürür.
- Ya da tamamen kaldırır: scale yerine hafif shadow artışı ve 2 yukarı kayma daha ölçülüdür.
- Mobilde hover olmadığını not eder; dokunma için ayrı state gerek.
- `all` yerine spesifik `transform, box-shadow` geçişi belirtir.
