# random_app
#
# VERSION               0.0.1

FROM      ubuntu
MAINTAINER Eli qiao <taget@163.com>

LABEL Description="Base image run randmo app" Vendor="Eli's BOOK" Version="1.0"
RUN apt-get update && apt-get install python-pip python-flask python-jsonschema python-redis -y
RUN pip install python-memcached
RUN pip install logging

# this is log file
RUN touch /random-debug.log

ADD run.py /run.py
ADD run.sh /run.sh
ADD app/ /app/

EXPOSE 5001

ENTRYPOINT ["bash", "/run.sh"]
