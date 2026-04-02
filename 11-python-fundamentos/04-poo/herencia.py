"""
Herencia en Python
===================
Mecanismo que permite crear clases nuevas basadas en clases existentes,
reutilizando y extendiendo su funcionalidad.

Ejecuta este archivo:
    python herencia.py
"""

# ============================================================
# 1. HERENCIA SIMPLE
# ============================================================

print("=== HERENCIA SIMPLE ===\n")


class Animal:
    """Clase base para todos los animales."""

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        """Método que cada subclase debe personalizar."""
        return f"{self.nombre} hace algún sonido"

    def presentarse(self):
        return f"Soy {self.nombre}, tengo {self.edad} años"

    def __str__(self):
        return f"{type(self).__name__}({self.nombre})"


class Perro(Animal):
    """Hereda de Animal y agrega comportamiento específico."""

    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llama al __init__ del padre
        self.raza = raza

    def hablar(self):
        """Override: reemplaza el método del padre."""
        return f"{self.nombre} dice: ¡Guau!"

    def traer_pelota(self):
        """Método exclusivo de Perro."""
        return f"{self.nombre} trae la pelota 🎾"


class Gato(Animal):
    """Otra subclase de Animal."""

    def __init__(self, nombre, edad, es_interior=True):
        super().__init__(nombre, edad)
        self.es_interior = es_interior

    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"

    def ronronear(self):
        return f"{self.nombre} ronronea..."


# Crear instancias
perro = Perro("Rex", 5, "Pastor Alemán")
gato = Gato("Michi", 3)

print(f"{perro} — {perro.hablar()}")
print(f"{gato} — {gato.hablar()}")
print(f"Presentación: {perro.presentarse()}")  # Heredado de Animal
print(f"Exclusivo: {perro.traer_pelota()}")

# Verificar herencia
print(f"\n¿perro es Animal? {isinstance(perro, Animal)}")
print(f"¿perro es Perro? {isinstance(perro, Perro)}")
print(f"¿perro es Gato? {isinstance(perro, Gato)}")
print(f"¿Perro subclase de Animal? {issubclass(Perro, Animal)}")

# ============================================================
# 2. CADENA DE HERENCIA
# ============================================================

print("\n=== CADENA DE HERENCIA ===\n")


class PerroGuia(Perro):
    """Hereda de Perro, que hereda de Animal."""

    def __init__(self, nombre, edad, raza, certificado):
        super().__init__(nombre, edad, raza)
        self.certificado = certificado

    def hablar(self):
        """Los perros guía son más discretos."""
        return f"{self.nombre} (guía certificado) ladra suavemente"

    def guiar(self):
        return f"{self.nombre} guía a su dueño de forma segura"


guia = PerroGuia("Buddy", 4, "Golden Retriever", "CG-2024-001")
print(f"{guia}")
print(f"Hablar: {guia.hablar()}")
print(f"Guiar: {guia.guiar()}")
print(f"Presentarse: {guia.presentarse()}")  # De Animal (2 niveles arriba)
print(f"Traer pelota: {guia.traer_pelota()}")  # De Perro (1 nivel arriba)

# MRO (Method Resolution Order)
print(f"\nMRO de PerroGuia: {[c.__name__ for c in PerroGuia.__mro__]}")

# ============================================================
# 3. HERENCIA MÚLTIPLE
# ============================================================

print("\n=== HERENCIA MÚLTIPLE ===\n")


class Volador:
    def volar(self):
        return f"{self.nombre} está volando"


class Nadador:
    def nadar(self):
        return f"{self.nombre} está nadando"


class Pato(Animal, Volador, Nadador):
    """Hereda de Animal, Volador Y Nadador."""

    def hablar(self):
        return f"{self.nombre} dice: ¡Cuac!"


pato = Pato("Donald", 2)
print(f"{pato.hablar()}")
print(f"{pato.volar()}")
print(f"{pato.nadar()}")
print(f"MRO: {[c.__name__ for c in Pato.__mro__]}")

