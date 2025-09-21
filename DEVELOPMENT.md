# Sasko.io Geliştirme Rehberi

🎰 **AI-Powered iGaming SaaS Platform Development Guide**

## 🚀 Hızlı Başlangıç

### Gereksinimler
- **Python 3.11+**
- **Node.js 18+**
- **Docker & Docker Compose**
- **PostgreSQL 14+**
- **Redis 6+**

### Kurulum

```bash
# Repository'yi klonla
git clone <repository-url>
cd sasko-io

# Tüm servisleri başlat
./start-project.sh

# Servisleri durdur
./stop-project.sh
```

## 🏗️ Proje Yapısı

```
sasko-io/
├── backend/                 # Django Backend
│   ├── apps/               # Django Apps
│   │   ├── core/          # Temel modeller
│   │   ├── player_engine/ # Oyuncu motoru
│   │   ├── bonus_engine/  # Bonus motoru
│   │   ├── affiliate_engine/ # Ortaklık motoru
│   │   ├── carkwheel_ai/  # Çark AI
│   │   ├── kaziwild/      # KazıWild
│   │   ├── rizziko_ai/    # Risk AI
│   │   ├── marketing_ai/  # Pazarlama AI
│   │   ├── payment_ai/    # Ödeme AI
│   │   └── api_gateway/   # API Gateway
│   ├── sasko_core/        # Django settings
│   ├── requirements.txt   # Python dependencies
│   └── manage.py         # Django management
├── frontend/              # Next.js Frontend
│   └── sasko-frontend/   # Next.js app
│       ├── src/          # Source code
│       ├── public/       # Static files
│       └── package.json  # Node dependencies
├── docker-compose.yml    # Docker services
├── start-project.sh     # Başlangıç scripti
├── stop-project.sh      # Durdurma scripti
└── README.md           # Proje dokümantasyonu
```

## 🛠️ Geliştirme Ortamı

### Backend Geliştirme

```bash
cd backend

# Virtual environment aktif et
source venv/bin/activate

# Yeni migration oluştur
python manage.py makemigrations

# Migration'ları uygula
python manage.py migrate

# Superuser oluştur
python manage.py createsuperuser

# Development server başlat
python manage.py runserver

# Django shell
python manage.py shell

# Test çalıştır
python manage.py test
```

### Frontend Geliştirme

```bash
cd frontend/sasko-frontend

# Development server başlat
npm run dev

# Build oluştur
npm run build

# Production server başlat
npm start

# Linting
npm run lint

# Type checking
npm run type-check
```

## 🎯 Modül Geliştirme

### Yeni Modül Oluşturma

```bash
# Backend'de yeni app oluştur
cd backend
python manage.py startapp yeni_modul apps/yeni_modul

# Settings.py'a ekle
# LOCAL_APPS listesine 'apps.yeni_modul' ekle
```

### Modül Yapısı

```python
# apps/yeni_modul/models.py
from django.db import models
from apps.core.models import User, Tenant

class YeniModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    # Diğer alanlar...

# apps/yeni_modul/serializers.py
from rest_framework import serializers
from .models import YeniModel

class YeniModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YeniModel
        fields = '__all__'

# apps/yeni_modul/views.py
from rest_framework import viewsets
from .models import YeniModel
from .serializers import YeniModelSerializer

class YeniModelViewSet(viewsets.ModelViewSet):
    queryset = YeniModel.objects.all()
    serializer_class = YeniModelSerializer
```

## 🌍 Çoklu Dil Desteği

### Backend (Django)

```python
# models.py
from django.utils.translation import gettext_lazy as _

class Model(models.Model):
    name = models.CharField(_('Name'), max_length=100)

# views.py
from django.utils.translation import gettext as _

def view(request):
    message = _('Welcome to Sasko.io')
```

### Frontend (Next.js)

```typescript
// lib/i18n.ts
import { createIntl, createIntlCache } from 'react-intl';

const cache = createIntlCache();

export const intl = createIntl({
  locale: 'tr',
  messages: {
    'welcome': 'Sasko.io\'ya Hoş Geldiniz'
  }
}, cache);

// components/Component.tsx
import { FormattedMessage } from 'react-intl';

export default function Component() {
  return (
    <FormattedMessage id="welcome" defaultMessage="Welcome to Sasko.io" />
  );
}
```

## 💰 Çoklu Para Birimi

### Backend

```python
# apps/core/utils.py
from decimal import Decimal
from .models import Currency

def convert_currency(amount: Decimal, from_currency: str, to_currency: str) -> Decimal:
    from_rate = Currency.objects.get(code=from_currency).exchange_rate
    to_rate = Currency.objects.get(code=to_currency).exchange_rate
    
    # USD'ye çevir, sonra hedef para birimine
    usd_amount = amount / from_rate
    return usd_amount * to_rate

# Kullanım
converted = convert_currency(Decimal('100'), 'TRY', 'USD')
```

### Frontend

