from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import DB_URL
import logging

logger = logging.getLogger(__name__)

class DatabaseConnector:
    def __init__(self):
        self.engine = create_engine(DB_URL)
        self.Session = sessionmaker(bind=self.engine)
        logger.info(f"Database connector initialized with URL: {DB_URL}")

    def get_engine(self):
        """Returns the SQLAlchemy engine."""
        return self.engine
    
    def get_session(self):
        """Returns a new session."""
        return self.Session()
