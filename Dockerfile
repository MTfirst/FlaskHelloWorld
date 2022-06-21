FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN mkdir /src

WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./src /src
WORKDIR /src