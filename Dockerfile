FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1 # environment variable
RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt