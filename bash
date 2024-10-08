#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Run Django management commands for migrations and static files
python manage.py makemigrations lib --noinput
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py create_grps

# Start Gunicorn server
gunicorn --bind 0.0.0.0:8080 library_management.wsgi:application
