# SECURITY.md

## Güvenlik Politikası

Bu repo, AI ajanlarının web projeleri için başvurduğu bir bilgi tabanıdır. İçerdiği yanlış veya
kötü niyetli bilgi doğrudan üretim sistemlerine yansıyabilir. Bu nedenle güvenlik ciddiye alınır.

## Raporlama

Bir güvenlik açığı, yanlış bilgi, gizli veri sızıntısı veya zararlı içerik bulursanız:

1. **Herkese açık issue açmayın** (güvenlik açığıysa).
2. Düzeltici katkıda bulunabiliyorsanız PR açın; açıklama kısmında güvenlik etkisini özetleyin.
3. Kritik (secret sızıntısı, aktif olarak zararlı kod örneği, yanlış auth rehberi) durumlarda
   commit'i revert edin veya dosyayı hemen kaldırın, sonra açıklama yazın.

## Bu Repoda Bulunmaması Gerekenler

- API anahtarı, token, secret, `.env` içeriği
- Gerçek kullanıcı/kurum kişisel verisi
- Açıkça zararlı kod örnekleri (XSS/CSRF/SQLi açıklarını kasıtlı olarak öğretmek, fidye yazılımı vb.
  — **ancak** eğitim amaçlı "şu kod neden güvenli değil, nasıl düzeltilir" örnekleri `anti-patterns/`
  altında kabul edilir; açıkça "ZARARLI ÖRNEK — EĞİTİM AMAÇLI" etiketiyle)
- Lisanssız üçüncü taraf içerik kopyaları
- Sızdırılmış model sistem promptları veya dahili şirket dokümanları

## MCP ve Ajan Güvenliği

Model Context Protocol (MCP) sunucuları ve ajan araçları yüksek yetkilerle çalışabilir. Bu repo:

- Her MCP kaydı için izin ve risk değerlendirmesi yapmak zorundadır (`registry/mcp-servers.yaml`).
- `knowledge/agent-engineering/mcp-security.md` altında ajan güvenliği rehberi sağlar.
- Prompt injection, araç zehirlemesi, veri sızdırma ve yetkisiz kod çalıştırma yüzeylerini
  açıkça belgelemekle yükümlüdür.

## Dependency Güvenliği

Bu repo minimal bağımlılıkla çalışır (validation script'leri için temel Python/Node paketleri).
CI'da düzenli olarak güvenlik taraması yapılması hedeflenir.

## Sorumluluk Reddi

Bu repo bir bilgi kaynağıdır. Buradaki her bir bilgi kendi doğrulamanızdan geçmelidir. Üretim
sistemine koymadan önce her zaman: güncel sürüm dokümanını okuyun, kendi testlerinizi yapın,
güvenlik denetiminden geçirin.
