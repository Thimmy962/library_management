# FROM python:3.10-slim

# ENV PYTHONUNBUFFERED=1

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install -r requirements.txt

# COPY /library_management .

# COPY library_management /app/library_management

# WORKDIR /app/library_management

# RUN python3 manage.py makemigrations lib
# RUN python3 manage.py migrate
# RUN python3 manage.py collectstatic --noinput
# RUN python3 manage.py create_grps

# EXPOSE 8080

# CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "library_management.wsgi:application" ]



# Start from the official Python slim image
FROM python:3.10-slim

# Disable buffering to ensure logs are immediately visible
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the entire source code (including requirements.txt)
COPY . /app/

# Install dependencies using the copied requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run Django management commands for migrations, static files, etc.
RUN python3 manage.py makemigrations lib && \
    python3 manage.py migrate && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py create_grps

# Expose port 8080 for the application
EXPOSE 8080

# Start the application using Gunicorn
CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "library_management.wsgi:application" ]
