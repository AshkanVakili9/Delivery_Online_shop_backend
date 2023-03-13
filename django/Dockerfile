FROM python:3.8-slim-buster
LABEL maintainer="NoobstrGTR"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /backend
WORKDIR /backend

COPY req.txt req.txt
RUN pip install -r req.txt && \
    pip install --upgrade pip 