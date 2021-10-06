FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3-pip

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app
COPY exercise_files /app/exercise_files

RUN pip install -r requirements.txt
