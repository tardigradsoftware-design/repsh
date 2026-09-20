# repsh — AI Web Development Knowledge Base

> Doğrulanmış teknik hafıza / karar destek katmanı. Web projelerinde çalışan AI ajanlarının
> "doğru bilgiyi, doğru anda, az token ile" çekmesi için tasarlanmış modüler bir Git reposu.

## Ne, Neden, Nasıl

**Ne:** Bu repo bir link çöplüğü ya da mega-prompt değildir. İçeriği; yürütülebilir iş akışları
(`skills/`), uçtan uca playbook'lar, doğrulanmış kaynak kayıtları (`registry/`), kanıtlanmış
kalıp ve tuzaklar ile teknoloji seçim rehberleridir.

**Neden:** AI ajanları web projelerinde tekrarlayan hatalar yapar: jenerik "AI-slop" tasarım,
tutarsız spacing/tipografi, uydurulmuş kütüphane/API bilgisi, eski sürüm kullanımı, test etmeden
"bitti" demek, güvenlik açıkları (auth, RLS, XSS, secret sızıntısı), gereksiz karmaşıklık.
Bu repo bu hataları azaltmak için var.

**Kimin için:** Öncelikle Türkiye pazarına yönelik web siteleri, e-ticaret ve dashboard/yönetim
panelleri üreten ekipler ve onlarla çalışan AI ajanları. İçerik Türkçe arayüz, yerel SEO,
ödeme/fatura/ERP entegrasyonu bağlamını gözetir.

## Klasör Yapısı

```
skills/          # Yürütülebilir iş akışları (SKILL.md) — her biri tek bir iş yapar
playbooks/       # Uçtan uca akışlar (ör. build-dashboard.md, release-checklist.md)
knowledge/       # Konu bilgisi (kısa, bölümlü, kaynaklı)
patterns/        # Kanıtlanmış uygulama kalıpları + kısa kod örnekleri
anti-patterns/   # Yaygın hatalar ve neden kötü oldukları
decisions/       # Teknoloji seçim rehberleri (Next.js vs..., Supabase vs...)
stacks/          # Önerilen hazır stack'ler
registry/        # Makine-okunur kaynak veritabanı (YAML)
evaluations/     # Test görevleri ve sonuçları
experimental/    # Henüz doğrulanmamış / AI üretimi adaylar (core'a karışmaz)
schemas/         # JSON Schema (skill, repository, source, mcp)
indexes/         # Arama/dolaşım indeksleri (ajanlar için)
scripts/         # Doğrulama, güncelleme, indeks üretme scriptleri
```

## Hızlı Başlangıç (Ajanlar için)

Herhangi bir web görevine başlamadan önce bu sırayla çalış:

1. **Görevi ayrıştır:** Hangi alanlar devrede? (ör. dashboard + auth + Supabase + Turkish UI)
2. **İndeksi oku:** `indexes/index.json` → ilgili skill ve playbook'ları belirle.
3. **Aşamalı aç:** İlk önce skill metadata, gerekirse gövdenin ilgili bölümü. Tüm repoyu yükleme.
4. **Karar ver:** `registry/` ve `decisions/`'dan kanıtlanmış çözümleri; `anti-patterns/`'dan
   tuzakları kontrol et.
5. **Tazeliği denetle:** Bir kaynağın `expires_at` tarihi geçmişse veya iş güncel sürüm bilgisi
   gerektiriyorsa, resmi dokümanı web'den yeniden doğrula.
6. **Uygula ve test et:** Plan → implement → Playwright ile gerçekten çalıştır.
7. **Gözden geçir:** `website-quality-review` ve `ai-slop-detection` skill'leri ile son kontrol.
8. **Yeni öğrenme:** İşe yarayan/yaramayan bir şey çıktıysa `experimental/` altına aday olarak
   not et; insan onayı olmadan `skills/` veya `registry/`'ye ekleme.

Ayrıntılı ajan protokolü için `AGENTS.md`'ye bak. Diğer projelerin `AGENTS.md`/`CLAUDE.md` dosyalarına
eklemek üzere hazır "nasıl kullan" bloğu `knowledge/agent-engineering/kb-usage-snippet.md` içinde.

## Güven Kuralları (Özet)

- **Uydurma yok.** Doğrulamadığın bilgi `unverified` kalır; hiçbir zaman gerçek diye sunma.
- **Tarih zorunlu.** "latest / best / current" gibi sabit iddialar yerine `verified_at`, `source`, `version`.
- **Kaynak hiyerarşisi:** Resmi doküman/resmi repo > maintainer dokümanı > paper > test edilmiş uygulama > topluluk > bireysel görüş.
- **Lisans:** Lisanssız içeriği kopyalama; dış repo README'lerini kopyalama; özet + link + lisans ver.
- **Gizlilik:** System prompt, sızdırılmış model verisi, API anahtarı, token, kişisel veri toplama ve saklama YASAK.
- **Kalite > miktar.** 40 doğrulanmış iyi kayıt, 400 yüzeysel kayıttan değerlidir.

## Katkıda Bulunma

`CONTRIBUTING.md` ve `AGENTS.md`'yi oku. Tüm değişiklikler için: doğrula → test et → kalite kapısından
geç → anlamlı commit at.

## Lisans

Bu repo içeriği MIT lisansı altındadır (`LICENSE`). `registry/`'deki üçüncü taraf kaynaklar
kendi lisanslarına sahiptir; özet ve link paylaşılırken o lisanslar korunur.

## Durum / Metadata

- **Repo oluşturulma (first curated):** 2026-09-20
- **Son audit:** —
- **Güvenlik politikası:** `SECURITY.md`
