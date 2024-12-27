FROM python:3.12.7-slim

WORKDIR /app

COPY pyproject.toml  /app/

RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi

COPY . /app

CMD ["python", "./app.py"]
