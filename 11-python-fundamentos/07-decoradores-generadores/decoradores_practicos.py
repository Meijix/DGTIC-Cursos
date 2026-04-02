"""
Decoradores Practicos — Uso Real en Python
=============================================
Decoradores del dia a dia: los que vienen con Python y los que
construiras en proyectos reales. Incluye decoradores con argumentos,
decoradores basados en clases y composicion de decoradores.

Ejecuta este archivo:
    python decoradores_practicos.py
"""

import functools
import time

# ============================================================
# 1. @functools.lru_cache — MEMORIZACION AUTOMATICA
# ============================================================

# lru_cache guarda los resultados de llamadas previas en un cache LRU
# (Least Recently Used). Si llamas la funcion con los mismos argumentos,
# retorna el resultado cacheado sin recalcular.

@functools.lru_cache(maxsize=128)
def fibonacci(n):
    """Fibonacci recursivo, pero eficiente gracias al cache."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("=== @functools.lru_cache ===")
print(f"fibonacci(50) = {fibonacci(50)}")  # Instantaneo gracias al cache
print(f"Cache info: {fibonacci.cache_info()}")
# CacheInfo(hits=48, misses=51, maxsize=128, currsize=51)

# cache_clear() limpia el cache
fibonacci.cache_clear()

# Python 3.9+ tiene @functools.cache (sin limite de tamanio)
# @functools.cache  # Equivale a lru_cache(maxsize=None)

# ============================================================
# 2. @property — GETTERS Y SETTERS PYTHONICOS
# ============================================================

class Circulo:
    """
    Ejemplo de @property para crear atributos calculados
    con validacion, sin cambiar la interfaz publica.
    """

    def __init__(self, radio):
        self._radio = radio    # Atributo "privado" por convencion

    @property
    def radio(self):
        """Getter: se accede como atributo, no como metodo."""
        return self._radio

    @radio.setter
    def radio(self, valor):
        """Setter: valida el valor antes de asignarlo."""
        if valor < 0:
            raise ValueError("El radio no puede ser negativo")
        self._radio = valor

    @property
    def area(self):
        """Atributo de solo lectura (no tiene setter)."""
        import math
        return math.pi * self._radio ** 2

    @property
    def perimetro(self):
        """Otro atributo calculado de solo lectura."""
        import math
        return 2 * math.pi * self._radio

print("\n=== @property ===")
c = Circulo(5)
print(f"Radio: {c.radio}")           # Llama al getter
print(f"Area: {c.area:.2f}")         # Atributo calculado
print(f"Perimetro: {c.perimetro:.2f}")

c.radio = 10                          # Llama al setter
print(f"Nuevo radio: {c.radio}")
print(f"Nueva area: {c.area:.2f}")

try:
    c.radio = -3                      # Setter rechaza valor negativo
except ValueError as e:
    print(f"Error: {e}")

# ============================================================
# 3. @staticmethod y @classmethod
# ============================================================

class Fecha:
    """Ejemplo de @staticmethod y @classmethod."""

    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    def __repr__(self):
        return f"Fecha({self.dia}/{self.mes}/{self.anio})"

    @classmethod
    def desde_string(cls, fecha_str):
        """
        @classmethod: recibe 'cls' (la clase) como primer argumento.
        Util para constructores alternativos.
        """
        dia, mes, anio = map(int, fecha_str.split("-"))
        return cls(dia, mes, anio)   # cls() permite herencia correcta

    @classmethod
    def hoy(cls):
        """Otro constructor alternativo."""
        import datetime
        ahora = datetime.date.today()
        return cls(ahora.day, ahora.month, ahora.year)

    @staticmethod
    def es_bisiesto(anio):
        """
        @staticmethod: no recibe ni self ni cls.
        Es una funcion normal que vive dentro de la clase
        por organizacion logica.
        """
        return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

print("\n=== @staticmethod y @classmethod ===")
# classmethod como constructor alternativo
f1 = Fecha.desde_string("15-03-2024")
print(f"Desde string: {f1}")

f2 = Fecha.hoy()
print(f"Hoy: {f2}")

# staticmethod como utilidad
print(f"2024 bisiesto: {Fecha.es_bisiesto(2024)}")
print(f"2023 bisiesto: {Fecha.es_bisiesto(2023)}")

# ============================================================
# 4. DECORADOR CON ARGUMENTOS (PATRON FACTORY)
# ============================================================

def limitar_llamadas(max_llamadas):
    """
    Decorador que limita cuantas veces se puede llamar una funcion.
    Requiere tres niveles de anidamiento porque acepta argumentos.

    Nivel 1: limitar_llamadas(max) -> retorna decorador
    Nivel 2: decorador(func) -> retorna wrapper
    Nivel 3: wrapper(*args) -> logica de ejecucion
    """
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if wrapper.llamadas >= max_llamadas:
                print(f"  [{func.__name__}] Limite de {max_llamadas} "
                      f"llamadas alcanzado!")
                return None
            wrapper.llamadas += 1
            print(f"  [{func.__name__}] Llamada {wrapper.llamadas}"
                  f"/{max_llamadas}")
            return func(*args, **kwargs)
        wrapper.llamadas = 0     # Atributo en la funcion wrapper
        return wrapper
    return decorador

@limitar_llamadas(3)
def api_request(url):
    """Simula una peticion a una API."""
    return f"Respuesta de {url}"

print("\n=== Decorador con argumentos ===")
for i in range(5):
    resultado = api_request(f"https://api.ejemplo.com/{i}")
    if resultado:
        print(f"  Resultado: {resultado}")

# ============================================================
# 5. DECORADOR BASADO EN CLASE
# ============================================================

class Cronometro:
    """
    Decorador implementado como clase.
    __init__ recibe la funcion, __call__ la ejecuta.
    Ventaja: puede mantener estado entre llamadas.
    """

    def __init__(self, func):
        functools.update_wrapper(self, func)  # Equivale a @wraps
        self.func = func
        self.tiempos = []    # Historial de tiempos

    def __call__(self, *args, **kwargs):
        inicio = time.perf_counter()
        resultado = self.func(*args, **kwargs)
        duracion = time.perf_counter() - inicio
        self.tiempos.append(duracion)
        print(f"  [{self.func.__name__}] {duracion:.6f}s "
              f"(promedio: {self.promedio:.6f}s)")
        return resultado

    @property
    def promedio(self):
        if not self.tiempos:
            return 0.0
        return sum(self.tiempos) / len(self.tiempos)

@Cronometro
def calcular_suma(n):
    """Suma numeros del 0 al n."""
    return sum(range(n))

print("\n=== Decorador basado en clase ===")
calcular_suma(100_000)
calcular_suma(500_000)
calcular_suma(1_000_000)
print(f"Promedio historico: {calcular_suma.promedio:.6f}s")

# ============================================================
# 6. APILAR (COMPONER) DECORADORES
# ============================================================

# Cuando apilas decoradores, se aplican de ABAJO hacia ARRIBA:
#
#   @A
#   @B
#   @C
#   def f(): ...
#
#   Equivale a: f = A(B(C(f)))
#   Se aplica C primero, luego B, luego A.
#   Al LLAMAR, se ejecuta A(exterior) -> B -> C -> f -> C -> B -> A

def negrita(func):
    """Envuelve el resultado en tags <b>."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def cursiva(func):
    """Envuelve el resultado en tags <i>."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

def parrafo(func):
    """Envuelve el resultado en tags <p>."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<p>{func(*args, **kwargs)}</p>"
    return wrapper

