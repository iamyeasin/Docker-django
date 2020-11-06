#pull base image
FROM python:3.7

#Set Environment Variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# SET WORKING DIR
WORKDIR /BOOKSTORE_PROJECT/

#install Dependencies
COPY Pipfile Pipfile.lock /BOOKSTORE_PROJECT/
run pip install pipenv && pipenv install --system

#copy project

COPY . /BOOKSTORE_PROJECT/



