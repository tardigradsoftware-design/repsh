---
name: code-review
version: 1.0.0
description: "Kod inceleme: guvenlik, okunabilirlik, tutarlilik, tip guvenligi, hata yonetimi, test ve mimari acidan PR inceleme."
category: quality
status: curated
confidence: high
requires: [security-audit]
tags: [code-review, pr, quality, consistency]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

PR'ların ana hatlarıyla güvenli, okunabilir, bakımı kolay, tutarlı ve testli olmasını sağlamak.
Kod yazanı suçlamak değil riski azaltmak ve kaliteyi yükseltmek.

# Ne zaman kullan

- Her PR merge öncesi
- Özellikle büyük özellikler, güvenlik hassas alanlar (auth, ödeme, veri)
- Ajan tarafından üretilmiş büyük değişikliklerde

# İnceleme Kontrol Listesi

## Doğruluk / İşlevsellik

- Kod ne yapıyor? PR açıklaması ile kod uyuşuyor mu?
- Edge case'ler düşünülmüş mü (boş, null, uzun metin, büyük sayı, yetkisiz kullanıcı)?
- Hata durumları ele alınmış mı; kullanıcıya anlamlı mesaj veriliyor mu?
- Senkron/asenkron doğru kullanılmış mı; race condition var mı?
- Tip güvenliği (TypeScript katı mod, any kaçınılmış)?

## Güvenlik

- `security-audit` checklist'inin ilgili bölümleri.
- Kullanıcı girdisi doğrulanıyor; XSS/CSRF/SQLi/IDOR yok.
- Yetki kontrolü server-side.
- Secret/commit sızıntısı yok.
- Webhook imzaları doğrulanıyor.
- Hassas veriler log'larda görünmüyor.

## Mimari ve tutarlılık

- Proje'nin mevcut klasör yapısı ve naming convention'ına uyulmuş mu?
- Tekrarlanan kod çıkarılmalı mı; ortak util/component'e çekilmeli mi?
- Gereksiz bağımlılık eklenmiş mi?
- Client/Server ayrımı doğru (server-only / use-client); RSC ihlali yok.
- Veri akışı tutarlı (React Query / Server Action / RSC seçimi doğru).

## Okunabilirlik

- Değişken/fonksiyon adları anlamlı.
- Fonksiyonlar kısa ve tek iş yapıyor (büyük fonksiyonlar kırılmalı).
- Yorumlar "neden"i açıklıyor, "ne"yi değil.
- Ölü kod (comment-out, kullanılmayan import/değişken) kaldırılmış.
- Console.log, debug print kaldırılmış.

## Test

- Yeni davranış için birim/E2E test eklenmiş.
- Test gerçek davranışı doğruluyor; önemsiz detaya odaklanmıyor.
- Hata/boş durumlar test edilmiş.

## Performans

- Gereksiz büyük import yok.
- N+1 sorgu veya büyük re-render potansiyeli var mı?
- Resim/veri lazy gerekiyorsa lazy.

## Tasarım ve erişilebilirlik

- Tasarım sistemi token'ları kullanılmış; doğrudan hardcode renk/yazı tipi yok.
- Temel a11y (etiket, klavye, kontrast) düşünülmüş.
- Responsive görünüm.

## Davranış

- Yapıcı ol; soru sor, alternatif öner; "bunu niye böyle yaptın?" yerine "bu X yaklaşımı daha mı uygun olur, neden?"
- Büyük PR'ları daha küçük parçalara bölmeyi öner.
- Sen de hata yapabileceğini unutma; kesin konuşmadan önce kendin doğrula.

# İnceleme sonrası

- Tüm yorumlar açıkça cevaplanmış ya da düzeltilmiş olmalı.
- CI geçiyor olmalı (testler, lint, type-check).
- Onay sonrası squash-merge veya temiz geçmişle birleştir.
- Öğrenilen bir şey varsa KB'ye not ekle (experimental/).

# Yaygın Hatalar (incelemecinin)

- Sadece stil/format yorumu yapıp işlevsel/güvenlik sorununu kaçırmak.
- Nit'leri engellemek (gerçek sorunlar ile keyfi tercihleri ayır).
- Çok büyük PR'ları tam okumadan onaylamak.
- Mimari tutarsızlıkları "sonra düzeltiriz" diye ertelemek (biriken teknik borç).

# İlgili Skill'ler

- `security-audit`
- `research-before-code`
- `browser-testing`
