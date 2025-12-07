import pandas as pd
import random
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from sqlalchemy import create_engine
import os


# GENERADOR DE DATOS DE PRUEBA

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

# ETL (EXTRACT, TRANSFORM, LOAD)

def procesar_datos():
    print("--- Iniciando Limpieza de Datos ---")
    
    # EXTRACCIÓN
    try:
        df = pd.read_csv('ventas_sucias.csv')
    except FileNotFoundError:
        print("El archivo no existe.")
        return None

    print(f"Filas originales: {len(df)}")

# TRANSFORMACIÓN (Limpieza)
    
    # 1. Eliminar filas donde falten datos críticos (Ej: sin Venta o Producto)
    df = df.dropna(subset=['Venta', 'Producto'])
    
    # 2. Limpiar columna 'Venta' (quitar '$' y convertir a número)
    # Convertimos a string, reemplazamos '$', y luego a numérico
    df['Venta'] = df['Venta'].astype(str).str.replace('$', '', regex=False)
    df['Venta'] = pd.to_numeric(df['Venta'], errors='coerce') # 'coerce' convierte errores en NaN
    
    # 3. Estandarizar Fechas
    # Intentamos convertir todo a datetime, los errores se vuelven NaT (Not a Time)
    df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce', dayfirst=False)
    
    # 4. Limpieza final: eliminar filas que quedaron con NaNs tras las conversiones
    df = df.dropna()

    print(f"Filas limpias: {len(df)}")
    print(df.head())
    print("\n")
    return df

