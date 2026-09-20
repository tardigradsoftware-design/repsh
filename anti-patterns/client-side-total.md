# Anti-Pattern: Client-Tarafı Toplam Tutar Hesabı (E-ticaret)

## Nasıl olur
Sepet toplamı, kargo ve indirim sadece istemcide JS ile hesaplanıp sunucuya gönderilir:
`POST /api/checkout { items, total: clientTotal }`
Sunucu da gelen toplamı güvenip siparişi oluşturur.

## Neden kötü
Kullanıcı browser DevTools ile total değerini düşürebilir (ör. ₺500 yerine ₺1). Sunucu
bunu doğrulamazsa sistemi istismar edip ucuza sipariş verebilir. Kupon manipülasyonu da aynı sınıfa girer.

## Nasıl düzeltilir
- Sunucu tarafında `cart.items` içinden tek tek fiyat, miktar, indirim, kargo, vergi üzerinden
  toplam her zaman yeniden hesaplanır.
- Gelen `total` değeri ya yok sayılır ya da sunucuda hesaplananla karşılaştırılır (farklıysa 409).
- Fiyat veritabanında decimal/tamsayı (kuruş) olarak saklanır; istemci sadece gösterim yapar.
- Kuponlar tek kullanımlık ve sona erme tarihli; sunucu tarafında doğrulanır.
- Ödeme sağlayıcıya geçilen tutar da ayrıca imzalanır/kimliği doğrulanır (Stripe payment intent, iyzico).

## Test
- Playwright testinde tarayıcıda fetch'e müdahale edip total'i 1'e çek; sunucu reddediyor mu?

## İlgili
- `ecommerce`, `security-audit`, `api-design`
