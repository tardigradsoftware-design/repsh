# Release Checklist (Canlı Yayın Öncesi)

Her canlıya alma öncesi bu listenin tamamı işaretlenmelidir. Yeni projede ilk yayın ve sonraki
her deploy için ilgili maddeler tekrarlanır.

## Kod
- [ ] `main` (veya release branch) en son commit'e güncel
- [ ] Lint ve type-check temiz
- [ ] Birim testler geçiyor
- [ ] E2E/Playwright testler geçiyor (kritik akışlar)
- [ ] DEBUG modu ve console.log temizlenmiş
- [ ] Ölü/kullanılmayan kod ve comment-out bloklar kaldırılmış
- [ ] Yeni env/secret production'a eklenmiş
- [ ] `npm audit` / bilinen CVE yok veya kabul edilmiş

## Veritabanı / Migration
- [ ] Migration staging'de denenmiş ve çalışıyor
- [ ] Rollback script hazır
- [ ] Büyük veri değişimi için bakım penceresi belirlenmiş
- [ ] Yeni tablo/kolonlar için RLS policy (Supabase) yazılmış

## Güvenlik
- [ ] Auth koruması test edildi (yetkisiz erişim yok)
- [ ] Secret/API anahtarı commit'lenmemiş veya log'larda görünmüyor
- [ ] Webhook imza doğrulaması var
- [ ] Rate limit kritik endpointlerde aktif
- [ ] Güvenlik header'ları (CSP, HSTS, X-Frame-Options, Referrer-Policy)
- [ ] HTTPS zorunlu ve yönlendirme var
- [ ] Admin paneli ekstra korumalı (IP/SSO/basic auth)
- [ ] Hassas veri log'da maskelenmiş (TCKN, kart, telefon)

## Performans
- [ ] Lighthouse Performance >85 (mobil)
- [ ] LCP <2.5s, INP <200ms, CLS <0.1
- [ ] Resimler optimize, lazy, modern format
- [ ] Fontlar swap + subset
- [ ] Kritik JS bundle bütçesi tutuluyor (<200KB gz hedef)
- [ ] 3. parti scriptler async/defer

## SEO / Meta
- [ ] Her sayfada benzersiz title/description
- [ ] Canonical ve hreflang (çoklu dil varsa)
- [ ] `robots.txt` ve `sitemap.xml` production'da erişilebilir; noindex yok
- [ ] Open Graph ve Twitter card görselleri
- [ ] Structured data (JSON-LD) gerekli sayfalarda; Rich Results Test geçiyor
- [ ] Yasal sayfalar (KVKK, Gizlilik, Çerez, Sözleşme) erişilebilir

## İçerik / Dil
- [ ] Tüm kullanıcıya görünen metinler Türkçe ve doğal (makine çevirisi kokmuyor)
- [ ] Lorem ipsum / placeholder metin yok
- [ ] Tarih/saat/para formatı TR locale
- [ ] Sahte/kanıtlanmamış metrik (%"100", "10 bin müşteri") yok ya da kanıtlanmış
- [ ] Kırık link yok (dahili link kontrolü yapıldı)
- [ ] 404 ve 500 hata sayfaları var

## Responsive / Erişilebilirlik
- [ ] 390/768/1024/1440px kırılımları test edildi
- [ ] Dokunma hedefleri 44×44px minimum
- [ ] Klavye ile gezinme çalışıyor, focus ring görünüyor
- [ ] Axe critical/serious ihlali yok
- [ ] Kontrast 4.5:1 (normal)/3:1 (büyük)
- [ ] Reduced-motion destekleniyor
- [ ] Resimlerde alt metin var

## Özellik / İşlevsellik
- [ ] Kritik akışlar gerçekten çalışıyor:
  - Kayıt/giriş/çıkış
  - Ürün gezme / sepete ekle / sepet
  - Checkout ve ödeme (test kartı ile)
  - Form gönderimi ve hata durumları
  - Sipariş / dashboard liste/filtre/sayfalama
- [ ] E-posta bildirimleri gönderiliyor (sipariş, şifre sıfırlama)
- [ ] Dosya yükleme/varsa medya depolama doğru

## İzleme
- [ ] Sentry (veya benzeri) hata izleme kurulu, DSN tanımlı
- [ ] Analytics (GA4/Plausible) çalışıyor
- [ ] Uptime monitör kurulu
- [ ] Web Vitals toplama aktif
- [ ] Log seviyeleri production'da uygun

## Deploy ve sonrası
- [ ] Preview deploy üzerinde son kontroller yapıldı
- [ ] Deploy atomic/rollback destekli
- [ ] CDN önbelleği invalidate edildi (gerekliyse)
- [ ] Canlı smoke test (5 dakika): ana sayfa, giriş, sepet, form
- [ ] 30 dk sonra hata oranları ve performans kontrol
- [ ] 24 saat sonra hata ve trafik kontrol
- [ ] Changelog ve duyuru hazır

## İşaret
- [ ] Release responsible (yayından sorumlu)
- [ ] Saat/tarih
- [ ] Sorun olursa ulaşılacak kişi
- [ ] Rollback kararı için eşik (5xx > %1, ödeme hatası, ana sayfa beyaz ekran → hemen geri al)
