#!/bin/bash

# Sasko.io Project Startup Script
# AI-Powered iGaming SaaS Platform

echo "🎰 Sasko.io - AI-Powered iGaming SaaS Platform"
echo "=============================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}$1${NC}"
}

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    print_error "Docker is not running. Please start Docker first."
    exit 1
fi

print_header "🐳 Starting Infrastructure Services..."

# Start infrastructure services
docker-compose up -d postgres redis rabbitmq elasticsearch

print_status "Waiting for services to be ready..."
sleep 10

print_header "🔧 Setting up Backend..."

# Backend setup
cd backend

# Activate virtual environment
if [ ! -d "venv" ]; then
    print_status "Creating Python virtual environment..."
    python3.11 -m venv venv
fi

source venv/bin/activate

# Install Python dependencies
print_status "Installing Python dependencies..."
pip install -r requirements.txt

# Run migrations
print_status "Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser if it doesn't exist
print_status "Creating superuser (if needed)..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@sasko.io', 'admin123')" | python manage.py shell

# Load initial data
print_status "Loading initial data..."
python manage.py loaddata fixtures/currencies.json 2>/dev/null || echo "Currency fixtures not found, skipping..."
python manage.py loaddata fixtures/languages.json 2>/dev/null || echo "Language fixtures not found, skipping..."

cd ..

print_header "⚛️ Setting up Frontend..."

# Frontend setup
cd frontend/sasko-frontend

# Install Node.js dependencies
print_status "Installing Node.js dependencies..."
npm install

cd ../..

print_header "🚀 Starting Development Servers..."

# Start backend in background
print_status "Starting Django backend server..."
cd backend
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000 &
BACKEND_PID=$!
cd ..

# Start frontend in background
print_status "Starting Next.js frontend server..."
cd frontend/sasko-frontend
npm run dev &
FRONTEND_PID=$!
cd ../..

# Start Celery worker
print_status "Starting Celery worker..."
cd backend
source venv/bin/activate
celery -A sasko_core worker -l info &
CELERY_PID=$!
cd ..

print_header "✅ Sasko.io Platform Started Successfully!"
echo ""
echo "🌐 Services:"
echo "   Frontend:  http://localhost:3000"
echo "   Backend:   http://localhost:8000"
echo "   Admin:     http://localhost:8000/admin (admin/admin123)"
echo "   API Docs:  http://localhost:8000/api/docs/"
echo ""
echo "🔧 Infrastructure:"
echo "   PostgreSQL: localhost:5432"
echo "   Redis:      localhost:6379"
echo "   RabbitMQ:   localhost:15672 (sasko_rabbit/rabbit_password_2024)"
echo ""
echo "📊 Monitoring:"
echo "   Grafana:    http://localhost:3001 (admin/sasko_grafana_2024)"
echo "   Prometheus: http://localhost:9090"
echo ""
echo "🛑 To stop all services, run: ./stop-project.sh"
echo ""

# Function to cleanup on exit
cleanup() {
    print_header "🛑 Stopping Sasko.io Platform..."
    kill $BACKEND_PID $FRONTEND_PID $CELERY_PID 2>/dev/null
    docker-compose down
    print_status "All services stopped."
}

# Set trap to cleanup on script exit
trap cleanup EXIT

# Wait for user input to stop
print_status "Press Ctrl+C to stop all services..."
wait
