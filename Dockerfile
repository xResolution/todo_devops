FROM python:3.9-slim

WORKDIR /todo-app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app
COPY templates/ ./app/templates
COPY static/ ./app/static

EXPOSE 5000
CMD ["python", "-m", "app"]