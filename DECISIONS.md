# DECISIONS.md — Mimari Kararlar ve Varsayımlar (ADR formatı)

Her karar kısa tutulur: bağlam, karar, gerekçe, sonuçlar, alternatifler, tarih.

---

## D-001 — Repo içerik dili Türkçe olacak

- **Tarih:** 2026-09-20
- **Bağlam:** Kullanıcı Türkçe arayüzlü, Türkiye pazarına yönelik projeler geliştiriyor.
- **Karar:** Birincil dokümantasyon dili Türkçe. Kod, komut, kütüphane adları ve teknik terimler
  doğal hallerinde bırakılır.
- **Gerekçe:** Ajanların kullanımında ana dili düşünmek hata oranını azaltır; yerel SEO, ödeme
  sistemleri ve yasal yükümlülük (KVKK, fatura, e-arşiv) notları Türkçe daha doğru aktarılır.
- **Sonuçlar:** Uluslararası topluluk katkısı sınırlı olabilir; kabul edilir.

## D-002 — Birincil hedef: web (sites, e-ticaret, dashboard)

- **Tarih:** 2026-09-20
- **Karar:** Repo, web projelerinde AI ajanı üretkenliğini ve kalitesini artırmak için optimize
  edilir. Genel AI araştırması, akademik LLM makaleleri, mobil native, oyun, veri bilimi, gömülü
  sistem ikincil önceliktir.
- **Gerekçe:** Kullanıcının ana iş kolu web; kalite > miktar.

## D-003 — Bilgi birimleri arasındaki ayrım: skill vs knowledge vs pattern vs decision

- **Tarih:** 2026-09-20
- **Karar:**
  - `skills/` = YÜRÜTÜLEBİLİR iş akışı. Adım adım, girdi/çıktı/doğrulama adımı olan, bir ajan
    tarafından takip edildiğinde somut sonuç üreten reçete.
  - `knowledge/` = BİLGİ. Kavramlar, açıklamalar, referans tabloları. İş akışı değil.
  - `patterns/` = KANITLANMIŞ KOD ÖRNEĞİ. Belli bir problemi çözen, tekrar kullanılabilir, kısa kod.
  - `anti-patterns/` = TUZAKLAR. Neden kötü, nasıl fark edilir, nasıl düzeltilir.
  - `decisions/` = SEÇİM REHBERİ. "X vs Y" karşılaştırması, hangi bağlamda hangisi seçilir.
  - `playbooks/` = UÇTAN UCA SENARYO. Birden fazla skill/pattern'ı bir sıraya dizen bütün akış.
- **Gerekçe:** Aynı bilgiyi birden fazla yerde tutmamak, ajanların doğru türde dosya çekmesini
  sağlamak.

## D-004 — Skill formatı Anthropic Agent Skills şablonuna uyumlu

- **Tarih:** 2026-09-20
- **Karar:** SKILL.md frontmatter'ı Anthropic Agent Skills spesifikasyonunu (name, description)
  temel alır; üzerine durum, güven, kategori, gereksinim, test, güncelleme tarihi gibi alanlar
  eklenir.
- **Gerekçe:** Var olan, olgun bir standardı yeniden icat etmemek; Claude Code / Claude API ile
  doğal uyum; topluluk araçlarıyla (skills.sh, plugin marketplace) potansiyel uyumluluk.
- **Kaynak:** https://github.com/anthropics/skills , https://agentskills.io
- **Alternatif:** Kendi özel formatımızı icat etmek. Reddedildi: ekosistem uyumu kaybı.

## D-005 — Her kaydın bir "son kullanma tarihi" (`expires_at`) olacak

- **Tarih:** 2026-09-20
- **Karar:** Bilginin türüne göre tazelik politikası:
  - Model/araç bilgisi (fiyat, özellik, sürüm): 7–30 gün
  - Framework/kütüphane sürüm bilgisi: 30–90 gün
  - Güvenlik açığı notları: 30 gün (kritikse 7 gün)
  - Araştırma makaleleri / benchmark'lar: 180–365 gün
  - Standartlar (WCAG, OWASP, HTTP, ECMAScript): 365+ gün
  - Genel prensip / mimari dersler: süresiz (yine de yıllık gözden geçir)
- **Gerekçe:** Eski bilgi en yaygın hata kaynağı; otomatik kontrollerin `expires_at`'i geçmiş
  kayıtları işaretlemesi hedeflenir.

## D-006 — Registry YAML, içerik Markdown

- **Tarih:** 2026-09-20
- **Karar:** `registry/*.yaml` makine-okunur veri (YAML 1.2, JSON Schema ile doğrulanır). İnsan
  tarafından okunan rehberler, skill'ler, pattern'ler Markdown.
