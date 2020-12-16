# Choose the base image
FROM python:3.7-alpine

# Anyone can be a MAINTAINER
MAINTAINER George Brian Busila

# When running in a container this avoids lots of complication
ENV PYTHONUNBUFFERED 1


# This copies the req file to the docker image root directory
COPY ./requirements.txt /requirements.txt
# Run pip on the image to install anything we put in the requirements.txt file
RUN pip install -r /requirements.txt

# Create a directory in the docker image to save the app source code
# It switches to the directory on the docker container
# It copies our code to the working dir :)
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Create a user that is going to run the app using docker and switch to the user
# -D means we add a user that is going to be used soley for running apps
# Security purposes
# Not running as root
RUN adduser -D user
USER user
