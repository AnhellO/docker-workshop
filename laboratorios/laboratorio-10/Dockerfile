FROM postgres:12

LABEL maintainer="angel.jaime@example.com"

ENV POSTGRES_DB random_cats
ENV POSTGRES_USER the_cat
ENV POSTGRES_PASSWORD secretcat123

EXPOSE 5432

COPY init.sql /docker-entrypoint-initdb.d/