```typescript
// hooks/useCurrency.ts
import { useContext } from 'react';
import { CurrencyContext } from '@/contexts/CurrencyContext';

export const useCurrency = () => {
  const context = useContext(CurrencyContext);
  
  const formatCurrency = (amount: number, currency?: string) => {
    const curr = currency || context.currency;
    return new Intl.NumberFormat('tr-TR', {
      style: 'currency',
      currency: curr
    }).format(amount);
  };
  
  return { formatCurrency, ...context };
};
```

## 🤖 AI Entegrasyonu

### AI Modül Yapısı

```python
# apps/player_engine/ai/player_analyzer.py
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class PlayerAnalyzer:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.is_trained = False
    
    def analyze_player(self, player_data):
        if not self.is_trained:
            self.train_model()
        
        features = self.extract_features(player_data)
        prediction = self.model.predict([features])
        
        return {
            'risk_score': prediction[0],
            'recommendations': self.generate_recommendations(prediction[0])
        }
    
    def train_model(self):
        # Model eğitimi
        pass
```

### Celery Task

```python
# apps/player_engine/tasks.py
from celery import shared_task
from .ai.player_analyzer import PlayerAnalyzer

@shared_task
def analyze_player_behavior(player_id):
    analyzer = PlayerAnalyzer()
    # Player verilerini al
    # Analiz yap
    # Sonuçları kaydet
    return result
```

## 🔌 API Geliştirme

### API Endpoint Oluşturma

```python
# apps/api_gateway/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'bonuses', BonusViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

# apps/player_engine/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

class PlayerViewSet(viewsets.ModelViewSet):
    @action(detail=True, methods=['post'])
    def analyze(self, request, pk=None):
        player = self.get_object()
        # AI analizi yap
        result = analyze_player_behavior.delay(player.id)
        return Response({'task_id': result.id})
```

### API Şubeleşme

```python
# apps/core/middleware.py
class APIBranchingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Tenant bazlı API şubeleşme
        tenant = self.get_tenant(request)
        request.api_config = self.get_api_config(tenant)
        
        response = self.get_response(request)
        return response
```

## 🧪 Test Yazma

### Backend Test

```python
# apps/player_engine/tests.py
from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Player

class PlayerModelTest(TestCase):
    def test_player_creation(self):
        player = Player.objects.create(username='test_player')
        self.assertEqual(player.username, 'test_player')

class PlayerAPITest(APITestCase):
    def test_player_list(self):
        response = self.client.get('/api/v1/players/')
        self.assertEqual(response.status_code, 200)
```

### Frontend Test

```typescript
// __tests__/components/PlayerCard.test.tsx
import { render, screen } from '@testing-library/react';
import PlayerCard from '@/components/PlayerCard';

describe('PlayerCard', () => {
  it('renders player information', () => {
    const player = { id: 1, name: 'Test Player' };
    render(<PlayerCard player={player} />);
    
    expect(screen.getByText('Test Player')).toBeInTheDocument();
  });
});
```

## 📊 Monitoring ve Logging

### Backend Logging

```python
# settings.py
LOGGING = {
    'version': 1,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'sasko.log',
        },
    },
    'loggers': {
        'sasko': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    },
}

# views.py
import logging

logger = logging.getLogger('sasko')

def my_view(request):
    logger.info(f'Player {request.user.id} accessed view')
```

### Metrics

```python
# apps/core/metrics.py
from django.core.cache import cache
import time

def track_api_call(endpoint, duration):
    key = f"api_metrics:{endpoint}"
    cache.set(key, {
        'calls': cache.get(f"{key}:calls", 0) + 1,
        'avg_duration': duration
    }, timeout=3600)
```

## 🚀 Deployment

### Docker Build

```bash
# Backend Dockerfile
docker build -t sasko-backend ./backend

# Frontend Dockerfile
docker build -t sasko-frontend ./frontend

# Full stack
docker-compose up -d
```

### Production Settings

```python
# backend/sasko_core/settings/production.py
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['sasko.io', 'api.sasko.io']

# Security settings
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
```

## 🔧 Troubleshooting

### Yaygın Sorunlar

1. **Database Connection Error**
   ```bash
   # PostgreSQL servisini kontrol et
   docker-compose ps postgres
   
   # Logs kontrol et
   docker-compose logs postgres
   ```

2. **Frontend Build Error**
   ```bash
   # Node modules temizle
   rm -rf node_modules package-lock.json
   npm install
   ```

3. **Celery Worker Çalışmıyor**
   ```bash
   # Redis bağlantısını kontrol et
   redis-cli ping
   
   # Celery worker restart
   pkill -f celery
   celery -A sasko_core worker -l info
   ```

## 📚 Kaynaklar

- [Django Documentation](https://docs.djangoproject.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Chakra UI Documentation](https://chakra-ui.com/docs)
- [Celery Documentation](https://docs.celeryproject.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

**Sasko.io ile iGaming'in geleceğini şekillendirin! 🎰✨**
