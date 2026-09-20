# Görev 03: SaaS Veritabanı Tasarımı
## Açıklama
Çoklu kiracılı (multi-tenant) proje yönetim SaaS'ı için Postgres veritabanı şeması tasarla:
workspace, user, workspace_member, project, task, comment.
## Başarı
- Tablo/kolon isimlendirme snake_case
- Her tabloda id/created_at/updated_at
- FK + indeksler doğru
- `workspace_id` üzerinden RLS policy (kullanıcı sadece kendi workspace verisini görür)
- Para varsa numeric; zaman timestamptz; enum veya lookup tablo durumlar için
- Migration idempotent ve geri döndürülebilir
- En az 3 yaygın sorgu için indeks tanımlı
- 5+ yaygın N+1 veya security riski yok
