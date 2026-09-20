# KB Kullanım Bloğu (diğer projelerin AGENTS.md / CLAUDE.md dosyalarına yapıştırmak için)

Aşağıdaki blok, repsh KB'sini kullanacak her projeye kopyalanmak üzere tasarlanmıştır:

```markdown
## repsh Bilgi Tabanı Protokolü

Bu projede çalışırken şu KB'ye başvur: ../repsh/ (veya ayarlanmış KB_PATH)

Her göreve başlamadan önce şu sırayı izle:

1. Görevi ayrıştır: web sitesi / dashboard / e-ticaret? Hangi alanlar var? (auth, DB, UI, SEO, güvenlik...)
2. `repsh/indexes/index.json` → ilgili skill ve playbook'ları bul.
3. İlk önce skill metadata (frontmatter) oku. Gerekirse sadece ilgili bölümü aç. Tüm KB'yi belleğe yükleme.
4. `repsh/registry/` ve `repsh/decisions/`'dan kanıtlanmış çözümleri; `repsh/anti-patterns/`'dan tuzakları kontrol et.
5. Bir kaynağın `expires_at` tarihi geçmişse veya iş güncel sürüm/API bilgisi gerektiriyorsa,
   resmi dokümanı web'den (web_search/fetch_page) yeniden doğrula. Asla varsayım yapma.
6. Plan → uygula → Playwright ile gerçekten test et.
7. Bitirirken `website-quality-review` ve `ai-slop-detection` skill'lerini uygula.
8. Yeni bir şey öğrenirsen veya bir kaynağın eskidiğini görürsen, KB'nin `experimental/` altına
   aday olarak not et; doğrudan KB core'una ekleme veya düzenleme yapma (ayrı bir gözden geçirmeyle yapılır).

Güven kuralları: uydurma yok, tarih/sürüm ver, lisanslı içeriğe saygı göster, secret/kişisel veri sızdırma.
```
