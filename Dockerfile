FROM python:3.8
USER root

ADD Pipfile.lock /code/Pipfile.lock
ADD Pipfile /code/Pipfile

ARG APP_VERSION=0
ENV PYTHONUNBUFFERED 1
WORKDIR /code/

RUN pip install pipenv --no-cache-dir \
    && env PIP_NO_CACHE_DIR=1 \
    && env PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

COPY . /code/.

EXPOSE 8081

CMD ["pipenv", "run", "python", "src/rest/applications/aiogram/application.py"]
