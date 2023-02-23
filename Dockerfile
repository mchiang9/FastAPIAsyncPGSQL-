FROM python:3.10

WORKDIR /app/

ENV POETRY_VERSION=1.1.13

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY pyproject.toml ./poetry.lock* /app/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

COPY ./app /app

ENV PYTHONPATH=/app