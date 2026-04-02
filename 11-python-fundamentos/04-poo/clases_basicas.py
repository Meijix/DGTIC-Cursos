"""
Clases Básicas en Python
==========================
Fundamentos de la Programación Orientada a Objetos:
clases, instancias, atributos, métodos y encapsulamiento.

Ejecuta este archivo:
    python clases_basicas.py
"""

# ============================================================
# 1. DEFINICIÓN BÁSICA DE UNA CLASE
# ============================================================

print("=== CLASE BÁSICA ===\n")


class Perro:
    """Representa un perro con nombre, raza y edad."""

    # Atributo de CLASE (compartido por todas las instancias)
    especie = "Canis lupus familiaris"
    total_perros = 0

    def __init__(self, nombre, raza, edad=0):
        """Constructor: se llama al crear cada instancia."""
        # Atributos de INSTANCIA (únicos para cada objeto)
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self._energia = 100       # Protegido (convención)
        self.__vacunas = []       # Privado (name mangling)

        # Modificar atributo de clase
        Perro.total_perros += 1

    def ladrar(self):
        """Método de instancia: opera sobre self."""
        if self._energia < 10:
            return f"{self.nombre} está muy cansado para ladrar"
        self._energia -= 10
        return f"{self.nombre} dice: ¡Guau! ¡Guau!"

    def comer(self, alimento):
        """Otro método de instancia."""
        self._energia = min(100, self._energia + 20)
        return f"{self.nombre} come {alimento}. Energía: {self._energia}"

    def info(self):
        """Muestra información del perro."""
        return f"{self.nombre} ({self.raza}), {self.edad} años, energía: {self._energia}"

    def __str__(self):
        """Representación legible (para print y str())."""
        return f"Perro({self.nombre}, {self.raza})"

    def __repr__(self):
        """Representación técnica (para debugging)."""
        return f"Perro(nombre={self.nombre!r}, raza={self.raza!r}, edad={self.edad})"


# Crear instancias
firulais = Perro("Firulais", "Labrador", 3)
rex = Perro("Rex", "Pastor Alemán", 5)

print(f"str:  {firulais}")
print(f"repr: {repr(firulais)}")
print(f"Info: {firulais.info()}")
print(f"Ladrar: {firulais.ladrar()}")
print(f"Comer: {firulais.comer('croquetas')}")
print(f"\nTotal perros creados: {Perro.total_perros}")
print(f"Especie: {Perro.especie}")

# ============================================================
# 2. ENCAPSULAMIENTO Y PROPIEDADES
# ============================================================

print("\n=== ENCAPSULAMIENTO ===\n")


class CuentaBancaria:
    """Cuenta bancaria con encapsulamiento."""

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular         # Público
        self._saldo = saldo_inicial    # Protegido
        self.__pin = "1234"            # Privado (name mangling)
        self._historial = []

    @property
    def saldo(self):
        """Getter: acceder a saldo como si fuera un atributo."""
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        """Setter: validar antes de asignar."""
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

    @property
    def historial(self):
        """Solo lectura: sin setter, no se puede asignar."""
        return self._historial.copy()  # Retorna copia para proteger el original

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self._saldo += cantidad
        self._historial.append(f"+${cantidad:,.2f}")
        return self._saldo

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self._saldo:
            raise ValueError("Fondos insuficientes")
        self._saldo -= cantidad
        self._historial.append(f"-${cantidad:,.2f}")
        return self._saldo

    def __str__(self):
        return f"Cuenta de {self.titular}: ${self._saldo:,.2f}"


cuenta = CuentaBancaria("Ana García", 1000)
print(cuenta)

# Usar el property (se ve como atributo pero ejecuta el getter)
print(f"Saldo: ${cuenta.saldo:,.2f}")

cuenta.depositar(500)
cuenta.retirar(200)
print(f"Después de operaciones: {cuenta}")
print(f"Historial: {cuenta.historial}")

# El setter valida:
# cuenta.saldo = -100  # ValueError

# Name mangling: el atributo privado se renombra
# print(cuenta.__pin)  # AttributeError
# Pero se puede acceder (NO recomendado):
print(f"PIN (acceso forzado): {cuenta._CuentaBancaria__pin}")

# ============================================================
# 3. MÉTODOS DE CLASE Y ESTÁTICOS
# ============================================================

print("\n=== CLASSMETHOD Y STATICMETHOD ===\n")


class Fecha:
    """Ejemplo de métodos de clase y estáticos."""

    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    @classmethod
    def desde_string(cls, fecha_str):
        """Factory method: crea una Fecha desde un string 'dd/mm/aaaa'."""
        dia, mes, anio = map(int, fecha_str.split("/"))
        return cls(dia, mes, anio)  # cls es la clase (Fecha)

    @classmethod
    def hoy(cls):
        """Factory method: crea la fecha de hoy."""
        from datetime import date
        today = date.today()
        return cls(today.day, today.month, today.year)

    @staticmethod
    def es_bisiesto(anio):
        """Método estático: no necesita self ni cls."""
        return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"


# Usar constructor normal
f1 = Fecha(25, 12, 2024)
print(f"Constructor: {f1}")

# Usar factory method (classmethod)
f2 = Fecha.desde_string("15/09/2025")
print(f"Desde string: {f2}")

f3 = Fecha.hoy()
print(f"Hoy: {f3}")

# Usar staticmethod (no necesita instancia)
print(f"¿2024 es bisiesto? {Fecha.es_bisiesto(2024)}")
print(f"¿2023 es bisiesto? {Fecha.es_bisiesto(2023)}")

# ============================================================
# 4. ATRIBUTOS DE CLASE vs INSTANCIA
# ============================================================

print("\n=== ATRIBUTOS DE CLASE vs INSTANCIA ===\n")


class Configuracion:
    """Demuestra la diferencia entre atributos de clase e instancia."""

    # Atributo de clase — compartido
    version = "1.0"
    instancias = 0

    # CUIDADO con mutables como atributo de clase
    # opciones_default = []  # MAL: todas las instancias comparten la misma lista

    def __init__(self, nombre):
        self.nombre = nombre              # Atributo de instancia
        self.opciones = []                 # Cada instancia tiene su propia lista
        Configuracion.instancias += 1

    def __str__(self):
        return f"Config({self.nombre}, v{self.version})"


c1 = Configuracion("producción")
c2 = Configuracion("desarrollo")

c1.opciones.append("debug=False")
c2.opciones.append("debug=True")

print(f"c1: {c1}, opciones: {c1.opciones}")
print(f"c2: {c2}, opciones: {c2.opciones}")
print(f"Instancias creadas: {Configuracion.instancias}")
print(f"Versión (clase): {Configuracion.version}")

# Si asignas un atributo de clase a una instancia, crea uno NUEVO de instancia
c1.version = "2.0"  # Crea atributo de instancia, NO modifica el de clase
print(f"\nc1.version: {c1.version}")            # 2.0 (instancia)
print(f"c2.version: {c2.version}")              # 1.0 (clase)
print(f"Configuracion.version: {Configuracion.version}")  # 1.0 (clase)
