"""
Ejemplo de Paquete Python
===========================
Este archivo __init__.py convierte el directorio en un paquete.

Se ejecuta automáticamente cuando se importa el paquete:
    import ejemplo_paquete
    from ejemplo_paquete import limpiar_texto, calcular_promedio

El __init__.py tiene tres propósitos principales:
1. Marcar el directorio como paquete Python
2. Inicializar el paquete (ejecutar código de setup)
3. Definir la API pública del paquete (qué se exporta)
"""

# Re-exportar las funciones principales de los submódulos
# para que el usuario pueda importar directamente del paquete
from .utils import limpiar_texto, calcular_promedio, formatear_moneda

# Metadatos del paquete
__version__ = "1.0.0"
__author__ = "Curso Python DGTIC"

# __all__ controla qué se exporta con "from ejemplo_paquete import *"
__all__ = [
    "limpiar_texto",
    "calcular_promedio",
    "formatear_moneda",
]

# Código de inicialización (se ejecuta al importar)
print(f"[ejemplo_paquete] Paquete cargado (v{__version__})")
