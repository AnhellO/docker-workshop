FROM python:3

WORKDIR /usr/src
RUN git clone https://github.com/joaoventura/flask-static-site.git
RUN pip install --no-cache-dir -r flask-static-site/requirements.txt

EXPOSE 8000

CMD [ "python", "flask-static-site/site.py" ]