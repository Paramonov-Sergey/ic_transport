FROM python:3.9

# Set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y libpq-dev gcc python3-dev libffi-dev libblas-dev liblapack-dev libatlas-base-dev gfortran postgresql postgresql-client

# Install dependencies
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN  pip install -r requirements.txt

# Copy project
COPY . /app

RUN chmod a+x docker/*.sh
