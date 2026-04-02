"""
Decoradores en Python — De Closure a @decorador
==================================================
Los decoradores son funciones que modifican el comportamiento de otras
funciones sin alterar su codigo fuente. Son una aplicacion elegante
del patron de diseno "wrapper" usando closures.

Ejecuta este archivo:
    python decoradores.py
"""

import time
import functools

# ============================================================
# 1. PASO A PASO: DE CLOSURE A DECORADOR
# ============================================================

# --- Paso 1: Una funcion normal ---
def saludar(nombre):
    """Saluda a alguien."""
    return f"Hola, {nombre}!"

# --- Paso 2: Envolver manualmente (closure) ---
# Queremos agregar logging SIN modificar 'saludar'.
# Creamos una funcion que la envuelve.

def saludar_con_log(nombre):
    print(f"[LOG] Llamando a saludar con: {nombre}")
    resultado = saludar(nombre)
    print(f"[LOG] saludar retorno: {resultado}")
    return resultado

print("=== Paso 2: Wrapper manual ===")
print(saludar_con_log("Ana"))

# --- Paso 3: Generalizarlo para CUALQUIER funcion ---
# Esta es la esencia de un decorador: una funcion que recibe
# una funcion y devuelve una nueva funcion mejorada.

def logger(func):
    """Decorador que imprime cuando se llama una funcion."""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Llamando {func.__name__}({args}, {kwargs})")
        resultado = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} retorno: {resultado}")
        return resultado
    return wrapper

# Uso manual del decorador
saludar_loggeada = logger(saludar)

print("\n=== Paso 3: Decorador manual ===")
print(saludar_loggeada("Carlos"))

# --- Paso 4: Sintaxis @ (azucar sintactica) ---
# @logger es EQUIVALENTE a: despedir = logger(despedir)

@logger
def despedir(nombre):
    """Se despide de alguien."""
    return f"Adios, {nombre}!"

print("\n=== Paso 4: Sintaxis @ ===")
print(despedir("Maria"))

# ============================================================
# 2. functools.wraps — PRESERVAR METADATOS
# ============================================================

# Problema: sin @wraps, el wrapper REEMPLAZA los metadatos originales
print("\n=== functools.wraps ===")
print(f"Nombre de 'despedir': {despedir.__name__}")  # wrapper (!)
print(f"Docstring de 'despedir': {despedir.__doc__}")  # None (!)

# Solucion: usar @functools.wraps

def logger_mejorado(func):
    """Decorador con @wraps para preservar metadatos."""
    @functools.wraps(func)  # Copia __name__, __doc__, __module__, etc.
    def wrapper(*args, **kwargs):
        print(f"[LOG] Llamando {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} termino")
        return resultado
    return wrapper

@logger_mejorado
def calcular(x, y):
    """Suma dos numeros."""
    return x + y

print(f"\nCon @wraps — nombre: {calcular.__name__}")   # calcular
print(f"Con @wraps — doc: {calcular.__doc__}")          # Suma dos numeros.
calcular(3, 5)

# ============================================================
# 3. DECORADOR PRACTICO: @timer
# ============================================================

def timer(func):
    """Mide el tiempo de ejecucion de una funcion."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"[TIMER] {func.__name__} tardo {fin - inicio:.6f} segundos")
        return resultado
    return wrapper

@timer
def operacion_lenta():
    """Simula una operacion que tarda."""
    total = sum(i ** 2 for i in range(100_000))
    return total

print("\n=== Decorador @timer ===")
resultado = operacion_lenta()
print(f"Resultado: {resultado}")

# ============================================================
# 4. DECORADOR PRACTICO: @retry
# ============================================================

import random

def retry(intentos=3, excepciones=(Exception,)):
    """
    Decorador con argumentos: reintenta la funcion si falla.
    Nota: cuando el decorador acepta argumentos, necesitamos
    TRES niveles de anidamiento (decorator factory).
    """
    def decorador(func):                    # Nivel 2: recibe la funcion
        @functools.wraps(func)
        def wrapper(*args, **kwargs):       # Nivel 3: envuelve la ejecucion
            for intento in range(1, intentos + 1):
                try:
                    return func(*args, **kwargs)
                except excepciones as e:
                    print(f"  Intento {intento}/{intentos} fallo: {e}")
                    if intento == intentos:
                        print(f"  Se agotaron los {intentos} intentos.")
                        raise
        return wrapper
    return decorador                        # Nivel 1: retorna el decorador

@retry(intentos=5, excepciones=(ValueError,))
def operacion_inestable():
    """Simula una operacion que falla aleatoriamente."""
    numero = random.randint(1, 4)
    if numero != 1:
        raise ValueError(f"Salio {numero}, esperaba 1")
    return "Exito!"

print("\n=== Decorador @retry ===")
try:
    resultado = operacion_inestable()
    print(f"Resultado: {resultado}")
except ValueError:
    print("La operacion fallo despues de todos los intentos")

# ============================================================
# 5. DECORADOR PRACTICO: @debug (con args y kwargs)
# ============================================================

def debug(func):
    """Muestra los argumentos y el resultado de cada llamada."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(repr(a) for a in args)
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        todos = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"[DEBUG] {func.__name__}({todos})")
        resultado = func(*args, **kwargs)
        print(f"[DEBUG] {func.__name__} -> {resultado!r}")
        return resultado
    return wrapper

@debug
def crear_saludo(nombre, entusiasta=False):
    """Crea un mensaje de saludo."""
    base = f"Hola, {nombre}"
    return f"{base}!!!" if entusiasta else f"{base}."

print("\n=== Decorador @debug ===")
crear_saludo("Pedro")
crear_saludo("Lucia", entusiasta=True)

# ============================================================
# 6. APILAR (STACKEAR) DECORADORES
# ============================================================

# Se pueden aplicar multiples decoradores. Se ejecutan de
# ABAJO hacia ARRIBA (el mas cercano a la funcion se aplica primero).

@timer
@debug
def fibonacci(n):
    """Calcula el n-esimo Fibonacci recursivamente."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print("\n=== Decoradores apilados (@timer + @debug) ===")
fibonacci(30)

# ============================================================
# RESUMEN
# ============================================================

print("""
=== RESUMEN DE DECORADORES ===

1. Un decorador es una funcion que recibe una funcion y devuelve otra.
2. @decorador es azucar sintactica para: func = decorador(func)
3. Siempre usa @functools.wraps(func) para preservar metadatos.
4. Para decoradores con argumentos, necesitas 3 niveles de anidamiento.
5. Los decoradores se apilan de abajo hacia arriba.

Patron basico:
    def mi_decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Logica ANTES
            resultado = func(*args, **kwargs)
            # Logica DESPUES
            return resultado
        return wrapper
""")
