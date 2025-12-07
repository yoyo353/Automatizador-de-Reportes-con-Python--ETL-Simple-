import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DB_URL = os.getenv("DB_URL", "sqlite:///data/ventas.db")
DATA_FILE = os.getenv("DATA_FILE", "data/raw/ventas_sucias.csv")
LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")

def setup_logging():
    """Configures logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
