FROM ubuntu:16.04

RUN apt update -y && apt install -y \
  apache2

RUN a2enmod cgi

COPY ./html/ /var/www/html/
COPY ./desafio.cgi /usr/lib/cgi-bin/

CMD ["-D", "FOREGROUND"]
ENTRYPOINT ["apachectl"]