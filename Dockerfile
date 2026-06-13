FROM python:3.11-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install pip, setuptools, wheel first
RUN pip install --upgrade pip setuptools wheel

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code  
COPY backend/ ./backend/

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Start FastAPI
CMD ["python", "-m", "uvicorn", "backend.milestone5_api:app", "--host", "0.0.0.0", "--port", "8000"]
