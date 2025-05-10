FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir python-dotenv

ENV AUTHOR=${AUTHOR} \
    PORT=${PORT} 

EXPOSE ${PORT}
CMD ["python", "server/server.py"]