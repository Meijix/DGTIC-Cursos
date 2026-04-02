"""
Type Hints (Anotaciones de Tipo) en Python
=============================================
Desde Python 3.5+, se pueden anotar los tipos de parámetros,
retornos y variables. Son OPCIONALES y NO se verifican en
tiempo de ejecución — sirven como documentación y para
herramientas de análisis estático como mypy.

Ejecuta este archivo:
    python type_hints.py
"""

from typing import Any, Callable, Optional, Union
from collections.abc import Sequence, Iterable, Iterator

# ============================================================
# 1. ANOTACIONES BÁSICAS
# ============================================================

print("=== ANOTACIONES BÁSICAS ===\n")


# Tipos primitivos
def saludar(nombre: str) -> str:
    """Recibe un str y retorna un str."""
    return f"Hola, {nombre}"


def area_circulo(radio: float) -> float:
    """Recibe un float y retorna un float."""
    import math
    return math.pi * radio ** 2


def es_mayor(edad: int) -> bool:
    """Recibe un int y retorna un bool."""
    return edad >= 18


# Variables anotadas
nombre: str = "Ana"
edad: int = 25
activo: bool = True
pi: float = 3.14159

print(f"{saludar('Ana')}")
print(f"Área (r=5): {area_circulo(5):.2f}")
print(f"¿Es mayor (17)? {es_mayor(17)}")

# Las anotaciones NO impiden pasar otros tipos:
print(f"saludar(42) = {saludar(42)}")  # Funciona, pero mypy marcaría error

# ============================================================
# 2. TIPOS COMPUESTOS (Python 3.9+)
# ============================================================

print("\n=== TIPOS COMPUESTOS ===\n")


# Python 3.9+: usar tipos built-in directamente (minúsculas)
def procesar_nombres(nombres: list[str]) -> list[str]:
    """Lista de strings → lista de strings en mayúsculas."""
    return [n.upper() for n in nombres]


def contar_palabras(texto: str) -> dict[str, int]:
    """Cuenta la frecuencia de cada palabra."""
    palabras = texto.lower().split()
    frecuencia: dict[str, int] = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia


def coordenada() -> tuple[float, float]:
    """Retorna una tupla de exactamente 2 floats."""
    return (19.4326, -99.1332)


def tags_unicos(textos: list[str]) -> set[str]:
    """Extrae palabras únicas de múltiples textos."""
    return {palabra for texto in textos for palabra in texto.split()}


print(f"Nombres: {procesar_nombres(['ana', 'luis', 'eva'])}")
print(f"Conteo: {contar_palabras('el gato y el perro')}")
print(f"Coordenada: {coordenada()}")
print(f"Tags: {tags_unicos(['hola mundo', 'mundo python'])}")

# ============================================================
# 3. OPTIONAL Y UNION
# ============================================================

print("\n=== OPTIONAL Y UNION ===\n")


# Optional[X] es equivalente a X | None
def buscar_usuario(user_id: int) -> Optional[dict]:
    """Retorna un usuario o None si no se encuentra."""
    usuarios = {
        1: {"nombre": "Ana", "edad": 25},
        2: {"nombre": "Luis", "edad": 30},
    }
    return usuarios.get(user_id)


# Python 3.10+: usar | en vez de Union
def formatear(valor: int | float | str) -> str:
    """Acepta int, float o str."""
    return str(valor)


user = buscar_usuario(1)
print(f"Usuario 1: {user}")
print(f"Usuario 99: {buscar_usuario(99)}")


# Parámetros con None como default
def conectar(host: str, port: int = 8080, timeout: int | None = None) -> str:
    """timeout puede ser un int o None (sin timeout)."""
    t = f", timeout={timeout}s" if timeout else ""
    return f"Conectado a {host}:{port}{t}"


print(f"\n{conectar('localhost')}")
print(f"{conectar('servidor.com', 3000, 30)}")

# ============================================================
# 4. CALLABLE — FUNCIONES COMO TIPO
# ============================================================

print("\n=== CALLABLE ===\n")


# Callable[[tipos_param], tipo_retorno]
def aplicar_a_lista(func: Callable[[int], int], datos: list[int]) -> list[int]:
    """Aplica una función a cada elemento."""
    return [func(x) for x in datos]


nums = [1, 2, 3, 4, 5]
print(f"Cuadrados: {aplicar_a_lista(lambda x: x**2, nums)}")
print(f"Dobles:    {aplicar_a_lista(lambda x: x*2, nums)}")


# Función que retorna función
def crear_saludo(idioma: str) -> Callable[[str], str]:
    """Retorna una función de saludo según el idioma."""
    saludos: dict[str, str] = {
        "es": "Hola",
        "en": "Hello",
        "fr": "Bonjour",
    }
    prefijo = saludos.get(idioma, "Hi")
    return lambda nombre: f"{prefijo}, {nombre}!"


saludar_es = crear_saludo("es")
saludar_en = crear_saludo("en")
print(f"\n{saludar_es('Ana')}")
print(f"{saludar_en('Ana')}")

# ============================================================
# 5. TIPOS GENÉRICOS CON COLLECTIONS.ABC
# ============================================================

