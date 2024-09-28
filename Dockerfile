FROM python:3.10-slim

WORKDIR /library_management

COPY ./library_management .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python3", "manage.py", "runserver"]