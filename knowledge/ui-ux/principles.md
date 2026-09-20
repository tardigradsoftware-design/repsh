# UI/UX İlkeleri

Bu dosya arayüz kalitesini belirleyen temel ilkeleri kısaca özetler.
Detaylı iş akışı `frontend-design` ve `design-system` skill'lerinde.

## 1. Hiyerarşi

Her ekranda bir birincil odak (ana başlık/CTA), ikincil destekleyici öğeler ve üçüncül
bilgi bulunur. Aynı renk/ağırlık/boşlukla her şeyi eşlersen "düz" bir sayfa çıkar.

## 2. 8px ızgara

Boşlukları 4px tabanla, tipik değerleri 8/12/16/24/32/48/64/96/128 olarak kullan. Keyfi
boşluklar (21px, 37px) görsel ritmi bozar.

## 3. Tipografik ölçek

Tek bir modüler ölçek (1.25 önerilir): 12, 14, 16, 18, 20, 24, 30, 36, 48 px.
- Satır yüksekliği başlıkta 1.1–1.2, gövdede 1.5–1.6
- Harf aralığı başlıklarda hafif negatif (-%0.5–1)

## 4. Renk disiplini

- 1 ana marka rengi (açık/koyu tonlarıyla)
- 1 opsiyonel ikincil
- Başarı/uyarı/hata semantik renk seti
- Geri kalan nötr palet (slate/cool gray)
Sayfada 3'ten fazla vurgu rengi bir arada olmamalı.

## 5. Ölçülü hareket

Hareket bir bilgiyi aktarmak için var; süs için değil.
- Süre 100–350 ms
- Transform/opacity kullan (layout boyutunu animate etme)
- `prefers-reduced-motion` destekle

## 6. Geri bildirim

Her etkileşim bir yanıt vermeli:
- Buton basımı → hafif görsel tepki + loading/success durumu
- Form gönderimi → toast veya inline hata
- Ağ isteği → iskelet/spinner
- Hata → kullanıcı ne yapması gerektiğini söyleyen metin

## 7. Boş durumlar

Veri yoksa kullanıcıya sadece "veri yok" değil ne yapması gerektiğini söyleyen metin +
mümkünse ilk adım CTA'sı göster.

## 8. Türkçe kullanıcı için özel notlar

- `İstanbul`, `İzmir`, `AĞRI` gibi büyük harf dönüşümü `toLocaleUpperCase('tr-TR')` ile yapılır.
- Fiyat biçimi `Intl.NumberFormat('tr-TR',{style:'currency',currency:'TRY'})` → `₺1.234,56`.
- Tarih/saat `tr-TR` locale'i ile; saat 24 saat düzeni.
- TCKN/VKN, telefon, posta kodu input mask'leri doğru uzunlukta.
- Kullanıcının klavyesi Türkçe Q/F; büyük "İ / ı / Ğ / Ş" karakterlerinde kırılma olmasın.

## Kaynaklar

- Refactoring UI (Adam Wathan, Steve Schoger)
- Material Design Principles
- Apple Human Interface Guidelines
- Linear/Stripe/Vercel ürünleri gözlemle
