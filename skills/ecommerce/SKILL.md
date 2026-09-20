---
name: ecommerce
version: 1.0.0
description: "E-ticaret siteleri icin urun listesi, urun detay, sepet, odeme akisi, stok/siparis modeli, guvenlik, donusum odakli UX, fatura/ERP entegrasyonu kalip ve kontrolleri."
category: frontend
status: curated
confidence: high
requires: [frontend-design, design-system, security-audit, seo-audit, responsive-mobile]
tags: [ecommerce, payment, cart, checkout, turkey, iyzico, paytr, fatura, erp, conversion]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

E-ticaret sitelerinde dönüşüm odaklı, güvenli, yasal uyumlu ve hızlı kullanıcı deneyimi sağlamak.
Türkiye pazarına özgü ödeme, fatura, kargo, KVKK ve i18n gerçeklerini gözetmek.

# Ne zaman kullan / kullanma

**Kullan:** Perakende satış, dijital ürün, abonelik SaaS, B2B sipariş portalı.
**Kullanma:** İçerik/blog, pazarlama sitesi (sipariş akışı yoksa).

# İş Akışı (CATALOG → PRODUCT → CART → CHECKOUT → PAYMENT → ORDER → POST)

## 1. CATALOG — Ürün listesi
- Filtreleme: kategori, fiyat aralığı, marka, özellik, stok durumu; çoklu seçim; aktif filtre chip'leri.
- Sıralama: popülerlik, yeni, fiyat artan/azalan, indirim oranı.
- Ürün kartı: resim (lazy-load, aspect-ratio), ad, fiyat, indirim, taksit bilgisi, yıldız (varsa),
  hızlı sepete ekle (hover veya ikincil buton).
- Görünüm: ızgara/liste; mobilde tek kolon, sonsuz kaydırma veya sayfalama.
- URL: kategori slug, filtreler query string'de (SEO için kalıcı URL önemli).

## 2. PRODUCT — Ürün detay
- Galeri (ana resim + küçükler; zoom; mobilde swipe; video varsa).
- Başlık, kısa açıklama, fiyat (eski fiyat üstü çizili, indirim %), taksit tablosu, stok durumu,
- Varyant seçimi: beden/renk (seçili olan belirgin; stokta olmayan pasif).
- Adet artır/azalt; "Sepete ekle" birincil büyük CTA; "Hemen al" ikincil (tek adım checkout).
- Güvence rozetleri: kargo süresi, iade süresi, güvenli ödeme.
- Açıklama sekmeleri: açıklama, özellikler, yorumlar, kargo/iade, taksit.
- İlgili ürünler / birlikte alanlar aldı / en çok satan.
- Structured data (Product, Offer, AggregateRating) → SEO için zorunlu.
- Türkçe: "Kargo bedava", "Taksit seçenekleri", "Stokta var / Son X ürün".

