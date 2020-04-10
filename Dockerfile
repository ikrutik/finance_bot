FROM python:3.8
RUN groupadd deploy && useradd -g deploy deploy

RUN pip install pipenv --no-cache-dir \
    && env PIP_NO_CACHE_DIR=1 pipenv install --deploy --verbose
