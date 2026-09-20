---
name: debugging
version: 1.0.0
description: "Hatayi yeniden uretme, hipotez kurma, daraltma, bulma, kanitla duzeltme ve regresyon onleme is akisi; herhangi bir hata aninda tetiklenir."
category: testing
status: curated
confidence: high
requires: [research-before-code, browser-testing]
tags: [debugging, troubleshooting, investigation, root-cause]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

Hataları gelişigüzel "dene-yanıl" ile değil; sistematik, bilimsel metotla bulmak ve bir daha olmamasını sağlamak.

# İş Akışı (REPRODUCE → READ → HYPOTHESIZE → ISOLATE → FIX → TEST → PREVENT)

## 1. REPRODUCE — Yeniden üret

- Hatanın tam koşullarını yaz: URL, kullanıcı, veri, tarayıcı, zaman, konsol hatası.
- Tutarlı yeniden üretim adımları. Bazı hatalar sadece production'da veya spesifik veri ile oluşur.
- Mümkünse en küçük tekrar üretim senaryosu (minimal repro).

## 2. READ — Kanıt topla

- Browser console: JS hataları, uyarılar, network hataları.
- Network tab: 4xx/5xx, yanlış body, çok yavaş istekler, CORS.
- Server log: stack trace, SQL sorgu süresi, hangi path hata vermiş.
- React DevTools: gereksiz render, state/props akışı.
- Son değişiklik: `git log -p`, en son deploy.

## 3. HYPOTHESIZE — Hipotez kur

"Hatanın nedeni X olabilir" cümlesini kur. Tek seferde tek hipotez test et; rastgele değiştirme.

## 4. ISOLATE — Daralt

- Hangi dosya/modülde? Hangi fonksiyon?
- Geçici log veya debugger ile kes noktası.
- Şüpheli kodu yorum yaparak kaldır veya minimal versiyonda test et.
- Veriden mi kaynaklanıyor? (bozuk veri, null alan, lokalizasyon)
- Ortam mı? (prod vs dev, tarayıcı, timezone, locale)

## 5. FIX — Kök nedeni düzelt

Semptomu değil kök nedeni düzelt:
- Null check ile etrafı sarmalamak yerine neden null geliyor? Onu düzelt.
- `setTimeout` ile düzeltmek yerine race condition'ın nedeni.
- `try/catch` ile hatayı yutmak yerine hata durumunu ele al.

Değişikliği küçük ve odaklı yap; commit mesajında kök nedeni yaz.

## 6. TEST — Doğrula ve regresyon koru

- Hata düzeldi mi? Manuel test veya Playwright testi ile.
- Düzeltmenin başka bir şeyi kırmadığını görmek için ilgili diğer testleri çalıştır.
- Hatanın bir daha olmaması için regression test ekle (birebir aynı senaryo).

## 7. PREVENT — Ders çıkar

- Aynı tür hata başka yerde de var mı? Kod tabanında tara.
- TypeScript/lint kuralı ile önlenebilir mi? O kuralı ekle.
- Test ile korunuyor mu? E2E veya birim testi yaz.
- Dokümante et; gerekirse pattern/anti-pattern ekle.

# Kalite Kontrol Listesi

- [ ] Hata yeniden üretilebilir
- [ ] Konsol/network/log kanıtları toplandı
- [ ] Tek hipotez üzerinde çalışıldı
- [ ] Kök neden semptom değil düzeltildi
- [ ] E2E/birim test eklendi
- [ ] Kod tabanında benzer hatalar tarandı
- [ ] Commit mesajı kök nedeni açıklıyor

# Yaygın Hatalar

- "Çalışıyor burada" → fark (env, veri, kullanıcı, tarayıcı) üzerine düşünmemek.
- Semptomu düzelten band-aid (boş check, try/catch gizleme).
- Aynı dosyada 10 şeyi birden değiştirip hangisinin düzelttiğini bilmemek.
- Hata için test yazmamak (ileride tekrar).
- Stack trace'i okumadan ilk sıradaki hataya odaklanmak (asıl hata çoğu zaman ilk sebep).

# İlgili Skill'ler

- `research-before-code`
- `browser-testing`
- `code-review`