## 3. CART — Sepet
- Mini sepet (header'dan açılır), tam sepet sayfası.
- Ürün resmi, adı (link), varyant, adet kontrolleri, birim fiyat, toplam.
- Kupon kodu alanı; kargo bedeli; ara toplam / kargo / indirim / genel toplam.
- Silme/azaltma için onay; sepet boşsa "Alışverişe başla" CTA + öneriler.
- Sepet kalıcılığı: kullanıcı giri$i yoksa cookie/localStorage; girişli kullanıcıda DB.
- **Dikkat:** Fiyatlar her zaman sunucu tarafından yeniden hesaplanmalı, client-side trust edilmemeli.

## 4. CHECKOUT — Ödeme akışı
En kritik bölüm; karmaşıklığı minimum tut:

1. **Adımlar:** İletişim → Kargo adresi → Kargo seçimi → Ödeme → Onay.
2. **Misafir (guest) alışveriş:** Zorunlu üyelik yok; sipariş sonrası hesap oluşturma imkanı (opsiyonel).
3. **Adres formu:** Türkiye'ye özgü alanlar (il, ilçe, mahalle, posta kodu, adres satırı 1–2, telefon, TCKN/VKN).
4. **Kargo seçimi:** firma, tahmini teslim süresi, ücret.
5. **Ödeme seçenekleri:**
   - Kredi/banka kartı (iyzico, PayTR, Shipy)
   - Havale/EFT
   - Kapıda ödeme (mümkünse)
   - 3D Secure zorunlu (Türkiye'de kartlı ödemelerde genellikle zorunlu/önerilen)
   - Taksit seçenekleri kart ağına göre sunulmalı (taksit bilgisi ödeme sağlayıcıdan gelmeli, uydurulmamalı)
6. **Fatura bilgisi:** Bireysel / kurumsal; kurumsal ise VKN/vergi dairesi/ünvan; e-fatura/e-arşiv.
7. **Sipariş özeti:** her zaman sağda/yapışkan; toplam tutar kargo dahil.
8. **Sözleşmeler:** mesafeli satış sözleşmesi ve KVKK aydınlatma metni onayı (checkbox, zorunlu); link.
9. **Form doğrulama:** sunucu tarafı mutlaka; istemci tarafı anında geri bildirim.
10. **Hata yönetimi:** kart reddi, 3D Secure hata, zaman aşımı için kullanıcı dostu mesaj.

## 5. PAYMENT — Ödeme güvenliği
- PCI-DSS uyumu: Kart bilgilerini asla kendi sunucunda tutma; ödeme sağlayıcının iframe/hosted field/API kullan.
- 3D Secure zorunlu.
- CSRF token; rate limiting; tutar manipülasyonu denetimi (sunucu tarafı toplam hesabı).
- Webhook doğrulaması (imza kontrolü); duplicate webhook idempotency.
- Sipariş durumu: `pending_payment → paid → processing → shipped → delivered | refunded | cancelled`.
- Test kartları ile uçtan uca test (iyzico/PayTR test ortamı).

## 6. ORDER — Sipariş sonrası
- Teşekkür sayfası: sipariş numarası, tahmini teslim, e-posta bilgilendirmesi.
- Sipariş detay sayfası: kargo takip numarası + kargo firması linki, durum geçmişi.
- E-posta/SMS bildirimleri (sipariş alındı, ödeme alındı, kargolandı, teslim edildi).
- İptal/iade talebi; iade koşulları (14 gün cayma hakkı — Mesafeli Sözleşme).

## 7. POST — Ek operasyon
- Stok takibi: rezerve / düşüm / iade.
- Fatura: e-arşiv/e-fatura (GİB entegrasyonu ya da özel entegratör: Foriba, Uyumsoft, Logo, Micro, iyzico/PayTR üstünden).
- Kargo: Yurtiçi, Aras, MNG, PTT, UPS; entegrasyon barkod ve takip numarası.
- ERP/Muhasebe: tahsilat eşleştirme, muhasebe fişi.
- KVKK: açık rıza, veri saklama süresi, silme/talep mekanizması.

# Çıktı

- Veri modeli (Product, Variant, Category, Order, OrderItem, Payment, Shipment, Invoice, Customer)
- Akış şeması (katalog → detay → sepet → checkout → ödeme → sonrası)
- Ödeme sağlayıcı seçim notu (TR için iyzico/PayTR; uluslararası Stripe)
- Güvenlik kontrol listesi
- SEO (ürün structured data) ve performans notları
- Türkçe metin örnekleri

# Kalite Kontrol Listesi

- [ ] Tüm fiyatlandırma sunucu tarafı
- [ ] 3D Secure ve PCI-DSS uyumu
- [ ] Misafir alışveriş destekleniyor
- [ ] Adres ve telefon formatı Türkiye'ye uygun
- [ ] Para formatı `₺1.234,56`, tarih `DD.MM.YYYY`
- [ ] Kupon/taksit/indirim hesapları tutarlı
- [ ] KVKK ve mesafeli satış onayları var
- [ ] Stok/ürün resmi/miktar tutarsızlığı yok
- [ ] E-posta/SMS bildirimleri planlanmış
- [ ] Structured data (Product, BreadcrumbList) eklendi
- [ ] Sayfa yüklenme hızı (resimler optimize, CDN, lazy-load)
- [ ] Sepet ve ödeme akışı Playwright ile test edildi
- [ ] Başarısız ödeme ve iptal/iade akışları test edildi

# Yaygın Hatalar

- **Hata:** Fiyatı/indirimi sadece istemcide hesaplamak → manipülasyona açık.
  **Düzeltme:** Tüm fiyatlar backend'de doğrulanır; client sadece gösterim yapar.
- **Hata:** Üyelik zorunlu tutmak; dönüşüm düşer.
  **Düzeltme:** Misafir alışveriş; sipariş sonrası hesap öner.
- **Hata:** 3D Secure'u atlatmaya çalışmak → dolandırıcılık riski ve ceza.
  **Düzeltme:** 3D Secure zorunlu.
- **Hata:** Kargo/taksit/indirim bilgilerini gerçek zamanlı çekmeden sabit yazmak.
  **Düzeltme:** Sağlayıcı API'sinden canlı al; test ortamıyla doğrula.
- **Hata:** Kırık/yanlış Türkçe ("ürünler sepete eklendi" yerine "added to cart").
  **Düzeltme:** Kullanıcının göreceği tüm metinleri bir yerde (i18n) topla; doğal Türkçe kullan.

# Referanslar

- iyzico dokümanı: https://docs.iyzico.com/
- PayTR: https://www.paytr.com/gelistirici
- Stripe: https://stripe.com/docs
- GİB e-belge: https://ebelge.gib.gov.tr/
- KVKK: https://kvkk.gov.tr/
- Bu KB: `security/owasp-top10`, `decisions/payment-providers.md`, `patterns/auth.md`

# İlgili Skill'ler

- `security-audit`
- `seo-audit`
- `performance-audit`
- `browser-testing`
- `database-design`
- `api-design`
