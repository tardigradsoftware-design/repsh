# Pattern: Dashboard Sidebar + Topbar Layout

## Yapı
```
<div className="grid min-h-screen grid-cols-1 md:grid-cols-[240px_1fr]">
  <Sidebar className="hidden md:block" />
  <div className="flex flex-col">
    <Topbar />
    <main className="flex-1 p-4 md:p-8">
      {children}
    </main>
  </div>
</div>
```
Mobilde hamburger ile açılan `<Sheet>` (drawer) Sidebar kullanılır.

## Sidebar özellikleri
- Logo + versiyon/ortam rozeti (DEV/STAGING mutlaka belli olsun).
- Grup bazlı menü (`NavMain`, `NavAdmin`); her link aktif durumda belirgin arka plan vurgu rengi.
- İkon + etiket; sadece ikon collapse versiyonu opsiyonel.
- En altta kullanıcı/ayar linki.
- Masaüstü 240px sabit genişlik; tablet ve altında drawer.

## Topbar
- Sol: mobil hamburger + breadcrumb veya sayfa başlığı.
- Orada/sağ: arama kutusu (⌘K ile komut paleti açılır).
- Sağ: bildirim, yardım, kullanıcı menüsü.
- Sticky yapıştırılır ama çok kalın değil (56–64px yükseklik).

## Komut paleti (⌘K)
- cmdk kütüphanesi veya benzeri; sayfa arası atlama, hızlı işlem.
- 1. seviye: sayfalar; 2. seviye: yeni kayıt, kullanıcı ara, ayarlar.

## Erişilebilirlik
- Drawer açıldığında focus trap; ESC ile kapanır.
- Aktif menü ögesi `aria-current="page"`.
- Küçük ekranlarda hamburger buton `aria-label` ve `aria-expanded`.
- Sidebar `nav` semantik etiketi.

## TR notları
- Menü etiketleri öz Türkçe: "Gösterge Paneli" yerine zaman zaman "Kontrol Paneli" veya toplulukta
  "Panel" de kullanılır ama ekip standardını seçip tutarlı kullan.
- "Dashboard" kelimesini Türkçe "Panel" olarak çevirmenin ek maliyeti yok ama "Dashboard" da
  sektörde benimsenmiştir; ekip kararına göre tek birini seç.

## Kaynak
- shadcn sidebar: https://ui.shadcn.com/docs/components/sidebar
- Linear sidebar referansı

## İlgili
- `dashboard-ui` skill'i
