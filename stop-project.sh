#!/bin/bash

# Sasko.io Project Stop Script
# AI-Powered iGaming SaaS Platform

echo "🛑 Stopping Sasko.io Platform..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

# Stop all Node.js processes (Next.js)
print_status "Stopping Next.js frontend..."
pkill -f "next dev" 2>/dev/null || true

# Stop all Python processes (Django)
print_status "Stopping Django backend..."
pkill -f "manage.py runserver" 2>/dev/null || true

# Stop Celery workers
print_status "Stopping Celery workers..."
pkill -f "celery.*worker" 2>/dev/null || true

# Stop Docker containers
print_status "Stopping Docker containers..."
docker-compose down

print_status "All Sasko.io services stopped successfully!"
