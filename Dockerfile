FROM python:3.10
WORKDIR .
# Install system dependencies
RUN apt-get update && apt-get install -y libasound2 && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 3333
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3333", "--workers", "1"]