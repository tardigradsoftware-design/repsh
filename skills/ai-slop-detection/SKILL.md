---
name: ai-slop-detection
version: 1.0.0
description: "Uretilmis yapay zeka arayuzlerini (jenerik, ai-slop) tespit et, nedenini acikla, somut duzeltme oner, yeniden yaz ve gozden gecir. Her gorsel cikti uzerinde uygulanir."
category: quality
status: curated
confidence: high
requires: []
tags: [ai-slop, visual-quality, design-review, anti-patterns, quality]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

AI ajanlarının ürettiği jenerik, "yapay zeka yapmış" hissi veren siteleri ve bileşenleri tespit
etmek; neden AI-slop olduğunu açıklamak; somut, ölçülebilir düzeltmeler önermek ve son çıktıyı
gözden geçirmek.

# Ne zaman kullan

- Herhangi bir görsel UI çıktısından sonra (landing, dashboard, e-ticaret, email template)
- PR incelemesinde görsel kalite kontrolü yaparken
- Tasarım sistemi ilk kurulduktan sonra referans sayfaları denetlerken
- "Bu site hazır şablon gibi duruyor" şikayeti geldiğinde

# Ne zaman kullanma

- Salt backend/API kodu (UI yok)
- Teknik CLI çıktıları
- Veri ve şema değişiklikleri

# Girdi

- Screenshot (Playwright MCP ile alınmış, birden fazla viewport: mobil/tablet/desktop)
- Sayfanın HTML/CSS/JS kaynak kodu (veya ilgili bileşenler)
- Varsa hedef referans (marka kılavuzu, benzer iyi örnekler)

# İş Akışı (DETECT → EXPLAIN → RECOMMEND → REWRITE → REVIEW)

## 1. DETECT — Tespit

Aşağıdaki belirtileri checklist ile tara. Her belirti için skoru 0 (yok) – 3 (belirgin) puanla.

### Renk ve yüzey
- [ ] **Gereksiz gradient kullanımı:** Her kartta / her başlıkta aynı mor-mavi (indigo-violet) gradient.
- [ ] **Glassmorphism gereksiz yere:** Şeffaf backdrop-blur kartlar, içerikle hiçbir hiyerarşi yok.
- [ ] **Aşırı büyük glow/ışık sızması:** Kutu arkasında dağınık renk glow, okunabilirliği düşürüyor.
- [ ] **Siyah-beyaz iki uç arasında kalmış gri palet:** Ya tam #000/#fff ya da 50 ton gri; renk yok.
- [ ] **Kontrast sorunlu açık-mor/açık-mavi birincil renkler:** Butonlar okunmuyor.

### Tipografi
- [ ] **Varsayılan Inter veya system font, hiçbir tipografik karar yok:** Satır yüksekliği, harf aralığı,
      başlık/metin oranı varsayılandan değiştirilmemiş.
- [ ] **Aşırı büyük hero başlığı:** 72-96px, "Build better X faster" türü anlamsız sözler.
- [ ] **H1 ve H2 arasında görsel hiyerarşi yok:** Boyut farkı az, ağırlık aynı.
- [ ] **Tüm metin tek satırda kesiliyor (line-clamp-1/2):** Kullanıcı içeriği göremiyor.
- [ ] **Tırnaklı / tırnaksız apostrof karışıklığı; Türkçe karakter hataları** (ı/i, ş/ã vb.).

### Düzen ve boşluk (spacing)
- [ ] **Her kartta aynı `p-6 rounded-xl shadow-lg`:** Tek tip, görsel ritim yok.
- [ ] **Aşırı yuvarlak köşeler:** `rounded-2xl/3xl/full` her yerde; kartlar gibi butonlar da tam yuvarlak.
- [ ] **Bölümler arası boşluklar keyfi:** `py-24` her section'da; içerik akışı yok.
- [ ] **Container her zaman ortada ve `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8` şablonu** — özgün yerleşim yok.
- [ ] **Grid 3 kolon, 3 özellik, 3 adım, 3 müşteri logosu** gibi otomatik şablon yapısı.

### İçerik ve kopya
- [ ] **Sahte/sallama metrikler:** "%99.9 uptime", "10x faster", "5000+ mutlu müşteri" — kanıtsız.
- [ ] **Anlamsız rozetler:** "Powered by AI", "Yeni", "Pro", "Beta" her kartın köşesinde.
- [ ] **Jenerik başlıklar:** "Welcome to the future", "Supercharge your workflow", "Build X faster".
- [ ] **Lorel ipsum / placeholder ikonlar:** Tüm boşluklar Lucide imleç veya sparkles ikonu ile dolu.
- [ ] **Tekrarlayan ikonlar:** Rocket, zap, shield, check-circle, sparkle — her özellikte aynı set.
- [ ] **Müşteri logoları:** Tanınmayan veya yapay isimler ("Acme Corp", "Globex"); gerçek sosyal kanıt yok.

