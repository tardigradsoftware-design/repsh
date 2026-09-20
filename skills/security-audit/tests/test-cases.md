# Test Senaryoları — security-audit

## Test 1: Supabase service role'ün client'a sızması

**Girdi:** `lib/supabase.ts` dosyasında:
`export const supabaseAdmin = createClient(url, process.env.SUPABASE_SERVICE_ROLE_KEY);`
ve `NEXT_PUBLIC_SUPABASE_SERVICE_ROLE_KEY` kullanılmış.

**Beklenen:**
- CRITICAL: Service role key client'e sızdırılıyor. Bu key RLS'i atlar, tüm veritabanına erişir.
- Düzeltme: Service role sadece server-side (Server Component/Route Handler/Server Action'da)
  okunabilen SUPABASE_SERVICE_ROLE_KEY olarak tut; istemciye gönderilmez. Client anon key kullan.
- `.gitignore` ve env kontrolü; secret geçmişte commitlendiyse rotate edilsin.

## Test 2: IDOR open endpoint

**Girdi:**
```js
app.get('/api/orders/:id', async (req, res) => {
  const order = await db.order.findUnique({ where: { id: req.params.id } });
  res.json(order);
});
```
Auth var ama sipariş sahibi kontrol edilmiyor.

**Beklenen:**
- CRITICAL IDOR açığı; herhangi bir giriş yapmış kullanıcı herhangi bir siparişi görebilir.
- Düzeltme: `where: { id, userId: req.user.id }` veya policy ile; ve test ekle.
- Aynı kategori başka endpoint'lerde de taranır.
