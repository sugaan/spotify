# Spotify Loader

[![Tests](https://github.com/yourusername/spotify-loader/actions/workflows/test.yml/badge.svg)](https://github.com/yourusername/spotify-loader/actions)

CLI tool to load [Spotify 2023 CSV](https://www.kaggle.com/datasets/nelgiriyewithana/spotify-music-data-2023) to PostgreSQL with Docker support.

## Quickstart
1. `git clone <repo> && cd spotify-loader`
2. `cp .env.example .env` → Edit `POSTGRES_PASSWORD`
3. `docker-compose up -d` (starts Postgres/pgAdmin)
4. `pip install -r requirements.txt`
5. `pip install -e .` (editable install)
6. `./data/raw/spotify-2023.csv` ← Add your file
7. `spotify-loader --table my_spotify`

View data: [localhost:8080](http://localhost:8080) (admin/admin) → host.docker.internal:5432.

## Development
- Tests: `pytest`
- Lint: `ruff check .`
