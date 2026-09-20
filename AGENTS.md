# AGENTS.md — Bu Repo Üzerinde Çalışan Ajanlar İçin Kurallar

Bu repo bir "hafıza katmanı" olarak çalışmak üzere tasarlanmıştır. Burayı bir uçuş kulesi gibi
düşün: her gelen uçak (web görevi) için doğru koridoru, doğru prosedürü, doğru veriyi sağlar.
Kulenin kendisi hatalıysa bütün uçuşlar risk altında olur. O yüzden bu dosyadaki kurallar tartışmasızdır.

---

## 1. TEMEL İLKE — UYDURMA YOK

- Bir bilgiyi (yıldız, lisans, son commit, sürüm, fiyat, model özelliği, API imzası) canlı kaynaktan
  doğrulamadıysan yazma. Alana `unverified` yaz veya açıkça "GENERATED" etiketiyle kendi çıkarımın
  olduğunu belirt.
- Kendi varsayımın/tahminin her zaman `confidence: low|unverified` ve `evidence_level: OPINION|HYPOTHESIS`
  alır; doğrulanmış bir olgu yanında aynı ağırlıkta gösterilemez.
- "best", "en popüler", "en yeni", "stable", "production-ready" gibi nitelendirmeler; tarih, sayı veya
  referans olmadan kullanılamaz.
- Emin değilsen: `unverified` yaz, devam et. Uydurarak repo'yu kirletmektense boş bırak daha iyi.

## 2. KAYNAK STANDARDI

Her birim (skill, registry kaydı, pattern, decision) şu zorunlu alanları taşır:

- `verified_at: YYYY-MM-DD` (bugün değilse bilgi eskimeli)
- `source:` (en az bir URL veya "GENERATED")
- `version:` framework/araç kayıtlarında zorunlu
- `confidence:` `very-high | high | medium | low | unverified | conflicting`
- `evidence_level:` `FACT | RECOMMENDATION | EXPERIMENT | OPINION | HYPOTHESIS | UNKNOWN`
- `license:` dış kayıtlar için zorunlu

Kaynaklar çelişiyorsa bunu `CONFLICTING` işaretiyle açıkla:

> **CONFLICTING** — Kaynak A şunu diyor: ... / Kaynak B şunu diyor: ... / Farkın olası nedeni: ... /
> Şu anki öneri: ... (gerekçe).

## 3. KAYNAK HİYERARŞİSİ

Bilgi önceliği (yukarıdan aşağı):

1. Resmi dokümantasyon ve resmi repo (ör. nextjs.org/docs, github.com/vercel/next.js)
2. Maintainer tarafından yazılan doküman / blog
3. Hakemli makale / resmi benchmark (OWASP, W3C, web.dev, MDN)
4. Test edilmiş, üretimde kullanıldığı kanıtlanabilir uygulama
5. Tanınmış topluluk yazıları (Smashing Magazine, CSS Tricks, A11y Project gibi)
6. Bireysel blog yazarı görüşü

Alt seviyedeki bir kaynak, üst seviyedekiyle çelişiyorsa üst olanı esas al; çelişkiyi not et.

## 4. ARŞİV / BAKIM DURUMU

GitHub repo kayıtlarında:

- `archived: true` veya son commit 12+ ay önce → `status: ARCHIVED` (eğer gerçekten kullanım dışıysa)
  veya `MAINTENANCE` (arada bir güvenlik yaması geliyorsa ama aktif özellik geliştirme yoksa).
- Son 6 ay içinde commit, son 3 ay içinde release, canlı issue yanıtları → `ACTIVE`.
- Sürüm 1.0+'dır, kırıcı değişiklik yok, sadece hata düzeltmesi → `STABLE`.
- Deneysel, hızlı değişiyor, production kullanımı için erken → `EXPERIMENTAL`.
- Sahipsiz, PR'lar birikmiş, issue'lar cevapsız → `ABANDONED`.

"aktif" diye yazıp geçmek YASAK. Neden aktif olduğunu metadata'da göster (son commit, release).

## 5. LİSANS

