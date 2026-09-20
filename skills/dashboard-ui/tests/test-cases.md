# Test Senaryoları — dashboard-ui

## Test 1: Sipariş listesi sayfası

**Girdi:**
> E-ticaret operasyon panelinde siparişler listelenecek. Sipariş numarası, müşteri, tutar,
> durum (Yeni/Onaylandı/Kargoda/Teslim/İade), tarih, ödeme durumu, kargo firması filtrelenecek.
> Yetkiler: Operatör görebilir ve durum güncelleyebilir; finans tutar görebilir ama sipariş
> düzenleyemez; yönetici her şeye erişebilir.

**Beklenen davranış:**
1. Rota ve yetki matrisi çıkar: hangi rol hangi kolonu görür / hangi butona basar.
2. Tablo kolonları tanımlanır; durum için renk + ikon + metin (sadece renk yetmez, a11y).
3. Filtreler: durum (çoklu seçim), tarih aralığı, arama (sipariş no / müşteri adı), kargo firması;
   aktif filtre chip'ler; URL'de query param olarak saklanır.
4. Toplu işlem: birden fazla sipariş seçilince üstte/alta "N sipariş seçili · Durumu güncelle · Yazdır" barı.
5. Loading (skeleton 5 satır), empty (ilk sipariş yoksa "Siparişiniz bulunmuyor" + nasıl sipariş
   geleceğine dair not), error (yeniden dene) durumları.
6. Para formatı `₺1.234,56`, tarih `DD.MM.YYYY HH:mm`; sıralama tarih ve tutar için aktif.
7. Sayfalama sunucu-tarafı (toplam kayıt / sayfa sayısı gösterimi).
8. Sayfalama ve tablo klavye ile gezinilebilir; odak çerçevesi görünür.

**Hata sayılacak davranış:**
- Sadece "durum" kolonunu renkle kodlayıp ikon/metin koymamak.
- Loading/error/empty durumlarını atlamak.
- Para formatını `1234.56 ₺` gibi İngilizce bırakmak.
- Filtreleri URL'ye yansıtmamak (sayfa yenilendiğinde filtre kaybolur).

---

## Test 2: Türkçe biçimlendirme hatası

**Girdi:** Ajan bir sipariş kartını şu şekilde yazmış:

```jsx
<div className="flex justify-between">
  <span>{order.customerName}</span>
  <span>{order.total} TL</span>
  <span>{new Date(order.createdAt).toLocaleDateString('en-US')}</span>
  <span>{order.status}</span>
</div>
```

**Beklenen düzeltme:**
1. `toLocaleDateString('tr-TR')` → DD.MM.YYYY formatı.
2. Para için `Intl.NumberFormat('tr-TR', { style: 'currency', currency: 'TRY' })` → `₺1.234,56`.
3. Durum metni Türkçe'ye çevrilir ve ayrıca bir `statusLabel` map kullanılır; enum değerini kullanıcıya gösterme.
4. Uzun müşteri adları için kartta taşma olmaz; `truncate` veya hyphenation.
5. Düzen tutarlı: satır yüksekliği, etiket/değer hiyerarşisi (örneğin müşteri adı büyük, tarih küçük gri).

**Hata sayılacak davranış:**
- Düzeltmeyi tüm dosyada merkezi bir fonksiyona (formatCurrency, formatDate, formatStatus)
  taşımamak; her yerde ayrı locale string yazmak.
- 'TL' yazmak yerine '₺' kullanmak (genellikle kabul edilir ama her ikisini aynı projede karıştırmamak).
- Tarih/saat formatı karışık bırakmak (bazı yerde ISO, bazı yerde en-US, bazı yerde tr-TR).
