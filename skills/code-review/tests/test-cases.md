# Test Senaryoları — code-review

## Test 1: Any kullanımı ve tip güvenliği

**Girdi:** `const data: any = await response.json(); render(data.user.name);`

**Beklenen:**
- CRITICAL/MEDIUM: `any` tip güvenliğini kırıyor; runtime hata riski (user null gelebilir).
- Düzeltme: zod şeması ile parse et; sonucun tipini çıkar; hata durumunu ele al.
- Kod tabanındaki diğer `any` kullanımları da işaretlenir; `unknown` + type-guard veya
  schema doğrulama önerilir.

## Test 2: Yorumlanmış kod ve console.log

**Girdi:**
```js
// const old = await legacyFetch(id);
console.log('DEBUG user', user);
// TODO: later add error handling
return user;
```

**Beklenen:**
- Ölü kodu (yoruma alınmış satırı) kaldır; git geçmişinden erişilebilir.
- console.log'u kaldır; gerekirse gözlenebilirlik (logging kütüphanesi) kullan ama production'da bilgi sızdırma.
- TODO'yu gerçek bir karta/issue'ya bağla; anonim TODO'lar unutulur.
