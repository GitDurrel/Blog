
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Commande de démarrage du serveur Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog_api.wsgi:application"]
