---
name: design-system
version: 1.0.0
description: "Proje icin token tabanli tutarli tasarim sistemi kurmak; renk, tipografi, spacing, radius, shadow, bileşen API'sini standartlastirmak."
category: frontend
status: curated
confidence: high
requires: [frontend-design]
tags: [design-system, tokens, css, theming, variables, consistency]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

Projede bütün UI çıktısını aynı standartta üretmek için temel olan tasarım token'larını
ve bileşen API'sini kurmak. Ajanın veya geliştiricinin her yeni ekranda keyfi karar vermesini
engeller; görsel tutarlılığı ve bakım kolaylığını sağlar.

# Ne zaman kullan

- Yeni proje başlangıcında ilk 1–2 gün
- Mevcut projede renk/spacing tutarsızlığı görülüyorsa (AI-slop denetimi sonrası)
- Tema (dark/light), marka değişimi veya çoklu markayı destekleyeceksen
- Tasarımcı elinden Figma çıktısı geliyorsa onu kod token'larına dökerken

# Ne zaman kullanma

- Sadece bir kerelik prototip (rastgele renklerle çalışmak sorun değil ama en azından temel
  tutarlılığı koru)

# Girdi

- Marka kimliği (logo, logo rengi, varsa tipografi)
- Figma veya referans taslak (varsa)
- Proje teknolojisi (Next.js + Tailwind, CSS Modules, SCSS, MUI, shadcn/ui vb.)
- Erişilebilirlik hedefi (WCAG 2.1 AA standart)

# İş Akışı (TOKENS → COMPONENTS → DOCUMENTATION → ENFORCEMENT)

## 1. TOKENS — Temel birimleri tanımla

### Renk
- **Ana (primary)** marka rengi: açık/koyu tonlarıyla (50,100,200...900,950). Tek renk seç.
- **İkincil (secondary)** opsiyonel; pazarlama/marka zenginliği için.
- **Nötr (neutral/slate/gray):** 50–950 arası 11 basamak, metin, yüzey, ayraç için.
- **Semantik:** `--color-success`, `--color-warning`, `--color-danger`, `--color-info`.
- **Yüzey (surface):** `--bg`, `--surface-1`, `--surface-2`, `--border`.
- **Metin:** `--fg` (ana metin), `--fg-muted`, `--fg-subtle`.
- Tüm renkler **HSL** veya **OKLCH** tanımlanıp **CSS custom property** olarak verilir; böylece
  dark mode ve tema değişimi tek yerden yapılır.
- Her renk çifti için kontrastı kontrol et (contrast checker veya axe-core).

### Tipografi
- **Font aileleri:** `--font-sans`, `--font-serif`, `--font-mono`. Türkçe desteği olan fontları seç.
- **Boyut ölçeği:** 1.25 modüler ölçek (12–14–16–18–20–24–30–36–48–60 px). `--text-xs/sm/base/lg/xl/2xl/3xl/4xl/5xl`.
- **Satır yüksekliği:** `--leading-tight (1.15)`, `--leading-snug (1.3)`, `--leading-normal (1.5)`, `--leading-relaxed (1.65)`.
- **Harf aralığı:** başlıklarda -%1 ile 0 arası; küçük etiketlerde hafif + tracking.
- **Ağırlık:** 400, 500, 600, 700; 300/800/900 gibi aşırı ağırlıklar genellikle gereksiz.

### Spacing
- 4px taban ızgara; `--space-1 (4px)` den `--space-24 (96px)`'ye kadar üslerle büyüyen ölçek.
  Tailwind gibi 0.5 (2px)'den başlayabilir ama 8px üstü 8px/16px/24px/32px/48px/64px/96px/128px
  olmalı.
- **Kesit arası boşluklar:** `--section-y-sm (48px)`, `--section-y (80px)`, `--section-y-lg (128px)`.
- Layout için container değerleri: `--container-sm (640px)`, `--container-md (768px)`, `--container-lg (1024px)`,
  `--container-xl (1280px)`.

### Radius
- `--radius-sm (4px)`, `--radius-md (8px)`, `--radius-lg (12px)`, `--radius-xl (16px)`, `--radius-full (9999px)`.
- Aynı öğe türü aynı radius kullanmalı (tüm kartlar lg, tüm butonlar md gibi).

