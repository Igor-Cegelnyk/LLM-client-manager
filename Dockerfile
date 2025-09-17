FROM python:3.11-slim

ARG APP_CONFIG__RUN__HOST
ARG APP_CONFIG__RUN__PORT

ENV POETRY_VERSION=1.8.0

RUN pip install poetry==${POETRY_VERSION}

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry install --no-root --only main

COPY ./app ./app

CMD ["sh","-c", "poetry run uvicorn app.main:main_app --host $APP_CONFIG__RUN__HOST --port $APP_CONFIG__RUN__PORT"]