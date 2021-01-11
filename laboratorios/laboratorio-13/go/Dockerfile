FROM golang:1.15

LABEL maintainer="AnhellO"

RUN go get -u -v github.com/streadway/amqp

WORKDIR /usr/src/app

COPY ./app .