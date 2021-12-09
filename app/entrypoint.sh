#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

apt-get install build-essential libssl-dev libffi-dev python-dev
python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate

exec "$@"
