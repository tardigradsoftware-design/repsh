# Stack: B2B Dashboard / Admin Panel / CRM

## Ne için
- Operasyon paneli, CRM, iç araçlar, veri görüntüleme, form yönetimi.

## Teknolojiler
- **Framework:** Next.js 16 App Router; Server Component öncelikli.
- **UI:** Tailwind + shadcn/ui + Radix + Lucide + tema token'ları.
- **Veri:** Supabase Postgres + RLS; ORM Prisma (veya Drizzle edge gerekirse).
- **Auth:** Supabase Auth (SSO gerekiyorsa Auth.js/Clerk).
- **State/Tablo:** TanStack Query (client fetch için) + TanStack Table.
- **Form:** react-hook-form + zod.
- **Grafik:** Chart.js/Recharts (basit) / ECharts (karmaşık).
- **Komut paleti:** cmdk.
- **Test:** Vitest + Playwright + axe-core.
- **İzleme:** Sentry + Vercel Analytics + Speed Insights.
- **Hosting:** Vercel + Supabase Cloud.
- **Dosya depolama:** Supabase Storage (veya Cloudflare R2).

## Opsiyonel
- Raport/PDF: react-pdf, jspdf, Recharts export.
- Gerçek zamanlı: Supabase Realtime.
- Çoklu kiracı (multi-tenant): `organization_id` + RLS policy.
