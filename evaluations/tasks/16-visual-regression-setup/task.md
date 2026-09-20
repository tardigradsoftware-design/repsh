# Görev 16: Playwright ile Görsel Regresyon Kurulumu
## Açıklama
Bir Next.js projesi için Playwright ile görsel regresyon testi kur. 3 kritik sayfa (ana sayfa, ürün detay, sepet).
## Başarı
- Playwright config ve 3 test dosyası
- Her tarayıcı için Chromium+Firefox+WebKit matrisi değil ama Chromium + 3 viewport
- Screenshot karşılaştırması toMatchScreenshot ile
- Auth state storageState ile giriş öncesi yapılmıyor
- CI komutu (`pnpm test:e2e:visual`)
- Animasyonlar kapatılmış (kararlı screenshot için)
- Flaky test önleyici önlemler (network idle, data seed sabit)
