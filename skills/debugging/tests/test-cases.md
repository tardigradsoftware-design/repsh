# Test Senaryoları — debugging

## Test 1: Production'da beyaz ekran

**Girdi:** Deploy sonrası production'da beyaz ekran; dev'de çalışıyor. Console: `Cannot read properties of undefined (reading 'map')`
`useProducts()` bazı durumlarda `products: undefined` dönüyor.

**Beklenen:**
1. Yeniden üret ve koşulu not eder (hangi kullanıcı/veri ile oluyor? misafir kullanıcı da?).
2. Neden undefined? API 404 mü, veri formatı mı farklı, RLS mi engelliyor, env eksik mi?
3. En dar değişiklik: default değer ekle (boş dizi) + API hata durumunu ele al; ama asıl kök neden
   (veri yapısı API'de mi farklı geldi, migration eksik mi?) bulunur.
4. Hata durumu için "veri yüklenemedi" gösterimi + yeniden dene butonu.
5. Regresyon testi: products null/undefined iken sayfa beyaz ekran vermemeli.
6. Kod tabanında aynı pattern (doğrudan `.map` kullanılıp null-check yapılmayan) aranır.

## Test 2: Tarih yanlış görünüyor

**Girdi:** 31 Aralık 2026 olarak beklenen tarih bir kullanıcıda "31.12.2025" görünüyor. UTC/TR saat dilimi farkı olabilir.

**Beklenen:**
- Hangi timezone'da ortaya çıkıyor? Sunucu UTC, kullanıcı GMT+3. Tarih saat 00:00 ise UTC'de önceki gün 21:00 olur → bir gün geri kayar.
- Kök neden: tarihleri tarihsiz (saatsiz) saklamak için `new Date('2026-12-31')` gibi UTC constructor kullanmak yerel saat farkı yaratır.
- Düzeltme: gün/ay/yıl olarak sakla veya zaman bileşeni olmadan TZ-belirsiz formatta. Tarih gösterimini locale + zaman dilimi bilgisiyle yap.
- Test: hem Europe/Istanbul hem UTC kullanıcıda doğru görünüyor mu.
