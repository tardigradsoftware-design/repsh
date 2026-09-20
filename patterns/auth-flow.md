# Pattern: Auth Akışı (Supabase / Next.js)

## Genel yapı
1. **Kayıt/Giriş sayfaları:** Merkezi `(auth)/login` ve `(auth)/register` route'ları.
2. **Middleware:** Her istekte cookie/session okunur; korumalı sayfalara giriş yoksa `/login?next=/...` yönlendirmesi yapılır.
3. **Client helper:** `createClient()` server ve client tarafında ayrı ayrı oluşturulur;
   service role sadece server-side'da.
4. **RLS:** Her tabloda `auth.uid() = user_id` veya organizasyon üyeliği ile policy.
5. **Email doğrulama, şifre sıfırlama, 2FA:** Sağlayıcı akışı; e-posta şablonları Türkçe.
6. **Çıkış:** Server action ile `supabase.auth.signOut()` ve `/login` yönlendirmesi.

## Middleware (Next.js)
```ts
export async function middleware(req: NextRequest) {
  const res = NextResponse.next();
  const supabase = createMiddlewareClient(req, res);
  const { data: { user } } = await supabase.auth.getUser();
  if (!user && req.nextUrl.pathname.startsWith('/panel')) {
    const url = req.nextUrl.clone();
    url.pathname = '/login';
    url.searchParams.set('next', req.nextUrl.pathname);
    return NextResponse.redirect(url);
  }
  return res;
}
```

## Güvenlik
- Anon key istemcide olabilir; service role yalnızca server action/route handler içinde tutulur.
- JWT süresi ve refresh token rotasyonu; logout ile cookie temizlenir.
- Hassas sayfalarda rol kontrolü ek olarak server component içinde yapılır.
- Şifre hash'lenmiş şekilde saklanır; asla plain text dönmez.
- Korumalı form/action'larda RLS + server tarafında tekrar rol kontrolü.

## Türkçe notlar
- "Invalid credentials" → "E-posta veya şifre hatalı"; hangisinin hatalı olduğunu açıkça verme
  (kullanıcı adı var mı yok mu bilgisi brute-force'a yol açar).
- Şifre sıfırlama e-postası TR; link süresi (1 saat).
- "Beni hatırla" opsiyonu; 30 gün oturum.

## Kaynak
- Supabase Auth + Next.js: https://supabase.com/docs/guides/auth/quickstarts/nextjs
- Auth.js (NextAuth): https://authjs.dev/

## İlgili
- `security-audit`, `database-design`, `api-design`
