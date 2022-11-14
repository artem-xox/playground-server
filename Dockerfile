FROM python:3.9-slim

RUN apt-get clean \
    && apt-get -y update \
    && apt-get -y install pip

COPY poetry.lock pyproject.toml ./
RUN pip install poetry
RUN poetry install --no-dev

WORKDIR /opt

COPY ./app ./app/
COPY scripts/run.sh run.sh

EXPOSE 5000

RUN chmod +x ./run.sh
CMD ["./run.sh"]