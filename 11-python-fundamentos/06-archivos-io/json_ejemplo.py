"""
Archivos JSON en Python
========================
JSON (JavaScript Object Notation) es el formato estándar
para intercambio de datos en APIs web. Python tiene el
módulo json incorporado.

Ejecuta este archivo:
    python json_ejemplo.py
"""

import json
import os
import tempfile
from datetime import datetime

TEMP_DIR = tempfile.mkdtemp(prefix="python_json_")

# ============================================================
# 1. SERIALIZACIÓN: Python → JSON
# ============================================================

print("=== PYTHON → JSON ===\n")

# Correspondencia de tipos:
# Python          JSON
# dict        →   object {}
# list/tuple  →   array []
# str         →   string ""
# int/float   →   number
# True/False  →   true/false
# None        →   null

datos = {
    "nombre": "Ana García",
    "edad": 25,
    "activo": True,
    "direccion": None,
    "habilidades": ["Python", "SQL", "Git"],
    "experiencia": {
        "empresa": "TechCorp",
        "años": 3,
    }
}

# dumps() — convierte a string JSON
json_string = json.dumps(datos, ensure_ascii=False, indent=2)
print(f"JSON como string:\n{json_string}")

# Opciones útiles de dumps:
# indent=2         → formato legible
# ensure_ascii=False → permite caracteres Unicode (acentos, ñ)
# sort_keys=True   → ordena las claves alfabéticamente

# ============================================================
# 2. DESERIALIZACIÓN: JSON → Python
# ============================================================

print("\n=== JSON → PYTHON ===\n")

json_texto = '{"nombre": "Luis", "edad": 30, "activo": false, "notas": [8.5, 9.0]}'

# loads() — convierte string JSON a objeto Python
obj = json.loads(json_texto)
print(f"Tipo: {type(obj)}")
print(f"Nombre: {obj['nombre']}")
print(f"Activo: {obj['activo']}")
print(f"Notas: {obj['notas']}")

# ============================================================
# 3. LEER Y ESCRIBIR ARCHIVOS JSON
# ============================================================

print("\n=== ARCHIVOS JSON ===\n")

ruta_json = os.path.join(TEMP_DIR, "config.json")

# dump() — escribe a archivo
configuracion = {
    "servidor": {
        "host": "localhost",
        "port": 8080,
        "debug": True,
    },
    "base_datos": {
        "motor": "postgresql",
        "nombre": "mi_app",
        "pool_size": 5,
    },
    "logging": {
        "nivel": "INFO",
        "archivo": "app.log",
    }
}

with open(ruta_json, "w", encoding="utf-8") as f:
    json.dump(configuracion, f, indent=2, ensure_ascii=False)
print(f"Configuración guardada en: {ruta_json}")

# load() — lee desde archivo
with open(ruta_json, "r", encoding="utf-8") as f:
    config_leida = json.load(f)

print(f"Servidor: {config_leida['servidor']['host']}:{config_leida['servidor']['port']}")
print(f"BD: {config_leida['base_datos']['motor']}")

# ============================================================
# 4. TIPOS NO SERIALIZABLES
# ============================================================

print("\n=== TIPOS NO SERIALIZABLES ===\n")

# JSON solo soporta los tipos básicos. datetime, set, etc. no son serializables.

# Solución 1: Función default personalizada
def serializar_custom(obj):
    """Convierte tipos no estándar a tipos serializables."""
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, set):
        return list(obj)
    if isinstance(obj, bytes):
        return obj.decode("utf-8")
    raise TypeError(f"Tipo {type(obj)} no es serializable")


datos_complejos = {
    "fecha": datetime(2024, 12, 25, 10, 30),
    "tags": {"python", "programación", "curso"},
    "binario": b"hola",
}

json_str = json.dumps(datos_complejos, default=serializar_custom, indent=2, ensure_ascii=False)
print(f"Con tipos custom:\n{json_str}")

# Solución 2: JSONEncoder personalizado
class MiEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return {"__datetime__": True, "valor": obj.isoformat()}
        if isinstance(obj, set):
            return {"__set__": True, "valor": list(obj)}
        return super().default(obj)

json_con_encoder = json.dumps(datos_complejos, cls=MiEncoder, indent=2, ensure_ascii=False)
print(f"\nCon JSONEncoder custom:\n{json_con_encoder}")

# ============================================================
# 5. JSON LINES (JSONL) — un JSON por línea
# ============================================================

print("\n=== JSON LINES ===\n")

# Útil para logs y datos que crecen incrementalmente
ruta_jsonl = os.path.join(TEMP_DIR, "eventos.jsonl")

eventos = [
    {"timestamp": "2024-01-15T10:30:00", "tipo": "login", "usuario": "ana"},
    {"timestamp": "2024-01-15T10:31:00", "tipo": "click", "usuario": "ana", "pagina": "/inicio"},
    {"timestamp": "2024-01-15T10:32:00", "tipo": "logout", "usuario": "ana"},
]

# Escribir JSONL
with open(ruta_jsonl, "w", encoding="utf-8") as f:
    for evento in eventos:
        f.write(json.dumps(evento, ensure_ascii=False) + "\n")

# Leer JSONL
print("Eventos cargados:")
with open(ruta_jsonl, "r", encoding="utf-8") as f:
    for linea in f:
        evento = json.loads(linea.strip())
        print(f"  [{evento['timestamp']}] {evento['tipo']} — {evento['usuario']}")

# ============================================================
# 6. EJEMPLO INTEGRADOR: SISTEMA DE CONFIGURACIÓN
# ============================================================

print("\n=== EJEMPLO: GESTOR DE CONFIGURACIÓN ===\n")


class GestorConfig:
    """Gestiona configuración persistente en JSON."""

    def __init__(self, ruta):
        self.ruta = ruta
        self._config = {}
        self._cargar()

    def _cargar(self):
        """Carga configuración desde archivo."""
        try:
            with open(self.ruta, "r", encoding="utf-8") as f:
                self._config = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self._config = {}

    def _guardar(self):
        """Guarda configuración a archivo."""
        with open(self.ruta, "w", encoding="utf-8") as f:
            json.dump(self._config, f, indent=2, ensure_ascii=False)

    def get(self, clave, default=None):
        """Obtiene un valor (soporta claves anidadas con '.')."""
        claves = clave.split(".")
        valor = self._config
        for k in claves:
            if isinstance(valor, dict) and k in valor:
                valor = valor[k]
            else:
                return default
        return valor

    def set(self, clave, valor):
        """Establece un valor (soporta claves anidadas con '.')."""
        claves = clave.split(".")
        config = self._config
        for k in claves[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[claves[-1]] = valor
        self._guardar()

    def mostrar(self):
        """Muestra la configuración actual."""
        print(json.dumps(self._config, indent=2, ensure_ascii=False))


# Usar el gestor
ruta_config = os.path.join(TEMP_DIR, "app_config.json")
config = GestorConfig(ruta_config)

# Establecer valores
config.set("app.nombre", "Mi Aplicación")
config.set("app.version", "1.0.0")
config.set("servidor.host", "localhost")
config.set("servidor.port", 8080)
config.set("servidor.debug", True)
config.set("bd.conexion", "postgresql://localhost/miapp")

# Leer valores
print(f"Nombre: {config.get('app.nombre')}")
print(f"Puerto: {config.get('servidor.port')}")
print(f"Cache (no existe): {config.get('cache.ttl', 300)}")

print("\nConfiguración completa:")
config.mostrar()
