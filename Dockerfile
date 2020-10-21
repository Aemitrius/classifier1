FROM python:3

ENV PYTHONUNBUFFERED 1
WORKDIR /classifier

ADD . /classifier

COPY ./requirements.txt /classifier/requirements.txt

RUN pip install -r requirements.txt

COPY . /classifier