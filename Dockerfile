# Use Python 3.12 slim image
FROM python:3.12-slim

# Prevent Python from buffering stdout/stderr (helpful for logs)
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /code

# Copy and install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all your code into the container
COPY . /code

# Expose Django's default port
EXPOSE 8000

# Default command to run the server (dev)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
