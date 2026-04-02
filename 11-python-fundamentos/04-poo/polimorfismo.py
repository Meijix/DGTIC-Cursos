"""
Polimorfismo en Python
========================
"Muchas formas": diferentes objetos responden al mismo mensaje
de maneras distintas. Python usa duck typing — no requiere
herencia formal para polimorfismo.

Ejecuta este archivo:
    python polimorfismo.py
"""

from abc import ABC, abstractmethod
import math

# ============================================================
# 1. POLIMORFISMO CON HERENCIA
# ============================================================

print("=== POLIMORFISMO CON HERENCIA ===\n")


class Forma(ABC):
    """Clase abstracta: define la interfaz que deben implementar las formas."""

    @abstractmethod
    def area(self) -> float:
        """Todas las formas deben calcular su área."""
        pass

    @abstractmethod
    def perimetro(self) -> float:
        """Todas las formas deben calcular su perímetro."""
        pass

    def descripcion(self) -> str:
        """Método concreto compartido por todas las formas."""
        return (f"{type(self).__name__}: "
                f"área={self.area():.2f}, perímetro={self.perimetro():.2f}")


class Circulo(Forma):
    def __init__(self, radio: float):
        self.radio = radio

    def area(self) -> float:
        return math.pi * self.radio ** 2

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio


class Rectangulo(Forma):
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    def area(self) -> float:
        return self.ancho * self.alto

    def perimetro(self) -> float:
        return 2 * (self.ancho + self.alto)


class Triangulo(Forma):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        # Fórmula de Herón
        s = self.perimetro() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimetro(self) -> float:
        return self.a + self.b + self.c


# Polimorfismo en acción: mismo código, diferentes tipos
formas: list[Forma] = [
    Circulo(5),
    Rectangulo(4, 6),
    Triangulo(3, 4, 5),
    Circulo(10),
    Rectangulo(8, 3),
]

print(f"{'Forma':<25} {'Área':>10} {'Perímetro':>10}")
print("-" * 48)
for forma in formas:
    print(f"{forma.descripcion()}")

# Área total — funciona con cualquier forma
area_total = sum(f.area() for f in formas)
print(f"\nÁrea total: {area_total:.2f}")

# La mayor forma
mayor = max(formas, key=lambda f: f.area())
print(f"Mayor por área: {mayor.descripcion()}")

# ============================================================
# 2. DUCK TYPING
# ============================================================

print("\n=== DUCK TYPING ===\n")


# "Si camina como pato y grazna como pato, es un pato."
# No necesitamos herencia — solo que el objeto tenga los métodos correctos.

class Archivo:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano

    def leer(self):
        return f"Leyendo archivo {self.nombre}"


class ConexionHTTP:
    def __init__(self, url):
        self.nombre = url
        self.tamano = 0

    def leer(self):
        return f"Leyendo datos de {self.nombre}"


class StringIO:
    def __init__(self, contenido):
        self.nombre = "<string>"
        self.tamano = len(contenido)
        self._contenido = contenido

    def leer(self):
        return f"Leyendo string: {self._contenido[:50]}"


def procesar_fuente(fuente):
    """Funciona con cualquier objeto que tenga .nombre y .leer()."""
    print(f"  Fuente: {fuente.nombre}")
    print(f"  {fuente.leer()}")


# Tres tipos completamente distintos — misma interfaz
fuentes = [
    Archivo("datos.csv", 1024),
    ConexionHTTP("https://api.ejemplo.com/datos"),
    StringIO("Estos son datos en memoria"),
]

for fuente in fuentes:
    procesar_fuente(fuente)
    print()

# ============================================================
# 3. PROTOCOLOS (INTERFACES IMPLÍCITAS)
# ============================================================

print("=== PROTOCOLOS ===\n")


# Python tiene protocolos built-in que cualquier clase puede implementar.