@parrafo       # Se aplica tercero (exterior)
@negrita       # Se aplica segundo
@cursiva       # Se aplica primero (mas cercano a la funcion)
def saludo(nombre):
    return f"Hola, {nombre}"

print("\n=== Decoradores apilados ===")
print(f"saludo('Ana') = {saludo('Ana')}")
# Resultado: <p><b><i>Hola, Ana</i></b></p>

# ============================================================
# 7. DECORADOR DE VALIDACION DE TIPOS
# ============================================================

def validar_tipos(**tipos_esperados):
    """
    Decorador que valida los tipos de los argumentos.
    Uso: @validar_tipos(x=int, y=float)
    """
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Obtener nombres de parametros
            import inspect
            sig = inspect.signature(func)
            params = list(sig.parameters.keys())

            # Validar argumentos posicionales
            for i, (param, valor) in enumerate(zip(params, args)):
                if param in tipos_esperados:
                    tipo = tipos_esperados[param]
                    if not isinstance(valor, tipo):
                        raise TypeError(
                            f"'{param}' debe ser {tipo.__name__}, "
                            f"recibio {type(valor).__name__}"
                        )

            # Validar argumentos por nombre
            for param, valor in kwargs.items():
                if param in tipos_esperados:
                    tipo = tipos_esperados[param]
                    if not isinstance(valor, tipo):
                        raise TypeError(
                            f"'{param}' debe ser {tipo.__name__}, "
                            f"recibio {type(valor).__name__}"
                        )

            return func(*args, **kwargs)
        return wrapper
    return decorador

@validar_tipos(nombre=str, edad=int)
def registrar(nombre, edad):
    """Registra un usuario."""
    return f"{nombre} ({edad} anios)"

print("\n=== Decorador de validacion de tipos ===")
print(registrar("Ana", 25))

try:
    registrar("Pedro", "treinta")  # Deberia fallar
except TypeError as e:
    print(f"Error esperado: {e}")

# ============================================================
# RESUMEN
# ============================================================

print("""
=== RESUMEN DE DECORADORES PRACTICOS ===

Built-in:
  @property           Getters/setters pythonicos
  @staticmethod       Metodo sin self/cls
  @classmethod        Metodo con cls (constructores alternativos)
  @functools.wraps    Preservar metadatos en decoradores
  @functools.lru_cache  Cache LRU automatico

Patrones:
  Decorador simple:        def dec(func): ... return wrapper
  Con argumentos (factory): def dec(arg): def decorador(func): ...
  Basado en clase:         class Dec: __init__(func), __call__(*args)
  Apilados:                Se aplican de abajo hacia arriba

Recuerda:
  - Siempre usa @functools.wraps(func) en tus decoradores.
  - Los decoradores con argumentos necesitan 3 niveles de anidamiento.
  - Los decoradores basados en clase son utiles cuando necesitas estado.
""")
