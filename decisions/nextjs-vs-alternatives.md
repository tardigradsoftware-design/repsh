# Karar: Next.js vs Diğer React/Vue Framework'leri

*Tarih: 2026-09-20 · Doğrulandı: 2026-09-20 · Bitiş: 2026-12-20*

## Adaylar
- **Next.js 16** (App Router, RSC)
- **Astro 5+** (content-first, islands)
- **Remix / React Router Framework** (React tabanlı, web standardı)
- **SvelteKit** (Svelte)
- **Nuxt 3** (Vue)
- **Vite + React SPA** (client-only)

## Karşılaştırma

| Boyut | Next.js | Astro | Remix | SvelteKit | Nuxt | Vite SPA |
|---|---|---|---|---|---|---|
| SSR/SSG/ISR | + | + | + | + | + | - |
| RSC | + | kısmi | - | - | - | - |
| SEO/Marketing/Pazarlama | + | ++ | + | + | + | - |
| Dashboard/B2B | + | - (az interaktif) | + | + | + | +/- |
| E-ticaret | + | +/- (katalog iyi, checkout için ek iş) | + | + | + | - |
| Ekosistem (UI, kütüphane) | ++ (çok geniş) | + | + | + | + | ++ |
| Vercel ile birinci sınıf | ++ | + | + | + | + | - |
| Öğrenme eğrisi | orta | kolay | orta | kolay-orta | orta | kolay |
| Backend/Server Action/Route | ++ | + | ++ | ++ | ++ | - |
| Edge/Serverless | ++ | + | + | + | + | - |

## Öneri
- **Varsayılan seçim Next.js 16 App Router.** Sebep: ekosistem zenginliği, Vercel dağıtım olgunluğu,
  RSC ile performans, pazarlama + dashboard + e-ticaret tek çatıda, pazar ve iş ilanında benimsenme.
- **İçerik odaklı, az interaktif siteler için Astro** (blog, doküman, basit landing).
- **Vue ekibiyle çalışılıyorsa Nuxt 3.**
- **Tamamen client-side, oyun/interaktif araç gibi nadir durumlarda Vite + React SPA** (SEO gerekmiyorsa).

## Kararlarımız
- Pazarlama, kurumsal site, dashboard, e-ticaret: **Next.js** (varsayılan).
- Blog/doküman: **Astro** veya Next.js.
- Mevcut React SPA yavaşça App Router'a taşınabilir; sıfırdan SPA başlatmayın.

## Kaynaklar
- nextjs.org/docs, astro.build, remix.run, kit.svelte.dev, nuxt.com
