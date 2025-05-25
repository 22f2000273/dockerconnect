FROM docker.io/python:3.12-slim
WORKDIR /app
COPY req.txt .
RUN pip install --no-cache-dir -r req.txt
COPY . .

CMD ["python3", "app.py"]
