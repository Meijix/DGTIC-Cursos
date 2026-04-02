"""
*args y **kwargs en Python
============================
Mecanismo para aceptar un número variable de argumentos
en funciones. Fundamental para crear APIs flexibles.

Ejecuta este archivo:
    python args_kwargs.py
"""

# ============================================================
# 1. *args — ARGUMENTOS POSICIONALES VARIABLES
# ============================================================

print("=== *args ===\n")


def sumar(*numeros):
    """Suma cualquier cantidad de números."""
    print(f"  numeros = {numeros}, tipo: {type(numeros).__name__}")
    return sum(numeros)


# Se puede llamar con cualquier cantidad de argumentos
print(f"sumar(1, 2) = {sumar(1, 2)}")
print(f"sumar(1, 2, 3, 4, 5) = {sumar(1, 2, 3, 4, 5)}")
print(f"sumar() = {sumar()}")


# *args se combina con parámetros normales
def describir(nombre, *caracteristicas):
    """El primer argumento es el nombre; el resto son características."""
    print(f"\n  {nombre}:")
    for c in caracteristicas:
        print(f"    - {c}")


describir("Python", "interpretado", "tipado dinámico", "multiparadigma")
describir("C", "compilado", "tipado estático")

# ============================================================
# 2. **kwargs — ARGUMENTOS CON NOMBRE VARIABLES
# ============================================================

print("\n=== **kwargs ===\n")


def crear_perfil(**datos):
    """Crea un perfil con cualquier cantidad de campos."""
    print(f"  datos = {datos}, tipo: {type(datos).__name__}")
    return datos


perfil = crear_perfil(nombre="Ana", edad=25, ciudad="CDMX", hobby="Python")
print(f"Perfil: {perfil}")


def configurar(host="localhost", **opciones):
    """Configuración con valores por defecto y opciones adicionales."""
    config = {"host": host}
    config.update(opciones)
    return config


config = configurar(host="192.168.1.1", port=8080, debug=True, workers=4)
print(f"\nConfig: {config}")

# ============================================================
# 3. COMBINANDO *args y **kwargs
# ============================================================

print("\n=== COMBINACIÓN *args + **kwargs ===\n")


def funcion_flexible(*args, **kwargs):
    """Acepta absolutamente cualquier combinación de argumentos."""
    print(f"  args: {args}")
    print(f"  kwargs: {kwargs}")


funcion_flexible(1, 2, 3, nombre="Ana", edad=25)
print()
funcion_flexible("solo", "posicionales")
print()
funcion_flexible(clave="solo keyword args")

# ============================================================
# 4. ORDEN DE PARÁMETROS
# ============================================================

print("\n=== ORDEN DE PARÁMETROS ===\n")

# El orden OBLIGATORIO es:
# 1. Parámetros posicionales normales
# 2. *args
# 3. Parámetros keyword-only (después de *args o de *)
# 4. **kwargs


def ejemplo_completo(a, b, *args, opcion=True, **kwargs):
    """Demuestra el orden completo de parámetros."""
    print(f"  a={a}, b={b}")
    print(f"  args={args}")
    print(f"  opcion={opcion}")
    print(f"  kwargs={kwargs}")


ejemplo_completo(1, 2, 3, 4, 5, opcion=False, extra="valor")

# ============================================================
# 5. KEYWORD-ONLY ARGUMENTS (solo por nombre)
# ============================================================

print("\n=== KEYWORD-ONLY ===\n")


# Usando * sin nombre para forzar keyword-only
def conectar(host, port, *, timeout=30, ssl=True):
    """timeout y ssl SOLO se pueden pasar por nombre."""
    print(f"  Conectando a {host}:{port} (timeout={timeout}, ssl={ssl})")


conectar("localhost", 8080)
conectar("localhost", 8080, timeout=10, ssl=False)
# conectar("localhost", 8080, 10, False)  # TypeError

# ============================================================
# 6. POSITIONAL-ONLY ARGUMENTS (Python 3.8+)
# ============================================================

print("\n=== POSITIONAL-ONLY (Python 3.8+) ===\n")


# Usando / para marcar el fin de positional-only
def potencia(base, exponente, /):
    """base y exponente SOLO se pueden pasar por posición."""
    return base ** exponente


print(f"potencia(2, 10) = {potencia(2, 10)}")
# potencia(base=2, exponente=10)  # TypeError


