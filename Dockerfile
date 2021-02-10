FROM python:3.8.5
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000 --timeout 120 --access-logfile '-' --error-logfile '-'
