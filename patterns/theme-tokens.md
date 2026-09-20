# Pattern: CSS Değişkenleri ile Tema/Tasarım Sistemi Token'ları

## Bağlam
Tailwind + shadcn/ui (veya herhangi bir React stack) ile renk, tipografi, spacing bir kez
tanımlanıp her yerde token olarak kullanılır. Aynı zamanda dark mode ve marka değişimi
tek yerden yönetilebilir.

## Kod (global.css)
```css
:root {
  --font-sans: 'Inter', system-ui, sans-serif;

  --background: 0 0% 100%;
  --foreground: 222 47% 11%;
  --card: 0 0% 100%;
  --card-foreground: 222 47% 11%;
  --muted: 210 40% 96%;
  --muted-foreground: 215 16% 47%;
  --border: 214 32% 91%;
  --input: 214 32% 91%;
  --primary: 217 91% 45%;         /* #1D4ED8 */
  --primary-foreground: 0 0% 100%;
  --secondary: 210 40% 96%;
  --secondary-foreground: 222 47% 11%;
  --accent: 210 40% 96%;
  --destructive: 0 84% 60%;
  --destructive-foreground: 0 0% 100%;
  --ring: 217 91% 60%;

  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
  --radius-xl: 1rem;

  --shadow-sm: 0 1px 2px rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 8px rgb(0 0 0 / 0.08);
}
.dark {
  --background: 222 47% 8%;
  --foreground: 210 40% 98%;
  --card: 222 47% 11%;
  --card-foreground: 210 40% 98%;
  --muted: 217 33% 17%;
  --muted-foreground: 215 20% 65%;
  --border: 217 33% 20%;
  --input: 217 33% 20%;
  --primary: 217 91% 60%;
  --primary-foreground: 222 47% 11%;
  --ring: 217 91% 60%;
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Tailwind config (kesit)
```ts
export default {
  darkMode: ['class'],
  theme: {
    extend: {
      colors: {
        border: 'hsl(var(--border))',
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        primary: { DEFAULT: 'hsl(var(--primary))', foreground: 'hsl(var(--primary-foreground))' },
        // ...
      },
      borderRadius: {
        lg: 'var(--radius-lg)',
        md: 'var(--radius-md)',
        sm: 'calc(var(--radius-sm))',
      }
    }
  }
}
```

## Neden iyi
- Renk kodları tek yerde; pazarlama/marka değişimi 10 satırda yapılır.
- Dark mode için ayrı kopya kod gerekmez.
- Hardcode `bg-blue-600` yerine `bg-primary`; tüm bileşenler otomatik uyar.
- Reduced-motion global bir güvenlik ağı.

## Yapılması gereken
- Hiçbir bileşende doğrudan hardcode hex/rgb kullanma.
- Renk eklerken hem light hem dark değeri tanımla.
- Tipografi ve spacing token'ları benzer şekilde ekleyebilirsin.

## Kaynak
- shadcn/ui theming: https://ui.shadcn.com/docs/theming
- Radix Colors: https://www.radix-ui.com/colors

## İlgili
- `design-system`, `frontend-design` skill'leri
