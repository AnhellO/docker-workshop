FROM python:3

WORKDIR /usr/src/app

COPY app.py /usr/src/app
COPY templates /usr/src/app/templates
COPY requirements.txt /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "./app.py"]