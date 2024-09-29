FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /library_management .

COPY library_management /app/library_management

WORKDIR /app/library_management

RUN python3 manage.py makemigrations lib
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py create_grps

EXPOSE 8080

CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "library_management.wsgi:application" ]
