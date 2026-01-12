# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy all files to container
COPY . .

# Command to run Python file
CMD ["python", "feedback_system.py"]
