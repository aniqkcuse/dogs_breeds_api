#!/bin/bash
echo "Creating migrations"
python manage.py makemigrations
echo "-----------------------"

echo "Starting migrations"
python manage.py migrate
echo "-----------------------"

echo "Starting server"
python manage.py runserver 0.0.0.0:8000
echo "-----------------------"

echo "Running testing"
pytest
echo "-----------------------"
