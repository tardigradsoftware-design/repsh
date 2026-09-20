# Playbook: build-ecommerce

## Amaç
Türkiye pazarına yönelik e-ticaret sitesi uçtan uca akış (perakende, dijital ürün veya B2B sipariş portalı).

## Fazlar

### 1. Kapsam ve hukuki hazırlık
- Satılacak ürün tipi (fiziksel / dijital / abonelik).
- Şirket bilgileri, vergi numarası, MERSİS; KVKK ve Mesafeli Satış Sözleşmesi metinleri hazır mı?
- İhtiyaç: stok takibi, kargo, fatura (e-arşiv/e-fatura), iade, taksit, kapıda ödeme, havale.
- Entegrasyonlar: ödeme (iyzico/PayTR/Stripe), kargo (Yurtiçi, Aras, MNG, PTT), fatura (Foriba/Uyumsoft), ERP ( Logo/Micro).

### 2. Mimari
- Next.js App Router + Tailwind + shadcn/ui; Supabase/Postgres; Prisma/Drizzle.
- Ürün medya için R2/S3 + CDN.
- Ödeme sağlayıcı seçimi ve test hesabı.
- Sepet (çerez + DB), auth (misafir + üye).

### 3. Veri modeli
- Product, Variant, Category, Brand, Media, ProductCategory, Review,
- Cart, CartItem, Order, OrderItem, Payment, Shipment, Invoice, Address, Customer, Coupon, StockMovement.
- Para numeric(12,2); stok hareketleri; sipariş durumu enum; ödeme durumu enum.
- `database-design` ile tablo/iliski/index/RLS kur.

### 4. Katalog ve ürün
- Kategori ağacı, filtreler, arama.
- Ürün kartı (resim, ad, fiyat, indirim, taksit, kargo bilgisi, Yıldız).
- Ürün detay (galeri, varyant, açıklama sekmeleri, taksit tablosu, yorum, ilgili ürün).
- Structured data (Product, BreadcrumbList, AggregateRating).

### 5. Sepet ve checkout
- Mini sepet + sepet sayfası.
- Adımlı checkout: iletişim → adres → kargo → ödeme → onay.
- Misafir alışveriş desteklenir; üyelik zorunlu değil.
- Adres formu TR formatı (il/ilçe/mahalle + posta kodu); telefon 0(5xx) format.
- Taksit seçenekleri ödeme sağlayıcıdan canlı gelmeli; sabit yazılmaz.
- 3D Secure zorunlu.

### 6. Güvenlik
- `security-audit`: tüm fiyatlar backend, coupon doğrulaması, webhook imza, rate limit, idempotency.
- PCI-DSS: kart bilgilerini sunucunda tutma, hosted field/iframe kullan.
- KVKK açık rıza ve mesafeli satış checkbox'ları.

### 7. Sipariş sonrası
- Teşekkür sayfası (sipariş no, tahmini teslim).
- Sipariş durumu sayfası + kargo takip linki.
- E-posta/SMS bildirimleri (şablonlar Türkçe).
- İade/iptal talebi; 14 gün cayma.

### 8. Performans ve SEO
- Görseller optimize (AVIF/WebP, srcset, aspect-ratio, lazy).
- LCP <2.5s; kategori sayfaları ISR/SSR; ürün sayfaları revalidate.
- `seo-audit`: title/description, schema, sitemap, Search Console.
- Yerel SEO: adres/iletişim sayfası, Google Business Profile entegrasyonu.

### 9. Test
- Playwright: ürün gezme → sepete ekle → adres → 3D test (test kartı) → başarı/hata durumları.
- Stres testi: indirim/kampanya döneminde trafik.
- Ödeme sağlayıcı sandbox ve production webhook testleri.
- Fatura kesimi testi (test ortamı).

### 10. Dağıtım ve son denetim
- Canlıya alma, domain SSL, CDN, stok/gerçek kargo testi.
- `website-quality-review` + özelleştirilmiş e-ticaret checklist (KVKK, ödeme, fatura).

## İlgili skill'ler
`ecommerce`, `database-design`, `security-audit`, `seo-audit`, `performance-audit`,
`browser-testing`, `deployment`.
