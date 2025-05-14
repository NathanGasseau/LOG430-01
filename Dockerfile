FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ ./src/
COPY tests/ ./tests/

CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q"]