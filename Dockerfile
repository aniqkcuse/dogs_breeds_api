FROM python:3.11.6-slim-bookworm

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x /app/start.sh

ENTRYPOINT ["/app/start.sh"]
