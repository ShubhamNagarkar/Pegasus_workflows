#Download base Ubuntu image
FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y \
  python3-pip \
  python3
  
RUN pip3 install --upgrade pip

RUN pip3 install emoji

WORKDIR /usr/bin

COPY add_thumbs_up.py .
RUN chmod a+x add_thumbs_up.py

