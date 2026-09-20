# Anti-Pattern: Service Role Key'i İstemciye Sızdırmak

## Nasıl olur
- Supabase projesinde `createClient(url, SUPABASE_SERVICE_ROLE_KEY)` ile client tarafında
  kullanılan örnek;
- `NEXT_PUBLIC_SUPABASE_SERVICE_ROLE_KEY` env değişkeni tanımlamak;
- `admin` client'ı client component'inde import etmek ve DB sorgusu yapmak;
- Kaynak kodda veya ağ isteklerinde service role key'in görünmesi.

## Neden kötü (kritik)
Service role key RLS'i atlar, tüm veritabanı üzerinde tam yetki verir. İstemciye düşerse
herhangi bir kullanıcı (veya tarayıcı uzantısı, bot) tüm veriyi okuyabilir, değiştirebilir, silebilir.
Kredi kartı, kişisel veri, siparişler her şey açılır.

## Nasıl fark edilir
- `grep -r "SUPABASE_SERVICE_ROLE_KEY" .` ve `grep -r "service_role" .`;
- Client bundle'da key string'i geçiyor mu?
- `.env.local` dosyasında `NEXT_PUBLIC_` ile başlayan service role var mı?
- Supabase dashboard auth log'larında anormal erişim.

## Nasıl düzeltilir
- Service role'ü yalnızca server-only dosyalarda (Server Component, Server Action, Route Handler)
  kullan; `"use server"` veya `server-only` paketi ile belirt.
- İstemci sadece `NEXT_PUBLIC_SUPABASE_URL` + `NEXT_PUBLIC_SUPABASE_ANON_KEY` kullanır.
- Key sızdıysa hemen Supabase dashboard'dan rotate et; eski key iptal olur.
- RLS policy'leri tablo başına yazılır; service role istemciye verilmemesi tek güvence DEĞİLDİR,
  RLS bağımsız olarak doğru olmalı.

## İlgili
- `security-audit`, `database-design`, `ecommerce`
