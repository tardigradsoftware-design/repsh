---
name: deployment
version: 1.0.0
description: "Production deployment sureci: ortam degiskenleri, build, onizleme, migrasyon, izleme, rollback, CDN, guvenlik header'lari, HTTPS."
category: devops
status: curated
confidence: high
requires: [security-audit, performance-audit, browser-testing]
tags: [deployment, vercel, cloudflare, ci, cd, migration, preview, monitoring, rollback]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

Kesintisiz, güvenli, ölçülebilir dağıtım; yanlışlıkla production bozmayı minimuma indiren prosedür.

# Ne zaman kullan

- Her canlıya alma öncesi
- Yeni ortam kurulumunda
- Migration / büyük şema değişikliği öncesi

# İş Akışı (PREPARE → PREVIEW → MIGRATE → DEPLOY → SMOKE → MONITOR → ROLLBACK)

## 1. PREPARE — Hazırlık

- Tüm env/secret yeni ortamda tanımlı; `NEXT_PUBLIC_` olanlar kamuya açık, olmayanlar gizli.
- Dependency audit (`npm audit`).
- Typecheck, lint, test geçiyor.
- Build yerelde temiz çalışıyor (production mod).
- Yeni çevresel bağımlılık (Redis, DB, S3, ödeme sağlayıcı) provision edilmiş.

## 2. PREVIEW — Preview deploy

- PR branch preview (Vercel/Cloudflare Preview) çalışıyor.
- Playwright smoke test preview üzerinde çalıştır.
- Lighthouse temel metrikleri kontrol et.
- Tasarım/manüel QA.

## 3. MIGRATE — DB migration

- Migration önce staging'de çalıştırılmalı ve test edilmeli.
- Production migration trafiğin düşük olduğu saatte.
- Geri alma planı hazır (rollback script veya restore).
- Migration çalışırken uygulama bakım moduna alınır ya da backward-compatible olur (yeni sütun
  nullable, varsayılan değerli; eski kod yeni sütunu görmese de çalışır).
- Büyük tablo alter için concurrently / online seçenekler.

## 4. DEPLOY — Canlıya alma

- Atomic deploy (örn. Vercel tüm trafiği bir kerede yeni sürüme geçirir; kesinti olmaz).
- CDN önbelleği gerekiyorsa invalidation.
- Build artifact'ları sürüm etiketiyle saklanır; hızlı geri dönüş mümkündür.

## 5. SMOKE — Canlı sonrası duman testi

- Sağlık kontrolü (`/api/health`).
- Ana sayfa, kritik sayfalar 200 dönüyor.
- Auth (giriş), sepete ekle, örnek bir API isteği (dikkat: test verisi ile).
- Lighthouse canlıda (URL'i izinsiz tarama).
- Hata oranı, tepki süresi metrikleri.
- Konsolda kritik JS hatası yok.

## 6. MONITOR — İzleme

- Hata izleme: Sentry veya benzeri.
- Analytics: GA4, Plausible.
- Performans: Web Vitals toplama (vercel analytics/speed-insights, cloudflare observability).
- Uptime: Updown/UptimeRobot ile 5 dk'da bir kontrol.
- Log seviyeleri; 5xx sayısı ve anormal artışlar alarmı.

## 7. ROLLBACK — Geri alma

- Sorun büyükse hemen son iyi sürüme dön.
- Migration geri alınabilir değilse veriyi koru; kod önce geri alınır.
- Neden sonra analiz edilir; düzeltme ayrı PR ile.

# Güvenlik ve yaygın önlemler

- HTTPS zorunlu; HSTS.
- Güvenlik header'ları (CSP, X-Frame-Options, Referrer-Policy, Permissions-Policy).
- Admin paneller IP kısıtlı / ek auth'lı (Cloudflare Zero Access, Vercel Protection).
- Debug mod kapalı; source map herkese açık değil (kamuya açıksa dikkat).
- Secret rotasyon prosedürü.
- Dependabot / security advisories haftalık kontrol.

# Kalite Kontrol Listesi

- [ ] Env/secret eksiksiz
- [ ] Lint/typecheck/test geçiyor
- [ ] Preview deploy + smoke test geçti
- [ ] Migration planı ve rollback hazır
- [ ] Deployment atomic ve kesintisiz
- [ ] CDN ve önbellek doğru
- [ ] Güvenlik header'ları ve HTTPS
- [ ] İzleme (Sentry, analytics, uptime) kurulu
- [ ] Smoke test canlıda koştu
- [ ] İade süreci dokümante

# Yaygın Hatalar

- Migration'ı uygulamadan deploy etmek (kodu yeni şemaya göre bekleyen tablo yok → 500).
- Secret'ları yanlış ortama koymak (prod yerine test API key).
- `NEXT_PUBLIC_` ile server-side secret'ı sızdırmak.
- Preview'da gerçek veritabanını kullanmak (testler veriyi bozar).
- Cache invalidasyonunu unutmak (eski HTML/asset servis edilir).
- CDN'de debug sayfası bırakmak.
- Hata izleme kurmamak; sorun kullanıcıdan haber alınca öğrenilir.

# İlgili Skill'ler

- `security-audit`
- `performance-audit`
- `browser-testing`
