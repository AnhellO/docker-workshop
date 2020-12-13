FROM python:3

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

RUN export FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]