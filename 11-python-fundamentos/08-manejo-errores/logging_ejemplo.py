"""
Logging en Python — Registro Profesional de Eventos
======================================================
El modulo logging es la forma correcta de registrar eventos en
aplicaciones Python. A diferencia de print(), permite controlar
niveles, formato, destinos y filtrado de mensajes.

Ejecuta este archivo:
    python logging_ejemplo.py
"""

import logging
import os
import tempfile

# ============================================================
# 1. CONFIGURACION BASICA
# ============================================================

# basicConfig configura el logger raiz. Se llama UNA vez al inicio.
# Si no lo llamas, logging usa WARNING como nivel por defecto.

logging.basicConfig(
    level=logging.DEBUG,          # Nivel minimo a mostrar
    format="%(asctime)s [%(levelname)-8s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)

# Crear un logger con nombre (buena practica: usar __name__)
logger = logging.getLogger(__name__)

print("=== Niveles de logging ===\n")

# Los 5 niveles estandar, de menor a mayor gravedad:
logger.debug("Esto es DEBUG — informacion detallada para diagnostico")
logger.info("Esto es INFO — confirmacion de funcionamiento normal")
logger.warning("Esto es WARNING — algo inesperado, pero el programa sigue")
logger.error("Esto es ERROR — una funcionalidad fallo")
logger.critical("Esto es CRITICAL — error fatal, posible terminacion")

# ============================================================
# 2. POR QUE NO USAR print()
# ============================================================

print("\n=== print() vs logging ===\n")

# print() tiene estas limitaciones:
# - No tiene niveles (no puedes filtrar mensajes)
# - No tiene formato estandar (fecha, modulo, linea)
# - No se puede redirigir facilmente a archivos
# - No se puede desactivar sin borrar las lineas
# - No es thread-safe

# logging resuelve TODO esto:
logger.info("Este mensaje incluye timestamp, nivel y origen automaticamente")

# ============================================================
# 3. LOGGING CON FORMATO (VARIABLES)
# ============================================================

print("\n=== Formato con variables ===\n")

usuario = "Ana"
accion = "login"
duracion = 0.342

# RECOMENDADO: usar % estilo (lazy evaluation — no formatea si no se muestra)
logger.info("Usuario %s realizo %s en %.3fs", usuario, accion, duracion)

# Tambien funciona con f-strings, pero es menos eficiente
# porque SIEMPRE formatea, incluso si el nivel no se muestra
logger.debug(f"Debug con f-string: {usuario}")  # Funciona pero no ideal

# ============================================================
# 4. LOGGING DE EXCEPCIONES
# ============================================================

print("\n=== Logging de excepciones ===\n")

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        # logger.exception() incluye el TRACEBACK automaticamente
        logger.exception("Error al dividir %s / %s", a, b)
        return None

resultado = dividir(10, 0)
print(f"Resultado: {resultado}")

# Alternativa: usar exc_info=True con cualquier nivel
try:
    int("no_es_numero")
except ValueError:
    logger.error("Error de conversion", exc_info=True)

# ============================================================
# 5. LOGGERS SEPARADOS POR MODULO
# ============================================================

print("\n=== Loggers por modulo ===\n")

# Cada modulo deberia tener su propio logger con su nombre.
# Esto permite controlar el nivel de cada modulo independientemente.

logger_db = logging.getLogger("basedatos")
logger_api = logging.getLogger("api")
logger_auth = logging.getLogger("autenticacion")

logger_db.info("Conexion a base de datos establecida")
logger_api.warning("Respuesta lenta del servidor externo")
logger_auth.error("Intento de acceso no autorizado")

# Se puede ajustar el nivel de un logger especifico:
# logger_db.setLevel(logging.WARNING)  # Solo WARNING+ para BD

# ============================================================
# 6. HANDLERS — ENVIAR LOGS A DIFERENTES DESTINOS
# ============================================================

print("\n=== Handlers (destinos multiples) ===\n")

# Crear un logger limpio para este ejemplo
logger_multi = logging.getLogger("multi_handler")
logger_multi.setLevel(logging.DEBUG)

# Handler 1: Consola (solo WARNING y superiores)
consola = logging.StreamHandler()
consola.setLevel(logging.WARNING)
formato_consola = logging.Formatter("[%(levelname)s] %(message)s")
consola.setFormatter(formato_consola)

# Handler 2: Archivo (todo desde DEBUG)
ruta_log = os.path.join(tempfile.gettempdir(), "ejemplo_python.log")
archivo = logging.FileHandler(ruta_log, mode="w", encoding="utf-8")
archivo.setLevel(logging.DEBUG)
formato_archivo = logging.Formatter(
    "%(asctime)s [%(levelname)-8s] %(name)s (%(filename)s:%(lineno)d): %(message)s"
)
archivo.setFormatter(formato_archivo)

# Agregar handlers al logger
logger_multi.addHandler(consola)
logger_multi.addHandler(archivo)

# Estos mensajes van SOLO al archivo (nivel DEBUG e INFO):
logger_multi.debug("Este debug solo va al archivo")
logger_multi.info("Este info solo va al archivo")

# Estos van a AMBOS destinos (WARNING+):
logger_multi.warning("Este warning va a consola Y archivo")
logger_multi.error("Este error va a consola Y archivo")

print(f"\nArchivo de log creado en: {ruta_log}")

# Leer y mostrar el contenido del archivo
with open(ruta_log, "r") as f:
    print("\nContenido del archivo de log:")
    for linea in f:
        print(f"  {linea.rstrip()}")

# ============================================================
# 7. EJEMPLO PRACTICO: APLICACION CON LOGGING
# ============================================================

print("\n=== Ejemplo practico ===\n")

logger_app = logging.getLogger("mi_app")

def procesar_pedidos(pedidos):
    """Procesa una lista de pedidos con logging apropiado."""
    logger_app.info("Iniciando procesamiento de %d pedidos", len(pedidos))

    exitosos = 0
    fallidos = 0

    for pedido in pedidos:
        try:
            # Simular validacion
            if pedido.get("total", 0) <= 0:
                raise ValueError(f"Total invalido: {pedido.get('total')}")

            if not pedido.get("cliente"):
                raise ValueError("Cliente no especificado")

            logger_app.debug("Procesando pedido #%s de %s",
                             pedido.get("id"), pedido.get("cliente"))
            exitosos += 1

        except ValueError as e:
            logger_app.warning("Pedido #%s rechazado: %s",
                               pedido.get("id", "??"), e)
            fallidos += 1

        except Exception:
            logger_app.exception("Error inesperado en pedido #%s",
                                 pedido.get("id", "??"))
            fallidos += 1

    logger_app.info("Procesamiento completado: %d exitosos, %d fallidos",
                    exitosos, fallidos)

pedidos = [
    {"id": 1, "cliente": "Ana", "total": 150.00},
    {"id": 2, "cliente": "Luis", "total": -10.00},   # Total invalido
    {"id": 3, "cliente": "", "total": 75.00},         # Sin cliente
    {"id": 4, "cliente": "Pedro", "total": 200.00},
]

procesar_pedidos(pedidos)

# Limpieza de handlers para evitar duplicados si se reimporta
logger_multi.handlers.clear()

print("""
=== RESUMEN DE LOGGING ===

Niveles: DEBUG < INFO < WARNING < ERROR < CRITICAL
Configuracion: logging.basicConfig() al inicio del programa
Logger por modulo: logging.getLogger(__name__)
Excepciones: logger.exception() incluye traceback automaticamente
Handlers: StreamHandler (consola), FileHandler (archivo)
Formato: %(asctime)s, %(levelname)s, %(name)s, %(message)s

NUNCA uses print() para logs en codigo de produccion.
""")
