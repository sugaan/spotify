"""Core loader logic and CLI."""
import logging
import click
import pandas as pd
from sqlalchemy import create_engine
from .config import DB_URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_spotify_data(csv_path: str, table_name: str = "spotify_data") -> str:
    """Load CSV to Postgres table."""
    try:
        df = pd.read_csv(csv_path, encoding='latin-1')
        logger.info(f"Loaded {len(df)} rows from {csv_path}")
        
        engine = create_engine(DB_URL)
        df.to_sql(table_name, engine, if_exists='replace', index=False, 
                  chunksize=1000, method='multi')
        return f"Successfully loaded {len(df)} rows to '{table_name}'"
    except Exception as e:
        logger.error(f"Load failed: {e}")
        raise

@click.command()
@click.option('--file', 'csv_path', default='data/raw/spotify-2023.csv',
              help='Path to Spotify CSV', type=click.Path(exists=True))
@click.option('--table', default='spotify_data', help='Target table name')
def cli(csv_path, table):
    """CLI entrypoint."""
    result = load_spotify_data(csv_path, table)
    logger.info(result)