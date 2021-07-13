# syntax=docker/dockerfile:1
FROM python:3.9.6-slim-buster

ENV http_proxy http://10.81.108.98:3128
ENV https_proxy http://10.81.108.98:3128

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app/