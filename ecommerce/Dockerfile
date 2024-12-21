# Use an official Python runtime as the base image
FROM python:3.9-slim

# Install build dependencies (gcc, make, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project into the container
COPY . /app/

# Expose the default Django port
EXPOSE 8000

# Set the default command to run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
