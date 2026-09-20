# Görev 14: Ödeme Güvenlik Entegrasyonu
## Açıklama
Hem Stripe (uluslararası) hem iyzico (TR) entegrasyonu olan bir projede ödeme akışını güvenlik açısından denetle.
## Başarı
- Kart bilgileri kendi sunucuya gelmiyor (hosted field/checkout)
- Webhook imzası doğrulaması var (her iki sağlayıcıda)
- Idempotency key kullanılmış
- 3D Secure zorunlu (iyzico tarafı)
- Test ve production anahtarları ayrılmış; production anahtarı log'da/istemcide yok
- Fatura bilgileri kurumsal için doğru alanlar (VKN/vergi dairesi)
- Başarısız ödeme kullanıcıya gösteriliyor ve log'lanıyor
