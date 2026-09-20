---
name: dashboard-ui
version: 1.0.0
description: "Yonetim paneli/B2B dashboard arayuzleri: tablolar, filtreler, sidebar, formlar, bos/loading/hata durumlari, grafikler, komut paleti, yogun veri arayuzleri ve Turkce arayuz notlari icin is akisi."
category: frontend
status: curated
confidence: high
requires: [frontend-design, design-system, responsive-mobile]
tags: [dashboard, admin, b2b, data-table, crud, sidebar, command-palette, turkish-ui]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

Veri yoğun yönetim panellerini (admin, B2B, CRM, operasyon paneli) tutarlı, kullanılabilir
ve hızlı üretmek. Yönetim panellerinin en sık düştüğü tuzakları (yapışmaz tablolar, kayıp
durumlar, kötü filtre, İngilizce kalan kısımlar) önlemek.

# Ne zaman kullan / kullanma

**Kullan:** Her türlü iç araç, admin paneli, CRM, operasyon ekranı, veri tablosu ağırlıklı sayfa.
**Kullanma:** Müşteriye-dönük pazarlama sitesi, basit landing page.

# Girdi

- Kullanıcı rolü (yönetici, operatör, müşteri temsilcisi, finans)
- Gösterilecek veri alanları, sık kullanılan işlemler
- Veri hacmi (onlarca, binlerce, milyonlarca satır)
- Yetki matrisi (hangi rol neyi görebilir / düzenleyebilir)
- Entegrasyonlar (ERP, muhasebe, kargo, fatura sistemleri)

# İş Akışı (ROLE-MAP → NAV → VIEWS → STATES → DATA → INTERACT → TURKISH → VALIDATE)

## 1. ROLE-MAP — Rota ve yetki matrisi

Tüm ekranları ve rolleri listele:
- Hangi rol hangi ekranı görüyor?
- Hangi rol hangi işlemi yapabiliyor? (create/read/update/delete/export/approve)
- Her ekranın en önemli birincil işlemi ne? (örn. Sipariş ekranı: listele + filtre + detay + durum güncelle)

## 2. NAV — Sidebar / navigation

- Sol taraf sabit sidebar (desktop), üstte bar (mobil) veya collapsible.
- Grup bazlı menü (Siparişler, Ürünler, Müşteriler, Ayarlar); en fazla 3 seviye.
- Aktif sayfa belirgin; hover/focus durumları net.
- Arama kutusu veya komut paleti kısayolu (⌘K) üstte.
- Kullanıcı menüsü sağ üstte (profil, çıkış, dil/şirket seçimi).
- **Mobil:** Hamburger + drawer; sidebar yerine alttan açılır.

## 3. VIEWS — Temel sayfa türleri

Her dashboard için tipik sayfalar:

1. **Liste (index):** Tablo/filtre/toplu işlem + yeni ekle butonu.
2. **Detay:** Tek kaydın tüm bilgileri, ilişkili kayıtlar, aktivite günlüğü.
3. **Yeni ekle / düzenle (form):** Bölümlere ayrılmış form, kaydet/iptal.
4. **Özet/dashboard ana sayfa:** Metrik kartları + son etkinlik + küçük grafikler.

## 4. STATES — Durum tasarımı (en çok unutulan kısım)

Her veri gösteren bileşen şu 4 durumu mutlaka sağlamalı:

- **Loading:** Skeleton (shimmer) veya spinner; tablo başlığı + satır iskeleti. Tüm sayfa yüklemesinde
  tam sayfa skeleton; sayfalama/yenilemede satır bazlı.
