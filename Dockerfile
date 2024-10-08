FROM ubuntu:20.04
RUN apt-get update -y
COPY . /app
COPY ./templates /app/templates
WORKDIR /app
RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip \
    && apt-get install -y mysql-client 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir -p static

EXPOSE 81
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
