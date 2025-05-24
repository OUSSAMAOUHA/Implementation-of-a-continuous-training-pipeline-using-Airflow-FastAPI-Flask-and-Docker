# Utilisez une image de base appropriée pour votre application FastAPI
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Copiez le contenu du projet local dans le conteneur
COPY ./ /app

# Installez les dépendances Python nécessaires
RUN pip install --no-cache-dir -r /app/requirements.txt

# Exposez le port sur lequel FastAPI écoute
EXPOSE 80

# Commande pour démarrer l'application FastAPI
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