### Hareket (motion)
- [ ] **Scroll-triggered fade-up her bölümde:** İzleyici alışıyor, anlamı kalmıyor.
- [ ] **Gereksiz hover scale:** Her karta `hover:scale-105` — tıklanabilir hissi gerçek değil.
- [ ] **Sonsuz kayan logo dizisi:** Kullanıcı ürüne bakmıyor logo kayıyor.
- [ ] **Reduced-motion desteği yok:** `prefers-reduced-motion` kontrol edilmemiş.

### Form ve etkileşim
- [ ] **Tek input + "Subscribe" hero formu:** Hiçbir değer önerisi yok, tek işlevi e-posta toplamak.
- [ ] **Aynı CTA:** Her bölümde "Get started" / "Learn more" — bağlam yok.
- [ ] **Loading, empty, error state yok:** Tüm kartlar dolu ve mükemmel görünüyor.

### Kod ve yapı
- [ ] **Tailwind sınıfları tamamen varsayılan renkleri kullanıyor:** `bg-indigo-500`, `text-violet-600`,
      `from-purple-400 to-pink-600` gibi — marka rengi yok, CSS değişkeni (token) yok.
- [ ] **Tüm bileşenler shadcn/ui varsayılan stilleriyle:** Özelleştirme sıfır.
- [ ] **Şişkin ve tekrar eden JSX:** 6 özellik kartı tek tek elle yazılmış, map yok.
- [ ] **Görseller Unsplash rastgele görselleri:** Aynı takım/toplantı/fotoğrafları.

## 2. EXPLAIN — Neden kötü?

Her tespit için açıkla:

1. **Bu deseni neden AI sıklıkla üretir?** (Eğitim verisinde çok var, tok-token en olası seçim, jenerik güvenli.)
2. **Neden sorunlu?** (Markayı benzersiz kılmaz, güven vermez, okunabilirliği düşürür, profesyonel durmaz.)
3. **Nerede yanlış?** (Kontrast, hiyerarşi, kültürel dil, bağlam eksikliği.)

## 3. RECOMMEND — Somut düzeltme

Her sorun için ölçülebilir, somut öneri ver:

- Renk: "Ana renk olarak tek bir marka rengi seç (ör. #0F766E teal veya #1D4ED8 mavi); ikincil ve nötr
  paleti tanımla; gradient'i sadece tek bir hero arka planında kullan."
- Tipografi: "Başlık/metin oranını 1.25 modüler ölçeğe göre ayarla; satır yüksekliği başlıkta 1.1,
  gövdede 1.5–1.6; fontu Inter dışında bir alternatifle (Satoshi, Geist, Inter Tight) özelleştir."
- Spacing: "Kart yuvarlaklığını `rounded-xl` ile sınırla; bölümler arası boşluğu 4/8/16/24/48 px
  tabanlı bir 8px ızgaraya oturt; her bölüm aynı `py-24` yerine içeriğe göre 48–96 px arasında değiştir."
