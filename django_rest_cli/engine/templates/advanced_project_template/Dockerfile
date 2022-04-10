FROM python:3-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
RUN mkdir /code/staticfiles

WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

