"""
Proyecto 3: Cliente de API del Clima
========================================
Consulta el clima actual de cualquier ciudad usando la API
gratuita de wttr.in. No requiere API key ni registro.

Conceptos integrados:
  - Modulos (urllib, json): hacer peticiones HTTP y parsear JSON
  - Excepciones: manejo de errores de red y datos
  - Diccionarios: acceder a datos JSON anidados
  - Strings y f-strings: formato de salida
  - Funciones: organizacion modular
  - Context managers: manejo de conexiones

Ejecuta este archivo:
    python api_clima.py                  # Modo interactivo
    python api_clima.py "Mexico City"    # Ciudad como argumento

API utilizada: https://wttr.in
  - Gratuita, sin API key
  - Formato JSON: https://wttr.in/Ciudad?format=j1
"""

import json
import sys
import urllib.request
import urllib.error

# ============================================================
# FUNCIONES DE CONSULTA A LA API
# ============================================================

def obtener_clima(ciudad):
    """
    Consulta el clima actual de una ciudad usando wttr.in.
    Integra seccion 05 (modulos) — uso de urllib y json.
    Integra seccion 08 (excepciones) — manejo de errores de red.

    Args:
        ciudad: Nombre de la ciudad (puede incluir espacios).

    Returns:
        dict: Datos del clima con temperatura, humedad, etc.

    Raises:
        ConnectionError: Si no hay conexion a internet.
        ValueError: Si la ciudad no es valida o no se encuentra.
    """
    # Codificar la ciudad para URL (espacios -> %20)
    ciudad_url = urllib.request.quote(ciudad)
    url = f"https://wttr.in/{ciudad_url}?format=j1"

    try:
        # Context manager para la conexion HTTP
        # Integra seccion 08 (context managers) — se cierra automaticamente
        with urllib.request.urlopen(url, timeout=10) as respuesta:
            datos_raw = respuesta.read()
            datos = json.loads(datos_raw)

    except urllib.error.URLError as e:
        # Error de conexion (sin internet, DNS fallo, etc.)
        raise ConnectionError(
            f"No se pudo conectar a wttr.in: {e.reason}"
        ) from e
    except urllib.error.HTTPError as e:
        # Error HTTP (404, 500, etc.)
        if e.code == 404:
            raise ValueError(f"Ciudad no encontrada: '{ciudad}'")
        raise ConnectionError(f"Error HTTP {e.code}: {e.reason}") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"Respuesta invalida del servidor: {e}") from e

    # Parsear los datos del JSON
    # Integra seccion 02 (diccionarios) — acceso a datos anidados
    return parsear_datos_clima(datos, ciudad)


def parsear_datos_clima(datos, ciudad):
    """
    Extrae la informacion relevante del JSON de wttr.in.
    Integra seccion 02 (diccionarios) — navegacion en datos anidados.

    El JSON de wttr.in tiene esta estructura:
    {
        "current_condition": [{"temp_C": "22", "humidity": "65", ...}],
        "nearest_area": [{"areaName": [{"value": "Ciudad"}], ...}],
        "weather": [{"maxtempC": "25", "mintempC": "15", ...}]
    }
    """
    try:
        actual = datos["current_condition"][0]
        area = datos["nearest_area"][0]
        pronostico_hoy = datos["weather"][0]

        # Extraer nombre del area
        nombre_area = area["areaName"][0]["value"]
        pais = area["country"][0]["value"]
        region = area["region"][0]["value"]

        # Descripcion del clima en espanol (si esta disponible)
        # Usamos la descripcion en ingles como respaldo
        desc = actual.get("lang_es", [{}])
        if desc and desc[0].get("value"):
            descripcion = desc[0]["value"]
        else:
            descripcion = actual.get("weatherDesc", [{}])[0].get("value", "N/A")

        return {
            "ciudad": nombre_area,
            "region": region,
            "pais": pais,
            "temperatura_c": int(actual["temp_C"]),
            "sensacion_termica_c": int(actual["FeelsLikeC"]),
            "humedad": int(actual["humidity"]),
            "descripcion": descripcion,
            "viento_kmh": int(actual["windspeedKmph"]),
            "direccion_viento": actual.get("winddir16Point", "N/A"),
            "visibilidad_km": int(actual.get("visibility", 0)),
            "presion_mb": int(actual.get("pressure", 0)),
            "temp_max_c": int(pronostico_hoy["maxtempC"]),
            "temp_min_c": int(pronostico_hoy["mintempC"]),
            "uv_index": int(actual.get("uvIndex", 0)),
        }

    except (KeyError, IndexError) as e:
        raise ValueError(
            f"Formato de datos inesperado para '{ciudad}': {e}"
        ) from e


# ============================================================
# FUNCIONES DE PRESENTACION
# ============================================================

