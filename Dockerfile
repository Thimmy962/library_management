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

# Expose port 8080 for the application
EXPOSE 8080

# Start the application using Gunicorn
# CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "library_management.wsgi:application" ]
CMD ["./start.sh"]