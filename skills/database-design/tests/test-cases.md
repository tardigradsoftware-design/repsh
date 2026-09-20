# Test Senaryoları — database-design

## Test 1: Para float kullanımı

**Girdi:** `price double precision` kolonunda sipariş tutarları tutuluyor.

**Beklenen:**
- Float para için yanlıştır (yuvarlama hataları). `numeric(12,2)` veya `integer` (kuruş cinsinden) önerir.
- Migrasyon ile veri dönüşümü planlanır; finans hesaplarında tutarsızlık riski için HIGH olarak işaretler.

## Test 2: RLS kapalı tablo

**Girdi:** Supabase'de `documents` tablosunda RLS etkin değil. Client anon key ile herkes her belgeyi okuyabilir.

**Beklenen:**
- CRITICAL: Hemen RLS etkinleştirilir; en azından kullanıcı `owner_id`'si ile kendi belgelerine erişim policy'si yazılır.
- Test kullanıcıları ile select/update/delete denemesi yapılır; başka kullanıcıya ait belge erişilemez olmalı.
