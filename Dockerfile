FROM python:3.8-slim

WORKDIR /app

COPY api /app

RUN pip install -r requirements.txt

ENV FLASK_APP=server.py
