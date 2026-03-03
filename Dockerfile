FROM python:3.11-slim

# Install system dependencies required by WeasyPrint(deployment)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libcairo2 \
    libgdk-pixbuf-2.0-0 \
    libffi-dev \
    libxml2 \
    libxslt1.1 \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 10000

# Run with gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]