# ============================================================
# 4. MIXINS (patrón de herencia múltiple)
# ============================================================

print("\n=== MIXINS ===\n")


# Un Mixin es una clase que provee funcionalidad adicional
# sin ser una clase base por sí misma.

class SerializableMixin:
    """Mixin que agrega serialización JSON."""

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items()
                if not k.startswith("_")}

    def to_json(self):
        import json
        return json.dumps(self.to_dict(), default=str, ensure_ascii=False)


class LogMixin:
    """Mixin que agrega logging."""

    def log(self, mensaje):
        print(f"  [{type(self).__name__}] {mensaje}")


class Usuario(SerializableMixin, LogMixin):
    """Usa mixins para obtener serialización y logging."""

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def cambiar_email(self, nuevo_email):
        self.log(f"Cambiando email de {self.email} a {nuevo_email}")
        self.email = nuevo_email


user = Usuario("Ana", "ana@ejemplo.com")
print(f"Dict: {user.to_dict()}")
print(f"JSON: {user.to_json()}")
user.cambiar_email("ana.nueva@ejemplo.com")

# ============================================================
# 5. SUPER() EN DETALLE
# ============================================================

print("\n=== SUPER() EN DETALLE ===\n")


class Base:
    def __init__(self):
        print("  Base.__init__")
        self.base_attr = "base"


class MedioA(Base):
    def __init__(self):
        print("  MedioA.__init__")
        super().__init__()  # Llama al siguiente en MRO
        self.medio_a_attr = "A"


class MedioB(Base):
    def __init__(self):
        print("  MedioB.__init__")
        super().__init__()  # Llama al siguiente en MRO
        self.medio_b_attr = "B"


class Derivada(MedioA, MedioB):
    def __init__(self):
        print("  Derivada.__init__")
        super().__init__()  # Sigue el MRO
        self.derivada_attr = "D"


print("Orden de llamadas en __init__:")
d = Derivada()
print(f"\nMRO: {[c.__name__ for c in Derivada.__mro__]}")
# Derivada → MedioA → MedioB → Base → object
# super() sigue este orden, NO solo llama al "padre directo"

# ============================================================
# 6. EJEMPLO INTEGRADOR: SISTEMA DE EMPLEADOS
# ============================================================

print("\n=== EJEMPLO: SISTEMA DE EMPLEADOS ===\n")


class Empleado:
    """Clase base para todos los empleados."""

    _contador = 0

    def __init__(self, nombre, salario_base):
        Empleado._contador += 1
        self.id = Empleado._contador
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        """Las subclases pueden personalizar este cálculo."""
        return self.salario_base

    def __str__(self):
        return f"[{self.id}] {self.nombre} — ${self.calcular_salario():,.2f}"


class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_salario(self):
        return self.salario_base + self.bono


class Desarrollador(Empleado):
    def __init__(self, nombre, salario_base, horas_extra=0):
        super().__init__(nombre, salario_base)
        self.horas_extra = horas_extra

    def calcular_salario(self):
        pago_extra = self.horas_extra * (self.salario_base / 160) * 1.5
        return self.salario_base + pago_extra


class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, ventas, comision=0.05):
        super().__init__(nombre, salario_base)
        self.ventas = ventas
        self.comision = comision

    def calcular_salario(self):
        return self.salario_base + (self.ventas * self.comision)


# Crear empleados
equipo = [
    Gerente("Ana García", 50000, 15000),
    Desarrollador("Luis Pérez", 35000, 20),
    Desarrollador("Eva Ruiz", 38000, 0),
    Vendedor("Carlos López", 20000, 100000),
    Vendedor("Diana Soto", 20000, 250000),
]

print(f"{'Empleado':<25} {'Tipo':<15} {'Salario':>12}")
print("-" * 55)
for emp in equipo:
    print(f"{emp.nombre:<25} {type(emp).__name__:<15} ${emp.calcular_salario():>10,.2f}")

total = sum(e.calcular_salario() for e in equipo)
print(f"\n{'TOTAL NÓMINA':<40} ${total:>10,.2f}")
