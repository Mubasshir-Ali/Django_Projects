python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn AI_ALIENEER.wsgi:application --bind 0.0.0.0:8000

#!/bin/sh

# python manage.py migrate --no-input
# python manage.py collectstatic --no-input

# gunicorn django_project.wsgi:application --bind 0.0.0.0:8000

