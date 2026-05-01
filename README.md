# 🎮 Bolalar O'yinlari Platformasi

3 ta qiziqarli o'yin bilan bolalar uchun interaktiv o'yin platformasi.

## 🚀 O'yinlar

1. **Shakllar** (`/game1/`) - Rangli shakllarni uychasiga joylashtirish
2. **Hayvonlar** (`/game2/`) - Hayvonlarni drag-drop bilan juftlashtirish
3. **Sehrli Daraxt** (`/game3/`) - Raqamlarni topib daraxtni gullatish

## 🛠 Texnologiyalar

- **Backend:** Django 4.2
- **Frontend:** HTML5, CSS3, JavaScript
- **Styling:** Tailwind CSS
- **Animations:** Canvas Confetti
- **Deployment:** Vercel

## 📦 O'rnatish

```bash
# Repository clone qilish
git clone <repository-url>
cd baby_game_site

# Virtual environment yaratish
python -m venv env
source env/bin/activate  # Linux/Mac
# yoki
env\Scripts\activate  # Windows

# Dependencies o'rnatish
pip install -r requirements.txt

# Server ishga tushirish
python manage.py runserver
```

## 🌐 Vercelga Deploy Qilish

### 1. Vercel CLI o'rnatish

```bash
npm i -g vercel
```

### 2. Vercelga login

```bash
vercel login
```

### 3. Loyihani deploy qilish

```bash
# Development deployment
vercel

# Production deployment
vercel --prod
```

### 4. Environment Variables (Vercel Dashboard)

Vercel dashboardga kiring va quyidagi environment variables qo'shing:

- `DJANGO_SECRET_KEY` - Django secret key (yangi generate qiling)
- `DEBUG` - `False` (production uchun)

Secret key generate qilish:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 🎯 O'yin Mexanikalari

### Shakllar (Game 1)
- 8 turli shakl
- Drag & drop mexanikasi
- Har bir to'g'ri javobda qarsak ovozi
- Barchasi to'g'ri bo'lsa g'alaba ovozi

### Hayvonlar (Game 2)
- 8 turli hayvon
- Drag & drop juftlashtirish
- **Bitta xato = o'yin tugaydi**
- Progress bar

### Sehrli Daraxt (Game 3)
- 5 ta savol
- **Bitta xato = mag'lubiyat**
- O'zbekcha ovoz: "1 raqamini toping"
- Progress bar

## 🔊 Ovoz Tizimi

Barcha o'yinlarda Web Audio API orqali ovozlar:
- To'g'ri javob - xursandchilik ovozi
- Noto'g'ri javob - xato ovozi
- G'alaba - g'alaba musiqasi

## ⚙️ Sozlamalar

Sozlamalar sahifasida (`/settings/`):
- Ovoz yoqish/o'chirish
- Fon musiqasi (toggle)
- Ovoz balandligi

## 📱 Responsive Dizayn

Barcha o'yinlar mobil qurilmalarga mos:
- Touch support
- Responsive grid
- Mobile-optimized UI

## 📝 Litsenziya

MIT License

## 🤝 Muallif

Bolalar o'yinlari platformasi - MVP