class Rango:
    """Implementa el protocolo de secuencia."""

    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin
        self._datos = list(range(inicio, fin))

    def __len__(self):
        """Protocolo de tamaño: len(obj)"""
        return len(self._datos)

    def __getitem__(self, indice):
        """Protocolo de acceso: obj[i]"""
        return self._datos[indice]

    def __contains__(self, valor):
        """Protocolo de pertenencia: x in obj"""
        return valor in self._datos

    def __iter__(self):
        """Protocolo de iteración: for x in obj"""
        return iter(self._datos)


r = Rango(1, 6)
print(f"len(r): {len(r)}")
print(f"r[0]: {r[0]}")
print(f"r[-1]: {r[-1]}")
print(f"3 in r: {3 in r}")
print(f"10 in r: {10 in r}")
print(f"list(r): {list(r)}")
print(f"sum(r): {sum(r)}")  # Funciona porque es iterable

# ============================================================
# 4. POLIMORFISMO CON FUNCIONES BUILT-IN
# ============================================================

print("\n=== POLIMORFISMO BUILT-IN ===\n")

# len() funciona con muchos tipos — eso es polimorfismo
print(f"len('hola'):      {len('hola')}")
print(f"len([1,2,3]):     {len([1, 2, 3])}")
print(f"len({{'a':1}}):     {len({'a': 1})}")

# + funciona diferente según el tipo
print(f"1 + 2:            {1 + 2}")
print(f"'ho' + 'la':      {'ho' + 'la'}")
print(f"[1] + [2]:        {[1] + [2]}")

# sorted() funciona con cualquier iterable comparable
print(f"sorted('python'): {sorted('python')}")
print(f"sorted([3,1,2]):  {sorted([3, 1, 2])}")

# ============================================================
# 5. EJEMPLO INTEGRADOR: PROCESADOR DE PAGOS
# ============================================================

print("\n=== EJEMPLO: PROCESADOR DE PAGOS ===\n")


class MetodoPago(ABC):
    """Interfaz abstracta para métodos de pago."""

    @abstractmethod
    def procesar(self, monto: float) -> bool:
        pass

    @abstractmethod
    def nombre_metodo(self) -> str:
        pass


class TarjetaCredito(MetodoPago):
    def __init__(self, numero: str, titular: str):
        self.numero = numero
        self.titular = titular

    def procesar(self, monto: float) -> bool:
        # Simulación
        print(f"  Procesando ${monto:,.2f} con tarjeta ****{self.numero[-4:]}")
        return monto <= 50000

    def nombre_metodo(self) -> str:
        return f"Tarjeta ****{self.numero[-4:]}"


class PayPal(MetodoPago):
    def __init__(self, email: str):
        self.email = email

    def procesar(self, monto: float) -> bool:
        print(f"  Procesando ${monto:,.2f} vía PayPal ({self.email})")
        return monto <= 30000

    def nombre_metodo(self) -> str:
        return f"PayPal ({self.email})"


class Transferencia(MetodoPago):
    def __init__(self, banco: str, clabe: str):
        self.banco = banco
        self.clabe = clabe

    def procesar(self, monto: float) -> bool:
        print(f"  Procesando ${monto:,.2f} por transferencia ({self.banco})")
        return True  # Sin límite

    def nombre_metodo(self) -> str:
        return f"Transferencia {self.banco}"


def realizar_pago(metodo: MetodoPago, monto: float) -> None:
    """Función polimórfica: funciona con cualquier MetodoPago."""
    print(f"\nIntentando cobrar ${monto:,.2f} con {metodo.nombre_metodo()}")
    if metodo.procesar(monto):
        print(f"  Pago EXITOSO")
    else:
        print(f"  Pago RECHAZADO (monto excede límite)")


# Diferentes métodos de pago — misma interfaz
metodos: list[MetodoPago] = [
    TarjetaCredito("4111111111111234", "Ana García"),
    PayPal("ana@ejemplo.com"),
    Transferencia("BBVA", "012180001234567890"),
]

# Procesar pagos de diferentes montos
for metodo in metodos:
    realizar_pago(metodo, 25000)
