FROM golang:1.15

LABEL maintainer="AnhellO"

WORKDIR /usr/src/app
ADD find.go /usr/src/app
ADD populate.go /usr/src/app

RUN go get -u -v go.mongodb.org/mongo-driver/bson
RUN go get -u -v go.mongodb.org/mongo-driver/bson/primitive
RUN go get -u -v go.mongodb.org/mongo-driver/mongo
RUN go get -u -v go.mongodb.org/mongo-driver/mongo/options
RUN go get -u -v go.mongodb.org/mongo-driver/mongo/readpref
RUN go build -o ./bin/mongo

CMD ./bin/mongo