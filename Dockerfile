FROM python:3.9-slim-buster

WORKDIR /app

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY . .
CMD uvicorn main:app --host 0.0.0.0 --port $PORT