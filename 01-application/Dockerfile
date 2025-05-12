FROM python:3.11-slim

WORKDIR /app
COPY . .

ENV PORT="8000"

EXPOSE ${PORT}

CMD ["python", "server/server.py"]