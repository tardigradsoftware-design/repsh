# Görev 02: Güvenli Auth Akışı (Next.js + Supabase)
## Açıklama
Next.js 16 + Supabase projesi için kayıt, giriş, şifre unuttum ve çıkış akışlarını kur.
Middleware ile korumalı `/panel` rotası; sadece giriş yapan kullanıcı erişebilsin.
## Başarı
- Kayıt e-posta+şifre; giriş; şifre sıfırlama linki; çıkış
- `/panel` login olmadan açılmıyor; login sonrası `?next` hedefine dönüyor
- Client'ta `SUPABASE_SERVICE_ROLE_KEY` kullanımı yok (grep ile doğrulanacak)
- Şifre alanı en az 8 karakter; zod ile doğrulama
- Formlar Türkçe, hata mesajları kullanıcı dostu
- Temel Playwright test: kayıt akışı (mock email) → giriş → korumalı sayfa erişimi
- RLS policy yok (sadece auth yeterli)
