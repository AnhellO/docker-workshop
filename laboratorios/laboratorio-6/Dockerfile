FROM golang:1.15

LABEL maintainer="AnhellO"

RUN go get -u -v go.mongodb.org/mongo-driver/bson
RUN go get -u -v go.mongodb.org/mongo-driver/bson/primitive
RUN go get -u -v go.mongodb.org/mongo-driver/mongo
RUN go get -u -v go.mongodb.org/mongo-driver/mongo/options
RUN go get -u -v go.mongodb.org/mongo-driver/mongo/readpref

# Primero inserta en la DB
COPY populate/main.go /usr/src/app/populate/
WORKDIR /usr/src/app/populate/
RUN go build -o /usr/src/app/bin/populate .

# Luego busca en la DB
COPY find/main.go /usr/src/app/find/
WORKDIR /usr/src/app/find/
RUN go build -o /usr/src/app/bin/find .

# Vamos al directorio de los binarios
WORKDIR /usr/src/app/bin

CMD ./populate ; ./find