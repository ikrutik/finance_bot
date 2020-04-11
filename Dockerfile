FROM python:3.8

ARG PORT=8081
ENV PYTHONPATH /usr/src/app

WORKDIR $PYTHONPATH

COPY . .
RUN mkdir logs

RUN pip install pipenv --no-cache-dir \
    && env PIP_NO_CACHE_DIR=1 pipenv install --deploy --verbose

ENV PYTHONUNBUFFERED 1

EXPOSE $PORT

CMD ["pipenv", "run", "python", "src/rest/applications/aiogram/application.py", "--mode=webhook"]
