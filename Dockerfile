#
# Musixmatch Python library for ETL
# @author Loreto Parisi (loreto at musixmatch dot com)
# Copyright (c) 2020 Musixmatch spa
#

FROM python:3.6.10-slim-buster

MAINTAINER Loreto Parisi loreto@musixmatch.com

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgtk2.0-dev

WORKDIR app

CMD ["bash"]