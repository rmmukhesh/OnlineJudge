# syntax=docker/dockerfile:1
FROM python:3.11-slim
WORKDIR /app

# System deps
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
     build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/*

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App code
COPY . .

# Build-time vars so collectstatic won’t crash
ENV DJANGO_SETTINGS_MODULE=my_project.settings \
    SECRET_KEY="docker-build-secret" \
    DEBUG="True" \
    ALLOWED_HOSTS="*"

# Collect static into STATIC_ROOT
RUN python manage.py collectstatic --no-input

# Entrypoint invocation
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]
