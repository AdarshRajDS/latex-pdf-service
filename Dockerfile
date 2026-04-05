FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl \
    && curl -L https://drop-sh.fullyjustified.net | sh \
    && mv tectonic /usr/local/bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv && uv sync

COPY . .

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]