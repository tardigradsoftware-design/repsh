# Test Senaryoları — accessibility-audit

## Test 1: Div ile yapılmış buton

**Girdi:** `<div className="btn" onClick={save}>Kaydet</div>`

**Beklenen:**
- CRITICAL olarak işaretler: native <button> olmalı, klavye erişimi yok, form submit entegrasyonu yok, ARIA rolü yok.
- Düzeltme: `<button type="button" onClick={save}>` veya submit ise `type="submit"`.
- Focus ring olduğundan emin olur.

## Test 2: Renk ile kodlanmış durum

**Girdi:**
```jsx
<span className={status === 'active' ? 'text-green-600' : 'text-red-600'}>
  {status === 'active' ? 'Aktif' : 'Pasif'}
</span>
```
(Burada aslında metin de var; sadece renk olsaydı daha kritik.)

**Beklenen:**
- Hem renk hem metin/ikon kullanıldığı için kısmen geçer; ancak renk köründe okunaklılığı için
  ek ikon (check/x) veya pill içinde arka plan + ikon kombinasyonu önerir.
- Kontrastı ölçer: 4.5:1'ye ulaşmıyorsa renk tonunu ayarlar.