### Gölge
- Hafif bir gölge sistemi: `--shadow-sm`, `--shadow-md`, `--shadow-lg`; çoğu öğede `border` kullan,
  gölgeyi yalnızca öne çıkarılması gereken (dropdown, modal, hover'lanan kart) yerlerde.

### Hareket
- `--dur-fast (120ms)`, `--dur-base (200ms)`, `--dur-slow (350ms)`
- `--ease-out: cubic-bezier(0.2, 0, 0, 1)`; `--ease-spring: cubic-bezier(0.2, 0.8, 0.2, 1)`

## 2. COMPONENTS — Bileşen API'sini kur

Her temel bileşeni sıfırdan yaz; shadcn/ui veya Radix primitive'leri taban alıp tema ile özelleştir:

- Button (primary, secondary, outline, ghost, destructive; sm/md/lg; loading, icon-only)
- Input, Textarea, Select, Checkbox, Radio, Switch (Form alanları)
- Card
- Dialog / Sheet / Popover / Tooltip / Dropdown (Radix/Floating UI tabanlı)
- Badge / Tag
- Tabs, Accordion
- Toast / Alert
- Table (base + sortable + pagination için primitive'ler)
- Skeleton / Spinner (loading)
- EmptyState (bağlama özel, tek tip Inbox ikonundan kaçın)
- Data viz primitives (eğer kullanılacaksa)

Her bileşen için:
- Bileşen kendi rengini doğrudan HARDCODE etmez, token kullanır (`bg-primary`, `text-primary-foreground`).
- Variant API (size, intent) tek bir `cva()` veya benzer mekanizma ile tanımlanır.
- `className` prop'u ile genişletilebilir (as-child veya polymorphic).
- Erişilebilirlik (ARIA, klavye, focus ring) hazır gelir.

## 3. DOCUMENTATION — Dokümante et

- `/docs` veya `/components` sayfası (Storybook veya basit bir Next.js sayfası).
- Her token için kullanım kuralı (ne zaman primary, ne zaman muted).
- Her bileşen için: amaç, ne zaman / ne zaman kullanılmayacağı, örnekler, accessibility notu.

## 4. ENFORCEMENT — Sistemi zorunlu kıl

- **ESLint kuralları:** Örn. tailwind config'de sadece tanımlı renkleri kullan, raw renk kodlarını engelle.
- **PR review checklist:** Yeni renk/spacing/radius eklenmiş mi? Yeni birimler sisteme eklenmeden kullanılmış mı?
- **Figma–kod köprüsü:** Token'lar Figma ile aynı isimde olmalı.
- **AI ajan talimatları:** Ajan yeni bir renk doğrudan yazmadan CSS değişkenini kullanmalı.

# Çıktı

- `app/globals.css` (veya `tokens.css`) — CSS değişkenleri ve temel reset.
- `tailwind.config.ts` — token eşleşmesi.
- `components/ui/` — temel bileşenler.
- `lib/utils.ts` — `cn()` yardımcısı ve variant'lar.
- Dokümantasyon sayfası.

# Kalite Kontrol Listesi

- [ ] Tüm renkler CSS değişkeni olarak tanımlı, hardcode yok
- [ ] Dark mode planı var (en azından değişkenler destekliyor)
- [ ] Tipografi ölçeği modüler ve Türkçe karakter testi yapıldı
- [ ] Spacing 4px/8px taban ızgarasına oturuyor
- [ ] Bileşenler token'ları kullanıyor; hiçbirinde doğrudan `bg-blue-600` yok
- [ ] Bileşenler erişilebilir (klavye, ARIA, kontrast)
- [ ] Loading/empty/error durumları tasarlandı
- [ ] En az birincil CTA'nın focus ring'i belirgin
- [ ] Reduced-motion support var
- [ ] Dokümantasyon veya örnek sayfası mevcut

# Yaygın Hatalar

- **Hata:** shadcn/ui'yi `npx shadcn add` ile ekleyip hiç özelleştirmemek.
  **Düzeltme:** Global CSS'de `--primary` ve diğer değişkenleri kendi markana göre ayarla.
- **Hata:** 50+ renk tanımlamak.
  **Düzeltme:** Bir ana renk, bir başarı/uyarı/hata seti; gerisi nötr.
- **Hata:** Her değer için yeni CSS değişkeni açmak.
  **Düzeltme:** Sayı sınırlı olsun; 100+ değişken kafa karıştırır.
- **Hata:** px ile değil de rem/em ile düşünmemek; font büyüdüğünde düzen bozuluyor.
  **Düzeltme:** Root 16px kabul et; spacing için rem kullan (Tailwind bunu zaten yapıyor).

# Örnek

```css
:root {
  --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
  --primary: 217 91% 45%;        /* #1D4ED8, OKLCH veya HSL */
  --primary-foreground: 0 0% 100%;
  --ring: 217 91% 60%;
  --bg: 0 0% 100%;
  --fg: 222 47% 11%;
  --muted: 210 40% 96%;
  --muted-fg: 215 16% 47%;
  --border: 214 32% 91%;
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
}
.dark {
  --bg: 222 47% 8%;
  --fg: 210 40% 98%;
  --muted: 217 33% 17%;
  --border: 217 33% 20%;
}
```

# Referanslar

- shadcn/ui theming: https://ui.shadcn.com/docs/theming
- Radix Colors: https://www.radix-ui.com/colors
- Open Color: https://yeun.github.io/open-color/
- Type Scale: https://type-scale.com/
- Bu KB: `patterns/theme-tokens.md`, `knowledge/ui-ux/`

# İlgili Skill'ler

- `frontend-design`
- `ai-slop-detection`
- `accessibility-audit`
