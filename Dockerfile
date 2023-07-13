# syntax=docker/dockerfile:1.5

FROM python:3.11.3-slim-bullseye  AS base

WORKDIR /app

ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN <<EOF
    python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python -
EOF
COPY . .
RUN --mount=type=cache,target=/root/.cache/pypoetry <<EOF
  poetry install --no-interaction --no-ansi
EOF

FROM python:3.11.3-slim-bullseye as app
ENV PATH="/app/.venv/bin:$PATH"
COPY --from=base /app /app
CMD mwe-fastapi
