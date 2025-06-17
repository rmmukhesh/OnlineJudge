#!/usr/bin/env bash
set -e
python manage.py migrate --no-input
python manage.py collectstatic --no-input
exec gunicorn my_project.wsgi:application --bind 0.0.0.0:8000 --workers 3
