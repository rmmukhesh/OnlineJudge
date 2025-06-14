# syntax=docker/dockerfile:1

FROM python:3.11-slim

# 1. Set working directory
WORKDIR /app

# 2. Install OS dependencies
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    build-essential libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# 3. Copy & install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy project code
COPY . .

# 5. Provide build‑time env for collectstatic
ENV DJANGO_SETTINGS_MODULE=my_project.settings
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY="docker-build-secret"
ENV DEBUG="True"
ENV ALLOWED_HOSTS="*"

# 6. Collect static files
RUN python manage.py collectstatic --no-input

# 7. Copy and mark entrypoint
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# 8. Expose port and launch via entrypoint
EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]
