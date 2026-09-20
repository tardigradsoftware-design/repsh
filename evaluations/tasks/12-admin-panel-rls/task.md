# Görev 12: Admin Panel RLS Denetimi
## Açıklama
Bir Supabase projesinde tablolar: customers, orders, invoices. RLS etkin ama policy'ler eksik. Bazı kullanıcılar rastgele müşteri kayıtlarını görebiliyor.
## Başarı
- Her tablo için okuma/yazma policy'leri doğru
- Admin rolu özel policy ile ayrıştırılmış
- Kullanıcılar birbirinin verisini göremiyor (Playwright ile 2 farklı kullanıcı ile test)
- Hassas alanlar (TCKN, telefon) metin olarak dönmüyor (maskeleme veya hariç tutma)
- Service role istemcide kullanımı yok
