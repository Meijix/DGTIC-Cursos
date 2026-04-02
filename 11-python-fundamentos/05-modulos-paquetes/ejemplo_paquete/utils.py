"""
Módulo de utilidades del paquete ejemplo_paquete
=================================================
Funciones de uso general para procesamiento de texto y números.

Se puede importar de varias formas:
    from ejemplo_paquete.utils import limpiar_texto
    from ejemplo_paquete import limpiar_texto  # Gracias al __init__.py
"""

import re
from collections import Counter

# ============================================================
# FUNCIONES DE TEXTO
# ============================================================


def limpiar_texto(texto):
    """
    Limpia un texto: quita espacios extra, normaliza espacios internos.

    Args:
        texto: String a limpiar.

    Returns:
        String limpio.

    Ejemplos:
        >>> limpiar_texto("  Hola   Mundo  ")
        'Hola Mundo'
    """
    # Quitar espacios al inicio y final
    texto = texto.strip()
    # Reemplazar múltiples espacios por uno solo
    texto = re.sub(r'\s+', ' ', texto)
    return texto


def contar_palabras(texto):
    """
    Cuenta la frecuencia de cada palabra en un texto.

    Args:
        texto: String a analizar.

    Returns:
        dict: Diccionario {palabra: frecuencia}.
    """
    palabras = limpiar_texto(texto).lower().split()
    return dict(Counter(palabras))


def extraer_emails(texto):
    """
    Extrae direcciones de email de un texto.

    Args:
        texto: String donde buscar emails.

    Returns:
        list[str]: Lista de emails encontrados.
    """
    patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(patron, texto)


# ============================================================
# FUNCIONES NUMÉRICAS
# ============================================================


def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Args:
        numeros: Lista o iterable de números.

    Returns:
        float: El promedio.

    Raises:
        ValueError: Si la lista está vacía.
    """
    lista = list(numeros)
    if not lista:
        raise ValueError("No se puede calcular el promedio de una lista vacía")
    return sum(lista) / len(lista)


def formatear_moneda(cantidad, moneda="MXN", decimales=2):
    """
    Formatea un número como moneda.

    Args:
        cantidad: Número a formatear.
        moneda: Código de moneda (default: MXN).
        decimales: Cantidad de decimales.

    Returns:
        str: Cantidad formateada.

    Ejemplos:
        >>> formatear_moneda(1234567.89)
        '$1,234,567.89 MXN'
    """
    simbolos = {"MXN": "$", "USD": "$", "EUR": "€", "GBP": "£"}
    simbolo = simbolos.get(moneda, "$")
    return f"{simbolo}{cantidad:,.{decimales}f} {moneda}"


def calcular_porcentaje(parte, total):
    """Calcula qué porcentaje es 'parte' de 'total'."""
    if total == 0:
        raise ValueError("El total no puede ser cero")
    return (parte / total) * 100


# ============================================================
# BLOQUE DE PRUEBAS
# ============================================================

if __name__ == "__main__":
    print("=== Pruebas de utils.py ===\n")

    print("--- limpiar_texto ---")
    print(f"  '{limpiar_texto('  Hola   Mundo  ')}'")

    print("\n--- contar_palabras ---")
    print(f"  {contar_palabras('el gato y el perro y el gato')}")

    print("\n--- extraer_emails ---")
    texto = "Contacto: ana@email.com y luis@empresa.mx"
    print(f"  {extraer_emails(texto)}")

    print("\n--- calcular_promedio ---")
    print(f"  {calcular_promedio([10, 20, 30, 40, 50])}")

    print("\n--- formatear_moneda ---")
    print(f"  {formatear_moneda(1234567.89)}")
    print(f"  {formatear_moneda(99.99, 'USD')}")

    print("\n¡Todas las pruebas pasaron!")
