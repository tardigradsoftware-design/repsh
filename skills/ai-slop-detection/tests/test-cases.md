# Test Senaryoları — ai-slop-detection

## Test 1: Jenerik SaaS landing page

**Girdi (JSX):**
```jsx
<section className="bg-gradient-to-br from-purple-500 via-pink-500 to-indigo-600 py-24">
  <div className="max-w-7xl mx-auto px-4 text-center text-white">
    <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-md px-4 py-1.5 rounded-full border border-white/20">
      <Sparkles className="w-4 h-4" /> <span>Powered by AI</span>
    </div>
    <h1 className="text-6xl font-bold mt-6">Supercharge your workflow</h1>
    <p className="mt-4 text-xl text-white/80">Build faster, ship smarter, scale better.</p>
    <button className="mt-8 bg-white text-indigo-600 px-8 py-3 rounded-full font-semibold hover:scale-105 transition">
      Get started
    </button>
  </div>
</section>
<section className="py-24 bg-white">
  <div className="max-w-7xl mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-8">
    {[{i:Zap,t:"Lightning Fast",d:"10x faster than competitors"},
      {i:Shield,t:"Secure",d:"Enterprise-grade security"},
      {i:Rocket,t:"Scalable",d:"Scale to millions"}].map(f => (
      <div key={f.t} className="p-6 rounded-2xl shadow-lg bg-white">
        <f.i className="w-12 h-12 text-indigo-600" />
        <h3 className="mt-4 text-xl font-bold">{f.t}</h3>
        <p className="mt-2 text-gray-600">{f.d}</p>
      </div>
    ))}
  </div>
</section>
```

**Beklenen çıktı:**
- Skor 30–45 arası (yüksek AI-slop).
- KRİTİK: "Supercharge your workflow", "10x faster" sahte iddia; "Powered by AI" anlamsız rozet;
  CTA İngilizce "Get started".
- HIGH: Her yer mor-pembe gradient + backdrop-blur glassmorphism; `hover:scale-105`; `rounded-full`
  buton/kart; `p-6 rounded-2xl shadow-lg` kartlar; Zap/Shield/Rocket klişe ikonlar; `max-w-7xl`
  şablonu; `py-24` her bölüm.
- MEDIUM: Başlık 6xl aşırı büyük; metin kopyası jenerik.
- Öneriler somut olmalı: renk paleti önerisi, başlık metni (kullanıcı faydası odaklı, Türkçe),
  rounded değerleri düşür, scale yerine hafif shadow/gölge değişimi, ikonları daha özgün
  kıl veya azalt, gerçek sosyal kanıt kullan.
- Sonrasında aynı JSX'in yeniden yazılmış hali verilmeli; en az 5 KRİTİK/HIGH madde giderilmiş olmalı.

**Hata sayılacak davranış:**
- Sadece "AI yapmış" deyip teşhisi koymamak.
- Sadece renk önerip kopyayı görmezden gelmek.
- Türkçe'ye çeviri ihtiyacını belirtmemek.

---

## Test 2: Görece iyi ama sorunlu dashboard

**Girdi:** Bir dashboard ekranı screenshot'ı:
- Sidebar lacivert (#0f172a), beyaz arka plan, `rounded-xl` beyaz kartlarda veri tablosu ve metrikler.
- Metrik kartları: 4 adet, herbiri `p-6 rounded-xl border shadow-sm`; sayılar büyük ve siyahta.
- Tablo: gayet düzenli, sıralama okları var, sayfalama var.
- Ancak:
  - "Welcome back, Admin" başlığı; veri yok "merhaba" hissi.
  - Metrikler "Toplam Kullanıcı", "Aktif Kullanıcı", "Toplam Gelir", "Başarı Oranı" şeklinde ama
    dipçik (small delta, değişim) yok; tekil sayı veriyor.
  - Tüm boş durumlarda Lucide `Inbox` ikonu ve "Veri bulunamadı" yazısı.
  - Buton `hover:scale-105`.
  - Birincil renk Tailwind varsayılanı `bg-blue-600`; marka rengi tanımlı değil.

**Beklenen çıktı:**
- Skor 60–70 (kullanılabilir ama belirgin şablon).
- HIGH: Karşılama mesajı "Welcome back, Admin" jenerik; metrik kartlarında değişim/trend bilgisi yok.
- MEDIUM: Boş durum görseli her yerde aynı ikon; hover scale; birincil renk varsayılan Tailwind mavisi.
- Düşük skorun nedeni: gerçekten kötü olmasa da herhangi bir shadcn/ui demo sitesinden ayırt
  edilemiyor; marka kimliği yok.
- Öneri: Gerçek kullanıcı adı, son giriş veya özet bağlam; metriklerin altına yüzde değişim ve
  yön oku; boş durumları bağlama özel çizim/mesajla özelleştir; birincil rengi marka rengine çek;
  hover animasyonunu ölçülü yap.

**Hata sayılacak davranış:**
- Her şeyi iyi görüp yüksek skor vermek.
- Sorunları fark edip ama somut iyileştirme sunmamak.
