# Web Güvenlik Açıkları — Hızlı Başvuru

Detaylı denetim `security-audit` skill'inde. Burada yaygın açık ve kısa korunma yolları:

## XSS (Cross-Site Scripting)
- **Ne:** Kullanıcı girdisi HTML olarak çalıştırılır.
- **Korun:** React JSX'te içerik otomatik kaçılır; `dangerouslySetInnerHTML` kullanıyorsan sanitize et (DOMPurify).
- Tarayıcıda da CSP ile ikinci hat.

## CSRF (Cross-Site Request Forgery)
- Kullanıcı başka sitede oturumu açıkken, kötü niyetli site onun adına istek gönderir.
- **Korun:** `SameSite=Lax/Strict` cookie; CSRF token; state/nonce (OAuth). Auth.js/NextAuth gibi
  olgun kütüphaneler bunu halleder; custom auth kullanıyorsan manuel ekle.

## SQL Injection
- Kullanıcı girdisi doğrudan SQL sorgusuna eklenir.
- **Korun:** ORM veya parametreli sorgu kullan; string concat ile sorgu kurma.

## IDOR (Insecure Direct Object Reference)
- `/api/orders/123` gibi endpoint kullanıcının kendi siparişi mi diye bakmıyor.
- **Korun:** Her endpointte kullanıcı kimliğini oturumdan al; kaynağın sahibiyle eşleşmiyorsa 403.

## RLS atlanırsa (Supabase)
- Service role key istemciye sızarsa RLS atlanır.
- **Korun:** Service role sadece server-side; anon key client-side; RLS policy'ler her tablo için.

## SSRF
- Kullanıcı verdiği URL'ye (image proxy, webhook vb.) istek atılıyor ama iç ağa erişebiliyor.
- **Korun:** Host beyaz liste; metadata IP'lerine (169.254.x.x, 10.x.x.x) izin verme.

## Path Traversal
- Kullanıcı dosya adı olarak `../../etc/passwd` gönderir.
- **Korun:** path.resolve ile kökü doğrula; kullanıcı girdisini güvenli map üzerinden geç.

## Açık Yönlendirme
- `?next=//evil.com` ile phishing.
- **Korun:** next hedefini path ile sınırla (dış URL reddet).

## Secret yönetimi
- `.env` commit'lenmez; client'e `NEXT_PUBLIC_` ile sızdırılmaz.
- Production secret'ları platformun secret store'unda.
- Dönüştürülebilir (rotate) uzunluk ve karmaşıklıkta.

## 3. parti script ve CSP
- Chat/analytics/reklam scriptleri üçüncü taraftan geldiğinde XSS ve izinsiz veri paylaşımı riski.
- **Korun:** CSP ile hangi kaynakların yükleneceğini kısıtla; nonce/hash ile onaysız script'i engelle.

## Rate Limit
- Login, şifre sıfırlama, ödeme, arama endpointleri kısıtlanmalı (brute force, DoS).

## Kaynaklar
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP LLM Top 10 (ajan/MCP dahil)
