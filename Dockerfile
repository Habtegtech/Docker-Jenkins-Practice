# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the dependencies in the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 (the default port for Flask)
EXPOSE 5000

# Run the application when the container launches
CMD ["python", "app.py"]
