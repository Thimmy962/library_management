# Start from the official Python slim image
FROM python:3.10-slim

# Disable buffering to ensure logs are immediately visible
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project (including the library_management folder)
COPY . /app/

# Install dependencies using the requirements.txt located in /app
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variables (recommended before copying requirements.txt)
ENV SECRET_KEY=$SECRET_KEY
ENV DB_URL=$DB_URL
ENV ALLOWED_HOSTS=$ALLOWED_HOSTS
ENV DEBUG=$DEBUG

# Change the working directory to the folder that contains manage.py
WORKDIR /app/library_management

# Run Django management commands for migrations, static files, etc.
RUN python3 manage.py makemigrations lib && \
  python3 manage.py migrate && \
  python3 manage.py collectstatic --noinput && \
  python3 manage.py create_grps

# Expose port 8080 for the application
EXPOSE 8080

# Start the application using Gunicorn
CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "library_management.wsgi:application" ]