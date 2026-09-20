---
name: research-before-code
version: 1.0.0
description: "Herhangi bir kod yazmaya baslamadan once dogru arastirma yapmak; mevcut kutuphane/pattern/MCP var mi diye bakmak, karsilastirmak, dogrulamak, sonra planlamak. Yeni kod yazdirmadan once tetiklenir."
category: workflow
status: curated
confidence: high
requires: []
tags: [research, workflow, planning, verification, decision]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

Her kod satırından önce gereksiz yeniden icat ve yanlış kütüphane seçimini önlemek. Jenerik,
uydurulmuş veya eski API bilgisiyle kod yazmaktan kaçınmak. Araştırma yapmadan kodlamaya başlamak
en pahalı hatadır.

# Ne zaman kullan

- Herhangi bir yeni özellik, yeni bileşen, yeni endpoint, yeni entegrasyon yazmadan önce
- Mevcut kodda ciddi bir değişiklik / yeniden yazma öncesi
- Kütüphane seçimi gerektiğinde (auth, chart, form, state, payment, i18n, testing...)
- "Bunu sıfırdan yazarım" düşüncesi belirdiği anda
- Özellikle AI ile çalışırken: ajan varsayılan olarak "kod yazma" moduna geçer, bu skill onu
  durdurup araştırmaya yönlendirir.

# Ne zaman kullanma

- 1–2 satırlık açık hata düzeltmeleri (typo, yanlış prop ismi vb.)
- Aynı kod tabanında zaten kanıtlanmış, defalarca kullanılmış deseni tekrar ederken
- TODO/task listende açıkça belirtilmiş, daha önce araştırılmış ve onaylanmış kararı uygularken

# Girdi

- Görev açıklaması (kullanıcı isteği / issue / özellik)
- Mevcut proje klasörü ve bağımlılıklar (`package.json`, mevcut dosya yapısı)
- Varsa takım/proje teknoloji kararı (DECISIONS, stacks/)

# İş Akışı (INPUT → PROCESS → OUTPUT → VALIDATION)

## 1. UNDERSTAND — Görevi anla

1. Kullanıcının istediği somut çıktıyı bir cümlede tekrar yaz.
2. Kabul kriterlerini listele (çalışır mı? erişilebilir mi? responsive mi? hangi tarayıcılar?).
3. Projenin mevcut stack'ini ve kısıtlarını çıkar (hangi framework, hangi sürüm, tasarım dili, DB).
4. Varsa proje `DECISIONS.md`, `AGENTS.md`, `README.md` dosyalarını oku.

## 2. SEARCH — Mevcut çözüm var mı?

Aşağıdaki sırayla ara ve not al:

1. **Bu KB içinde ara:** `indexes/index.json` → ilgili `skills/`, `patterns/`, `anti-patterns/`,
   `decisions/`, `stacks/`, `registry/`.
2. **Projede zaten uygulanmış mı?** Aynı sorunu çözen bir dosya/modül bak.
3. **Resmi doküman:** MDN, framework'ün kendi docs'u, önerilen reçete.
4. **Olgun kütüphaneler:** npmtrends, bundlephobia, GitHub stars + son commit + release durumu;
   `registry/` kaydı var mı bak; yoksa eklemek üzere not al ama doğrulamadan kullanma.
5. **MCP / AI aracı var mı?** Özellikle Playwright MCP, Supabase MCP gibi otomasyon araçları sorunu
   daha hızlı çözer mi?

**Ararken bakılacak sinyaller:**
- Son 6 ay içinde commit var mı?
- Son 3 ay içinde release var mı?
- Açık critical issue / CVE var mı?
- Lisans ticari kullanıma uygun mu?
- Bundle boyutu (bundlephobia) / tree-shake destekli mi?
- Tip desteği var mı (TypeScript)?
- Topluluk benimsemesi kaç indirme / kaç kullanıcı?

## 3. COMPARE — En az 2 seçeneği karşılaştır

"İlk bulduğum kütüphaneyi kullan" tuzağına düşme. En az 2 alternatifi şu başlıklarda karşılaştır:

- Özellik kapsamı (fazlası mı, tam mı?)
- Bundle boyutu
- API kararlılığı / sürüm durumu
- Bakım durumu (son commit, release)
- Lisans
- Dokümantasyon kalitesi
- Bu proje ile uyum (mevcut stack, tasarım sistemi)
- Topluluk büyüklüğü / issue cevap süresi
- Güvenlik geçmişi

Karşılaştırmayı kısa bir tablo veya liste olarak yaz. Tek seçenek geçerliyse nedenini belirt.

## 4. VERIFY — Bilgiyi doğrula

- Resmi dokümantasyondan en güncel sürüm notunu kontrol et.
- En küçük kod parçasıyla (10–20 satır) çalışıp çalışmadığını hemen dene (tercihen Playwright MCP
  veya Node REPL ile).
