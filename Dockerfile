FROM python:3.11-slim

# Install system dependencies (IMPORTANT)
RUN apt-get update && apt-get install -y \
    curl \
    libgraphite2-3 \
    && rm -rf /var/lib/apt/lists/*

# Install tectonic
RUN curl -L https://drop-sh.fullyjustified.net | sh \
    && mv tectonic /usr/local/bin/

WORKDIR /app

COPY . .

# Install Python deps
RUN pip install --no-cache-dir fastapi uvicorn pydantic pydantic-settings

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]