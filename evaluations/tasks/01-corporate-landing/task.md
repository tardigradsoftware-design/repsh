# Görev 01: Kurumsal Landing Page

## Açıklama
Bir lojistik firması için Türkçe kurumsal web sitesinin ana sayfasını Next.js + Tailwind ile
sıfırdan oluştur. Sayfada şu bölümler olmalı:
- Üst navbar (logo, Anasayfa, Hizmetler, Hakkımızda, İletişim, "Teklif Al" butonu)
- Hero: "Türkiye'nin güvenilir lojistik çözüm ortağı" ana mesaj + 2 CTA
- Hizmetler (4 hizmet kartı: Karayolu Taşımacılığı, Depolama, Uluslararası Taşıma, Dağıtım)
- Neden biz (3 güven göstergesi)
- Müşteri logoları (yerine placeholder veya gerçek dışı isim değil, 4–6 gerçek logo yerleştirmeyin,
  "Referanslar" başlığı altında örnek şirket isimleri kullan)
- İletişim formu (ad, şirket, e-posta, telefon, mesaj)
- Footer (KVKK, Gizlilik, Çerez, İletişim linkleri)

## Kısıtlar
- Mobil uyumlu olsun
- Form gönderiminde hata/başarı durumunu ele al (gerçek API bağlamana gerek yok, client-side feedback)
- Türkçe doğal olmalı; "Get started", "Learn more" kalmasın
- Tailwind token'ları kullanılsın; hardcode renk yerine tema değişkeni (CSS değişkeni)
- Sahte metrik kullanma; "%99.9 hizmet kalitesi" gibi rakamlar kanıtsız olmayacak

## Başarı ölçütleri

| Ölçüt | Hedef |
|---|---|
| Sayfa çalışıyor, derleniyor | yapar/yapmaz |
| 390/768/1280px responsive | düzgün |
| Lighthouse Perf/SEO/A11y | 90+ her biri |
| Axe critical/serious | 0 |
| AI-slop skoru (website-quality-review) | 75+ |
| Türkçe içerik doğal | jenerik çeviri yok |
| Form erişilebilir (label, klavye) | yapar |
| Token kullanımı (KB ile / KB'siz) | KB'li daha kısa ve doğru plan |
| Hardcode renk sayısı | 0 (token kullanılmış) |
| Sahte/iddaalı metrik sayısı | 0 |
