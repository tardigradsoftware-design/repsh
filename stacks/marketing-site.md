# Stack: Pazarlama / Kurumsal Site

## Ne için
- Hizmet/ürün tanıtım sitesi, landing page, kurumsal site, kişisel portföy.
- İçerik ağırlıklı, etkileşim az (form, blog, basit SSS).

## Teknolojiler
- **Framework:** Next.js 16 (App Router)
- **Stil:** Tailwind v4 + shadcn/ui (özelleştirilmiş)
- **CMS (içerik):** İlk sürüm Markdown/MDX; büyürse Contentlayer/Sanity/Payload.
- **Form:** react-hook-form + zod; Server Action ile e-posta gönder (Resend/SMTP).
- **Spam koruma:** Cloudflare Turnstile veya honeypot.
- **Hosting:** Vercel (domain Vercel veya Cloudflare üzeri).
- **Analytics:** Plausible (gizlilik dostu) veya GA4.
- **SEO:** Next.js metadata + JSON-LD (Organization, WebSite, Breadcrumb, Service).
- **Erişilebilirlik:** WCAG 2.2 AA; axe ile denetim.

## Hariç
- Auth, admin paneli, ödeme (bu stack'te yok).
- İhtiyaç olursa ayrı panel kurulur; anasiteye karışmaz.
