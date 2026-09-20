# Stack: Türkiye E-Ticaret Sitesi

## Ne için
- TR pazarı için fiziksel ürün e-ticareti; kargo, taksit, 3D Secure, e-arşiv fatura.

## Teknolojiler
- **Framework:** Next.js 16 App Router.
- **UI:** Tailwind + özelleştirilmiş shadcn/ui; tasarım sistemi mutlaka marka dili ile.
- **Backend/DB:** Supabase Postgres (veya özel Node backend + Postgres); Prisma/Drizzle.
- **Auth:** Supabase Auth (misafir alışveriş destekli).
- **Sepet:** Cookie + DB kalıcılık.
- **Ödeme:** iyzico veya PayTR (TR); uluslararası Stripe. 3D Secure zorunlu; hosted checkout veya form.
- **Kargo:** Entegrasyon için seçilen firmanın SOAP/REST API'si (Yurtiçi Kargo, Aras, MNG, PTT Kargo, UPS).
- **Fatura:** Özel entegratör (Foriba, Uyumsoft, Logo Connect) veya iyzico/PayTR içinden e-arşiv.
- **Search/filter:** Başlangıçta Postgres full-text / trigram; büyüyünce Typesense/Meilisearch.
- **Medya:** Cloudflare R2/Supabase Storage, CDN, AVIF/WebP dönüşümü.
- **Email:** Resend/Mailtrap + TR SMTP relay (iyzico mailleri ayrıca).
- **KVKK/Gizlilik:** Açık rıza kaydı; VERBİS yükümlülüğü notu.
- **İzleme:** GA4 + Meta Pixel + Sentry + Cloudflare Web Analytics.
- **Test:** Playwright (katalog, sepet, checkout, 3D test kartı ile); Lighthouse.
- **Hosting:** Vercel + Supabase; kargo/fatura entegrasyonları için ek Node servis (opsiyonel).

## Kritik kontroller
- Tüm fiyatlar sunucu tarafı; kupon ve indirim doğrulaması.
- 3D Secure zorunlu; kart bilgisi kendi sistemine temas etmiyor.
- Sipariş durumu ve kargo takip linki kullanıcıya iletiliyor.
- KVKK aydınlatma ve mesafeli satış onayları alınıyor.
- Türkçe metin doğal; para/tarih formatı `tr-TR`.
