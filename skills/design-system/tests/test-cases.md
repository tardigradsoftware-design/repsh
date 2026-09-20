# Test Senaryoları — design-system

## Test 1: Hardcode renklerin token'a çevrilmesi

**Girdi:** Bir Next.js + Tailwind projesinin bileşenlerinde dağınık renkler kullanılmış:
- `bg-blue-600` butonlarda
- `bg-blue-700` buton hover'da
- `bg-sky-500` linklerde (aynı mavi ailesi ama ton farklı)
- `text-gray-700` bazı metinlerde, `text-slate-600` diğerlerinde
- `border-gray-200` ve `border-zinc-200` karışık

**Beklenen davranış:**
1. Tek bir primary mavi belirler (örn. `hsl(217 91% 45%)` → `--primary`).
2. Nötr paleti slate veya gray olarak birleştirir; border ve muted için tek ton kullanır.
3. `tailwind.config.ts`'de `colors: { primary: {...}, muted: {...} }` olarak CSS değişkenine bağlar.
4. Bileşenlerde `bg-primary text-primary-foreground hover:bg-primary/90` ve `text-muted-foreground`
   gibi token-tabanlı sınıflara dönüştürür.
5. Tüm bileşenlerin aynı nötr paleti kullandığını denetler.
6. Dark mode değişkenlerini `:root` ve `.dark` altında tanımlar.

**Hata sayılacak davranış:**
- `bg-blue-600` yerine `bg-[#1D4ED8]` gibi hardcode hex kullanmak.
- Hem slate hem gray kullanmaya devam etmek.
- Dark mode'u tamamen unutmak.

## Test 2: Button bileşeni API'si

**Girdi:** Projede 4 ayrı yerde `<button>` etiketi farklı stillerle kullanılıyor:
- Hero'da büyük mavi CTA,
- formda küçük gri "iptal",
- tabloda kırmızı "sil" linki,
- kartta ghost "düzenle" butonu.

**Beklenen davranış:**
1. Tek bir `<Button>` bileşeni tanımlar; variant: `primary | secondary | outline | ghost | destructive`;
   size: `sm | md | lg | icon`; loading state, disabled, asChild.
2. Tüm eski 4 butonu bu bileşeni kullanacak şekilde dönüştürür.
3. cva (class-variance-authority) veya benzer bir mekanizma ile varyantları tanımlar.
4. Focus ring, disabled state, cursor, icon spacing standart hale gelir.
5. Türkçe `aria-label` erişilebilirlik notu ekler (sadece ikonlu butonlar için).
6. `className` ile özelleştirmeye izin verir ama varsayılan stilleri tutarlı yapar.

**Hata sayılacak davranış:**
- Her variant için ayrı bileşen yazmak (ButtonPrimary, ButtonSecondary gibi — DRY ihlali).
- Yeni bileşende eski stillerden kalan sınıflar yüzünden tutarsız görünüm.
- Loading/Disabled state'leri eklememek.
