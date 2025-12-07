from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class PDFGenerator:
    def __init__(self, output_path='reporte_ventas.pdf'):
        self.output_path = output_path

    def generate(self, df):
        """Generates a PDF report with basic statistics."""
        logger.info(f"Generating PDF report at {self.output_path}...")
        try:
            # Calculate stats
            total_sales = df['Venta'].sum()
            avg_sales = df['Venta'].mean()
            # Mode can return multiple values, take the first one
            best_seller = df['Vendedor'].mode()[0] if not df['Vendedor'].mode().empty else "N/A"

            c = canvas.Canvas(self.output_path, pagesize=letter)
            width, height = letter

            # Title
            c.setFont("Helvetica-Bold", 20)
            c.drawString(50, height - 50, "Reporte de Ventas")

            # Stats
            c.setFont("Helvetica", 12)
            c.drawString(50, height - 100, f"Total de Ventas: ${total_sales:,.2f}")
            c.drawString(50, height - 120, f"Promedio de Venta: ${avg_sales:,.2f}")
            c.drawString(50, height - 140, f"Mejor Vendedor: {best_seller}")

            c.save()
            logger.info("PDF report generated successfully.")
        except Exception as e:
            logger.error(f"Error generating PDF: {e}")
            raise
