# Görev 05: Bozuk Next.js Projesi Onarma
## Açıklama
Bir Next.js projesinde şu hatalar var: production deploy sonrası beyaz ekran (products.map undefined),
resimler 5MB ve yavaş, `dangerouslySetInnerHTML` ile kullanıcı yorumları basılıyor,
`.env.local` repo'da duruyor (SUPABASE_SERVICE_ROLE_KEY), `noindex` meta production'a sızmış.
## Başarı
- Beyaz ekran düzeltilmiş (veri yüklenemedi durumu + default değer)
- Resimler Image ile optimize (width/height, webp)
- XSS açığı kapatılmış (sanitize veya kaç)
- Secret commit geçmişi temizlenmiş; .env .gitignore'a eklenmiş; key rotate edilmiş (belge)
- noindex production'da kaldırılmış
- Lighthouse 90+
