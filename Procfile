release: python manage.py migrate
web: gunicorn storefront.wsgi:application
worker: celery -A storefront worker