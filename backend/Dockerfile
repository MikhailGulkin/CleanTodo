FROM python:3.11 as build_app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false


COPY . /app


FROM build_app as test
RUN poetry install --with dev
ENV CONFIG_PATH='./config/test-config.toml'
CMD alembic upgrade head && pytest -v -s
