# Test Senaryoları — research-before-code

## Test 1: Yeni grafik kütüphanesi seçimi

**Girdi:**
> Projemiz Next.js 15 + Tailwind + shadcn/ui. Dashboard'da son 6 ayın aylık gelir çizgi grafiği ve
> ürün kırılımı pasta grafiği eklemeliyiz. Hafif olsun, özelleştirme kolay olsun.

**Beklenen ajan davranışı:**
1. UNDERSTAND: Grafik tipi (çizgi + pasta), ortam (Next.js + Tailwind), kısıt (hafif, özelleştirilebilir).
2. SEARCH:
   - KB `registry/frameworks.yaml`'da chartjs, echarts, recharts kayıtlarını bulur.
   - En az bir resmi kaynak açar (chartjs.org, recharts.org, echarts.apache.org).
   - Bundle boyutlarını karşılaştırır (chartjs ~60KB, recharts ~100KB+, echarts ~1MB).
   - Projede halihazırda herhangi bir grafik kütüphanesi olup olmadığını `package.json`'a bakarak
     kontrol eder.
3. COMPARE: En az 2 seçenek (ör. Chart.js vs Recharts) için boyut / bakım / lisans / tema uyumu
   tablosu çıkarır.
4. VERIFY: Seçilen kütüphanenin en son sürümünü `npm view` ile teyit eder; küçük bir örnek kod
   parçasının (dataset tanımı + `<Line />` veya `<canvas />`) derlenip derlenmediğini kontrol eder.
5. PLAN: 5–8 maddelik plan, seçilen kütüphane ve sürüm, test metodu.
6. TEST ETMEZ / uygulamaya geçmeden önce planı sunar.

**Hata sayılacak davranış:**
- Hemen `npm install recharts` veya herhangi birini yazmak (karşılaştırma yapmadan).
- "Chart.js en iyisidir" gibi kanıtsız iddia.
- Mevcut projede zaten echarts yüklüyken chartjs önermek.
- Sürüm numarası veya güncellik belirtmemek.

---

## Test 2: Halihazırda çözülmüş problemi yeniden yazma tuzağı

**Girdi:**
> Next.js form sayfasında e-posta ve şifre alanlarını doğrulayan kod yazacağım; e-posta formatı
> ve minimum 8 karakter şifre, ayrıca şifre ile şifre tekrarı eşleşmeli.

**Beklenen ajan davranışı:**
1. UNDERSTAND: Basit form doğrulaması.
2. SEARCH:
   - KB'de `react-hook-form` ve `zod` kayıtlarını fark eder.
   - Projede bu ikisinin kurulu olup olmadığını kontrol eder.
   - Kuruluysa mevcut `useForm + zodResolver` örneklerini projede arar.
   - Kurulu değilse RHF+Zod'un yaygın ve tip-güvenli çözüm olduğunu not eder.
3. COMPARE: "sıfırdan manuel doğrulama yazmak" vs "RHF + Zod kullanmak" — hangisi daha az kod, daha
   güvenli, mevcut stack ile uyumlu?
4. VERIFY: Örnek bir `z.object({...})` şeması yazarak tip çıkarımını kontrol eder.
5. PLAN: Şema dosyası + form bileşeni + hata mesajları (Türkçe) + temel test.
6. Uygulamaya geçerken kütüphane tercihini açıkça belirtir.

**Hata sayılacak davranış:**
- Hiç bakmadan 50 satırlık elle `if/else` doğrulaması yazmak.
- Kütüphane kullanılması gerektiğini belirtmeden kendi çözümünü empoze etmek.
- Türkçe hata mesajlarını İngilizce bırakmak / hiç localization düşünmemek.
