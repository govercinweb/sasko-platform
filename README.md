# How to run celery
```shell
celery -A sasko worker --beat --loglevel=info
```

# Sasko.io - AI-Powered iGaming SaaS Platform

🎰 **Çılgın Deneyimlerle iGaming Endüstrisine Devrim Getiren Platform**

## 🚀 Proje Genel Bakış

Sasko.io, iGaming operatörlerine AI destekli modüller, çoklu para birimi desteği ve esnek API mimarisi sunan yeni nesil SaaS platformudur.

### 🎯 Temel Özellikler 

- **🤖 AI-Powered Modüller:** 8 farklı AI destekli modül
- **💰 Çoklu Para Birimi:** 50+ para birimi desteği
- **🌍 Çoklu Dil:** 25+ dil desteği
- **🏗️ Mikroservis Mimarisi:** Ölçeklenebilir ve esnek yapı
- **🔌 API-First:** RESTful API ile tam entegrasyon
- **⚡ Hızlı MVP:** Chakra UI ile hızlı geliştirme

## 🏛️ Mimari

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend (Next.js + Chakra UI)          │
├─────────────────────────────────────────────────────────────┤
│                    API Gateway (Django)                    │
├─────────────────────────────────────────────────────────────┤
│  Player    │ Bonus   │ Affiliate │ CarkWheel │ KazıWild    │
│  Engine    │ Engine  │ Engine    │ AI        │             │
├─────────────────────────────────────────────────────────────┤
│  Rizziko   │ Marketing│ Player    │           │             │
│  AI        │ Board AI │ to Pay AI │           │             │
├─────────────────────────────────────────────────────────────┤
│              PostgreSQL + Redis + TimescaleDB              │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Teknoloji Yığını

### Backend
- **Python 3.11+** - Ana programlama dili
- **Django 4.2+** - Web framework
- **Django REST Framework** - API geliştirme
- **Celery** - Asenkron görev yönetimi
- **PostgreSQL** - Ana veritabanı
- **Redis** - Önbellekleme ve mesaj kuyruğu
- **TimescaleDB** - Zaman serisi verileri

### Frontend
- **Next.js 14+** - React framework
- **TypeScript** - Tip güvenliği
- **Chakra UI** - UI bileşen kütüphanesi
- **React Query** - Veri yönetimi
- **Zustand** - State management

### DevOps & Infrastructure
- **Docker** - Konteynerizasyon
- **Kubernetes** - Orkestrasyon
- **GitHub Actions** - CI/CD
- **AWS/GCP** - Cloud infrastructure

## 📦 Modüller

| Modül | Açıklama | Durum |
|-------|----------|-------|
| **Player Engine** | AI destekli oyuncu yönetimi | 🚧 Geliştiriliyor |
| **Automatic Bonus Engine AI** | Akıllı bonus sistemi | 🚧 Geliştiriliyor |
| **Affiliate Engine** | Ortaklık yönetimi | 📋 Planlanan |
| **CarkWheel AI** | Çark oyunları motoru | 📋 Planlanan |
| **KazıWild** | Türk kültürü kazan kazan | 📋 Planlanan |
| **Rizziko AI** | Risk yönetimi ve analiz | 🚧 Geliştiriliyor |
| **Marketing Board AI** | Pazarlama panosu | 📋 Planlanan |
| **Player to Pay AI** | Ödeme sistemi | 📋 Planlanan |

## 🚀 Hızlı Başlangıç

### Gereksinimler
- Python 3.11+
- Node.js 18+
- PostgreSQL 14+
- Redis 6+
- Docker & Docker Compose

### Kurulum

```bash
# Repository'yi klonla
git clone https://github.com/sasko-io/sasko-platform.git
cd sasko-platform

# Backend kurulumu
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# Frontend kurulumu
cd ../frontend
npm install

# Veritabanı kurulumu
docker-compose up -d postgres redis

# Migrasyonları çalıştır
cd ../backend
python manage.py migrate

# Geliştirme sunucularını başlat
python manage.py runserver &
cd ../frontend && npm run dev
```

## 🌍 Çoklu Dil ve Para Birimi

### Desteklenen Diller
🇹🇷 Türkçe | 🇺🇸 English | 🇩🇪 Deutsch | 🇫🇷 Français | 🇪🇸 Español | 🇮🇹 Italiano | 🇷🇺 Русский | 🇨🇳 中文 | 🇯🇵 日本語 | 🇰🇷 한국어

### Desteklenen Para Birimleri
💵 USD | 💶 EUR | 💷 GBP | 💴 JPY | 🇹🇷 TRY | 🇨🇦 CAD | 🇦🇺 AUD | 🇨🇭 CHF | 🇸🇪 SEK | 🇳🇴 NOK | ₿ BTC | Ξ ETH

## 🤖 AI Entegrasyonu

Sasko.io, gelişen AI teknolojilerine açık bir mimari sunar:

- **Modüler AI Sistemi:** Her modül kendi AI motoruna sahip
- **Plugin Mimarisi:** Yeni AI algoritmalarının kolay entegrasyonu
- **Real-time Learning:** Canlı veri ile sürekli öğrenme
- **Multi-model Support:** TensorFlow, PyTorch, Scikit-learn desteği

## 📊 API Dokümantasyonu

API dokümantasyonuna erişim:
- **Swagger UI:** `http://localhost:8000/api/docs/`
- **ReDoc:** `http://localhost:8000/api/redoc/`
- **Postman Collection:** `docs/api/sasko-api.postman_collection.json`

## 🔧 Geliştirme

### Kod Standartları
- **Python:** PEP 8, Black formatter
- **TypeScript:** ESLint, Prettier
- **Commit:** Conventional Commits
- **Testing:** 90%+ test coverage

### Branching Strategy
- `main` - Production
- `develop` - Development
- `feature/*` - Yeni özellikler
- `hotfix/*` - Acil düzeltmeler

## 🚀 Deployment

### Staging
```bash
docker-compose -f docker-compose.staging.yml up -d
```

### Production
```bash
kubectl apply -f k8s/
```

## 📈 Monitoring

- **Metrics:** Prometheus + Grafana
- **Logging:** ELK Stack
- **Tracing:** Jaeger
- **Alerts:** PagerDuty

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'feat: add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 📞 İletişim

- **Website:** https://sasko.io
- **Email:** dev@sasko.io
- **Discord:** https://discord.gg/sasko-io
- **Twitter:** [@SaskoIO](https://twitter.com/SaskoIO)

---

**Sasko.io ile iGaming'in geleceğini şekillendirin! 🎰✨**