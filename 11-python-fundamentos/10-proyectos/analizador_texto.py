"""
Proyecto 2: Analizador de Texto
==================================
Herramienta que analiza un archivo de texto y muestra estadisticas:
frecuencia de palabras, palabras unicas, longitud promedio, etc.

Conceptos integrados:
  - Diccionarios: conteo de frecuencia
  - Conjuntos (sets): palabras unicas
  - Comprehensions: filtrado y transformacion
  - Archivos: lectura de texto
  - Funciones: organizacion modular
  - Strings: limpieza y procesamiento
  - Excepciones: manejo de errores

Ejecuta este archivo:
    python analizador_texto.py                # Texto de ejemplo
    python analizador_texto.py archivo.txt    # Tu propio archivo
"""

import os
import sys
import string
import tempfile
from collections import Counter

# ============================================================
# FUNCIONES DE ANALISIS
# ============================================================

def limpiar_palabra(palabra):
    """
    Limpia una palabra: quita puntuacion y convierte a minusculas.
    Integra seccion 01 (strings) — manipulacion de texto.
    """
    # strip con string.punctuation quita signos al inicio y final
    limpia = palabra.strip(string.punctuation + "¿¡«»""''")
    return limpia.lower()


def extraer_palabras(texto):
    """
    Extrae una lista de palabras limpias de un texto.
    Integra seccion 02 (comprehensions) — list comprehension con filtro.
    """
    # Dividir por espacios, limpiar cada palabra, filtrar vacias
    palabras = [
        limpiar_palabra(p)
        for linea in texto.split("\n")
        for p in linea.split()
        if limpiar_palabra(p)   # Filtrar palabras que quedan vacias
    ]
    return palabras


def contar_frecuencia(palabras):
    """
    Cuenta la frecuencia de cada palabra.
    Integra seccion 02 (diccionarios) — Counter es un dict especializado.
    """
    return Counter(palabras)


def obtener_palabras_unicas(palabras):
    """
    Obtiene el conjunto de palabras unicas.
    Integra seccion 02 (conjuntos/sets) — elimina duplicados.
    """
    return set(palabras)


def calcular_estadisticas(texto):
    """
    Calcula estadisticas completas de un texto.
    Integra seccion 03 (funciones) — funcion que organiza la logica.

    Returns:
        dict: Diccionario con todas las estadisticas.
    """
    lineas = texto.split("\n")
    lineas_no_vacias = [l for l in lineas if l.strip()]
    palabras = extraer_palabras(texto)
    frecuencia = contar_frecuencia(palabras)
    unicas = obtener_palabras_unicas(palabras)

    # Calcular longitud promedio de palabras
    if palabras:
        longitud_promedio = sum(len(p) for p in palabras) / len(palabras)
    else:
        longitud_promedio = 0

    # Encontrar la palabra mas larga
    palabra_mas_larga = max(palabras, key=len) if palabras else ""

    # Distribucion de longitudes (dict comprehension)
    distribucion = {}
    for p in palabras:
        longitud = len(p)
        distribucion[longitud] = distribucion.get(longitud, 0) + 1

    return {
        "total_lineas": len(lineas),
        "lineas_no_vacias": len(lineas_no_vacias),
        "total_palabras": len(palabras),
        "palabras_unicas": len(unicas),
        "longitud_promedio": longitud_promedio,
        "palabra_mas_larga": palabra_mas_larga,
        "frecuencia": frecuencia,
        "distribucion_longitudes": dict(sorted(distribucion.items())),
        "caracteres_total": len(texto),
        "caracteres_sin_espacios": len(texto.replace(" ", "").replace("\n", "")),
    }


# ============================================================
# FUNCIONES DE PRESENTACION
# ============================================================

