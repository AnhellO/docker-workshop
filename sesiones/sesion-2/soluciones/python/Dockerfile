FROM python:3

LABEL maintainer="AnhellO"

WORKDIR /usr/src/app
COPY find.py .
COPY populate.py .

RUN pip install pymongo

CMD python ./populate.py ; python ./find.py