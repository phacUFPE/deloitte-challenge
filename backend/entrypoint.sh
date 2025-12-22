#!/bin/sh

set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Seeding products..."
python manage.py seed_products --total 100 || true

echo "Starting Gunicorn..."
exec gunicorn products.wsgi:application --bind 0.0.0.0:8000