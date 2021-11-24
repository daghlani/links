FROM tiangolo/uwsgi-nginx-flask:latest
LABEL creator="Ali Daghlani <alidaghlani@gmail.com>"
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . /app