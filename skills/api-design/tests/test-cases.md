# Test Senaryoları — api-design

## Test 1: Fiil odaklı route

**Girdi:** `/api/getUserOrders?userId=5`

**Beklenen:** Kaynak odaklı REST önerisi: `/api/users/5/orders` veya `/api/orders?userId=5`; GET zaten listeleme olduğu için fiil gereksiz; yetki kontrolleri `userId` yerine oturumdaki kullanıcıdan alınmalı.

## Test 2: Input doğrulaması yok

**Girdi:**
```js
export async function POST(req) {
  const body = await req.json();
  await db.order.create({ data: { total: body.total } });
}
```

**Beklenen:**
- Zod şeması ile total'in sayı ve >=0, pozitif sayı olduğunu doğrula; eksik alanları 400 ile dön.
- Oturumdan kullanıcıyı al; body'den `userId` kabul etme.
- Hata durumunda uygun HTTP kodu ve yapılandırılmış hata nesnesi.
