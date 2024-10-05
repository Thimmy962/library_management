# Start from the official Python slim image
FROM python:3.10-slim

# Disable buffering to ensure logs are immediately visible
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project (including the library_management folder)
COPY . /app/

# Install dependencies using the requirements.txt located in /app
RUN pip install -r requirements.txt

# Change the working directory to the folder that contains manage.py
WORKDIR /app/library_management


# Expose port 8080 for the application
EXPOSE 8080

# Start the application using Gunicorn
CMD [ "./bash"]