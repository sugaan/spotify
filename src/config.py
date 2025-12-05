"""Configuration loader using .env."""
import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "test")
DB_URL = f"postgresql://postgres:{POSTGRES_PASSWORD}@localhost:5432/postgres"