# Test Senaryoları — frontend-design

## Test 1: Hiyerarşi kuramayan ajana düzeltme

**Girdi:** Bir ajan, bir B2B SaaS için landing page'i şöyle çıkarmış:
- Navbar + hero (başlık + alt başlık + CTA) aynı yatay seviyede ve aynı beyaz arka planda;
- hero başlığı 32px, navbar linkleri 16px; aradaki fark az;
- 3 özellik kartı ile 3 fiyat kartı tamamen aynı görsel ağırlıkta (aynı `p-6 rounded-xl shadow`);
- birden fazla turuncu/pembe/mor vurgu;
- 3 tane aynı görsel ağırlıkta CTA ("Başla", "Demo", "Dokümantasyon").

**Beklenen davranış:**
1. Hiyerarşi katmanlarını yeniden atar: Hero ve ana CTA katman 1, özellikler katman 3, fiyatlandırma
   katman 3 ama ayrı bölümde, ikincil CTA'lar katman 4.
2. Başlık 44–56px, navbar link 14px; kontrast sağlar.
3. Özellik kartları ile fiyat kartlarını görsel olarak ayırır (fiyat kartlarını vurgulu yapar,
   örneğin popüler planda hafif renk arka planı ve "En popüler" rozeti).
4. Tek bir ana renk (örn. marka mavisi); turuncu sadece "indirim/yeni" rozetinde, pembe/mor kaldırılır.
5. CTA'ları birincil + ikincil (hayalet) olarak düzenler; üçüncüyü kaldırır veya metin link yapar.

**Hata sayılacak davranış:**
- Hiyerarşiyi tamamen düz bırakıp sadece renkleri değiştirmek.
- Birden fazla CTA'yı aynı boyutta tutmak.

---

## Test 2: Uzun Türkçe metinlerin kutuya sığması

**Girdi:** Kullanıcı "Güvenli ve Özelleştirilebilir E-Fatura Entegrasyonu" özelliğini kartta göstermek istiyor.
Şu anki kod:

```jsx
<h3 className="text-lg font-bold">Güvenli ve Özelleştirilebilir E-Fatura Entegrasyonu</h3>
```

200px genişliğinde, 24px satır yüksekliğinde bir kartta taşma oluyor.

**Beklenen davranış:**
- Uzun kelimelerin kutuyu kırmasını engellemek için `hyphens: auto`, `overflow-wrap: break-word` veya
  güvenli `word-break: break-word` önerir.
- Kart minimum yüksekliğini standartlaştırır (grid'de tüm kartlar aynı boyda kalsın).
- Başlığın 2 satırı geçmesi durumunda metni kısaltma alternatifi sunar (kullanıcıya sorarak):
  örn. "E-Fatura Entegrasyonu (Güvenli, Özelleştirilebilir)".
- Line-height 1.3'e çeker; Türkçe uzun kelimeleri kırarken satır sonu tirelerini doğru ayarlar.
- Tüm özellik kartlarında tutarlılık sağlar (3 satıra çıkan diğer kartlar da varsa onlar da uyumlu olsun).

**Hata sayılacak davranış:**
- `truncate` veya `line-clamp-1` kullanıp metni kesmek (bilgi kaybı).
- `w-[300px]` verip kartı keyfi genişletmek (grid hizalamasını bozmak).
- `text-sm` yapmak (okunurluk düşer).