- Lisansı olmayan içeriği (`LICENSE` dosyası yok, `package.json`'da `license` alanı yok) **kopyalama**,
  yalnızca özetle ve link ver.
- README'leri birebir kopyalama. Kendi cümlelerinle özetle: ne yapar, neden bize yararlı, ne zaman
  kullanırız, ne zaman kullanmayız, sınırları.
- Copyleft lisanslar (GPL, AGPL) için özel not ekle: kendi kodumuzu bulaştırma riski.
- MIT / Apache-2.0 / BSD: genellikle güvenlidir; yine de lisans alanını doldur.
- Bu repodaki özgün içerik MIT lisanslıdır.

## 6. GİZLİLİK VE ETİK

ASLA toplama, kaydetme, commit'leme veya dağıtma:

- API anahtarı, token, secret, `.env` içeriği
- Kişisel veri (gerçek kullanıcı bilgileri, e-posta listeleri vb.)
- Sızdırılmış model içi akıl yürütme / sistem prompt
- Çalıntı veri setleri
- Başka bir sistemin dahili dokümantasyonunu kamuya açmak

Model akıl yürütme konusunda yalnızca kamusal araştırma, açık model dokümanı, yayımlanmış yöntem
ve benchmark'lar (örn. Anthropic engineering blog, OpenAI cookbooks, arXiv preprint'ler) referans al.

## 7. DOSYA BOYUTU VE MODÜLARLİK

- Hiçbir dosya tek başına mega-prompt'a dönüşmemeli. Yumuşak sınır: 400 satır.
- Bir dosya tek bir iş yapmalı. İlgili olduğu yerden link almalı ve link vermeli.
- Aynı bilgiyi iki yerde tekrar etme ("single source of truth").
- Skill dosyaları gerçek iş akışı (adım adım, INPUT→PROCESS→OUTPUT→VALIDATION) olmalı;
  "iyi tasarla" tarzı genel tavsiye listeleri geçersizdir.

## 8. EKLEME / GÜNCELLEME İŞ AKIŞI

Yeni bir kayıt eklerken:

1. Kaynak URL'yi aç, gerçekten var mı, archived mi bak.
2. Son commit/release ne zaman? Durumunu (ACTIVE/MAINTENANCE/ARCHIVED/...) belirle.
3. Lisansı ne?
4. Maintainer kim, resmi mi?
5. Dokümantasyon ve örnekler çalışıyor mu? (mümkünse bir kısa komut/kod ile doğrula)
6. Bilinen güvenlik sorunu var mı? (Security advisories, CVE)
7. Başka bağımsız kaynaklar destekliyor mu?
8. İddia ettiğini gerçekten yapıyor mu?

Bunları geçerse kayıt `curated` olur; aksi halde `experimental/` altında başlar.

## 9. KALİTE KAPISI (Quality Gate)

Bir değişiklik `main`'e girmeden önce şunlar sağlanmalı:

- [ ] Şemaya uygunluk (frontmatter alanları tam, YAML/JSON geçerli)
- [ ] Gerekli tüm metadata alanları dolu (verified_at, source, license, confidence)
- [ ] Kırık link yok
- [ ] Referans verilen dosya mevcut
- [ ] Kopya/tekrar yok
- [ ] Hiçbir secret, token, kişisel veri commit'lenmemiş
- [ ] Skill'ler için en az 2 test senaryosu (`tests/` altında)
- [ ] Türkçe/Türkiye bağlamı gerektiren yerlerde bu not düşülmüş

## 10. PROGRESSIVE DISCLOSURE (Ajan Bağlam Verimliliği)

Ajan tüm repoyu bir kerede belleğe YÜKLEMEMELİ. Şu sırayı izle:

1. `indexes/index.json` (en küçük, ~10 KB)
2. İlgili birimin metadata/frontmatter'ı
3. İlgili bölüm (ör. sadece "Workflow" veya "Checklist")
4. Tam dosya (ancak gerekirse)
5. Referanslar ve registry detayları (ancak gerçekten ihtiyaç varsa)

Büyük belgeleri özetle, tam metni yükleme.

## 11. ÖĞRENME VE GERİ BİLDİRİM

- Yeni bir şey öğrenirsen (işe yarayan pattern, karşılaşılan tuzak, eskimiş kaynak), önce
  `experimental/` altına **aday** olarak yaz.
- İnsan incelemesi + test + kanıt sonrası `skills/` veya `registry/`'ye taşınır.
- Düzmece sonucu ("benchmark yendi", "en iyi yöntem") kanıtsız yazılamaz.

## 12. DİL

- Birincil içerik dili: Türkçe.
- Kod, terim, komut ve İngilizce jargon doğal haliyle bırakılır.
- Kaynak isimleri ve kütüphane adları çevrilmez (Next.js, shadcn/ui, Supabase...).
- Türkçe arayüz/yerelleştirme ile ilgili notlar özellikle belirtilir.

## 13. BU DOSYA DEĞİŞİR Mİ?

Bu dosya niyet beyanıdır. Küçük iyileştirmeler yapılabilir ama temel ilkeler (uydurma yok,
kaynak doğrula, lisansa saygı, gizlilik, kalite > miktar) tartışılamaz ve değiştirilemez.
Değişiklik önerisi `DECISIONS.md`'de ADR olarak kayda geçer.
