# bot/Dockerfile
FROM python:3.9-slim

WORKDIR /bot

COPY . .

RUN pip install --no-cache-dir aiogram requests

CMD ["python", "bot.py"]
