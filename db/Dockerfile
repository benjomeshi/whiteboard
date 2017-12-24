FROM mysql:5.7

COPY init/setup.sh /mysql/setup.sh
COPY init/setup.sql /mysql/setup.sql
RUN /mysql/setup.sh
