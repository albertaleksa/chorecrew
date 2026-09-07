# ChoreCrew

ChoreCrew is a shared household chore-management application built with Django.

## Development

The project requires Python 3.13.

### Run directly

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install --editable .
.venv/bin/python manage.py check
.venv/bin/python manage.py test
```

Direct development uses SQLite and safe local settings by default. Every
setting used by the container environment can also be overridden locally; see
[`.env.example`](.env.example) for the supported variables.

### Run with PostgreSQL and Redis

Docker Compose provides the Django development server, PostgreSQL 18.6, and
Redis 8.10.1. From a fresh checkout, build and start all three services with:

```bash
docker compose up --build
```

The application is then available at <http://localhost:8000>. PostgreSQL data
and uploaded media use named volumes, so they survive container recreation and
`docker compose down`. Running `docker compose down --volumes` deliberately
deletes both volumes.

Run Django's checks and complete test suite against the containerized
PostgreSQL configuration with:

```bash
docker compose run --rm web python manage.py check
docker compose run --rm web python manage.py test
```

PostgreSQL and Redis must pass their health checks before the web container
starts. To inspect their current state, run:

```bash
docker compose ps
```

Copy `.env.example` to `.env` when you need to override the safe development
defaults. The `.env` file is ignored by Git; never put real secrets in a
committed file.