- Kopya: "Tüm 'Build faster' ve 'AI-powered' ifadeleri kaldır; yerine kullanıcının somut faydası
  yazsın ('Türkiye'nin fatura sürecini 3 adımda tamamla', 'Kargo takibini tek panelden gör')."
- Hareket: "Hover scale'leri kaldır veya %2 yerine %5 oranla ve gölge artışıyla destekle; scroll
  animasyonlarını sadece gerçekten bilgi ekleyen bölümlerde kullan; reduced-motion'a uyu."
- Kod: "Renk ve spacing token'larını CSS değişkenleriyle tanımla; shadcn/ui bileşenlerini tema
  üstünden özelleştir; tekrar eden kartları `features.map(...)` ile döndür."

## 4. REWRITE — Yeniden yaz

- Düzeltmeyi doğrudan uygula (kod/HTML/Tailwind).
- Değişikliğin önce/sonra karşılaştırması için 2 screenshot al (eskisi + yenisi).
- Her değişikliği commit'le veya açık bir yama (patch) olarak bırak.

## 5. REVIEW — Son kontrol

Düzeltmeden sonra skoru yeniden hesapla. İyileşme yoksa adım 3–4'i tekrarla.
Ayrıca aşağıdakilere bak:
- Aşırı düzeltme yapıp karakteri bozmuş muyuz? (soğuk, sıkıcı, kurumsal gri de bir başka tuzak)
- Türkçe metin doğal duruyor mu? Çeviri kokuyor mu?
- Gerçek bir markanın kimliğini taşıyor mu, yoksa yine jenerik mi?

# Çıktı

- **SKOR:** 0–100 arası (100 = tamamen doğal ve profesyonel, 0 = saf AI-slop).
- **KRİTİK:** Anında düzeltilmesi gerekenler (okunurluk, kontrast, sahte metrikler).
- **HIGH:** Belirgin jeneriklik belirtileri.
- **MEDIUM:** İyileştirme alanları.
- **LOW:** Küçük rötuşlar.
- **ÖNERİLER:** Madde madde somut düzeltmeler.
- **ÖNCE/SONRA:** Screenshot referansı.

# Kalite Kontrol Listesi

- [ ] Checklist'in tamamı dolduruldu
- [ ] Her "kötü" işaretin neden-sonuç ilişkisi açıklandı
- [ ] Öneriler muğlak değil, ölçülebilir (renk kodu, px değeri, font adı, metin örneği)
- [ ] Yeniden yazma yapıldı
- [ ] Önce/sonra mevcut
- [ ] Türkçe metinlerin doğallığı ve karakter uyumu denetlendi
- [ ] Reduced-motion ve erişilebilirlik unutulmadı
- [ ] Sahte metrikler ya kanıtlandı ya da kaldırıldı

# Yaygın Hatalar

- **Hata:** "Bu AI yapmış" demek ama nedenini göstermemek.
  **Düzeltme:** Her iddia için kanıt noktası (kontrast, spacing, metin kopyası) göster.
- **Hata:** Her şeyi "kötü" ilan edip somut öneri sunmamak.
  **Düzeltme:** Her madde için "şöyle olmalı" kısmını yaz.
- **Hata:** Aşırı düzeltme: tüm renk/animasyonu kaldırıp sıkıcı bir sayfa çıkarmak.
  **Düzeltme:** Karakterli, özgün ama ölçülü bir denge kur. Az ve yerinde animasyon, doğru renk.
- **Hata:** Türkçe metinleri görmezden gelip İngilizce odaklı düzeltme yapmak.
  **Düzeltme:** Türkçe karakterler, uzun kelimeler, fiyat/tarih biçimi kontrol edilmeli.

# Örnek

**İncelenen sayfa:** Yeni bir SaaS landing page (screenshot alındı).
**Tespitler:**
- Hero'da mor-pembe gradient + glow + cam kart (3 puan)
- Tüm özellik kartları `p-6 rounded-2xl shadow-lg` (2 puan)
- "Supercharge your workflow" başlığı ve "%40 faster" sahte metrik (3 puan)
- Her kartta sparkle/zap/shield ikonları (2 puan)
- Sonsuz kayan müşteri logoları (1 puan)
- Türkçe'ye çevrilmemiş "Get started" CTA (3 puan)

**İlk skor:** 35/100 (belirgin AI-slop)

**Düzeltmeler:**
1. Hero gradient'ini kaldır; yerine marka rengi (koyu lacivert #0B1220) arka plan + tek vurgu
   noktasında yumuşak bir ışıma kullan.
2. Özellik kartlarını ikiye ayır: bazıları vurgulu büyük kart (daha fazla padding, görsel öge),
   bazıları daha kompakt. `rounded-xl` ve hafif border kullan; shadow'u yumuşat.
3. Başlığı somut faydayla değiştir: "Türkiye'deki KOBİ'lerin fatura ve tahsilat sürecini %40 hızlandırın"
   — ama eğer %40 kanıtlanmamışsa "süreci kısaltın" olarak değiştir.
4. İkonları özgün illüstrasyon veya tek renkli, marka rengine boyanmış minimal line icon'lar ile
   özelleştir; her karta ikon koyma zorunluluğunu kaldır.
5. Kayan logoları kaldır; yerine 4–6 gerçek referans (logo + kısa alıntı) koy.
6. CTA'yı Türkçeleştir: "14 gün ücretsiz dene" ve yanında "Demo talep et".

**Skor sonrası:** 78/100. İyileşme var; renkler ve tipografi hâlâ özelleştirilmeli.

# Referanslar

- Stripe Design: https://stripe.com/blog/design-tips
- Linear tasarım dili: https://linear.app/ (örnek: sadelik, hareket ölçüsü)
- Vercel design: https://vercel.com/design
- Bu KB: `anti-patterns/ai-slop.md` (henüz yazılacak), `knowledge/ui-ux/`, `patterns/`
- Refactoring UI (Adam Wathan & Steve Schoger)

# İlgili Skill'ler

- `frontend-design`
- `design-system`
- `website-quality-review`
- `accessibility-audit`
- `animation-motion`
