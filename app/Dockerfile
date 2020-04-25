FROM python:3.8-slim-buster

# for potential C dependencies
# and just as example
RUN apt-get update && apt-get install git gcc g++ -y

COPY . /app
WORKDIR /app

ARG CACHE_DATE
RUN pip install -r requirements.txt
