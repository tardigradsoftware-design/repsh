# Playbook: build-dashboard (B2B/Admin/Operasyon Paneli)

## Amaç
Veri yoğun yönetim paneli / B2B SaaS / CRM / operasyon ekranı inşa akışı.

## Fazlar

### 1. Kapsam ve yetki
- Rol matrisi (admin, operatör, finans, müşteri temsilcisi).
- Hangi ekranlar var (liste, detay, form, özet, rapor)?
- Yetkilendirme modeli: hangi rol hangi veriyi görür / değiştirir / siler / onaylar.
- Entegrasyon listesi: ERP, kargo, muhasebe, fatura, bildirim.

### 2. Stack ve mimari
- Next.js + React + Tailwind + shadcn/ui (özelleştirilmiş) + TanStack Table/Query; form için react-hook-form + zod;
- Supabase/Postgres + Prisma/Drizzle; auth (Supabase Auth/Auth.js/Clerk);
- Grafik için Chart.js veya Recharts (basit) / ECharts (karmaşık).
- `dashboard-ui` skill'in desenlerini uygula.

### 3. Tasarım sistemi ve navigation
- Kurumsal/marka renkleri token'la.
- Sidebar gruplu menü (mobil drawer), üst arama/komut paleti, kullanıcı menüsü.
- Komut paleti (⌘K), klavye kısayolları.
- Boş/loading/error/durum bileşenleri; bunları yapmadan tablolara geçme.

### 4. Veri modeli
- `database-design` ile tablo şeması, FK, enum, indeks, RLS policy.
- Audit log (kim neyi ne zaman değiştirdi).
- Soft delete arşiv tablosu.
- Migration stratejisi.

### 5. Sayfalar
1. Giriş/şifre unuttum/2FA
2. Özet (metrics + son etkinlik + küçük grafikler)
3. Ana listeler (tablo + filtre + toplu işlem)
4. Detay (sekmeli, ilişkili kayıtlar, aktivite)
5. Yeni/düzenle formları (bölümlü, kaydet/iptal, kaydedilmemiş uyarısı)
6. Ayarlar/profil/şirket

Her liste için: sunucu tarafı pagination, URL tabanlı filtre, sıralama, aktif filtre chip'leri.

### 6. Form akışları
- Bölümlü form; hata özeti + inline hata.
- Yanlış girişte anında dönüt; kaydetmeden önce değişiklikler varsa çıkışta uyarı.
- Yıkıcı işlemler onay dialog'u.
- Başarılı işlem toast + yönlendirme.

### 7. Güvenlik
- `security-audit`: RLS, IDOR, rate limit, auth, cookie ayarları.
- Production'da admin paneli ekstra koruma (IP kısıt / SSO / MFA).
- KVKK maskeleme (TCKN, telefon tam görünmesin).

### 8. Test
- Playwright ile her rol için akışlar (admin yapabiliyor, viewer yapamıyor).
- Büyük veri ile performans (sanal liste gerekli mi?).
- Klavye/erişilebilirlik.

### 9. İzleme ve dağıtım
- Hata izleme (Sentry); audit log; kullanıcı aktivite metriği.
- Deploy: preview/staging/production.

### 10. Son denetim
- `website-quality-review` dashboard varyasyonu; skor 80+ ise canlı.

## İlgili skill'ler
`dashboard-ui`, `design-system`, `database-design`, `api-design`, `security-audit`,
`browser-testing`, `accessibility-audit`.
