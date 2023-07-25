FROM python:3.11

WORKDIR /app

ADD poetry.lock pyproject.toml /app/
RUN pip install poetry && poetry install --no-dev --no-root

ADD dyndns /app/dyndns
RUN poetry install --only main

ENTRYPOINT ["poetry", "run", "python", "-m", "dyndns"]
