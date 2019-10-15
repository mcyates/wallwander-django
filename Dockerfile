FROM python:3.7

WORKDIR /app

RUN pip install pipenv
COPY Pipfile Pipfile.lock .env ./
RUN pipenv install --system

COPY ./ ./
