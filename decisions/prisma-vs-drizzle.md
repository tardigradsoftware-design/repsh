# Karar: Prisma vs Drizzle ORM

*Tarih: 2026-09-20 · Son*

| Boyut | Prisma | Drizzle |
|---|---|---|
| Tip güvenliği | ++ | ++ |
| Öğrenme | kolay | kolay-orta (SQL-benzeri) |
| Migration | ++ Prisma Migrate | + Drizzle Kit |
| Edge/Serverless destek | sınırlı (wasm ile) | ++ (hafif, edge uyumlu) |
| Soyutlama | yüksek (Prisma Client) | düşük, SQL'e yakın |
| Bundle boyutu | daha büyük | çok küçük |
| Topluluk | daha olgun | hızlı büyüyen |
| Geliştirme deneyimi | ++ (Prisma Studio) | + (drizzle studio) |

## Öneri
- Kurumsal/CRUD ağırlıklı, ekip yeni başlıyorsa **Prisma**.
- Edge/Serverless hedef, Vercel Edge/Cloudflare Workers, performans kritikse **Drizzle**.
- Ekibin SQL hakimiyeti yüksekse ve "ORM fazla soyutlama" hissinden kaçınmak istiyorsanız Drizzle.

## Kararlarımız
- Yeni projede ikisi de kabul edilir; varsayılan **Prisma** (olgunluk ve dokümantasyon nedeniyle).
- Edge runtime şartı varsa Drizzle.
