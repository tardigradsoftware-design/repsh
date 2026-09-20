---
name: database-design
version: 1.0.0
description: "Veri modeli ve iliskisel veritabani tasarimi: tablo, iliski, indeks, RLS, migrasyon, soft delete, audit trail, veri dogrulama."
category: database
status: curated
confidence: high
requires: [research-before-code, security-audit]
tags: [database, postgres, schema, modeling, rls, migration, index]
updated: 2026-09-20
verified_at: 2026-09-20
evidence_level: RECOMMENDATION
---

# Amaç

İlişkisel veritabanı (genellikle PostgreSQL) şeması tasarlarken tekrar kullanılabilir,
ölçeklenebilir, güvenli ve veri bütünlüğünü koruyan yapı kurmak.

# Ne zaman kullan

- Yeni proje/özellik başlangıcında
- Mevcut şema değişikliklerinde (migration)
- Performans/yavaş sorgu şikayetlerinde

# İş Akışı (MODEL → NORMALIZE → INDEX → RLS → MIGRATE → VALIDATE)

## 1. MODEL — Varlıkları ve ilişkileri belirle

- İş kurallarını İngilizce/Türkçe cümlelerle yaz. Örn: "Bir siparişin bir müşterisi olur; bir müşterinin birçok siparişi olur; bir siparişte birçok kalem bulunur."
- Ana varlıklar: User, Organization, Product, Category, Order, OrderItem, Payment, Shipment, Invoice, Address, File, Log.
- İsimlendirme: tekil, `snake_case` (Postgres geleneği); çoğul tablo yerine tekil tercih et, takım standardı neyse onu tutarlı kullan.
- Her tabloya `id` (uuid veya bigserial), `created_at timestamptz default now()`, `updated_at timestamptz`.

## 2. NORMALIZE

- 1., 2., 3. normal form: her bilgi tek yerde tutulur; çoktan çoğa ilişki için junction tablo (örn. `order_items`, `product_category`).
- Enum'lar Postgres enum tipi veya lookup tablo. Durum ve tip alanlarında enum kullan; serbest string kullanma.
- Para: `numeric(12,2)` veya `integer` en küçük birim (kuruş) cinsinden; float kullanma (hata).
- Zaman: `timestamptz` (saat dilimi bilgisi); tarih (saatsiz) için `date`.
- JSONB yalnızca esnek şema gerektiğinde; düzenli sütuna alabileceğin alanları JSONB'ye gömme.
- Soft delete gerekli mi? `deleted_at timestamptz null`; ancak çoğu durumda arşiv tablosu veya durum alanı daha iyidir.
- Audit trail: önemli tablolarda `created_by`, `updated_by`; ayrı audit log tablosu (trigger ile).

## 3. INDEX — Performans

- Birincil anahtar zaten indeksli.
- Foreign key kolonlarına indeks ekle (join performansı).
- Sık sorgulanan kolonlar (`email`, `slug`, `status`) için indeks.
- Composite index: filtre+sıralama birleşimlerinde (örn. `(organization_id, created_at desc)`).
- Çok indeks ekleme: her yazma yavaşlar.
- GIN indeksi: JSONB ve full-text search için.

## 4. RLS / YETKİ (Supabase veya benzeri)

- Her kullanıcı sadece kendi verisini görmeli / değiştirebilmeli.
- Basit bir RLS şablonu:
  ```sql
  alter table orders enable row level security;
  create policy "users read own orders" on orders for select
    using (auth.uid() = user_id);
  ```
- Admin/service-role için bypass; ama service role'ü asla istemcide kullanma.
- Policy'leri test et (farklı kullanıcı ile SQL çalıştırarak veya Playwright E2E).

## 5. MIGRATE — Migration yaz

- Her şema değişikliği bir migration dosyası ile (Prisma migrate, Drizzle kit, raw SQL).
- Migration geri döndürülebilir olmalı (down script).
- Büyük tablolarda ALTER TABLE kilit süresine dikkat; geniş deployment saatlerinde çalıştır.
- Migration'ları kod ile birlikte commit'le ve CI'da tekrar çalıştırılabilir olsun.

## 6. VALIDATE

- Şema değişikliğini test ortamında uygula.
- Örnek verilerle migration sonrası veri bütünlüğü bozulmamış mı?
- Kritik sorguları açıkla (`explain analyze`); indeks kullanıyor mu?
- RLS policy testi (yetkisiz kullanıcı gerçekten erişemiyor mu?).
- Seed verisi ile uygulama çalıştırıp Playwright test et.

# Kalite Kontrol Listesi

- [ ] Varlıklar ve ilişkiler net
- [ ] Her tablo id/created_at/updated_at
- [ ] FK ve indeksler doğru
- [ ] Para numeric/integer; float yok
- [ ] Zaman timestamptz
- [ ] Enum ve durumlar enum/lookup tablo ile sabitlenmiş
- [ ] RLS policy'leri tablo başına
- [ ] Audit/soft-delete ihtiyacı değerlendirildi
- [ ] Migration geri döndürülebilir ve idempotent
- [ ] Kritik sorgular explain ile doğrulandı

# Yaygın Hatalar

- Her şeyi `users` tablosuna koymak (address, profile, settings ayrı olmalı).
- Para alanlarını float/double kullanmak.
- `timestamp without time zone` kullanmak (saat dilimi sorunları).
- RLS policy yazmadan tabloyu istemciye açmak (herkes tüm veriyi görür).
- FK'leri unutup veritabanı bütünlüğünü uygulamaya bırakmak.
- Çok fazla/cok az indeks.
- JSONB içine düzenli veriyi koymak (sorgu ve bütünlük kaybı).

# Referanslar

- PostgreSQL docs: https://www.postgresql.org/docs/
- Supabase RLS: https://supabase.com/docs/guides/database/postgres/row-level-security
- Prisma Schema: https://www.prisma.io/docs/orm/prisma-schema
- Drizzle Schema: https://orm.drizzle.team/docs/schemas

# İlgili Skill'ler

- `api-design`
- `security-audit`
- `research-before-code`
