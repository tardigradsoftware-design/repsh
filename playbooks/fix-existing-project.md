# Playbook: fix-existing-project (Mevcut projeyi iyileştir/onar)

## Amaç
Bozuk, yavaş, güvensiz veya "AI-slop" haldeki mevcut bir projeyi denetleyip iyileştirmek;
sıfırdan yazmak yerine stratejik düzeltmelerle kaliteyi yükseltmek.

## Fazlar

### 1. Keşif ve envanter (ilk 1–2 saat)
1. `git status`, son commit'ler, branch yapısı.
2. `package.json`: bağımlılıklar ve sürümleri; çok eski veya uyumsuz paket var mı?
3. `README`, `DECISIONS`, `AGENTS.md` var mı? Proje hakkında dökümantasyon ne düzeyde?
4. Çalıştır: `npm install`, dev server açılıyor mu? Build alınabiliyor mu? Tip/lint temiz mi?
5. Hangi sorunlar bildirilmiş? Kullanıcı şikayetleri neler? Hata log'ları ve Sentry kayıtları var mı?
6. Tarayıcıda ana sayfaları aç; açık JS hataları, 404 asset, konsol uyarısı.

### 2. Denetim (yarım gün)
- `ai-slop-detection` ile görsel tarama.
- `security-audit` hızlı tarama (auth, secret, RLS, XSS).
- `performance-audit` Lighthouse ile temel metrik.
- `accessibility-audit` axe ile.
- `seo-audit` meta/robots/canonical kontrol.
- Kodu hızla tarayarak: tip güvenliği, any kullanımı, tekrarlar, ölü kod, büyük component'ler,
  N+1 sorgu, hata yönetimi.

### 3. Skor ve öncelik
- `website-quality-review` skorunu hesapla.
- Bulguları CRITICAL/HIGH/MEDIUM/LOW olarak grupla.
- Kullanıcı ile beklenti ve süre mutabakatı yap: 1 haftalık hızlı kazanım mı, yoksa 4–6 haftalık
  köklü onarım mı?

### 4. Hızlı kazanımlar (1–3 gün)
Küçük ama etkili dokunuşlar:
- Bariz bug fix (beyaz ekran, kırık link, bozuk form).
- Konsol hataları.
- Temel güvenlik açıkları (secret sızıntısı, IDOR).
- Görsel en kötü AI-slop sayfaları (hero, boş durum, buton stilleri).
- Build ve tip hatalarını temizle.
- Lighthouse skoru 50 altıysa kolay performans düzeltmeleri (resim, font, lazy).

### 5. Köklü iyileştirmeler (1–4 hafta)
- Tasarım sistemi kurulumu (renk/spacing token'ları, bileşenler).
- Veri modeli düzeltmeleri / migration.
- Test altyapısı (Vitest + Playwright) kur.
- Güvenlik sertleştirmesi (CSP, rate limit, audit log).
- Eksik sayfalar (boş durumlar, loading, error, 404).
- Responsive kırılımlar.
- Animasyon ve hareket ayarı.

### 6. Test ve regresyon
- Her ana akış için Playwright testi yaz.
- Canlı öncesi smoke test.
- Bilinen hatalar için regression test.

### 7. Yayın ve izleme
- `deployment` playbook'una göre aşamalı publish.
- Hata izleme, analytics, uptime monitör kur.
- Son `website-quality-review` skoru ve öncekiyle karşılaştırma raporla.

## Prensip

- "Hepsini birden silip yeniden yaz" refleksine diren. Büyük rewrite genellikle yeni bug'lar getirir.
- Önce CRITICAL'ları kapat; sonra HIGH; MEDIUM ve LOW'yu kapsam dahilinde veya sonraki iterasyona bırak.
- Her küçük düzeltme ayrı commit; gözden geçirilebilir.
- Yeni bir şey eklemeden önce var olan bozuk olanı düzelt.

## İlgili skill'ler
`debugging`, `browser-testing`, `security-audit`, `performance-audit`, `ai-slop-detection`,
`code-review`, `website-quality-review`.
