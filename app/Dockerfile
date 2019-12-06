FROM python:3.7

RUN pip install flask==1.1.1 psycopg2

ADD . /app

EXPOSE 5000

WORKDIR /app

ENV FLASK_APP=equipe.py
ENV FLASK_DEBUG=1

CMD ["flask", "run", "--host=0.0.0.0"]
