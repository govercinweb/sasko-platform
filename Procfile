release: python manage.py migrate
web: gunicorn sasko.wsgi
worker: celery -A sasko worker --beat --loglevel=info