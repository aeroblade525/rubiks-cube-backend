FROM python:3.11-slim

WORKDIR /app

# Install deps first so Docker caches this layer when only code changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the actual app code
COPY app/ ./app/
COPY algorithms/ ./algorithms/
COPY PythonMain.py .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]