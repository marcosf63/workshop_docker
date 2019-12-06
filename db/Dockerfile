FROM postgres

ADD ./init.sql /docker-entrypoint-initdb.d/init.sql

VOLUME /var/lib/postgresql/data
