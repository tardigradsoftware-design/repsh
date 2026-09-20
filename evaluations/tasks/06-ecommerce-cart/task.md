# Görev 06: E-Ticaret Sepet ve Checkout
## Açıklama
Next.js + Supabase + iyzico test hesabı ile sepet, adres ve ödeme adımını kur.
## Başarı
- Misafir kullanıcı da sepeti görebiliyor (cookie)
- Adres formu TR formatı (il/ilçe)
- 3D Secure test kartı ile ödeme akışı çalışıyor (sandbox)
- Toplam tutar yalnızca sunucuda hesaplanıyor (client güvenilmiyor)
- İndirim kuponu varsa sunucu doğrulaması
- Başarısız ödeme kullanıcıya gösteriliyor
- Webhook endpoint imza doğrulaması yapıyor
- Temel Playwright test: ürün → sepet → adres → ödeme akışı sandbox'ta
