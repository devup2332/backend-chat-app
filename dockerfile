FROM python:3.9.5

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .