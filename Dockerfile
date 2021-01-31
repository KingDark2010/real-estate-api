#image name | who is editing it
FROM python:3.9.1-alpine
LABEL maintainer="King Dark"

#environment var
ENV PYTHONUNBUFFERED 1

#upgraded pip to latest version for less issues
RUN /usr/local/bin/python -m pip install --upgrade pip

#forcing pip to install app dep
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

#creating app main folder
RUN mkdir /app
WORKDIR /app
COPY ./app /app


#running app with a non root user
RUN addgroup -S appgroup && adduser -D appuser -G appgroup

USER appuser
