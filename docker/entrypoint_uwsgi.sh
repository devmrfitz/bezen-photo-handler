#!/bin/bash

set -e

until cd /opt/deploy/bezen
do
    echo "Waiting for server volume..."
done

# Apply database migrations
echo "Waiting for db to be ready..."
# makemigrations is needed only for the durin package.
# The customization of the parameters is not applied until the migration is done
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

echo "------------------------------"
echo "DEBUG: " $DEBUG
echo "DJANGO_TEST_SERVER: " $DJANGO_TEST_SERVER
echo "------------------------------"

if [[ $DEBUG == "True" ]] && [[ $DJANGO_TEST_SERVER == "True" ]];
then
    python manage.py runserver 0.0.0.0:80
else
    gunicorn backend.wsgi:application --bind 0.0.0.0:80
fi