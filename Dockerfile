# STEP 1
#FROM python:3.8 AS Base
FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
LABEL creator="Ali Daghlani <alidaghlani@gmail.com>"
ENV PYTHONUNBUFFERED 1
RUN mkdir /Links
WORKDIR /Links
ADD requirements.txt /Links
RUN pip3 install -r requirements.txt

# STEP 2
FROM Base AS Links
ENV TZ="Asia/Tehran"
RUN date
ENV PYTHONUNBUFFERED 1
ADD . /Links
WORKDIR /Links
#VOLUME /Links/config/
#EXPOSE 8003
#EXPOSE 9600
#ENTRYPOINT python app.py
CMD /bin/bash run.sh