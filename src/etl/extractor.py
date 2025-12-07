import pandas as pd
import logging
import os

logger = logging.getLogger(__name__)

class Extractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract(self):
        """Reads data from the CSV file."""
        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"File not found: {self.file_path}")
            
            logger.info(f"Extracting data from {self.file_path}")
            df = pd.read_csv(self.file_path)
            logger.info(f"Extracted {len(df)} rows.")
            return df
        except Exception as e:
            logger.error(f"Error extracting data: {e}")
            raise