def mostrar_resultados(estadisticas, top_n=15):
    """
    Muestra los resultados de forma legible.
    Integra seccion 01 (f-strings) — formato avanzado de texto.
    """
    est = estadisticas

    print("\n" + "=" * 55)
    print("           ANALISIS DE TEXTO")
    print("=" * 55)

    # --- Estadisticas generales ---
    print(f"\n  Lineas totales:          {est['total_lineas']}")
    print(f"  Lineas no vacias:        {est['lineas_no_vacias']}")
    print(f"  Total de palabras:       {est['total_palabras']}")
    print(f"  Palabras unicas:         {est['palabras_unicas']}")
    print(f"  Caracteres (total):      {est['caracteres_total']}")
    print(f"  Caracteres (sin espacio):{est['caracteres_sin_espacios']}")
    print(f"  Longitud promedio:       {est['longitud_promedio']:.1f} caracteres")
    print(f"  Palabra mas larga:       '{est['palabra_mas_larga']}'")

    # --- Indice de riqueza lexica ---
    if est["total_palabras"] > 0:
        riqueza = est["palabras_unicas"] / est["total_palabras"] * 100
        print(f"  Riqueza lexica:          {riqueza:.1f}%")
        print(f"    (palabras unicas / total)")

    # --- Top N palabras mas frecuentes ---
    print(f"\n  TOP {top_n} PALABRAS MAS FRECUENTES")
    print("  " + "-" * 40)

    frecuencia = est["frecuencia"]
    max_count = max(frecuencia.values()) if frecuencia else 1

    for palabra, cuenta in frecuencia.most_common(top_n):
        # Barra visual proporcional
        barra_len = int((cuenta / max_count) * 20)
        barra = "#" * barra_len
        print(f"  {palabra:20s} {cuenta:4d} |{barra}")

    # --- Distribucion de longitudes ---
    print(f"\n  DISTRIBUCION DE LONGITUD DE PALABRAS")
    print("  " + "-" * 40)

    for longitud, cuenta in est["distribucion_longitudes"].items():
        barra_len = min(cuenta, 30)
        barra = "#" * barra_len
        print(f"  {longitud:2d} letras: {cuenta:4d} |{barra}")

    print("\n" + "=" * 55)


# ============================================================
# LECTURA DE ARCHIVOS
# ============================================================

def leer_archivo(ruta):
    """
    Lee el contenido de un archivo de texto.
    Integra seccion 06 (archivos) y seccion 08 (excepciones).
    """
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"El archivo no existe: {ruta}")

    # Intentar con diferentes encodings
    for encoding in ["utf-8", "latin-1", "cp1252"]:
        try:
            with open(ruta, "r", encoding=encoding) as f:
                contenido = f.read()
            print(f"  Archivo leido con encoding: {encoding}")
            return contenido
        except UnicodeDecodeError:
            continue

    raise UnicodeDecodeError(
        "multiple", b"", 0, 1,
        f"No se pudo leer {ruta} con ningun encoding conocido"
    )


def crear_texto_ejemplo():
    """Crea un texto de ejemplo para demostrar el analizador."""
    return """Python es un lenguaje de programacion interpretado y multiparadigma.
Fue creado por Guido van Rossum y su primera version fue publicada en 1991.
Python es ampliamente utilizado en ciencia de datos, desarrollo web,
inteligencia artificial, automatizacion y scripting.

Una de las principales ventajas de Python es su sintaxis clara y legible.
Python enfatiza la legibilidad del codigo, lo que facilita el aprendizaje
para programadores principiantes y mejora la productividad de los
desarrolladores experimentados.

La comunidad de Python es una de las mas grandes y activas del mundo.
Existen miles de bibliotecas y frameworks disponibles, como Django para
desarrollo web, NumPy y Pandas para ciencia de datos, TensorFlow y
PyTorch para aprendizaje automatico, y Flask para APIs.

Python sigue la filosofia de que deberia haber una y preferiblemente
solo una forma obvia de hacer las cosas. Esta filosofia se conoce
como "The Zen of Python" y se puede ver ejecutando import this en
el interprete de Python.

El tipado dinamico de Python permite escribir codigo rapidamente,
aunque para proyectos grandes se recomienda usar type hints para
mejorar la mantenibilidad. Python soporta programacion orientada
a objetos, programacion funcional y programacion imperativa.

Python es un lenguaje que se ejecuta en multiples plataformas
incluyendo Windows, macOS y Linux. Esta versatilidad lo convierte
en una herramienta fundamental para cualquier programador.
"""


# ============================================================
# FUNCION PRINCIPAL
# ============================================================

def main():
    """Punto de entrada principal del analizador."""
    print("\n  ANALIZADOR DE TEXTO")
    print("  " + "=" * 30)

    # Determinar la fuente del texto
    if len(sys.argv) > 1:
        # Archivo pasado como argumento
        ruta = sys.argv[1]
        try:
            texto = leer_archivo(ruta)
            print(f"  Analizando: {ruta}")
        except FileNotFoundError as e:
            print(f"  Error: {e}")
            sys.exit(1)
        except UnicodeDecodeError as e:
            print(f"  Error de encoding: {e}")
            sys.exit(1)
    else:
        # Usar texto de ejemplo
        texto = crear_texto_ejemplo()
        print("  Usando texto de ejemplo (Python)")
        print("  (Pasa un archivo como argumento para analizar tu texto)")

    # Calcular y mostrar estadisticas
    estadisticas = calcular_estadisticas(texto)
    mostrar_resultados(estadisticas)


# ============================================================
# PUNTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
    main()
