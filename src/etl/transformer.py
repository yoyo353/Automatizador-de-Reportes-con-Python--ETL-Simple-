import pandas as pd
import logging

logger = logging.getLogger(__name__)

class Transformer:
    def transform(self, df):
        """Cleans and transforms the dataframe."""
        logger.info("Starting data transformation...")
        initial_count = len(df)
        
        # 1. Remove rows with critical nulls (Fecha, Producto, Venta)
        df = df.dropna(subset=['Fecha', 'Producto', 'Venta'])
        logger.info(f"Dropped {initial_count - len(df)} rows with nulls.")
        
        # 2. Clean 'Venta': Remove '$' and convert to numeric
        # Assuming Venta is string. If already numeric, this might fail or needs check.
        # But dummy data has strings '$1000'
        try:
            df['Venta'] = df['Venta'].astype(str).str.replace('$', '', regex=False).astype(float)
        except Exception as e:
            logger.error(f"Error converting 'Venta' to numeric: {e}")
            raise

        # 3. Standardize dates
        # Mixed YYYY-MM-DD and DD/MM/YYYY
        # pd.to_datetime handles mixed formats with some help or auto inference, but dayfirst=True/False is tricky if ambiguous.
        # The prompt says: "YYYY-MM-DD and DD/MM/YYYY".
        # 02/01/2023 -> 2nd Jan or 1st Feb? Usually Latin America uses DD/MM/YYYY.
        # '2023-01-01' is clear.
        # I will use pd.to_datetime which is generally smart, but verify.
        # If I can't be sure, I might use a custom parser or dayfirst=True is safer for mixed if we assume DD/MM/YYYY when ambiguous.
        
        try:
            # Using dayfirst=True because DD/MM/YYYY is common in non-US contexts
            df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True, errors='coerce')
            
            # Check if any dates became NaT
            null_dates = df['Fecha'].isna().sum()
            if null_dates > 0:
                logger.warning(f"{null_dates} rows have invalid dates and will be dropped.")
                df = df.dropna(subset=['Fecha'])
                
        except Exception as e:
            logger.error(f"Error parsing dates: {e}")
            raise

        logger.info("Data transformation complete.")
        return df
