FROM python:3.7-slim

MAINTAINER Jon Daly "jondaly01@gmail.com"

# Install git - temporary
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y python-pip python-dev build-essential libpq-dev libssl-dev libffi-dev

# Working directory is app
COPY . /app
WORKDIR /app

# Environment variables
ENV FLASK_APP brood_backend/autoapp.py

# Install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Upgrade and run when the container launches
CMD ["python3", "-m", "brood_backend"]
