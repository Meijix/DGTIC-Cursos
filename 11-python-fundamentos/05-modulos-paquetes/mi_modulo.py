"""
Mi Módulo — Ejemplo de módulo Python
======================================
Este archivo es un MÓDULO: un archivo .py que contiene código
reutilizable (funciones, clases, constantes).

Se puede importar desde otro archivo:
    from mi_modulo import factorial, es_primo

O ejecutar directamente:
    python mi_modulo.py
"""

# ============================================================
# CONSTANTES DEL MÓDULO
# ============================================================

VERSION = "1.0.0"
AUTOR = "Curso Python DGTIC"

# Constantes matemáticas
PI = 3.14159265358979
E = 2.71828182845905
PHI = 1.61803398874989  # Proporción áurea

# ============================================================
# FUNCIONES DEL MÓDULO
# ============================================================


def factorial(n):
    """
    Calcula el factorial de n (n!).

    Args:
        n: Entero no negativo.

    Returns:
        int: El factorial de n.

    Raises:
        ValueError: Si n es negativo.

    Ejemplos:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n < 0:
        raise ValueError(f"El factorial no está definido para números negativos: {n}")
    if n <= 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def fibonacci(n):
    """
    Genera los primeros n números de Fibonacci.

    Args:
        n: Cantidad de números a generar.

    Returns:
        list[int]: Lista con los primeros n números de Fibonacci.

    Ejemplos:
        >>> fibonacci(8)
        [0, 1, 1, 2, 3, 5, 8, 13]
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]

    fibs = [0, 1]
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def es_primo(n):
    """
    Verifica si un número es primo.

    Args:
        n: Entero a verificar.

    Returns:
        bool: True si n es primo.

    Ejemplos:
        >>> es_primo(7)
        True
        >>> es_primo(4)
        False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def primos_hasta(n):
    """
    Encuentra todos los números primos menores o iguales a n.
    Usa la Criba de Eratóstenes.

    Args:
        n: Límite superior.

    Returns:
        list[int]: Lista de primos <= n.
    """
    if n < 2:
        return []

    # Criba de Eratóstenes
    es_primo_arr = [True] * (n + 1)
    es_primo_arr[0] = es_primo_arr[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if es_primo_arr[i]:
            for j in range(i * i, n + 1, i):
                es_primo_arr[j] = False

    return [i for i, primo in enumerate(es_primo_arr) if primo]


def mcd(a, b):
    """Máximo Común Divisor usando el algoritmo de Euclides."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def mcm(a, b):
    """Mínimo Común Múltiplo."""
    return abs(a * b) // mcd(a, b)


# ============================================================
# CLASES DEL MÓDULO
# ============================================================


class Estadisticas:
    """Calculadora de estadísticas básicas."""

    def __init__(self, datos):
        if not datos:
            raise ValueError("La lista de datos no puede estar vacía")
        self.datos = sorted(datos)
        self.n = len(datos)

    @property
    def media(self):
        return sum(self.datos) / self.n

    @property
    def mediana(self):
        mid = self.n // 2
        if self.n % 2 == 0:
            return (self.datos[mid - 1] + self.datos[mid]) / 2
        return self.datos[mid]

    @property
    def rango(self):
        return self.datos[-1] - self.datos[0]

    def resumen(self):
        return {
            "n": self.n,
            "media": round(self.media, 2),
            "mediana": self.mediana,
            "min": self.datos[0],
            "max": self.datos[-1],
            "rango": self.rango,
        }


# ============================================================
# VARIABLE __all__ — controla "from mi_modulo import *"
# ============================================================

__all__ = [
    "factorial",
    "fibonacci",
    "es_primo",
    "primos_hasta",
    "mcd",
    "mcm",
    "Estadisticas",
    "PI",
    "E",
]

# ============================================================
# BLOQUE PRINCIPAL — solo se ejecuta al correr directamente
# ============================================================

if __name__ == "__main__":
    # Este código NO se ejecuta cuando el módulo es importado.
    # Solo cuando se ejecuta: python mi_modulo.py

    print(f"=== Mi Módulo v{VERSION} ===\n")

    # Tests rápidos
    print("--- Factorial ---")
    for n in [0, 1, 5, 10]:
        print(f"  {n}! = {factorial(n)}")

    print("\n--- Fibonacci ---")
    print(f"  Primeros 10: {fibonacci(10)}")

    print("\n--- Primos ---")
    print(f"  Primos hasta 50: {primos_hasta(50)}")

    print("\n--- MCD y MCM ---")
    print(f"  MCD(12, 18) = {mcd(12, 18)}")
    print(f"  MCM(12, 18) = {mcm(12, 18)}")

    print("\n--- Estadísticas ---")
    datos = [4, 8, 15, 16, 23, 42]
    stats = Estadisticas(datos)
    print(f"  Datos: {datos}")
    print(f"  Resumen: {stats.resumen()}")

    print("\n¡Todos los tests pasaron!")
