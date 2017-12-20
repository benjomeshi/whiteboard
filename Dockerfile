FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN yum install -y mysql mysql-server

RUN echo "NETWORKING=yes" >> /etc/sysconfig/network
ADD ./setup.sql
RUN /usr/bin/mysql_safe & sleep 10s && cat setup.sql | mysql


