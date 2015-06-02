# random_app
#
# VERSION               0.0.1

FROM      ubuntu
MAINTAINER Eli qiao <taget@163.com>

LABEL Description="This image is used to start the foobar executable" Vendor="ACME Products" Version="1.0"
RUN apt-get update && apt-get install python-pip python-flask -y
RUN pip install python-memcached

EXPOSE 5001
