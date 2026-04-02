"""
Magic Methods (Métodos Dunder) en Python
==========================================
Métodos especiales con doble guión bajo que Python llama
automáticamente en ciertas operaciones. Permiten que tus
clases se integren naturalmente con la sintaxis del lenguaje.

Ejecuta este archivo:
    python magic_methods.py
"""

import math
from functools import total_ordering

# ============================================================
# 1. __str__ y __repr__
# ============================================================

print("=== __str__ y __repr__ ===\n")


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Para humanos: print(), str(), f-string."""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Para desarrolladores: REPL, debugging, repr()."""
        return f"Punto(x={self.x}, y={self.y})"


p = Punto(3, 4)
print(f"str:  {p}")           # Llama a __str__
print(f"repr: {p!r}")         # Llama a __repr__
print(f"repr: {repr(p)}")     # También __repr__
# En el REPL, escribir 'p' muestra __repr__

# Si no defines __str__, Python usa __repr__ como fallback.

# ============================================================
# 2. OPERADORES ARITMÉTICOS
# ============================================================

print("\n=== OPERADORES ARITMÉTICOS ===\n")


class Vector:
    """Vector 2D con soporte completo de operadores."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # --- Operadores aritméticos ---
    def __add__(self, otro):
        """self + otro"""
        if isinstance(otro, Vector):
            return Vector(self.x + otro.x, self.y + otro.y)
        return NotImplemented

    def __sub__(self, otro):
        """self - otro"""
        if isinstance(otro, Vector):
            return Vector(self.x - otro.x, self.y - otro.y)
        return NotImplemented

    def __mul__(self, escalar):
        """self * escalar"""
        if isinstance(escalar, (int, float)):
            return Vector(self.x * escalar, self.y * escalar)
        return NotImplemented

    def __rmul__(self, escalar):
        """escalar * self (cuando el escalar está a la izquierda)."""
        return self.__mul__(escalar)

    def __neg__(self):
        """-self"""
        return Vector(-self.x, -self.y)

    def __abs__(self):
        """abs(self) — magnitud del vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # --- Comparación ---
    def __eq__(self, otro):
        """self == otro"""
        if isinstance(otro, Vector):
            return self.x == otro.x and self.y == otro.y
        return NotImplemented

    # --- Representación ---
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # --- Otros ---
    def __bool__(self):
        """bool(self) — False si es el vector nulo."""
        return self.x != 0 or self.y != 0

    def __hash__(self):
        """Necesario si defines __eq__ y quieres usar en sets/dicts."""
        return hash((self.x, self.y))

    # Método adicional
    def punto(self, otro):
        """Producto punto."""
        return self.x * otro.x + self.y * otro.y


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 3 = {v1 * 3}")
print(f"3 * v1 = {3 * v1}")       # Usa __rmul__
print(f"-v1 = {-v1}")
print(f"|v1| = {abs(v1)}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == Vector(3,4): {v1 == Vector(3, 4)}")
print(f"v1 · v2 = {v1.punto(v2)}")
print(f"bool(Vector(0,0)): {bool(Vector(0, 0))}")

# ============================================================
# 3. OPERADORES DE COMPARACIÓN
# ============================================================

print("\n=== OPERADORES DE COMPARACIÓN ===\n")


@total_ordering  # Genera __le__, __gt__, __ge__ a partir de __eq__ y __lt__
class Temperatura:
    """Temperatura con comparaciones completas."""

    def __init__(self, grados, escala="C"):
        self.grados = grados
        self.escala = escala

    def _a_celsius(self):
        if self.escala == "C":
            return self.grados
        elif self.escala == "F":
            return (self.grados - 32) * 5 / 9
        elif self.escala == "K":
            return self.grados - 273.15
        raise ValueError(f"Escala desconocida: {self.escala}")

    def __eq__(self, otra):
        if isinstance(otra, Temperatura):
            return abs(self._a_celsius() - otra._a_celsius()) < 0.01
        return NotImplemented

    def __lt__(self, otra):
        if isinstance(otra, Temperatura):
            return self._a_celsius() < otra._a_celsius()
        return NotImplemented

    def __str__(self):
        return f"{self.grados}°{self.escala}"

    def __repr__(self):
        return f"Temperatura({self.grados}, {self.escala!r})"


t1 = Temperatura(100, "C")
t2 = Temperatura(212, "F")
t3 = Temperatura(373.15, "K")
t4 = Temperatura(0, "C")

