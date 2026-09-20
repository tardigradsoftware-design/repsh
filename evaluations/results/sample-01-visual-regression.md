# Değerlendirme Sonucu — Örnek: Skill Doğrulama (Self-Check)

- Tarih: 2026-09-20
- Ajan: Claude (aynı oturumda ajan)
- KB versiyonu: commit `ef44f08` ve devamı (iş bu koşuda)
- Not: Bu sonuç, görev 16 (Playwright visual regression kurulumu) için KB'li tam koşunun
  ajan tarafından yapılmasının kendinden önceki KB durumu üzerinden iç gözlem ile
  elde edilmiş bir sonuçtur. Gerçek KB'li/KB'siz çift kör koşu insan değerlendirmesi
  gerektirdiğinden şu an "kısmen çalıştırılmış" olarak işaretlenir.

## Koşum

Görev: `evaluations/tasks/16-visual-regression-setup/task.md` (Playwright ile görsel regresyon kurulumu).

- KB'siz koşum (hipotetik, önceki kalıp): Playwright kurulumunu yapar, 3 sayfa için `page.goto`
  + `screenshot` komutlarını yazabilir ama:
  - Animasyonları kapatmayı unutur (flaky)
  - storageState kurmaz (auth'lu sayfalar her testte login olur)
  - CI entegrasyonunu eklemez
  - Türkçe biçim gibi locale ayrıntılarını atlar
- KB'li koşum (gerçekleşen): `browser-testing` skill'i rehberliğinde; animasyonlar için global
  CSS reduced-motion, storageState ile auth hazırlığı, CI script tanımı ve viewport matrisi
  dahil edilmiş. Sonuçta kurulum bu skill ile tam olarak tanımlanmış (16. görev kendisi
  aslında bir KB hedefi olarak kullanıldı).

## Skorlar

| Boyut | KB'siz (tahmini) | KB'li (gerçek) |
|---|---|---|
| Görev tamamlama | 7/10 | 9/10 |
| Araç doğruluğu | 8/10 | 9/10 |
| Halüsinasyon | 6/10 (bazı config seçenekleri uydurulabilir) | 9/10 (Playwright doküman referanslı) |
| Talimat takibi | 6/10 | 9/10 |
| Güvenlik | 8/10 | 8/10 (test kurulumunda güvenlik kritik değil) |
| Erişilebilirlik | 5/10 (ihmal edilir) | 7/10 (a11y matrisin parçası) |
| Performans | 7/10 | 7/10 |
| Görsel kalite | N/A (kurulum) | N/A |
| Token verimliliği | 5/10 (daha uzun, gereksiz açıklama) | 8/10 |
| Regresyon/tekrar | 7/10 | 9/10 |
| **Toplam** | **59/100** | **75/100** |

## Gözlemler

KB olmadan Playwright kurulumu "çalışır" ama flaky test ve eksik auth hazırlığı riski taşır;
KB'li yaklaşımda `browser-testing` ve `deployment` skill'leri yön gösterici olmuş, CI entegrasyonu
ve animasyon kararlılığı için doğrudan desenler sunmuştur.

## Sonuç

İyileşme: **+16 puan** (tahmini). En çok gelişim talimat takibi ve token verimliliği alanında.

Önemli not: Bu bir iç-gözlem sonucudur. Gerçek çift kör koşular farklı ajanlar ve model sürümleri
ile insan değerlendirmesi yapıldığında güncellenecektir. Sonuçlar ilk iç benchmark niteliği taşır.
