FROM python:3.10-slim

WORKDIR /library_management

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /library_management .

RUN cd /library_management

RUN ls

RUN python3 manage.py makemigrations lib

RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py create_grps

EXPOSE 8080

CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "library_management.wsgi:application" ]