---
name: frontend-design
version: 1.0.0
description: "Web arayuzu tasarlarken tutarlilik, hiyerarsi, okunabilirlik ve profesyonel gorunum icin izlenecek is akisi. Yeni sayfa/bilesen tasarlarken tetiklenir."
category: frontend
status: curated
confidence: high
requires: [design-system]
tags: [frontend, design, layout, hierarchy, typography, spacing, visual-quality]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

Ajanın sıfırdan bir arayüzü (sayfa veya bileşen) tasarlarken profesyonel, tutarlı, erişilebilir
ve karakterli sonuç üretmesini sağlamak. "İyi görünsün" genel tavsiyesi yerine ölçülebilir
kararlar listesi sunar.

# Ne zaman kullan

- Yeni sayfa (landing, pricing, dashboard, ürün detay, checkout) tasarımı
- Mevcut sayfanın görsel yeniden tasarımı
- Yeni bir bileşen seti kurulumu
- AI-slop tespiti sonrası yeniden tasarlama

# Ne zaman kullanma

- Sadece backend/API işleri
- Renk, tipografi, spacing kararları zaten tasarım sistemi tarafından tam olarak sabitlenmiş
  ve sadece o sisteme uyan küçük bir bileşen yazılıyorsa (bu durumda sadece `design-system`
  kurallarını uygula).

# Girdi