- **Gerekçe:** YAML insan tarafından da kolay okunur/düzenlenir, JSON'a kolay çevrilir; Markdown
  zaten AI ajanlarının en iyi sindirdiği format.

## D-007 — Dış repo README'lerini kopyalamıyoruz

- **Tarih:** 2026-09-20
- **Karar:** Bir üçüncü taraf repo için kayıt eklerken README'yi değil, özlü bir özet, bize neden
  faydalı olduğu, ne zaman ve ne zaman kullanılmayacağı, sınırlar, lisans ve URL eklenir.
- **Gerekçe:** Telif/lisans riski; repo'nun amacı özet ve bağlam sağlamak, arşivlemek değil.

## D-008 — experimental/ ve core/ ayrımı sert olacak

- **Tarih:** 2026-09-20
- **Karar:** AI tarafından üretilmiş veya henüz doğrulanmamış içerik doğrudan `skills/` veya
  `registry/`'ye giremez. Önce `experimental/` altında başlar, insan incelemesi + test + kanıt
  sonrası core'a taşınır.
- **Gerekçe:** Güvenilirlik. Core'a giren her bilginin izi sürülebilir, doğrulanabilir olmalı.

## D-009 — License: MIT (içerik), üçüncü taraf referansları ayrı tutulur

- **Tarih:** 2026-09-20
- **Karar:** Bu repodaki özgün içerik (skills, docs, patterns, scripts) MIT lisansı altında
  yayımlanır. `registry/`'deki üçüncü taraf projeler kendi lisansları altında kalır; burada
  yalnızca özet ve link paylaşılır.
- **Gerekçe:** MIT geniş izin verir, ticari kullanıma uygundur, ajanın farklı projelerde
  kullanımını kolaylaştırır.

## D-010 — Commit dili ve mesaj standardı

- **Tarih:** 2026-09-20
- **Karar:** Conventional Commits formatı (`feat:`, `docs:`, `chore:`, `fix:`, `refactor:`,
  `test:`). Commit mesajı kısa ve açıklayıcı. Faz geçişlerinde anlamlı tek commit.
- **Gerekçe:** Geçmişin okunabilirliği, gelecekte CHANGELOG otomasyonuna imkân.

## D-011 — Secret / kişisel veri taraması zorunlu

- **Tarih:** 2026-09-20
- **Karar:** Her commit öncesi (ve CI'da) secret taraması çalıştır. `.env`, API key, token, özel
  anahtar, kişisel veri commit'lenemez.
- **Gerekçe:** Bu repo birden fazla projede ajan hafızası olarak kullanılacak; sızıntı etkisi
  yüksek olur.

## D-012 — Türkçe web özelinde yerleşik notlar

- **Tarih:** 2026-09-20
- **Karar:** İlgili yerlerde (seo-audit, ecommerce, design-system, dashboard-ui) Türkçe'ye özgü
  notlar bulunur: Latin-5 karakterler, ı/i/İ/ş/ğ/ö/ü uyumu, tarih/saat biçimi (DD.MM.YYYY, 24 saat),
  para birimi (₺, bin ayracı nokta, ondalık virgül — dikkat: frontend'de sayı formatı Türkiye'de
  1.234,56 TL), fatura/e-arşiv/e-fatura, KVKK, KEP, adres yapısı, TR saat dilimi (Europe/Istanbul,
  yaz-kış saati uygulaması 2016'dan beri yok, GMT+3 sabit), yerel ödeme (iyzico, PayTR, Shipy),
  kargo firmaları.
- **Gerekçe:** Türkiye pazarına özel yaygın tuzaklar; jenerik uluslararası rehberler kaçırıyor.

## D-013 — Skill'lerde test senaryosu zorunlu

- **Tarih:** 2026-09-20
- **Karar:** Her skill'in `tests/` klasörü altında en az 2 test senaryosu bulunur: örnek girdi ve
  beklenen davranış/çıktı açıklaması. Testler başlangıçta doküman düzeyinde (doğal dil) olacak;
  otomasyon Faz 7+'da gelir.
- **Gerekçe:** Test edilmemiş skill'in güvenilirliği düşüktür; ajanların skill'i uyguladıktan
  sonra doğru çıktıyı tanıyabilmesi için referans gerekir.

## D-014 — MCP sunucuları için güvenlik değerlendirmesi zorunlu

- **Tarih:** 2026-09-20
- **Karar:** Her MCP kaydı için `permissions`, `network_access`, `credential_access`,
  `code_execution`, `security_risk`, `local_or_remote`, `setup_complexity` alanları doldurulur.
  Ayrıntılı rehber `knowledge/agent-engineering/mcp-security.md`'de yer alır.
- **Gerekçe:** MCP'ler güçlü ama yüksek yetkiyle çalışır; yanlış izinler prompt injection ve
  veri sızıntısı yüzeyi yaratır.
