# Test Senaryoları — responsive-mobile

## Test 1: Navbar + sidebar mobil davranışı

**Girdi:** Desktop sidebar sabit 240px genişlik; üstte arama ve kullanıcı menüsü.

**Beklenen:**
- 1024px altına indiğinde sidebar drawer olur (hamburger açar, overlay kapatır, ESC ile kapanır).
- Üst bar kalır ama yüksekliği azalmaz; dokunma hedefleri 44px kalır.
- Arama kutusu 768px altında ikon-gerişli (tıkla tam genişlik açılır) veya kısaltılmış.
- Safe-area bottom ayarı var; sabit alt element yok.
- 390px'de hiçbir taşma yok.

## Test 2: Büyük tablo mobil kırılımı

**Girdi:** 7 kolonlu sipariş tablosu; her kolon 150px+ (toplam 1200px).

**Beklenen:**
- 390px'de ana 2-3 kolon (sipariş no, müşteri, tutar, durum) görünür;
- diğer kolonlar yatay kaydırılabilir bir kapta veya "detay için satıra tıkla" akışına döner;
- sticky ilk kolon (sipariş no) kaydırmada görünür kalır;
- hücre içeriği sıkışıp okunamaz hale gelmez (örn. `whitespace-nowrap` + overflow yerine kısaltma).

**Hata:** 7 kolonu sıkıştırıp her kolonda 2-3 harf göstermek; veri okunamaz.
