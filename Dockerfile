FROM ubuntu:18.04

#MAINTANER Your Name "alvarolandaluce@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev


COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip3 install -r requirements.txt

#COPY ./requirements.txt /app/requirements.txt

WORKDIR /weather_app

#RUN pip install -r requirements.txt

COPY . /weather_app

ENTRYPOINT [ "python" ]

CMD app.py