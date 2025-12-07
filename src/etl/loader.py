import pandas as pd
import logging
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

class Loader:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def load(self, df, table_name='ventas'):
        """Loads data into the database."""
        logger.info(f"Loading {len(df)} rows into table '{table_name}'...")
        try:
            engine = self.db_connector.get_engine()
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            logger.info("Data loaded successfully.")
        except Exception as e:
            logger.error(f"Error loading data to database: {e}")
            raise
