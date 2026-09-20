# Ajan Çerçeveleri Kısa Karşılaştırma

*Doğrulama: 2026-09-20*

Web projeleri geliştirirken (kod yazdırma, tarayıcı otomasyonu, belge işleme vb.) ajan çerçevesi
gerekebilir. Web projeleri için çoğu zaman doğrudan kod kütüphanesi kullanmak yerine CLI ajanları
(Claude Code, Codex, Cursor) ve onların skill/MCP ekosistemi ile çalışmak daha verimli. Özel
otomasyon (dokümantasyon üretimi, toplu veri çekme, çok adımlı test) gerektiğinde aşağıdaki
seçenekler değerlendirilir.

## Tablo

| Framework | Dil | Durum | Web için uygunluk | Not |
|---|---|---|---|---|
| **LangGraph** | Python/TS | ACTIVE | Orta | Dayanıklı yürütme (durable), insan-onayı; araştırma/otomasyon için iyi. Frontend işi için fazla ağır. |
| **Pydantic AI** | Python | ACTIVE | Orta | Tip-güvenli, Logfire gözlemi; Python script'leri ve araştırma için temiz seçenek. |
| **Microsoft Agent Framework** | .NET/Python | ACTIVE (1.x) | Düşük | Kurumsal .NET dünyası; AutoGen'in halefi. JS/TS topluluğu için geriden geliyor. |
| **AutoGen** | Python/.NET | MAINTENANCE | Düşük | Yeni projede başlangıç noktası değil; MAF'a geçiş öneriliyor. |
| **Vercel AI SDK** | TS | ACTIVE | Yüksek | Ürün içine AI chat/akıllı özellik gömmek için (web UI ile); kendi ajan otomasyonumuz için değil. |
| **Browser-use** | Python | ACTIVE | Yüksek | Web otomasyon ve tarayıcı tabanlı işler için Playwright üzerine iyi soyutlama. |

## Öneri

- **Kendi KB/ajan otomasyonumuz için:** Ağır bir çerçeveye ihtiyaç yok. Playwright MCP + tarayıcı
  + GitHub MCP + bizim KB skill/playbook'ları ile çöz.
- **Python ile otomasyon scripti (test/araştırma/döküman):** Pydantic AI veya LangGraph.
- **Ürün içine AI chat/öneri ekleme:** Vercel AI SDK.
- **Web kazıma/otomasyon:** Browser-use veya doğrudan Playwright MCP.

Kurumsal çoklu-ajan senaryoları (.NET ekibi) dışında Microsoft Agent Framework ve AutoGen'i
web işinde önermiyoruz.
