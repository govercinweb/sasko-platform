# GitHub'ta Sasko.io Repository Kurulum Rehberi

🎰 **AI-Powered iGaming SaaS Platform**

Bu rehber, Sasko.io projesini GitHub'ta yayınlamak için gerekli adımları açıklar.

## 🚀 Hızlı Kurulum

### 1. GitHub Repository Oluşturma

1. [GitHub](https://github.com) hesabınıza giriş yapın
2. "New repository" butonuna tıklayın
3. Repository bilgilerini doldurun:
   - **Repository name:** `sasko-platform`
   - **Description:** `🎰 AI-Powered iGaming SaaS Platform - Mikroservis mimarisi ile çoklu dil ve para birimi desteği`
   - **Visibility:** Public (veya Private)
   - **Initialize:** Hiçbir şeyi işaretlemeyin (README, .gitignore, license)

### 2. Local Repository'yi GitHub'a Bağlama

```bash
# Mevcut dizinde olduğunuzdan emin olun
cd /home/ubuntu/sasko-io

# GitHub repository'sini remote olarak ekleyin
git remote add origin https://github.com/KULLANICI_ADINIZ/sasko-platform.git

# Ana branch'i push edin
git push -u origin main
```

### 3. Repository Ayarları

#### Branch Protection Rules

1. Repository → Settings → Branches
2. "Add rule" butonuna tıklayın
3. Branch name pattern: `main`
4. Aşağıdaki seçenekleri işaretleyin:
   - ✅ Require a pull request before merging
   - ✅ Require status checks to pass before merging
   - ✅ Require branches to be up to date before merging
   - ✅ Restrict pushes that create files larger than 100MB

#### Secrets Ekleme

1. Repository → Settings → Secrets and variables → Actions
2. "New repository secret" butonuna tıklayın
3. Aşağıdaki secret'ları ekleyin:

```
DOCKERHUB_USERNAME=your-dockerhub-username
DOCKERHUB_TOKEN=your-dockerhub-access-token
SONAR_TOKEN=your-sonarcloud-token
```

#### Labels Oluşturma

1. Repository → Issues → Labels
2. Aşağıdaki label'ları oluşturun:

| Label | Color | Description |
|-------|-------|-------------|
| `bug` | `#d73a4a` | Hata bildirimi |
| `enhancement` | `#a2eeef` | Yeni özellik |
| `documentation` | `#0075ca` | Dokümantasyon |
| `good first issue` | `#7057ff` | Yeni başlayanlar için |
| `help wanted` | `#008672` | Yardım aranıyor |
| `priority: high` | `#ff6b6b` | Yüksek öncelik |
| `priority: medium` | `#ffa726` | Orta öncelik |
| `priority: low` | `#66bb6a` | Düşük öncelik |
| `module: player-engine` | `#e1f5fe` | Player Engine modülü |
| `module: bonus-engine` | `#f3e5f5` | Bonus Engine modülü |
| `module: ai` | `#fff3e0` | AI modülleri |
| `frontend` | `#e8f5e8` | Frontend değişiklikleri |
| `backend` | `#fff8e1` | Backend değişiklikleri |

## 🔧 CI/CD Kurulumu

### GitHub Actions

CI/CD pipeline otomatik olarak çalışacak. İlk push'tan sonra:

1. Repository → Actions sekmesine gidin
2. Workflow'ların çalıştığını kontrol edin
3. Hata varsa logs'ları inceleyin

### SonarCloud Entegrasyonu

1. [SonarCloud](https://sonarcloud.io) hesabı oluşturun
2. GitHub hesabınızla bağlayın
3. Repository'yi import edin
4. Token'ı GitHub Secrets'a ekleyin

### Docker Hub Entegrasyonu

1. [Docker Hub](https://hub.docker.com) hesabı oluşturun
2. Access token oluşturun
3. Token'ı GitHub Secrets'a ekleyin

## 📋 Repository Yönetimi

### Issue Templates

Aşağıdaki issue template'leri otomatik olarak eklendi:
- 🐛 Bug Report
- ✨ Feature Request

### Pull Request Template

PR template'i otomatik olarak eklendi ve aşağıdaki kontrolleri içerir:
- Değişiklik türü
- Test durumu
- Code review checklist
- Deployment notları

### Branch Strategy

```
main (production)
├── develop (development)
├── feature/player-analytics
├── feature/bonus-optimization
├── hotfix/security-patch
└── release/v1.1.0
```

## 🌟 Repository Özelleştirme

### About Section

1. Repository ana sayfasında ⚙️ (Settings) butonuna tıklayın
2. About section'ı düzenleyin:
   - **Description:** `🎰 AI-Powered iGaming SaaS Platform with microservices architecture`
   - **Website:** `https://sasko.io`
   - **Topics:** `igaming`, `saas`, `ai`, `microservices`, `django`, `nextjs`, `casino`, `sportsbook`

### README Badges

README.md dosyasına aşağıdaki badge'leri ekleyin:

```markdown
[![CI/CD](https://github.com/KULLANICI_ADINIZ/sasko-platform/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/KULLANICI_ADINIZ/sasko-platform/actions)
[![codecov](https://codecov.io/gh/KULLANICI_ADINIZ/sasko-platform/branch/main/graph/badge.svg)](https://codecov.io/gh/KULLANICI_ADINIZ/sasko-platform)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=sasko-platform&metric=alert_status)](https://sonarcloud.io/dashboard?id=sasko-platform)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Node.js](https://img.shields.io/badge/node.js-18+-green.svg)](https://nodejs.org/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
```

### Social Preview

1. Repository → Settings → General
2. Social preview section'da "Upload an image" butonuna tıklayın
3. Sasko.io logo'sunu veya proje görselini yükleyin

## 🤝 Community Features

### Discussions

1. Repository → Settings → General
2. Features section'da "Discussions" seçeneğini aktif edin
3. Kategoriler oluşturun:
   - 💡 Ideas
   - 🙋 Q&A
   - 📢 Announcements
   - 🗣️ General

### Wiki

1. Repository → Settings → General
2. Features section'da "Wikis" seçeneğini aktif edin
3. İlk wiki sayfasını oluşturun

### Projects

1. Repository → Projects → "New project"
2. Template: "Team backlog"
3. Proje adı: "Sasko.io Development"

## 📊 Analytics ve Monitoring

### GitHub Insights

1. Repository → Insights sekmesine gidin
2. Aşağıdaki metrikleri takip edin:
   - Contributors
   - Commits
   - Code frequency
   - Dependency graph
   - Network

### Release Management

```bash
# Yeni release oluşturma
git tag -a v1.0.0 -m "Initial release of Sasko.io platform"
git push origin v1.0.0
```

1. Repository → Releases → "Create a new release"
2. Tag version: `v1.0.0`
3. Release title: `🎰 Sasko.io v1.0.0 - Initial Release`
4. Release notes'u otomatik generate edin

## 🔒 Security

### Security Policy

1. Repository → Security → "Security policy"
2. SECURITY.md dosyası oluşturun
3. Vulnerability reporting process'ini tanımlayın

### Dependabot

1. Repository → Settings → Security & analysis
2. "Dependabot alerts" ve "Dependabot security updates" seçeneklerini aktif edin

### Code Scanning

1. Repository → Security → "Code scanning alerts"
2. "Set up code scanning" butonuna tıklayın
3. CodeQL analysis'i aktif edin

## 📈 Marketing ve Visibility

### GitHub Topics

Repository'ye aşağıdaki topic'leri ekleyin:
- `igaming`
- `saas`
- `ai`
- `microservices`
- `django`
- `nextjs`
- `casino`
- `sportsbook`
- `typescript`
- `python`
- `docker`
- `kubernetes`

### Star History

Repository'yi star'layarak visibility'sini artırın ve arkadaşlarınızı da star'lamaya teşvik edin.

## 🎯 Next Steps

1. **Documentation:** Wiki sayfalarını doldurun
2. **Community:** Discord sunucusu oluşturun
3. **Website:** GitHub Pages ile dokümantasyon sitesi oluşturun
4. **Package:** PyPI ve NPM'e paket olarak yayınlayın
5. **Showcase:** GitHub'ın "Explore" sekmesinde görünmek için trending'e girmeye çalışın

## 📞 Destek

Kurulum sırasında sorun yaşarsanız:
- GitHub Issues'da soru sorun
- Discord sunucumuza katılın
- Email: dev@sasko.io

---

**Sasko.io ile iGaming'in geleceğini GitHub'ta paylaşın! 🎰✨**
