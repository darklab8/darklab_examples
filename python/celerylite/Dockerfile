FROM python:3.10.5-slim-buster as base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /code

FROM base as dep-venv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY requirements.txt constraints.txt ./
RUN pip install -r requirements.txt -c constraints.txt


RUN mkdir -p /code/data
COPY app.py app.py