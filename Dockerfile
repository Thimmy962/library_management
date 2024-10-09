# Start from the official Python slim image
FROM python:3.10-slim

# Disable buffering to ensure logs are immediately visible
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project (including the library_management folder)
COPY requirements.txt /app/

# Install dependencies using the requirements.txt located in /app
RUN pip install -r requirements.txt

COPY . /app/

# Change the working directory to the folder that contains manage.py
WORKDIR /app/


# Expose port 8080 for the application
EXPOSE 8080

# Start the application using Gunicorn
CMD [ "./bash"]