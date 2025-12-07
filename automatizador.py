import pandas as pd
import random
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from sqlalchemy import create_engine
import os

# ==========================================
# 1. GENERADOR DE DATOS DE PRUEBA (MOCK DATA)
# ==========================================
def crear_archivo_sucio():
    """Crea un CSV con datos 'sucios' para simular el problema real"""
    print("--- Generando archivo 'ventas_sucias.csv' ---")
    
    data = {
        'Fecha': ['2023-01-01', '01/02/2023', 'invalid_date', '2023-01-04', None], # Formatos mezclados y nulos
        'Producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Laptop'],
        'Venta': ['$1000', '20', '50', '$200', None], # Símbolos de dinero y nulos
        'Vendedor': ['Ana', 'Luis', None, 'Ana', 'Luis']
    }
    df = pd.DataFrame(data)
    df.to_csv('ventas_sucias.csv', index=False)
    print("Archivo creado con éxito.\n")

    