"""
Archivos CSV en Python
========================
CSV (Comma-Separated Values) es un formato de texto plano
para datos tabulares. Python tiene el módulo csv incorporado.

Ejecuta este archivo:
    python csv_ejemplo.py
"""

import csv
import os
import tempfile

TEMP_DIR = tempfile.mkdtemp(prefix="python_csv_")

# ============================================================
# 1. ESCRIBIR CSV
# ============================================================

print("=== ESCRIBIR CSV ===\n")

ruta_csv = os.path.join(TEMP_DIR, "estudiantes.csv")

# csv.writer — escribe listas
with open(ruta_csv, "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)

    # Escribir encabezados
    escritor.writerow(["nombre", "edad", "carrera", "promedio"])

    # Escribir filas individuales
    escritor.writerow(["Ana García", 20, "Computación", 9.2])
    escritor.writerow(["Luis Pérez", 22, "Matemáticas", 8.5])

    # Escribir múltiples filas de una vez
    datos = [
        ["Eva Ruiz", 21, "Computación", 9.8],
        ["Carlos López", 23, "Física", 7.3],
        ["Diana Soto", 20, "Computación", 8.9],
    ]
    escritor.writerows(datos)

print(f"CSV escrito: {ruta_csv}")

# Verificar contenido
with open(ruta_csv, "r", encoding="utf-8") as f:
    print(f.read())

# ============================================================
# 2. LEER CSV CON csv.reader
# ============================================================

print("=== LEER CON csv.reader ===\n")

with open(ruta_csv, "r", newline="", encoding="utf-8") as f:
    lector = csv.reader(f)

    encabezados = next(lector)  # Primera fila = encabezados
    print(f"Encabezados: {encabezados}")

    print("\nDatos:")
    for fila in lector:
        # Cada fila es una LISTA de strings
        nombre, edad, carrera, promedio = fila
        print(f"  {nombre:<15s} | {edad:>3s} | {carrera:<12s} | {promedio}")

# ============================================================
# 3. LEER CSV CON csv.DictReader
# ============================================================

print("\n=== LEER CON DictReader ===\n")

# DictReader convierte cada fila en un diccionario
with open(ruta_csv, "r", newline="", encoding="utf-8") as f:
    lector = csv.DictReader(f)

    # lector.fieldnames contiene los encabezados
    print(f"Campos: {lector.fieldnames}")

    estudiantes = []
    for fila in lector:
        # Cada fila es un dict con los encabezados como claves
        print(f"  {fila['nombre']}: {fila['promedio']}")
        estudiantes.append(fila)

# ============================================================
# 4. ESCRIBIR CON DictWriter
# ============================================================

print("\n=== ESCRIBIR CON DictWriter ===\n")

ruta_dict_csv = os.path.join(TEMP_DIR, "productos.csv")
productos = [
    {"nombre": "Laptop", "precio": 15000, "stock": 10},
    {"nombre": "Mouse", "precio": 250, "stock": 50},
    {"nombre": "Teclado", "precio": 800, "stock": 30},
    {"nombre": "Monitor", "precio": 5000, "stock": 15},
]

with open(ruta_dict_csv, "w", newline="", encoding="utf-8") as f:
    campos = ["nombre", "precio", "stock"]
    escritor = csv.DictWriter(f, fieldnames=campos)

    escritor.writeheader()  # Escribe los encabezados
    escritor.writerows(productos)

print(f"CSV de productos escrito: {ruta_dict_csv}")

with open(ruta_dict_csv, "r", encoding="utf-8") as f:
    print(f.read())

# ============================================================
# 5. DELIMITADORES PERSONALIZADOS
# ============================================================

print("=== DELIMITADORES ===\n")

# CSV con punto y coma (común en Excel en español)
ruta_semicolon = os.path.join(TEMP_DIR, "datos_semicolon.csv")
with open(ruta_semicolon, "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f, delimiter=";")
    escritor.writerow(["nombre", "ciudad", "salario"])
    escritor.writerow(["Ana", "CDMX", "45,000"])  # La coma en el salario no confunde
    escritor.writerow(["Luis", "GDL", "38,000"])

print("CSV con punto y coma:")
with open(ruta_semicolon, "r", encoding="utf-8") as f:
    print(f.read())

# TSV (Tab-Separated Values)
ruta_tsv = os.path.join(TEMP_DIR, "datos.tsv")
with open(ruta_tsv, "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f, delimiter="\t")
    escritor.writerow(["nombre", "edad", "ciudad"])
    escritor.writerow(["Ana García", 25, "Ciudad de México"])
    escritor.writerow(["Luis Pérez", 30, "Guadalajara"])

# ============================================================
# 6. EJEMPLO INTEGRADOR: PROCESAMIENTO DE DATOS
# ============================================================

print("=== EJEMPLO: ANÁLISIS DE VENTAS ===\n")

# Crear CSV de ventas
ruta_ventas = os.path.join(TEMP_DIR, "ventas.csv")
ventas_data = [
    ["fecha", "producto", "cantidad", "precio_unitario", "vendedor"],
    ["2024-01-15", "Laptop", "2", "15000", "Ana"],
    ["2024-01-15", "Mouse", "10", "250", "Luis"],
    ["2024-01-16", "Monitor", "3", "5000", "Ana"],
    ["2024-01-16", "Teclado", "5", "800", "Eva"],
    ["2024-01-17", "Laptop", "1", "15000", "Luis"],
    ["2024-01-17", "Mouse", "20", "250", "Ana"],
    ["2024-01-18", "Monitor", "2", "5000", "Eva"],
    ["2024-01-18", "Laptop", "3", "15000", "Ana"],
]

with open(ruta_ventas, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(ventas_data)

# Procesar ventas
from collections import defaultdict

total_por_vendedor = defaultdict(float)
total_por_producto = defaultdict(float)
ventas_totales = 0

with open(ruta_ventas, "r", newline="", encoding="utf-8") as f:
    lector = csv.DictReader(f)

    for venta in lector:
        subtotal = int(venta["cantidad"]) * float(venta["precio_unitario"])
        total_por_vendedor[venta["vendedor"]] += subtotal
        total_por_producto[venta["producto"]] += subtotal
        ventas_totales += subtotal

# Reporte
print(f"{'REPORTE DE VENTAS':=^50}")

print(f"\nTotal ventas: ${ventas_totales:,.2f}")

print(f"\n{'Por vendedor:'}")
for vendedor, total in sorted(total_por_vendedor.items(), key=lambda x: x[1], reverse=True):
    porcentaje = (total / ventas_totales) * 100
    print(f"  {vendedor:<10s}: ${total:>12,.2f} ({porcentaje:.1f}%)")

print(f"\n{'Por producto:'}")
for producto, total in sorted(total_por_producto.items(), key=lambda x: x[1], reverse=True):
    print(f"  {producto:<10s}: ${total:>12,.2f}")

# Guardar reporte en CSV
ruta_reporte = os.path.join(TEMP_DIR, "reporte.csv")
with open(ruta_reporte, "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["vendedor", "total_ventas", "porcentaje"])
    for vendedor, total in sorted(total_por_vendedor.items(), key=lambda x: x[1], reverse=True):
        porcentaje = (total / ventas_totales) * 100
        escritor.writerow([vendedor, f"{total:.2f}", f"{porcentaje:.1f}%"])

print(f"\nReporte guardado en: {ruta_reporte}")
