# Test Senaryoları — ecommerce

## Test 1: Fiyat manipülasyonu güvenlik açığı

**Girdi:** Ajan, sepette toplam tutarı istemcide hesaplayıp sunucuya gönderiyor:
`POST /api/checkout { items: [...], total: clientTotal }`

**Beklenen davranış:**
- Güvenlik açığını tespit eder: client'tan gelen total değeri güvenilmezdir.
- Düzenleme: Sunucu tarafında `cart.items` ve güncel ürün fiyatları ile toplamı yeniden hesaplar;
  kupon/indirim/kargo ücretlerini de sunucu doğrular; istemci toplamını yok sayar veya
  doğrular (farklıysa hata döner).
- 3D Secure zorunluluğunu, idempotent order id'sini not eder.

**Hata sayılacak davranış:** Sorunu görmemek; client'tan gelen toplam ile sipariş oluşturmak.

---

## Test 2: Türkçe format ve metin hataları

**Girdi:** Ürün kartında:
- Fiyat: `1299.99 TL` — nokta ondalık, TL yazısı.
- İndirim: `-%20` instead of `%20 indirim`.
- Buton: "Add to Cart".
- Kargo: "Free shipping".

**Beklenen düzeltme:**
- `₺1.299,99` (Intl.NumberFormat tr-TRY).
- İndirim rozeti: `%20 indirimli` veya `İndirim %20`.
- Buton: "Sepete ekle".
- Kargo: "Kargo bedava" veya "Ücretsiz kargo".
- Tarih ve teslim süreleri de Türkçe olmalı.

**Hata:** Fiyatı düzeltip TL/₺ karışıklığı bırakmak; tek tek string replace yapmak yerine
merkezi `formatCurrency()` fonksiyonuna yönlendirmemek.
