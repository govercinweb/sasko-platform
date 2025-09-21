# Sasko.io'ya Katkıda Bulunma Rehberi

🎰 **AI-Powered iGaming SaaS Platform**

Sasko.io projesine katkıda bulunduğunuz için teşekkür ederiz! Bu rehber, projeye nasıl katkıda bulunabileceğinizi açıklar.

## 📋 İçindekiler

- [Davranış Kuralları](#davranış-kuralları)
- [Nasıl Katkıda Bulunurum?](#nasıl-katkıda-bulunurum)
- [Geliştirme Ortamı Kurulumu](#geliştirme-ortamı-kurulumu)
- [Pull Request Süreci](#pull-request-süreci)
- [Kod Standartları](#kod-standartları)
- [Test Yazma](#test-yazma)
- [Dokümantasyon](#dokümantasyon)

## 🤝 Davranış Kuralları

Bu proje [Contributor Covenant](https://www.contributor-covenant.org/) davranış kurallarını benimser. Katılım göstererek bu kuralları takip etmeyi kabul etmiş olursunuz.

### Beklentilerimiz

- **Saygılı olun:** Farklı görüşlere ve deneyimlere saygı gösterin
- **Yapıcı olun:** Eleştirilerinizi yapıcı bir şekilde iletin
- **Kapsayıcı olun:** Herkesi dahil eden bir ortam yaratın
- **Öğrenmeye açık olun:** Hatalardan öğrenmeye istekli olun

## 🚀 Nasıl Katkıda Bulunurum?

### 1. Issue Bildirme

Bir hata bulduysanız veya yeni bir özellik önerisi varsa:

1. [Issues](https://github.com/sasko-io/sasko-platform/issues) sayfasını kontrol edin
2. Benzer bir issue yoksa yeni bir issue oluşturun
3. Aşağıdaki şablonu kullanın:

```markdown
## Hata Raporu / Özellik Önerisi

### Açıklama
[Hatayı veya özelliği detaylı açıklayın]

### Adımlar (Hata için)
1. [İlk adım]
2. [İkinci adım]
3. [Hatanın oluştuğu adım]

### Beklenen Davranış
[Ne olmasını bekliyordunuz]

### Gerçek Davranış
[Ne oldu]

### Ortam
- OS: [örn. Ubuntu 22.04]
- Python: [örn. 3.11]
- Node.js: [örn. 18.17]
- Browser: [örn. Chrome 118]

### Ekran Görüntüleri
[Varsa ekran görüntüleri ekleyin]
```

### 2. Kod Katkısı

1. **Fork yapın:** Repository'yi kendi hesabınıza fork edin
2. **Branch oluşturun:** `git checkout -b feature/amazing-feature`
3. **Geliştirin:** Kodunuzu yazın ve test edin
4. **Commit yapın:** `git commit -m 'feat: add amazing feature'`
5. **Push yapın:** `git push origin feature/amazing-feature`
6. **Pull Request açın:** GitHub'da pull request oluşturun

## 🛠️ Geliştirme Ortamı Kurulumu

### Gereksinimler

- Python 3.11+
- Node.js 18+
- Docker & Docker Compose
- Git

### Kurulum

```bash
# Repository'yi klonlayın
git clone https://github.com/sasko-io/sasko-platform.git
cd sasko-platform

# Environment variables kopyalayın
cp .env.example .env

# Geliştirme ortamını başlatın
./start-project.sh
```

### Geliştirme Sunucuları

- **Backend:** http://localhost:8000
- **Frontend:** http://localhost:3000
- **Admin:** http://localhost:8000/admin
- **API Docs:** http://localhost:8000/api/docs/

## 📝 Pull Request Süreci

### 1. PR Hazırlığı

- [ ] Kodunuz test edildi mi?
- [ ] Dokümantasyon güncellendi mi?
- [ ] Commit mesajları [Conventional Commits](https://conventionalcommits.org/) standardına uygun mu?
- [ ] Kod standartlarına uyuyor mu?

### 2. PR Şablonu

```markdown
## Değişiklik Türü

- [ ] Bug fix (kırılmayan değişiklik)
- [ ] New feature (kırılmayan değişiklik)
- [ ] Breaking change (mevcut işlevselliği etkileyen değişiklik)
- [ ] Documentation update

## Açıklama

[Değişikliklerinizi detaylı açıklayın]

## Test Edilen Durumlar

- [ ] Test A
- [ ] Test B
- [ ] Test C

## Ekran Görüntüleri

[Varsa ekran görüntüleri ekleyin]

## Checklist

- [ ] Kodumun proje standartlarına uygun olduğunu kontrol ettim
- [ ] Self-review yaptım
- [ ] Koduma yorum ekledim (özellikle anlaşılması zor kısımlara)
- [ ] Dokümantasyonu güncelledim
- [ ] Değişikliklerim uyarı vermedi
- [ ] Test ekledim
- [ ] Yeni ve mevcut testler geçiyor
```

### 3. Review Süreci

1. **Otomatik Kontroller:** CI/CD pipeline'ı çalışır
2. **Code Review:** En az bir maintainer review yapar
3. **Test:** Değişiklikler test edilir
4. **Merge:** Onaylandıktan sonra merge edilir

## 📏 Kod Standartları

### Python (Backend)

```python
# PEP 8 standartlarını takip edin
# Black formatter kullanın
# Type hints ekleyin

from typing import List, Optional
from django.db import models

class Player(models.Model):
    """Oyuncu modeli."""
    
    username: str = models.CharField(max_length=100)
    email: str = models.EmailField()
    is_active: bool = models.BooleanField(default=True)
    
    def get_full_name(self) -> str:
        """Oyuncunun tam adını döndürür."""
        return f"{self.first_name} {self.last_name}"
```

### TypeScript (Frontend)

```typescript
// ESLint ve Prettier kullanın
// Interface'leri tanımlayın
// Prop types belirtin

interface PlayerProps {
  id: string;
  username: string;
  email: string;
  isActive: boolean;
}

const PlayerCard: React.FC<PlayerProps> = ({ 
  id, 
  username, 
  email, 
  isActive 
}) => {
  return (
    <Box p={4} borderWidth={1} borderRadius="md">
      <Text fontWeight="bold">{username}</Text>
      <Text color="gray.500">{email}</Text>
      <Badge colorScheme={isActive ? 'green' : 'red'}>
        {isActive ? 'Active' : 'Inactive'}
      </Badge>
    </Box>
  );
};
```

### Commit Mesajları

[Conventional Commits](https://conventionalcommits.org/) standardını kullanın:

```bash
# Örnekler
feat: add player analytics dashboard
fix: resolve currency conversion bug
docs: update API documentation
style: format code with prettier
refactor: optimize database queries
test: add unit tests for bonus engine
chore: update dependencies
```

## 🧪 Test Yazma

### Backend Tests

```python
# apps/player_engine/tests.py
from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Player

class PlayerModelTest(TestCase):
    def setUp(self):
        self.player = Player.objects.create(
            username='testplayer',
            email='test@example.com'
        )
    
    def test_player_creation(self):
        self.assertEqual(self.player.username, 'testplayer')
        self.assertTrue(self.player.is_active)

class PlayerAPITest(APITestCase):
    def test_player_list(self):
        response = self.client.get('/api/v1/players/')
        self.assertEqual(response.status_code, 200)
```

### Frontend Tests

```typescript
// __tests__/components/PlayerCard.test.tsx
import { render, screen } from '@testing-library/react';
import { ChakraProvider } from '@chakra-ui/react';
import PlayerCard from '@/components/PlayerCard';

const renderWithChakra = (component: React.ReactElement) => {
  return render(
    <ChakraProvider>
      {component}
    </ChakraProvider>
  );
};

describe('PlayerCard', () => {
  const mockPlayer = {
    id: '1',
    username: 'testplayer',
    email: 'test@example.com',
    isActive: true
  };

  it('renders player information correctly', () => {
    renderWithChakra(<PlayerCard {...mockPlayer} />);
    
    expect(screen.getByText('testplayer')).toBeInTheDocument();
    expect(screen.getByText('test@example.com')).toBeInTheDocument();
    expect(screen.getByText('Active')).toBeInTheDocument();
  });
});
```

## 📚 Dokümantasyon

### API Dokümantasyonu

```python
# views.py
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action

class PlayerViewSet(viewsets.ModelViewSet):
    @extend_schema(
        summary="Oyuncu analizi",
        description="AI destekli oyuncu davranış analizi yapar",
        responses={200: PlayerAnalysisSerializer}
    )
    @action(detail=True, methods=['post'])
    def analyze(self, request, pk=None):
        """Oyuncu davranış analizi yapar."""
        pass
```

### README Güncellemeleri

Yeni özellik eklediğinizde README.md dosyasını güncellemeyi unutmayın:

- Kurulum adımlarını güncelleyin
- Yeni API endpoint'lerini ekleyin
- Örnekleri güncelleyin

## 🏷️ Versiyonlama

[Semantic Versioning](https://semver.org/) kullanıyoruz:

- **MAJOR:** Kırıcı değişiklikler
- **MINOR:** Yeni özellikler (geriye uyumlu)
- **PATCH:** Hata düzeltmeleri

## 🎯 Öncelikli Alanlar

Katkıda bulunabileceğiniz öncelikli alanlar:

### 🤖 AI Modülleri
- Player behavior analysis
- Bonus optimization algorithms
- Risk assessment models
- Marketing automation

### 🌍 Internationalization
- Yeni dil desteği
- Çeviri iyileştirmeleri
- Yerel kültür adaptasyonları

### 🔌 API Entegrasyonları
- Yeni iGaming provider entegrasyonları
- Payment gateway entegrasyonları
- Third-party service entegrasyonları

### 📊 Analytics & Reporting
- Dashboard geliştirmeleri
- Yeni metrikler
- Görselleştirme iyileştirmeleri

### 🧪 Testing
- Unit test coverage artırma
- Integration test yazma
- E2E test senaryoları

## 🆘 Yardım Alma

Takıldığınız bir yer varsa:

1. **Documentation:** [DEVELOPMENT.md](DEVELOPMENT.md) dosyasını kontrol edin
2. **Issues:** Mevcut issue'ları arayın
3. **Discussions:** GitHub Discussions'da soru sorun
4. **Discord:** [Discord sunucumuza](https://discord.gg/sasko-io) katılın

## 🏆 Katkıda Bulunanlar

Tüm katkıda bulunanlara teşekkür ederiz! Katkılarınız [Contributors](https://github.com/sasko-io/sasko-platform/graphs/contributors) sayfasında görüntülenir.

### Hall of Fame

Özel katkıları olan geliştiriciler:

- 🥇 **Top Contributor:** En çok commit yapan
- 🐛 **Bug Hunter:** En çok hata bulan
- 📚 **Documentation Master:** En çok dokümantasyon katkısı yapan
- 🧪 **Test Champion:** En çok test yazan
- 🌍 **Globalization Hero:** En çok çeviri katkısı yapan

## 📞 İletişim

- **Email:** dev@sasko.io
- **Discord:** https://discord.gg/sasko-io
- **Twitter:** [@SaskoIO](https://twitter.com/SaskoIO)

---

**Sasko.io ile iGaming'in geleceğini birlikte şekillendirelim! 🎰✨**
