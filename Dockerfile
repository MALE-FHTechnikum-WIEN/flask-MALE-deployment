# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /flask-app

# Copy requirements.txt to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY /flask-app .

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run your application
CMD ["python", "main.py"]