- Sayfanın amacı (dönüşüm mü, veri sunumu mu, form akışı mı?)
- Kullanıcı kitlesi (B2C, B2B, kamu, yaşlı kullanıcı, oyuncu...)
- Mevcut tasarım sistemi (token'lar, bileşenler)
- İçerik (metin, görsel, veri)
- Marka dili (renk, ton, varsa logo/illustrasyon)
- Referanslar (Linear, Stripe, Vercel gibi iyi örnekler; kopyalamadan ilke çıkarmak için)

# İş Akışı (RESEARCH → HIERARCHY → SYSTEM → COMPOSE → MOTION → VALIDATE)

## 1. RESEARCH — Bağlamı kur

1. Sayfanın birincil amacı ne? (cta: satın al / oku / kayıt ol / bak / veri gir)
2. Kullanıcı bu sayfada hangi soruyu cevaplamaya geliyor?
3. Başarılı benzer sayfaları (3–5 tane) incele: Stripe, Linear, Vercel, Notion, uygun olan sektör
   liderleri. Rengi kopyalama, ilkeleri çıkar:
   - Hiyerarşi nasıl kurulmuş? (başlık/alt başlık/metin/ikincil bilgi)
   - Boşluk ve ritim nasıl?
   - Göz hangi sırayla akıyor?
   - Hangi yerde görsel destek (illüstrasyon, ekran görüntüsü) kullanılmış?
   - CTA nasıl öne çıkarılmış, sayı ve konumu?
4. Proje `design-system` token'larını yükle (renk, tipografi, spacing, radius, shadow).

## 2. HIERARCHY — Sayfa hiyerarşisini kur

Sayfayı 3–5 katmanlı düşün:

1. **Odak (focal point):** Hero başlığı + CTA veya ana içerik kartı. Kullanıcı ilk baktığında bunu görmeli.
2. **Destekleyici:** Alt başlık, kısa açıklama, görsel/video. Odaktan sonra gelir.
3. **İçerik bölümleri:** Özellikler, sosyal kanıt, SSS, fiyatlandırma.
4. **İkincil:** İkincil CTA, footer linkleri, dil seçimi, yasal uyarı.
5. **Gezinme:** Üst navbar, sidebar, breadcrumb.

Her katman arasında görsel ağırlık farkı olmalı. Aynı renk/ağırlık/boşlukla her şeyi eşitlersen
düz (flat) bir görüntü çıkar.

## 3. SYSTEM — Token'ları tutarlı kullan

- **Renk:** En fazla 1 birincil + 1 ikincil + nötr palet (50-950). Aynı anda sayfada 3'ten fazla
  vurgu rengi olmasın.
- **Tipografi:** Başlık/metin için orantılı ölçek (1.20–1.33 modüler ölçek). Örn. 12, 14, 16, 20, 24, 30, 36, 48 px.
  Satır yüksekliği: başlıklarda 1.1–1.2, gövdede 1.5–1.6, küçük metinde 1.4.
- **Spacing:** 4 px taban ızgarası; boşluklar 4/8/12/16/24/32/48/64/96/128 px olmalı; keyfi `21px`/`37px` kullanma.
- **Radius:** Tutarlı birkaç değer: küçük (4–6), kart (8–12), büyük (16–20); hepsini aynı yapma
  ama her eleman için farklı da kullanma.
- **Shadow:** Hafif ve seyrek kullan; her kartta belirgin gölge yerine 1–2 katman belirgin +
  gerisi border/yumuşak gölge.
- **Typography ailesi:** Bir yazı ailesi (karakter) seç; başlık/gövde aynı ailede veya tamamlayıcı
  iki ailede olsun (karakter başlık + nötr gövde). Türkçe karakterleri (ğ, ı, İ, ş, ö, ü)
  iyi gösteren fontlar tercih et (Inter, Geist, Satoshi, Inter Tight, IBM Plex). Kaçın: Comic Sans,
  Papyrus, aşırı dekoratif fontlar.

## 4. COMPOSE — Kompozisyon

- **F-deseni / Z-deseni:** İçerik sayfaları için F-deseni (dikey kaydırma, başlık satırı), açılış
  sayfası için Z-deseni (başlık → görsel → özellik).
- **Negatif boşluk:** Öğeler arası nefes aldır; hiçbir bölüm sıkışık olmasın.
- **Grid ve hizalama:** Tek bir 12 kolonlu grid ve 8px boşluk tabanı kullan. Elemanlar yatay ve
  dikeyde birbirine hizalı olsun; kırık hizalama dikkat dağıtır.
- **Denge:** Görsel ağırlığı simetrik dağıt (sol büyük görsel + sağ metin, tersi de olabilir).
- **CTA:** Sayfada görünür birincil tek CTA; ikincil bağlantı metin olarak. Üçüncü CTA butonu
  sayfayı kirlilikten başka bir şey yapmaz.
- **Görseller:** Rastgele Unsplash yerine bağlama özel illüstrasyon, ekran görüntüsü veya çok
  basit grafik öğe.

## 5. MOTION — Ölçülü hareket

- Hareket bilgi veriyorsa yap; süs için yapma (bkz. `animation-motion` skill).
- `prefers-reduced-motion` destekle.
- Hız: 150–300 ms; ease-out veya cubic-bezier(0.2,0,0,1).
- Sayfa ilk yüklendiğinde 1'den fazla fade-up animasyonu zinciri YOK.
- Hover'da `scale-105` kullanmak yerine hafif shadow, renk veya yukarı kayma (2–4 px) kullan.

## 6. VALIDATE — Denetle

- **Gözden 3 adım uzaklaş:** Monitörden 1 metre geride dur; ilk 3 saniyede ne görüyorsun? O sayfanın
  ana mesajı olmalı.
- **Squint testi:** Gözlerini kıs; hangi öğe öne çıkıyor? O CTA/ana mesaj olmalı.
- **Kontrast:** Tüm metinler 4.5:1 (normal) veya 3:1 (büyük başlık) kontrastı sağlıyor mu?
- **Klavye navigasyonu:** Tab ile her etkileşimli öğe ulaşılabiliyor, focus ring görünüyor mu?
- **Türkçe metin:** Karakterler doğru görünüyor mu? Satır sonlarında kelime bölünmesi tuhaf mı?
- **Responsive:** 390/768/1024/1440px kırılımlarında bozulma var mı?
- **`ai-slop-detection` çalıştır.**

# Çıktı

- Sayfa kompozisyonu (bölüm/eleman listesi ve seviyesi)
- Kullanılan token'lar (renk, tipografi, spacing)
- Gerekirse kısa figma/kâğıt taslak açıklaması
- Kod (HTML/JSX), token'ları referans alarak
- Doğrulama checklist sonucu

# Kalite Kontrol Listesi

- [ ] Sayfa amacı tek cümlede yazıldı
- [ ] Hiyerarşi katmanları kuruldu (1–5 arası)
- [ ] Token'lar kullanıldı; keyfi renk/spacing/font yok
- [ ] Grid ve 8px boşluk tabanına uyuldu
- [ ] CTA hiyerarşisi net (birincil/ikincil)
- [ ] Türkçe karakter ve tipografi kontrolü yapıldı
- [ ] Kontrast ve temel a11y kontrolü yapıldı
- [ ] Responsive kırılımlar planlandı
- [ ] AI-slop taraması yapıldı ve temizlendi
- [ ] Referanslardan ilke çıkarıldı, birebir kopya yok

# Yaygın Hatalar

- **Hata:** Birden fazla ana renk ve her yerde gradient kullanmak.
  **Düzeltme:** Bir ana renk, bir vurgu; gradient'i sadece tek odak alanında.
- **Hata:** Her kart gölgeli ve yuvarlak, hepsi aynı "template" görünümünde.
  **Düzeltme:** Kart yüzeylerini çeşitlendir; bazıları düz border, bazıları hafif gölge, bazıları
  renk arka plan; sadece önemli ögeler öne çıksın.
- **Hata:** 72px başlık + 80px hero padding ilk ekranın yarısını boş bırakıyor.
  **Düzeltme:** Başlık/boşluk oranını koru ama mobilde aşağı çek; katmanları orantılı küçült.
- **Hata:** Uzun Türkçe kelimeler kutudan taşıyor, tire ile bölünmüyor.
  **Düzeltme:** `hyphens: auto` ve `overflow-wrap: break-word`; dar alanlarda daha kısa alternatif metin.
- **Hata:** Bileşenleri birebir Linear/Stripe'dan kopyalamak.
  **Düzeltme:** İlke al, uyarlama yap. Aynı mavi rengi kullanmak yerine "tek birincil renk + yumuşak
  gölge + ince border" ilkesini kendi renginle uygula.

# Örnek

**Görev:** Bir SaaS için landing page (Türkiye pazarına yönelik, proje yönetim aracı).

1. **Bağlam:** B2B; karar verici ofis çalışanı; ana CTA "Ücretsiz dene"; referanslar Linear ve Asana.
2. **Hiyerarşi:**
   - Katman 1 (odak): "Türkiye'nin en hızlı proje takip aracı" + 14 gün ücretsiz CTA + kısa alt açıklama.
   - Katman 2: Ürün ekran görüntüsü (sağda).
   - Katman 3: 3 temel özellik, 3 müşteri alıntısı.
   - Katman 4: Fiyatlandırma, SSS.
   - Katman 5: Footer, yardım linkleri.
3. **Token:** Birincil renk #1D4ED8 (mavi), nötr palet slate, Inter font, radius lg (8px), spacing 8px taban.
4. **Kompozisyon:** Z-deseni; iki sütun hero; 3 kolon özellik; stack teklifler.
5. **Hareket:** Hafif fade-in (200 ms) ilk görselde; CTA hover'da gölge artışı ve hafif yukarı kalkma (2px); scroll-trigger yok.
6. **Doğrula:** Kontrast, tab ile navigasyon, 390/768/1440, Türkçe metinler, slop taraması.

# Referanslar

- Refactoring UI — Adam Wathan & Steve Schoger
- Linear design: https://linear.app/
- Stripe design: https://stripe.com/design
- Vercel design: https://vercel.com/design
- Bu KB: `knowledge/ui-ux/`, `patterns/`, `anti-patterns/`

# İlgili Skill'ler

- `design-system`
- `ai-slop-detection`
- `responsive-mobile`
- `accessibility-audit`
- `animation-motion`
- `website-quality-review`
