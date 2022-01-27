#FROM python:3.9
FROM python:3.9.10-slim-buster

LABEL creator="Ali Daghlani <alidaghlani@gmail.com>"

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran nginx supervisor

RUN pip3 install uwsgi

COPY ./requirements.txt /project/requirements.txt

RUN pip3 install -r /project/requirements.txt

RUN useradd --no-create-home nginx

RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache

COPY conf/nginx.conf /etc/nginx/
COPY conf/flask.conf /etc/nginx/conf.d/
COPY conf/uwsgi.ini /etc/uwsgi/
COPY conf/supervisord.conf /etc/

COPY . /app

WORKDIR /app

CMD bash /app/run.sh
