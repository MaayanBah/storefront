release: python manage.py migrate
web: gunicorn storefront.wsg
worker: celery -A storefront worker