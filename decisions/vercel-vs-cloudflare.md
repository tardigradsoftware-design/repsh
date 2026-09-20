# Karar: Vercel vs Cloudflare (veya Hibrit)

*Tarih: 2026-09-20*

| Boyut | Vercel | Cloudflare | Netlify |
|---|---|---|---|
| Next.js birinci sınıf | ++ | + (OpenNext ile) | + |
| Edge runtime | ++ Edge Functions | ++ Workers | + Edge Functions |
| CDN | Global | Global (kendi omurga) | Global |
| Preview deploy | ++ | + Pages Preview | ++ |
| Analytics/Speed Insights | ++ (built-in) | Web Analytics + RUM | ++ |
| Fiyatlandırma | Projeler arası pahalanabilir; kurumsal | trafik başına çok ucuz | orta |
| KV/Storage | Blob/Postgres (entegre) | R2, D1, KV, Queues, Durable Objects | Blob/KV |
| Kısıtlar | Next.js odaklı; ayar esnekliği orta | Wrangler/Workers biraz özel bilgi | az |

## Öneri
- Next.js projeleri için **varsayılan Vercel** (zero-config, App Router/ISR/RSC en iyi orada çalışır).
- Yüksek trafikli / global veya medya dağıtım ihtiyacı varsa Vercel frontend + Cloudflare proxy (ön yüz),
  veya medya/R2 Cloudflare'da tutma (hibrit).
- Sadece statik site / Workers / edge API yoğun ise Cloudflare Pages/Workers.
- Küçük projeler için Vercel en hızlı yol; büyüdükçe maliyet için Cloudflare hibrit değerlendir.

## Kararlarımız
- Varsayılan hosting **Vercel**.
- CDN ve DDoS koruması için Cloudflare (domain proxy) opsiyonel.
- Medya depolama ihtiyacında Cloudflare R2 veya Supabase Storage; maliyet duyarlıysa R2.
