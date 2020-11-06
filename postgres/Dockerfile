#Pull base image
FROM python:3.7


#set environment variable

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set working directory
WORKDIR /postgres/

#install Dependencies
COPY Pipfile Pipfile.lock /postgres/
RUN pip install pipenv && pipenv install --system

#Copy project 
COPY . /postgres/
