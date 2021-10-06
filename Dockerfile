FROM python:3.9

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app
COPY exercise_files /app/exercise_files

COPY mycode /app/mycode

RUN pip install -r requirements.txt
