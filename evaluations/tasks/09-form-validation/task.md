# Görev 09: Çok Bölümlü Form Doğrulaması
## Açıklama
Bireysel/kuruumsal fatura bilgisi formu: ad/soyad veya ünvan/VKN, TCKN (11 hane), vergi dairesi, adres, telefon, e-posta. Bölümler halinde (kişisel, fatura, adres). react-hook-form + zod.
## Başarı
- Bireysel/kurumsal seçimine göre alanlar dinamik
- TCKN/VKN basit format/algoritma kontrolü
- Telefon 0(5xx) XXX XX XX formatı
- Anında doğrulama (blur) + hata özeti başlıkta
- Kaydedilmemiş değişiklik uyarısı (sayfadan çıkarken)
- Erişilebilir: label, aria-describedby, hata duyurusu
- Klavye ile tam akış çalışıyor
