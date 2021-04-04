#image name | who is editing it
FROM python:3.9.1-alpine
LABEL maintainer="King Dark"

#environment var
ENV PYTHONUNBUFFERED 1

#upgraded pip to latest version for less issues
RUN /usr/local/bin/python -m pip install --upgrade pip

#forcing pip to install app dep
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

RUN pip install -r requirements.txt

RUN apk del .tmp-build-deps
#creating app main folder
RUN mkdir /app
WORKDIR /app
COPY ./app /app


#running app with a non root user
RUN addgroup -S appgroup && adduser -D appuser -G appgroup

USER appuser
