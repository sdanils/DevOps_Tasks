FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install python-dotenv

ENV AUTHOR=${AUTHOR} \
    PORT=${PORT} 

EXPOSE ${PORT}
CMD ["python", "server.py"]