# Use a Python base image
FROM python:3.7

# Set the working directory in the container
WORKDIR /app

# Create the directory for serverdata with write permissions
RUN mkdir -p /serverdata && chmod 777 /serverdata

# Copy the Python script into the container
COPY app/text_gen.py .

# Run the Python script when the container starts
CMD ["python", "text_gen.py"]