print("\n=== TIPOS ABSTRACTOS ===\n")


# Sequence acepta list, tuple, str, etc.
def primer_elemento(secuencia: Sequence[int]) -> int:
    """Funciona con cualquier secuencia indexable."""
    return secuencia[0]


# Iterable acepta cualquier cosa sobre la que se pueda iterar
def sumar_todos(datos: Iterable[int | float]) -> float:
    """Funciona con list, tuple, set, generator, etc."""
    return sum(datos)


print(f"Primero de lista: {primer_elemento([10, 20, 30])}")
print(f"Primero de tupla: {primer_elemento((100, 200))}")
print(f"Suma de set: {sumar_todos({1, 2, 3, 4, 5})}")

# ============================================================
# 6. TYPE ALIASES
# ============================================================

print("\n=== TYPE ALIASES ===\n")

# Crear alias para tipos complejos — mejora legibilidad
Punto = tuple[float, float]
Matriz = list[list[float]]
Registro = dict[str, str | int | float]
Transformacion = Callable[[Punto], Punto]

def distancia(p1: Punto, p2: Punto) -> float:
    """Calcula distancia entre dos puntos."""
    import math
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)


def trasladar(dx: float, dy: float) -> Transformacion:
    """Crea una función de traslación."""
    def transform(punto: Punto) -> Punto:
        return (punto[0] + dx, punto[1] + dy)
    return transform


p1: Punto = (0.0, 0.0)
p2: Punto = (3.0, 4.0)
print(f"Distancia: {distancia(p1, p2)}")

mover = trasladar(10, 20)
print(f"Trasladar (3,4) por (10,20): {mover((3, 4))}")

# ============================================================
# 7. ANOTACIONES EN CLASES
# ============================================================

print("\n=== ANOTACIONES EN CLASES ===\n")


class Estudiante:
    """Ejemplo de clase con type hints."""

    nombre: str
    edad: int
    calificaciones: list[float]

    def __init__(self, nombre: str, edad: int, calificaciones: list[float] | None = None):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones or []

    def promedio(self) -> float:
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)

    def es_aprobado(self, minimo: float = 6.0) -> bool:
        return self.promedio() >= minimo

    def __repr__(self) -> str:
        return f"Estudiante({self.nombre!r}, promedio={self.promedio():.1f})"


alumno = Estudiante("Ana", 20, [9.5, 8.0, 9.2, 7.8])
print(f"Alumno: {alumno}")
print(f"Promedio: {alumno.promedio():.2f}")
print(f"¿Aprobado? {alumno.es_aprobado()}")

# ============================================================
# 8. INSPECCIONAR ANOTACIONES EN RUNTIME
# ============================================================

print("\n=== INSPECCIÓN DE ANOTACIONES ===\n")

import inspect


def ejemplo(a: int, b: str = "hola", c: float = 3.14) -> bool:
    """Función de ejemplo para inspeccionar."""
    return True


# Ver anotaciones
print(f"Anotaciones: {ejemplo.__annotations__}")

# Inspección con el módulo inspect
sig = inspect.signature(ejemplo)
for nombre, param in sig.parameters.items():
    print(f"  {nombre}: tipo={param.annotation.__name__}, "
          f"default={param.default}")
print(f"  retorno: {sig.return_annotation.__name__}")

# ============================================================
# 9. EJEMPLO INTEGRADOR: API TIPADA
# ============================================================

print("\n=== EJEMPLO: API TIPADA ===\n")

from dataclasses import dataclass


@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int


def buscar_productos(
    catalogo: list[Producto],
    *,
    precio_max: float | None = None,
    en_stock: bool = True,
    ordenar_por: str = "nombre",
) -> list[Producto]:
    """
    Busca productos con filtros opcionales.

    Args:
        catalogo: Lista de productos disponibles.
        precio_max: Filtrar por precio máximo.
        en_stock: Si True, solo productos con stock > 0.
        ordenar_por: Campo para ordenar ('nombre', 'precio', 'stock').

    Returns:
        Lista filtrada y ordenada de productos.
    """
    resultado = catalogo.copy()

    if en_stock:
        resultado = [p for p in resultado if p.stock > 0]

    if precio_max is not None:
        resultado = [p for p in resultado if p.precio <= precio_max]

    campos: dict[str, Callable] = {
        "nombre": lambda p: p.nombre,
        "precio": lambda p: p.precio,
        "stock": lambda p: p.stock,
    }
    key_func = campos.get(ordenar_por, campos["nombre"])
    resultado.sort(key=key_func)

    return resultado


# Datos de prueba
catalogo: list[Producto] = [
    Producto("Laptop", 15000, 5),
    Producto("Mouse", 250, 50),
    Producto("Teclado", 800, 0),
    Producto("Monitor", 5000, 10),
    Producto("USB Cable", 50, 100),
]

baratos = buscar_productos(catalogo, precio_max=1000, ordenar_por="precio")
print("Productos baratos (< $1000) en stock:")
for p in baratos:
    print(f"  {p.nombre}: ${p.precio:.0f} ({p.stock} unidades)")
