# Türkiye'ye Özel SEO Notları

Genel teknik SEO `seo-audit` skill'inde. Burada Türkiye pazarına özgü püf noktaları:

## Teknik
- `<html lang="tr">` zorunlu.
- URL'ler Türkçe karakter içerebilir (Unicode) ama çoğu zaman ASCII slug kullanmak daha güvenli
  (örn. `istanbul-da-ev-temizligi` → slug'ı `istanbul-da-ev-temizligi` yapabilirsin; karakterleri
  düzgün normalize et, tutarlı ol).
- Fiyatlar sayfada KDV dahil görünmeli (Türkiye'de etiket fiyatı KDV dahil olur). Schema.org
  `priceSpecification` içinde `valueAddedTaxIncluded: true` ve para birimi `TRY` olarak belirt.
- `hreflang="tr-TR"`; çoklu dil (TR/EN/DE) varsa doğru sayfaları işaretle.

## Structured data
- **LocalBusiness:** Restoran, hizmet, mağaza için adres (sokak, ilçe, il, posta kodu), telefon,
  çalışma saatleri, enlem/boylam, Google Business Profile URL.
- **Organization:** Logo, iletişim, sosyal profil linkleri.
- **BreadcrumbList** (Türkçe isimlerle).
- **Product, AggregateRating** ürün sayfalarında; gerçek yorum/yıldız verisi yoksa ekleme.
- **FAQPage** SSS sayfaları için.
- **WebSite** (iç site arama).

## Google Business Profile (eski Google Benim İşletmem)
- Yerel işletmeler için profil doğrula ve güncel tut: adres, telefon, çalışma saatleri, fotoğraf,
  müşteri yorumları.
- Harita gömümü (iframe) iletişim sayfasında (gizlilik politikasına not et).

## Yasal sayfalar
- **KVKK Aydınlatma Metni:** kişisel veri toplama amacı, saklama süresi, haklar.
- **Çerez Politikası:** açık rıza banner'ı; zorunlu çerezler ve analitik/pazarlama ayrımı.
- **Mesafeli Satış Sözleşmesi** (e-ticaret / satış yapan site): teslimat, iade, cayma (14 gün), teminat.
- **Gizlilik Politikası, İptal/İade Koşulları** (e-ticaret).
- **İletişim:** şirket unvanı, adres, MERSİS numarası (e-ticaret için zorunlu bilgiler).

## Dil ve içerik
- Anahtar kelimeleri doğal kullan; "İstanbul'da kurye", "İzmir içi teslimat" gibi şehir/bölge
  long-tail'leri düşün.
- Karakter kodlaması UTF-8; Türkçe karakterler (ı, İ, ğ, ş, ö, ü, ç) doğru render ediliyor mu?
- Başlık/meta açıklamaları doğal Türkçe; Google çevirisiyle üretilmiş makine dili kokuyorsa
  kullanıcı ve arama motorları güvensizlik hisseder.

## Performans ve mobil
- Türkiye'de mobil trafiğin payı yüksek; Lighthouse mobil hedefi 90+.
- LCP için hero resmi optimize et; kritik fontlar preconnect.
- CDN kullan (Vercel/Cloudflare) ile ilk byte'ı Türkiye'den servis et.
- Hosting Vercel/Cloudflare (Avrupa bölgesi) yeterli; çok yüksek trafikte TR lokasyon
  sunucu (Istanbul) düşünülebilir.

## Ölçüm ve izleme
- Google Search Console'u aç; TR hedefli sayfaları izle.
- GA4 veya Plausible gibi gizlilik dostu alternatif.
- Google Trends ile arama ilgisini kontrol et (içerik planı için).

## Kaynaklar
- Google Search Central: https://developers.google.com/search
- Schema.org: https://schema.org/
- KVKK: https://kvkk.gov.tr/
- Rich Results Test: https://search.google.com/test/rich-results
