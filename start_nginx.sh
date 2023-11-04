#!/bin/bash

# Execute the migration and save all the static files
python manage.py migrate --no-input

python manage.py collectstatic --no-input --clear