print(f"100°C == 212°F: {t1 == t2}")     # True
print(f"100°C == 373.15K: {t1 == t3}")   # True
print(f"0°C < 100°C: {t4 < t1}")         # True
print(f"100°C > 0°C: {t1 > t4}")         # True (generado por @total_ordering)
print(f"Ordenar: {sorted([t1, t4, t3, t2])}")

# ============================================================
# 4. __getitem__, __setitem__, __len__
# ============================================================

print("\n=== ACCESO POR ÍNDICE ===\n")


class Matriz:
    """Matriz 2D con acceso por índice."""

    def __init__(self, filas, columnas, valor_default=0):
        self.filas = filas
        self.columnas = columnas
        self._datos = [[valor_default] * columnas for _ in range(filas)]

    def __getitem__(self, pos):
        """m[fila, col] o m[fila]"""
        if isinstance(pos, tuple):
            fila, col = pos
            return self._datos[fila][col]
        return self._datos[pos]

    def __setitem__(self, pos, valor):
        """m[fila, col] = valor"""
        if isinstance(pos, tuple):
            fila, col = pos
            self._datos[fila][col] = valor
        else:
            self._datos[pos] = valor

    def __len__(self):
        """len(m) — número total de elementos."""
        return self.filas * self.columnas

    def __contains__(self, valor):
        """valor in m"""
        return any(valor in fila for fila in self._datos)

    def __str__(self):
        lineas = []
        for fila in self._datos:
            lineas.append("  [" + ", ".join(f"{v:4}" for v in fila) + "]")
        return "[\n" + "\n".join(lineas) + "\n]"


m = Matriz(3, 3)
m[0, 0] = 1
m[1, 1] = 5
m[2, 2] = 9
m[0, 2] = 3

print(f"Matriz:\n{m}")
print(f"m[1,1] = {m[1, 1]}")
print(f"len(m) = {len(m)}")
print(f"5 in m: {5 in m}")
print(f"7 in m: {7 in m}")

# ============================================================
# 5. __call__ — OBJETOS INVOCABLES
# ============================================================

print("\n=== __call__ ===\n")


class Promediador:
    """Objeto que acumula valores y calcula promedio."""

    def __init__(self):
        self._valores = []

    def __call__(self, valor):
        """Permite usar el objeto como función."""
        self._valores.append(valor)
        return sum(self._valores) / len(self._valores)

    def __str__(self):
        return f"Promedio de {len(self._valores)} valores: {self():.2f}" if self._valores else "Sin datos"

    def __len__(self):
        return len(self._valores)


promedio = Promediador()
print(f"Agregar 10: {promedio(10):.2f}")
print(f"Agregar 20: {promedio(20):.2f}")
print(f"Agregar 30: {promedio(30):.2f}")
print(f"Agregar 40: {promedio(40):.2f}")
print(f"Valores acumulados: {len(promedio)}")

# Es callable:
print(f"¿Es callable? {callable(promedio)}")

# ============================================================
# 6. CONTEXT MANAGER: __enter__ / __exit__
# ============================================================

print("\n=== CONTEXT MANAGER ===\n")


class Timer:
    """Mide el tiempo de ejecución usando 'with'."""

    def __init__(self, nombre=""):
        self.nombre = nombre

    def __enter__(self):
        """Se ejecuta al entrar al bloque 'with'."""
        import time
        self._inicio = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Se ejecuta al salir del bloque 'with'."""
        import time
        self.duracion = time.perf_counter() - self._inicio
        etiqueta = f" ({self.nombre})" if self.nombre else ""
        print(f"  Timer{etiqueta}: {self.duracion:.4f}s")
        return False  # No suprimir excepciones


with Timer("cuadrados"):
    resultado = [x**2 for x in range(100_000)]

with Timer("suma"):
    total = sum(range(1_000_000))

# ============================================================
# 7. __iter__ y __next__
# ============================================================

print("\n=== ITERADOR PERSONALIZADO ===\n")


class Fibonacci:
    """Genera números de Fibonacci como iterador."""

    def __init__(self, maximo):
        self.maximo = maximo

    def __iter__(self):
        self.a, self.b = 0, 1
        self.count = 0
        return self

    def __next__(self):
        if self.count >= self.maximo:
            raise StopIteration
        valor = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return valor


fib = Fibonacci(10)
print(f"Primeros 10 Fibonacci: {list(fib)}")

# Funciona en for:
print("Fibonacci < 100:", end=" ")
for n in Fibonacci(20):
    if n >= 100:
        break
    print(n, end=" ")
print()