def mostrar_clima(clima):
    """
    Muestra los datos del clima de forma visual.
    Integra seccion 01 (f-strings) — formato avanzado.
    """
    # Seleccionar emoji/icono segun la descripcion
    desc_lower = clima["descripcion"].lower()
    if any(w in desc_lower for w in ["sol", "sun", "clear", "despejado"]):
        icono = "Sol"
    elif any(w in desc_lower for w in ["nub", "cloud", "overcast"]):
        icono = "Nubes"
    elif any(w in desc_lower for w in ["lluv", "rain", "shower"]):
        icono = "Lluvia"
    elif any(w in desc_lower for w in ["niev", "snow"]):
        icono = "Nieve"
    elif any(w in desc_lower for w in ["torm", "thunder"]):
        icono = "Tormenta"
    else:
        icono = "---"

    print(f"""
  ╔══════════════════════════════════════════╗
  ║  CLIMA ACTUAL                            ║
  ╠══════════════════════════════════════════╣
  ║  {clima['ciudad']}, {clima['region']}
  ║  {clima['pais']}
  ║                                          ║
  ║  {icono}  {clima['descripcion']}
  ║                                          ║
  ║  Temperatura:     {clima['temperatura_c']:3d} C               ║
  ║  Sensacion:       {clima['sensacion_termica_c']:3d} C               ║
  ║  Max / Min:       {clima['temp_max_c']:3d} C / {clima['temp_min_c']:3d} C         ║
  ║  Humedad:         {clima['humedad']:3d}%                ║
  ║  Viento:          {clima['viento_kmh']:3d} km/h ({clima['direccion_viento']})
  ║  Visibilidad:     {clima['visibilidad_km']:3d} km               ║
  ║  Presion:        {clima['presion_mb']:4d} mb               ║
  ║  Indice UV:       {clima['uv_index']:3d}                 ║
  ╚══════════════════════════════════════════╝""")


def mostrar_comparacion(climas):
    """
    Muestra una comparacion entre varias ciudades.
    Integra seccion 02 (listas de diccionarios).
    """
    if not climas:
        return

    print(f"\n  {'CIUDAD':20s} {'TEMP':>6s} {'HUM':>6s} {'VIENTO':>8s}  DESCRIPCION")
    print("  " + "-" * 70)

    for c in climas:
        print(f"  {c['ciudad']:20s} {c['temperatura_c']:4d} C {c['humedad']:4d}% "
              f"{c['viento_kmh']:4d}km/h  {c['descripcion']}")


# ============================================================
# FUNCION PRINCIPAL — MODO INTERACTIVO
# ============================================================

def modo_interactivo():
    """
    Bucle interactivo para consultar el clima.
    Integra seccion 08 (excepciones) — manejo de input del usuario.
    """
    print("""
  ╔══════════════════════════════════════════╗
  ║      CONSULTA DEL CLIMA                  ║
  ║  API: wttr.in (gratuita, sin API key)    ║
  ╠══════════════════════════════════════════╣
  ║  Escribe el nombre de una ciudad         ║
  ║  Escribe 'comparar' para varias ciudades ║
  ║  Escribe 'salir' para terminar           ║
  ╚══════════════════════════════════════════╝""")

    while True:
        try:
            entrada = input("\n  Ciudad: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Hasta luego!")
            break

        if not entrada:
            continue

        if entrada.lower() == "salir":
            print("  Hasta luego!")
            break

        if entrada.lower() == "comparar":
            comparar_ciudades()
            continue

        consultar_ciudad(entrada)


def consultar_ciudad(ciudad):
    """Consulta y muestra el clima de una ciudad."""
    print(f"\n  Consultando clima de '{ciudad}'...")

    try:
        clima = obtener_clima(ciudad)
        mostrar_clima(clima)
    except ConnectionError as e:
        print(f"\n  Error de conexion: {e}")
        print("  Verifica tu conexion a internet.")
    except ValueError as e:
        print(f"\n  Error: {e}")
        print("  Intenta con otra ciudad o verifica la ortografia.")


def comparar_ciudades():
    """
    Permite comparar el clima de varias ciudades.
    Integra seccion 02 (listas) — acumular resultados.
    """
    print("  Escribe ciudades separadas por coma:")
    try:
        entrada = input("  Ciudades: ").strip()
    except (EOFError, KeyboardInterrupt):
        return

    ciudades = [c.strip() for c in entrada.split(",") if c.strip()]

    if not ciudades:
        print("  No se ingresaron ciudades.")
        return

    print(f"\n  Consultando {len(ciudades)} ciudades...")
    climas = []

    for ciudad in ciudades:
        try:
            clima = obtener_clima(ciudad)
            climas.append(clima)
            print(f"  + {ciudad}: {clima['temperatura_c']} C")
        except (ConnectionError, ValueError) as e:
            print(f"  x {ciudad}: Error — {e}")

    if climas:
        mostrar_comparacion(climas)


# ============================================================
# PUNTO DE ENTRADA
# ============================================================

def main():
    """
    Punto de entrada: acepta ciudad como argumento o inicia modo interactivo.
    """
    if len(sys.argv) > 1:
        # Ciudad pasada como argumento de linea de comandos
        ciudad = " ".join(sys.argv[1:])
        consultar_ciudad(ciudad)
    else:
        modo_interactivo()


if __name__ == "__main__":
    main()
