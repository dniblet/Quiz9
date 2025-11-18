
FROM python:3.12-slim

WORKDIR /home

COPY analyzer.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY test_analyzer.py .

CMD ["pytest", "-q"]
