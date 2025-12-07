import logging
import sys
from src.config import DATA_FILE, setup_logging
from src.db.connector import DatabaseConnector
from src.etl.extractor import Extractor
from src.etl.transformer import Transformer
from src.etl.loader import Loader
from src.reports.pdf_generator import PDFGenerator

# Initialize Logging
setup_logging()
logger = logging.getLogger("Main")

def main():
    logger.info("Starting ETL Pipeline...")

    try:
        # 1. Initialize Components
        db = DatabaseConnector()
        extractor = Extractor(DATA_FILE)
        transformer = Transformer()
        loader = Loader(db)
        reporter = PDFGenerator(output_path='reporte_ventas.pdf')

        # 2. Extract
        df_raw = extractor.extract()

        # 3. Transform
        df_clean = transformer.transform(df_raw)

        # 4. Load
        loader.load(df_clean)

        # 5. Report
        reporter.generate(df_clean)
        
        logger.info("ETL Pipeline completed successfully.")

    except Exception as e:
        logger.critical(f"ETL Pipeline failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
