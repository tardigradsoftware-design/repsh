# CONTRIBUTING.md

## Ön Koşul

Bu repo bir AI ajanı hafıza katmanıdır. Katkı yapmadan önce lütfen `AGENTS.md`'yi tamamıyla okuyun.
Oradaki kurallar tartışmasızdır.

## Katkı Türleri

- **Yeni skill:** `skills/<skill-adı>/SKILL.md`, `tests/` ile birlikte. Önce `experimental/skills/`
  altında başlayın; doğrulama sonrası `skills/`'ye taşınır.
- **Yeni kaynak kaydı:** `registry/*.yaml`. Zorunlu alanları doldurun; `verified_at` ve `license`
  olmadan kayıt kabul edilmez.
- **Düzeltme / güncelleme:** Eski bir kaydı güncellerken `verified_at` tarihini bugüne çekin ve
  neyin değiştiğini commit mesajında belirtin.
- **Yeni pattern/anti-pattern:** Kısa, kod örneği içeren, kaynaklı olsun.
- **Karar rehberi / stack önerisi:** Tarafsız olun; hangi bağlamda hangisini seçeceğimizi net yazın.
  Reklam dili kullanmayın.

## İş Akışı

1. Branch açın (`feat/...`, `fix/...`, `docs/...`). Bu oturumda `arena/01a0bdb2-repsh` kullanılır.
2. Değişikliği yapın.
3. Doğrulayın:
   - `scripts/validate/` altındaki ilgili kontrolleri çalıştırın (henüz yazılmadıysa manuel kontrol:
     YAML/JSON sözdizimi, frontmatter, kırık link).
   - `git diff` ile hiçbir secret / kişisel veri girmediğinizden emin olun.
4. Test edin: Skill eklediyseniz test senaryolarını gözden geçirin.
5. Anlamlı commit atın (Conventional Commits).
6. PR açın veya branch'e pushlayın.

## Yazım Kuralları

- Birincil dil Türkçe.
- Kod bloklarında kullanılan yorumlar da tercihen Türkçe.
- "En iyi", "mükemmel", "devrimsel" gibi subjektif sıfatlar kaçının; kanıt, ölçüm veya referans verin.
- "latest/current/best" yerine sürüm ve tarih verin.
- Her iddia için kaynak gösterin; kendi fikrinizse açıkça "Bence / GENERATED" olarak işaretleyin.

## Kalite Kapısı

Bir katkı kabul edilmeden önce:

- [ ] Tüm zorunlu metadata alanları dolu (verified_at, source, confidence, license vb.)
- [ ] Şema doğrulamasından geçiyor
- [ ] Kırık link yok
- [ ] Kopya/tekrar bilgi yok
- [ ] Lisanssız içerik kopyalanmamış
- [ ] Secret/kişisel veri yok
- [ ] Yeni skill için en az 2 test senaryosu var
- [ ] Türkçe/Türkiye bağlamı gerektiren yerlerde not düşülmüş

## Davranış

Saygılı, yapıcı, kanıta dayalı tartışma. Teknoloji seçimlerinde dini savaşlara girmeyin;
bağlamı, artıyı/eksiyi, ödünleşimi (trade-off) yazın, okuyucu karar versin.
