# Karar: Supabase vs Firebase vs Geleneksel Kendi Backend'in

*Tarih: 2026-09-20 · Doğrulandı: 2026-09-20 · Bitiş: 2026-12-20*

## Boyutlar

| Boyut | Supabase | Firebase | Convex | Kendi Backend (Node/Express/Nest) |
|---|---|---|---|---|
| Veritabanı | Postgres (ilişkisel, açık) | Firestore (NoSQL) | Convex DB (reactive) | Herhangi |
| Auth | + (email, OAuth, phone) | + (Google öncelikli, çok geniş) | + | siz kurarsınız |
| RLS/Yetki | ++ (Postgres RLS) | + (Security Rules) | + (functions-based) | siz kurarsınız |
| Realtime | + | + | ++ | siz kurarsınız |
| Edge Functions | + (Deno) | + (Cloud Functions) | + | + |
| Depolama | + Storage | + Cloud Storage | + | S3/R2 sizin |
| Taşınabilirlik | ++ (Postgres standart) | - (vendor lock-in güçlü) | - | ++ |
| Fiyat / free tier | cömert | cömert | yeni, sınırlı | size bağlı |
| Ekosistem/olgunluk | + | ++ | genç | +++ |
| Tip desteği | ++ (TS + Prisma/Drizzle) | + (TS SDK) | + | +++ |

## Öneri
- **MVP, startup, küçük/orta ölçek:** Supabase. Postgres + RLS + Realtime + Storage hepsi hazır;
  hızlı başlarsın; ileride dışarı çıkmak Postgres olduğu için kolay.
- **Çok yüksek trafik / karmaşık iş kuralları / ERP entegrasyonu ağır:** Kendi backend
  (NestJS veya Next.js Route Handler + Postgres).
- **Mobil öncelikli, basit senkron, gerçek zamanlı:** Firebase (ama lock-in göze almak lazım).
- **Gerçek zamanlı iş birliği (whiteboard, doc):** Convex veya Liveblocks gibi özel seçenekler
  (Supabase Realtime ile kısmen).

## Kararlarımız
- Web projelerimizin varsayılanı **Supabase + Postgres** (güvenli kullanım şartıyla: RLS zorunlu,
  service role server-only).
- Kurumsal/e-ticaret kompleks senaryolarda kendi API katmanı (Next.js Route Handler veya Nest)
  eklenebilir; DB olarak yine Postgres/Supabase kullanılır.

## Kaynaklar
- supabase.com/docs, firebase.google.com/docs, convex.dev
