FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV STATIC_INDEX 1

COPY requirements.txt /pip/requirements.txt
RUN pip install -r /pip/requirements.txt
