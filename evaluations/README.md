# Değerlendirme (Evaluations)

Bu klasör KB'nin ajan üretimini ne kadar iyileştirdiğini ölçmek için görevler ve sonuçlar
içerir. Amaç: "iyi görünüyor" hissi yerine sayısal/kanıtlanabilir gelişim.

## Nasıl çalışır

1. `tasks/` altında gerçekçi görev tanımları bulunur; her görev net başarı ölçütleri içerir.
2. Aynı görev KB olmadan ve KB ile (ajanın kullanım protokolünü izleyerek) iki kez çalıştırılır.
3. Sonuçlar aşağıdaki metriklerle skorlanır ve `results/` altında kaydedilir.
4. Her KB değişikliği sonrası regresyon testi olarak tekrar çalıştırılabilir.

## Metrikler (0–10 her biri, toplam 100)

| Metrik | Açıklama |
|---|---|
| **Görev tamamlama (task completion)** | Görev tamamen çalışır halde teslim mi? (0=hiç çalışmıyor; 10=tam ve doğru) |
| **Araç doğruluğu (tool accuracy)** | Seçilen kütüphane/araç doğru, güncel ve mi? Halüsinatif API kullanımı yok mu? |
| **Halüsinasyon (hallucination)** | Var olmayan fonksiyon/özellik/sürüm/iddia var mı? |
| **Talimat takibi (instruction following)** | İstenen kapsam, kısıtlar ve format tutuldu mu? |
| **Güvenlik (security)** | Auth, RLS, secret, XSS, KVKK uyumu, ödeme doğrulaması |
| **Erişilebilirlik (accessibility)** | Temel a11y kurallarına uyum (klavye, etiket, kontrast, alt metin) |
| **Performans (performance)** | Görsel/CWV hedefleri, gereksiz büyük kütüphane yok |
| **Görsel kalite (visual quality)** | AI-slop skorundan ters; tutarlılık, hiyerarşi, tipografi |
| **Token verimliliği (token efficiency)** | Aynı işi daha az token/bağlam ile yapıyor mu? (KB yokken uzun anlamsız çıktı riski) |
| **Regresyon/tekrar (regression/repetition)** | Aynı kodu tekrar yazdırıyor, aynı hataya tekrar düşüyor mu? |

Toplam 10 boyut 10'ar puan, toplam 100.

## Çalıştırma prosedürü

### Kontrollü koşu (manual)
1. Temiz bir çalışma klasörü aç (sandbox veya ayrı repo).
2. Ajanı KB olmadan görevlendir: "Aşağıdaki görevi yap." Sonucu not al.
3. Çıktıyı skorla (yukarıdaki 10 boyut; notlar ve bulgularla).
4. Aynı görevi KB ile tekrar çalıştır: `indexes/index.json` → skill/playbook/registry erişimi
   vererek; kullanım protokolünü uygula.
5. Çıktıyı skorla.
6. İki skoru karşılaştır ve `results/` altında kaydet.

### Otomatik koşu (Faz 7+ sonrası hedef)
- Playwright ile çalışan doğrulama script'leri (site açılıyor mu, form çalışıyor mu, Lighthouse skoru,
  axe violation sayısı);
- Manuel subjektif skor (görsel kalite, talimat takibi) için insan incelemesi notu.

## Dürüstlük ilkesi

- **Çalıştırılamayan test "çalıştırılmadı" olarak işaretlenir.** Uydurma skor verilemez.
- Bir görev henüz yazılmadıysa veya eksikse, atlanır, başarılı sayılmaz.
- Sonuçları başarıyla kanıtlamak için sadece "çalışıyor" demek yetmez; komut/screenshot/log eklenir.

## Sonuç dosyası formatı

`results/eval-YYYY-MM-DD-<gorev-id>.md`:

```markdown
# Değerlendirme Sonucu — <gorev-adi>

- Tarih: 2026-09-20
- Ajan: <model/versiyon>
- KB versiyonu: <commit>
- KB'li/KB'siz süre: <süre>

## Skorlar
| Boyut | KB'siz | KB'li |
|---|---|---|
| Görev tamamlama | X | Y |
| ... | ... | ... |
| Toplam | XX | YY |

## Gözlemler
- KB'siz çalıştırırken ...
- KB ile çalıştırırken ...

## Kanıtlar
- URL/screenshot/Playwright log linki
- Hata örnekleri / başarılı örnekler

## Sonuç
KB, görevde XX puanlık gelişim sağladı / sağlamadı. En çok iyileşme: ...
```

## Görev listesi (özet)
`tasks/` altındaki klasörler 1–20 arası numaralandırılmıştır; bkz. orası.
