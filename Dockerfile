FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y mysql-server
WORKDIR /usr/src/app

COPY . .

RUN /etc/init.d/mysql start && mysql -h localhost -P 3306 -u root
RUN CREATE DATABASE library;
RUN source /usr/src/app/create.sql;
RUN source /usr/src/app/insert.sql;
RUN exit;

RUN python3 -m venv env
RUN source env/bin/activate
RUN pip install -r requirements.txt

EXPOSE 8080
RUN export FLASK_APP=app
CMD ["flask", "run"]