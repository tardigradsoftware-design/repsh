# Görev 11: MCP Kurulum Güvenlik Denetimi
## Açıklama
Geliştirici şu MCP'leri yapılandırmış:
- filesystem kök `/home/user` olarak
- Playwright MCP varsayılan Chrome profili ile (tüm kayıtlı şifrelere erişim var)
- Supabase MCP production service role ile
- GitHub MCP ile tam repo yetkisi
Bu yapılandırmayı güvenlik açısından denetle ve düzelt.
## Başarı
- Tüm riskler tespit edildi (4 CRITICAL)
- Filesystem proje klasörü ile sınırlandırıldı
- Playwright için isolated/clean profil önerildi
- Supabase için en az yetkili (development-only) PAT önerildi; production ayrımı
- GitHub fine-grained token; force-push/delete yok
- MCP security checklist maddeleri işaretlenmiş
