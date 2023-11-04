#!/bin/bash

# Verifying if the database start

if [ "$DATABASE" = "postgres" ]
then
	echo "Waiting for postgres..."

	while ! nc -z $DB_HOST $DB_PORT; do
		sleep 0.1
	done

	echo "PostgreSQL started"
fi

echo "$@"

gunicorn main.wsgi:application --bind 0.0.0.0:8000