- **Empty:** Bağlama özel boş durum (sadece "Veri bulunamadı" yetmez; yönlendirici metin ve mümkünse ilk adım CTA'sı).
- **Error:** Hata mesajı (Türkçe, anlaşılır) + "Yeniden dene" butonu.
- **Success/veri:** Normal görünüm, toplu işlem sonrası toast bildirimi.

## 5. DATA — Tablo ve veri yoğunluğu

- **Temel tablo özellikleri:**
  - Sıralama (tıklanabilir kolon başlığı, ok ikonu)
  - Sütun ayarlama (isteğe bağlı olarak hangi kolonlar görünsün)
  - Yatay kaydırma (mobil ve çok kolonlu tablolarda)
  - Sabit (sticky) ilk kolon ve son kolon (eylem butonları)
  - Satır tekil seçim (checkbox) + toplu seçim
  - Sayfalama veya sonsuz kaydırma (1000+ satır için sunucu tarafı)
  - Satır detayı (genişletme, inline)
- **Filtreler:**
  - Yüzeye çıkan yaygın filtreler (durum, tarih aralığı, arama kutusu)
  - Gelişmiş filtreler "Filtrele" butonu arkasında
  - Aktif filtreler chip/rozet olarak görünmeli; tek tek veya toplu temizlenebilmeli
  - Filtre URL'de yansıtılmalı (`?status=active&page=2`) → paylaşılabilir, geri-tuyla geri döndürülebilir
- **Toplu işlemler:** Satır seçilince altta/üstte floating bar (örn. "5 sipariş seçildi · Onayla · Yazdır · İptal").
- **Sütun başına veri formatı:**
  - Sayılar: Türkiye formatı `1.234,56` (Intl.NumberFormat('tr-TR'))
  - Para: `₺1.234,56` (narrow non-breaking space veya düz boşluk)
  - Tarih: `DD.MM.YYYY` (`tr-TR` locale)
  - Saat: `HH:mm` (24 saat)
  - Telefon: `0 (532) 123 45 67`
  - TCKN/VKN: uygun format

## 6. INTERACT — Etkileşim

- Formlar için: bölümlere ayır, uzun formlarda step/sekme kullan; anında doğrulama (zod + react-hook-form);
  başlıkta kaydedilmemiş değişiklik uyarısı.
- Silme/yıkıcı işlemler için onay dialog'u (tekrar doğrulama veya metinle onay isteme).
- Komut paleti (⌘K): hızlıca sayfaya atlama, arama, sık işlemler.
- Klavye kısayolları: J/K ile satır gezme, N yeni ekle, / ara, Cmd+Enter kaydet.
- Bildirimler/toast: başarılı/hata/bilgi; 3–5 sn sonra otomatik kaybolur, yığılma olmaz.

## 7. TURKISH — Türkçe arayüz özel notları

- **İ/ı problemi:** Büyük-küçük dönüşümde (i→İ, I→ı) `toLocaleUpperCase('tr-TR')` kullan; aksi
  takdirde filtreleme ve aramada hatalar oluşur.
- **Tarih biçimi:** DD.MM.YYYY; ABD formatı MM/DD/YYYY kesinlikle yok. Saat 24 saat.
- **Para:** ₺ sembolü sol tarafta; bin ayracı nokta, ondalık virgül.
- **Çeviri kalitesi:** "Loading" → "Yükleniyor"; "Save" → "Kaydet"; "Delete" → "Sil";
  makine çevirisi kokan (doğal durmayan) ifadeleri düzeltmek için gerçek bir kullanıcı gibi oku.
- **Filtre etiketleri:** "Hepsi", "Bugün", "Bu hafta", "Bu ay", "Özel aralık" takvim algısına uymalı.
- **Boş durumlar:** Türkçe, samimi ama profesyonel dil; "Burada henüz bir şey yok" + ne yapacağına
  dair yol gösterici metin.
- **Zaman farkı:** "2 saat önce", "dün", "3 gün önce" göreli zaman gösterimleri Türkçe ve doğru
  olmalı (Intl.RelativeTimeFormat('tr')).
- **KVKK:** Kişisel veri gösterilen ekranlarda maskeleme (örn. TCKN'nın ilk 3 ve son 2 hanesi).

## 8. VALIDATE — Doğrula

- 1280px+ (dizüstü), 768px (tablet), 390px (telefon) kırılımlarında test et.
- Gerçek veri hacmi ile (200+ satır) tablo performansı; sanal listeleme gerekli mi bak.
- Klavye ile gezme: Tab ile tüm etkileşimli öğelere ulaşılıyor mu?
- Ekran okuyucu: kolon başlıkları, satır kimliği, durum rozeti açıklamaları.
- Renk körü dostu: durum rozetleri sadece renkle değil, ikon/kelime ile de ayırt edilmeli.

# Çıktı

- Sidebar menü yapısı (gruplar + linkler + yetkiler)
- Ana layout (sidebar + topbar + content + footer minimal)
- Sayfa tipleri (liste, detay, form, özet)
- Tablo iskeleti (column config, filtre yapısı, sayfalama)
- Form alanları ve validasyon şeması
- Loading/empty/error/success durum bileşenleri

# Kalite Kontrol Listesi

- [ ] Rota ve yetki matrisi çıkarıldı
- [ ] Sidebar/nav tasarlandı, aktif durum net
- [ ] Loading/empty/error durumları tasarlandı
- [ ] Tablo: sıralama, filtre, sayfalama, toplu işlem var
- [ ] Filtreler URL'ye yansıyor
- [ ] Silme/yıkıcı işlem onayı var
- [ ] Türkçe biçimlendirme (tarih, para, telefon, TCKN) doğru
- [ ] Komut paleti (⌘K) veya hızlı arama var
- [ ] KVKK maskelemesi ve kişisel veri koruması düşünülmüş
- [ ] Klavye navigasyonu ve temel a11y kontrol edildi
- [ ] Büyük liste için sanallaştırma kararı (gerekli/gerekli değil) verildi

# Yaygın Hatalar

- **Hata:** Tablo dolu görünümü tasarlayıp loading/empty/error durumlarını unutmak.
- **Düzeltme:** 4 durumu da her liste için yaz; skeleton ve empty state birinci gün hazır olsun.
- **Hata:** Filtreleri sidebar'a veya popup'ın içine tıkmak, kullanıcı hangi filtrelerin aktif olduğunu görmüyor.
- **Düzeltme:** Aktif filtreleri chip olarak üstte göster; temizleme imkanı ver.
- **Hata:** Tarih ve parayı İngilizce formatta bırakmak.
- **Düzeltme:** Intl.* API'lerini merkezi bir format() fonksiyonunda topla; tüm UI oradan kullansın.
- **Hata:** Sil butonunu her satırda kırmızı yapmak — çok gürültü, yanlış tıklama riski.
- **Düzeltme:** Silme işlemini ya toplu işlemde ya satır açılır menüsünde ikincil işlem olarak ver.
- **Hata:** Komut paleti yerine her yere buton koymak.
- **Düzeltme:** Sık işlemleri komut paletine ekle; uzun vadede kullanıcı verimliliği artar.

# Referanslar

- TanStack Table: https://tanstack.com/table
- Refine: https://refine.dev/
- React Admin: https://marmelab.com/react-admin/
- Linear (komut paleti ve klavye kullanımı referansı)
- shadcn/data-table: https://ui.shadcn.com/docs/components/data-table
- Bu KB: `patterns/table-with-filters.md`, `patterns/sidebar.md`

# İlgili Skill'ler

- `frontend-design`
- `design-system`
- `responsive-mobile`
- `browser-testing`
- `security-audit` (yetki ve veri maskeleme)
- `accessibility-audit`