- `npm view <paket> version` ile en son sürümü ve yayın tarihini al.
- Uydurulmuş bilgi (halüsinasyon) riskine karşı: "emin değilim" diye biliyorsan `unverified` bırak,
  kullanmadan önce doğrula.
- Son commit tarihi 1 yıldan eskiyse dikkat; archived veya maintenance mi kontrol et.

## 5. PLAN — Uygulama planını yaz (kısa)

- Hangi dosyaları değiştireceksin / oluşturacaksın (en fazla 5–8 kalem);
- Hangi kütüphane/versiyonu kullanacaksın ve neden;
- Hangi testleri yazacaksın (birim + en az 1 Playwright senaryosu);
- Bilinen riskler / geri alma noktası;
- Tahmini adım sayısı (büyük işleri kır).

## 6. IMPLEMENT — Planı uygula

Plan yazmadan ve kullanıcı/insan onayı (gerekli görülürse) almadan büyük implementasyona geçme.
Küçük adımlarla: her adımda çalışan bir şey üret, aşırı büyük PR'lerden kaçın.

## 7. TEST — Gerçekten test et

- Birim test (Vitest/Jest)
- Tarayıcıda gerçekten çalışıyor mu? (Playwright MCP veya manuel)
- Edge case'ler (boş, yükleniyor, hata)
- Türkçe karakter, uzun metin, mobil görünüm
- a11y temel kontrolleri (klavye ile gezinme, kontrast)

## 8. REVIEW — Son kontrol

- `website-quality-review` skill'ini uygula.
- `ai-slop-detection` ile görsel/metinsel jenerikleşme kontrolü yap.
- Güvenlik: auth, RLS, XSS, secret sızıntısı.
- Kod kendi kendini açıklıyor mu? Gereksiz yorum/silinebilir kod var mı?

# Çıktı

- Karar notu (hangi seçenek, neden, alternatifler, sürüm)
- Uygulama planı (5–8 madde)
- Doğrulama kanıtı (çalışan en küçük örnek veya link)
- Test stratejisi

# Kalite Kontrol Listesi

- [ ] KB içi tarama yapıldı
- [ ] En az iki alternatif karşılaştırıldı
- [ ] Sürüm ve son commit bilgisi doğrulandı
- [ ] Lisans kontrol edildi
- [ ] Güvenlik notlarına bakıldı (CVE, advisories)
- [ ] En küçük çalışan örnek denendi
- [ ] Plan yazıldı
- [ ] Test metodu belirlendi
- [ ] Hiçbir bilgi uydurulmadı; `unverified` olan açıkça işaretlendi

# Yaygın Hatalar

- **Hata:** İlk Google sonucundaki blog yazısına göre kütüphane seçmek.
  **Düzeltme:** Resmi doküman + registry + bakım durumu bir arada değerlendir.
- **Hata:** Yıldız sayısına bakıp "en iyi bu" demek.
  **Düzeltme:** Yıldız + son commit + release + bundle boyutu + dokümantasyon + lisans hepsine bak.
- **Hata:** "Bunu sıfırdan yazarım, 2 saat sürer."
  **Düzeltme:** Önce "npm'de 10 yıl önce çözülmüş mü?" diye bak; zamanını iş mantığına harca.
- **Hata:** AI'nın söylediği fonksiyon/API gerçekte yok.
  **Düzeltme:** Her API ismini resmi dokümandan teyit et; küçük bir örnekle doğrula.
- **Hata:** Sürüm notlarına bakmadan eski StackOverflow cevabını kopyalamak.
  **Düzeltme:** Cevaptaki yöntemin güncel sürümde hâlâ geçerli olduğunu doğrula.

# Örnek

**Görev:** Next.js 16 + Supabase projemde bir tabloya filtre/sıralama/pagination eklemeliyim.

1. **Anla:** 20+ kolonlu müşteri listesi; sunucu tarafı pagination; çilek temalı tasarım dilimiz.
2. **KB içi bak:** `registry/tanstack-table`, `decisions/table-libraries.md` var. Projede `@tanstack/react-table` zaten var.
3. **Karşılaştır:** TanStack Table (zaten var), MUI X DataGrid (lisanslı, bizim temayla uymaz), ag-Grid (çok ağır).
4. **Doğrula:** `npm view @tanstack/react-table version` → 8.x; son release 2 hafta önce. Resmi docs'ta Server-side pagination örneğini kopyala-çalıştır.
5. **Plan:** `components/data-table/` klasörü oluştur; `useReactTable` hook'unu sar; sayfalama state'i URL'de (searchParams); loading/empty/error state'leri ekle; Playwright ile 2 test.
6. **Uygula, test et, review et.**

# Referanslar

- Bu KB: `decisions/`, `registry/repositories.yaml`, `stacks/`
- Rehber: https://xkcd.com/927/ (standartlar paradoksu — yeni standart yazmama prensibi)
- Doğrulama için resmi dokümanlar: `registry/sources.yaml`

# İlgili Skill'ler

- `code-review`
- `debugging`
- `browser-testing`
- `security-audit`
- `website-quality-review`
