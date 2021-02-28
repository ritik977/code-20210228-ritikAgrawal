FROM FROM python:alpine AS base
WORKDIR /app
USER root
SHELL ["/bin/bash", "-c"]
MAINTAINER Ritik
RUN pip install -r requirements.txt
RUN CMD ["python","bmi_index"]