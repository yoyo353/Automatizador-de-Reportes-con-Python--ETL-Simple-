# Automatizador de Reportes con Python (ETL Simple)

Este proyecto es una refactorización de un script de ETL simple a una arquitectura modular profesional.
Toma datos "sucios" de un CSV, los limpia, los carga en una base de datos SQLite y genera un reporte en PDF.

## Requisitos

- Python 3.8+
- pip

## Estructura del Proyecto

```
nombre_proyecto_etl/
├── .env                  # Variables de entorno
├── requirements.txt      # Dependencias
├── README.md             # Documentación
├── data/
│   └── raw/              # Datos de entrada
│       └── generate_data.py # Script para generar datos de prueba
├── logs/                 # Archivos de log
├── src/
│   ├── main.py           # Orquestador principal
│   ├── config.py         # Configuración y logging
│   ├── db/               # Conexión a Base de Datos
│   ├── etl/              # Módulos de Extracción, Transformación y Carga
│   └── reports/          # Generación de Reportes
```

## Instalación

1. **Clonar el repositorio** (si aplica) o navegar a la carpeta del proyecto.

2. **Crear un entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno:**
   - Asegúrate de tener el archivo `.env` en la raíz (se incluye uno por defecto).

## Ejecución

1. **Generar datos de prueba (opcional, si no existe el CSV):**
   ```bash
   python data/raw/generate_data.py
   ```

2. **Ejecutar el pipeline ETL:**
   ```bash
   python -m src.main
   ```
   *Nota: Se ejecuta como módulo (`-m src.main`) para asegurar que las importaciones relativas funcionen correctamente.*

## Resultados

- **Logs:** Se generan en `logs/app.log`.
- **Base de Datos:** Se crea/actualiza `data/ventas.db`.
- **Reporte:** Se genera `reporte_ventas.pdf` en la raíz del proyecto.
