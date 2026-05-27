FROM python:3.11-slim

# Enforce stable, unbuffered console logs for easy debugging inside Jelastic logs
ENV PYTHONUNBUFFERED=1

# Install system layout engines required strictly by WeasyPrint 68+
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libharfbuzz0b \
    gobject-introspection \
    libffi-dev \
    libjpeg-dev \
    libopenjp2-7-dev \
    shared-mime-info \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Optimize layer caching by installing dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the modern FastAPI application structure
COPY . .

# Expose port 8080 (standard, highly reliable port mapping on Jelastic)
EXPOSE 8080

# Spin up the Uvicorn engine pointing to your actual main entrypoint
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]