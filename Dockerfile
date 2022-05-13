FROM python:3.10

WORKDIR /app

ADD poetry.lock pyproject.toml /app/
RUN pip install poetry && poetry install --no-dev --no-root

ADD dyndns /app/dyndns
RUN poetry install --no-dev

ENTRYPOINT ["poetry", "run", "python", "-m", "dyndns"]