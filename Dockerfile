FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
ENV PYTHONPATH=/app/src

EXPOSE 5000
# Serveur de développement Flask : suffisant pour apprendre, pas pour la production.
CMD ["python", "-m", "ticket_ai.api"]
