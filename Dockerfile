FROM python:3.9

# install packages
RUN apt-get update && \
    apt-get install -y curl \
    wget \
    openjdk-11-jdk

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

RUN export JAVA_HOME

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app
COPY exercise_files /app/exercise_files

COPY mycode /app/mycode

RUN pip install -r requirements.txt
