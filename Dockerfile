# Docker configuration for backend development. Not created for production use.
# It does not include front-end .
# Main production build is done using Dockerfile in the root of the project
FROM python:3.10-bullseye

WORKDIR /code
ADD requirements.txt /code/
RUN python -V && pip install --upgrade pip && pip install -r requirements.txt
ADD . /code