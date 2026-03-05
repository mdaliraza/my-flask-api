# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your local code into the container
COPY . /app

# Install Flask (and requests if your app uses it)
RUN pip install flask requests

# The port your Flask app runs on
EXPOSE 5000

# Command to run your app
CMD ["python", "app.py"]