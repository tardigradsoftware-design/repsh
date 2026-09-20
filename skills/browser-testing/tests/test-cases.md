# Test Senaryoları — browser-testing

## Test 1: Kırılgan selector seçimi

**Girdi:**
```js
await page.click('.sc-1x3bc2a > div:nth-child(2) > button');
```

**Beklenen:**
- Kırılgan selector olduğunu tespit eder; CSS hash sınıfı ve nth-child kırılmaya mahkum.
- Düzeltme: `<button data-testid="add-to-cart">Sepete ekle</button>` → `page.getByTestId('add-to-cart')` veya
  `page.getByRole('button', { name: /Sepete ekle/i })`.
- Benzer kırılgan selectorleri tüm dosyada tarar.

## Test 2: Wait-for-timeout anti-pattern

**Girdi:**
```js
await page.click('button[type=submit]');
await page.waitForTimeout(3000);
expect(await page.textContent('.success')).toContain('başarıyla');
```

**Beklenen:**
- Sabit wait flaky kaynaktır; web first assertion ile değiştirir:
  `await expect(page.locator('.success')).toContainText('başarıyla', { timeout: 10000 });`
- Ya da belirli network isteğinin tamamlanmasını `page.waitForResponse(...)` ile bekler.
- Sabit timeout'ları dosyada tarar.