# Combinación completa: pos-only / normal * kw-only
def completa(pos_only, /, normal, *, kw_only):
    """Ejemplo con los tres tipos de parámetros."""
    print(f"  pos_only={pos_only}, normal={normal}, kw_only={kw_only}")


completa(1, 2, kw_only=3)
completa(1, normal=2, kw_only=3)

# ============================================================
# 7. DESEMPAQUETADO AL LLAMAR
# ============================================================

print("\n=== DESEMPAQUETADO AL LLAMAR ===\n")


def sumar_tres(a, b, c):
    return a + b + c


# Desempaquetar lista/tupla con *
numeros = [10, 20, 30]
print(f"sumar_tres(*[10,20,30]) = {sumar_tres(*numeros)}")

# Desempaquetar diccionario con **
params = {"a": 100, "b": 200, "c": 300}
print(f"sumar_tres(**dict) = {sumar_tres(**params)}")

# Combinar: * y **
def crear_mensaje(saludo, nombre, puntuacion="!"):
    return f"{saludo}, {nombre}{puntuacion}"

args = ("Hola",)
kwargs = {"nombre": "Ana", "puntuacion": "!!!"}
print(f"Desempaquetado mixto: {crear_mensaje(*args, **kwargs)}")

# ============================================================
# 8. PATRÓN: WRAPPER / PROXY
# ============================================================

print("\n=== PATRÓN WRAPPER ===\n")


def logger(func):
    """Envuelve una función para registrar sus llamadas."""
    def wrapper(*args, **kwargs):
        print(f"  [LOG] Llamando {func.__name__}(args={args}, kwargs={kwargs})")
        resultado = func(*args, **kwargs)
        print(f"  [LOG] {func.__name__} retornó: {resultado}")
        return resultado
    return wrapper


# Decorar manualmente (la sección 07 cubre @decorador)
sumar_logged = logger(sumar_tres)
sumar_logged(1, 2, 3)

# Este patrón funciona con CUALQUIER función gracias a *args/**kwargs
print()
def saludar(nombre, entusiasmo=1):
    return f"¡Hola, {nombre}" + "!" * entusiasmo

saludar_logged = logger(saludar)
saludar_logged("Ana", entusiasmo=3)

# ============================================================
# 9. PATRÓN: DICCIONARIO DE CONFIGURACIÓN
# ============================================================

print("\n=== PATRÓN CONFIGURACIÓN ===\n")


def crear_servidor(**config):
    """Crea un servidor con configuración flexible."""
    defaults = {
        "host": "0.0.0.0",
        "port": 8080,
        "workers": 4,
        "debug": False,
        "log_level": "INFO",
    }
    # Fusionar defaults con config (config tiene prioridad)
    final = {**defaults, **config}

    print("  Configuración del servidor:")
    for clave, valor in final.items():
        marcador = " *" if clave in config else ""
        print(f"    {clave}: {valor}{marcador}")
    return final


print("Servidor con defaults:")
crear_servidor()
print("\nServidor personalizado:")
crear_servidor(port=3000, debug=True, workers=8)

# ============================================================
# 10. EJEMPLO INTEGRADOR
# ============================================================

print("\n=== EJEMPLO: SISTEMA DE EVENTOS ===\n")


class EventBus:
    """Sistema simple de eventos usando *args/**kwargs."""

    def __init__(self):
        self._handlers = {}

    def on(self, evento, handler):
        """Registra un handler para un evento."""
        if evento not in self._handlers:
            self._handlers[evento] = []
        self._handlers[evento].append(handler)

    def emit(self, evento, *args, **kwargs):
        """Emite un evento, pasando argumentos a los handlers."""
        if evento in self._handlers:
            for handler in self._handlers[evento]:
                handler(*args, **kwargs)


# Crear bus de eventos
bus = EventBus()

# Registrar handlers
bus.on("usuario_creado", lambda nombre, **kw: print(f"  [DB] Guardando usuario: {nombre}"))
bus.on("usuario_creado", lambda nombre, **kw: print(f"  [EMAIL] Enviando bienvenida a: {nombre}"))
bus.on("usuario_creado", lambda nombre, email="?", **kw: print(f"  [LOG] Nuevo usuario: {nombre} ({email})"))

# Emitir evento — los handlers reciben *args y **kwargs
bus.emit("usuario_creado", "Ana García", email="ana@ejemplo.com")
