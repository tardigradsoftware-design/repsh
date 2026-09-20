# Anti-Pattern: AI Slop Görsel Tuzağı

## Yaygın belirtiler
- Mor/pembe/mavi geçişli gradient her yerde (hero, kart başlığı, buton);
- Aşırı glow / ışık sızması;
- glassmorphism şeffaf kartlar;
- `rounded-3xl` her kart; `rounded-full` her buton;
- `hover:scale-105` bütün interaktif öğede;
- Her özellik kartında sparkle/rocket/shield/zap ikonu;
- "Supercharge your workflow", "Build faster", "AI-powered" gibi jenerik başlıklar;
- Sahte metrikler ("%99.9 uptime", "10x faster", "5000+ müşteri") kanıtsız.

## Neden kötü?
- Güven vermez; ziyaretçi "bu bir şablon/AI sitesi" diye düşünür ve çıkar.
- Marka farklılaşmaz; her yeni girişim sitesi birbirine benzer.
- Okunurluk ve kontrast düşer; cam/gradient arkasında metin zor okunur.
- Performansı düşürür (büyük gradient, glow filtreleri GPU/CPU tüketir).

## Nasıl fark edilir?
- Skrini uzaklaştır/squint testi; her bölüm aynı "renk cümbüşü" ise slop.
- 3 ayrı kullanıcıya "bu site ne yapıyor, hangi firmanın?" diye sor; cevap veremiyorlarsa
  marka iletişimi zayıf ve slop ihtimali yüksek.
- `ai-slop-detection` checklist'inden 5+ madde işaretleniyorsa.

## Nasıl düzeltilir?
- Bir tek ana marka rengi; gradient yalnız tek (hero) vurgu alanında.
- Kartlar düz, hafif border ve düşük gölge; radius `rounded-xl` ile sınırla.
- İkonları özelleştir (marka rengine boya veya illüstrasyon kullan); her karta ikon koyma zorunda değilsin.
- Başlığı somut faydaya çevir: "İstanbul içi teslimatta 24 saatte kargoda" gibi.
- Kanıtlanmamış metrikleri kaldır; gerçek veri veya müşteri alıntısı koy.
- Hover animasyonunu scale değil hafif shadow ve 2px yukarı kalkma; 150 ms.

## İlgili
- `ai-slop-detection`, `frontend-design`, `animation-motion`
