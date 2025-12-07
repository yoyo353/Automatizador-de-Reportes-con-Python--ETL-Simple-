import pandas as pd
import numpy as np
import os

def generate_dummy_data():
    """Generates dummy data for testing the ETL pipeline."""
    # Ensure directory exists
    os.makedirs('data/raw', exist_ok=True)
    
    data = {
        'Fecha': ['2023-01-01', '02/01/2023', '2023-01-03', None, '05/01/2023', '2023-01-06'],
        'Producto': ['Laptop', 'Mouse', 'Monitor', 'Teclado', None, 'Mouse'],
        'Venta': ['$1000', '$20', '$200', '$50', '$30', '$20'],
        'Vendedor': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Bob']
    }
    
    df = pd.DataFrame(data)
    
    # Introduce some dirt
    # already handled by mixed dates and nulls in 'Fecha' and 'Producto'
    
    output_path = 'data/raw/ventas_sucias.csv'
    df.to_csv(output_path, index=False)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_dummy_data()
