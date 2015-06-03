# random_app
#
# VERSION               0.0.1

FROM      ubuntu
MAINTAINER Eli qiao <taget@163.com>

LABEL Description="This image is used to start the foobar executable" Vendor="ACME Products" Version="1.0"
RUN apt-get update && apt-get install python-pip python-flask -y
RUN pip install python-memcached

ADD run.py /run.py
ADD app/ /app/

EXPOSE 5001

ENTRYPOINT ["python", "/run.py"]
