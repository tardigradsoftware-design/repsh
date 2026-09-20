# Pattern: Veri Tablosu + Filtre + Sayfalama (Sunucu Tabanlı)

## Bileşenler
1. `data-table.tsx` — TanStack Table sarmalayıcı; kolon tanımı, sıralama, seçim.
2. `data-table-pagination.tsx` — Sayfalama kontrolü.
3. `data-table-toolbar.tsx` — Arama, filtre chip'leri, görünür kolon, yeni ekle butonu.
4. `data-table-faceted-filter.tsx` — Çoklu seçim filtreleri (durum, kategori).
5. `columns.tsx` — Kolon tanımı; her kolon erişilebilir başlık ve hücre render'ı.

## Temel ilkeler
- Filtre, sıralama, sayfa, sayfa boyutu URL search param olarak tutulur (paylaşılabilir, geri tuyla dönülebilir).
- Veri sunucudan sayfa başına gelir; 1000+ satır için tam liste çekme.
- Loading durumunda tablo satırları skeleton ile gösterilir.
- Toplu işlem seçimi varsa floating bar görünür.
- Yatay kaydırma (mobil/çok kolon) için `<div className="overflow-x-auto">` ile sarmala; ilk kolon sticky.

## Sayfalama response şekli
```ts
type Paginated<T> = { data: T[]; pageCount: number; rowCount: number };
```
Server action/query bu objeyi döner.

## URL state örneği (Next.js)
```ts
const searchParams = useSearchParams();
const page = Number(searchParams.get('page') ?? '1');
const q = searchParams.get('q') ?? '';
const status = searchParams.get('status') ?? '';
```

## Türkçe format
- Sayı/payımlayıcı: `Intl.NumberFormat('tr-TR')`
- Para: `Intl.NumberFormat('tr-TR',{style:'currency',currency:'TRY'})`
- Tarih/saat: `Intl.DateTimeFormat('tr-TR')`; saat 24 saat.

## Erişilebilirlik
- Tablo `<table>` semantiği ile (role="grid" değil, gerçek table).
- Kolon başlıkları `<th scope="col">`; sıralama ikonları `aria-sort` ile bildirilir.
- Satır seçimi checkbox ile; `aria-label` ile hangi satırın seçildiği duyurulur.
- Loading için `aria-busy` ve `aria-live`.
- Boş durum açıklayıcı metin ve gerekirse CTA.

## Kaynak
- shadcn/data-table: https://ui.shadcn.com/docs/components/data-table
- TanStack Table: https://tanstack.com/table

## İlgili
- `dashboard-ui` skill'i
