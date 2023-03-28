FROM python:3.11.2-slim

ENV APP_HOME=/home/wss

WORKDIR $APP_HOME

COPY requirements.txt $APP_HOME/

RUN pip install --upgrade pip \
    pip install --no-cache-dir -r $APP_HOME/requirements.txt
