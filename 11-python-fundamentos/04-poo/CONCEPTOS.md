# 04 — Programación Orientada a Objetos (POO)

## Índice

1. [Clases y Objetos](#clases-y-objetos)
2. [Atributos y Métodos](#atributos-y-métodos)
3. [Encapsulamiento](#encapsulamiento)
4. [Herencia](#herencia)
5. [Polimorfismo](#polimorfismo)
6. [Magic Methods (Métodos Dunder)](#magic-methods)
7. [Decoradores de Clase](#decoradores-de-clase)
8. [Clases Abstractas](#clases-abstractas)
9. [Dataclasses](#dataclasses)
10. [Errores Comunes](#errores-comunes)
11. [Ejercicios](#ejercicios)

---

## Clases y Objetos

Una **clase** es un molde para crear objetos. Un **objeto** (instancia) es
una entidad con estado (atributos) y comportamiento (métodos).

```
  Clase "Perro" (molde)            Objetos (instancias)
  ┌────────────────────┐           ┌──────────────────┐
  │ Atributos:         │           │ firulais         │
  │   nombre           │──────────▶│ nombre="Firulais"│
  │   raza             │           │ raza="Labrador"  │
  │   edad             │           └──────────────────┘
  │                    │           ┌──────────────────┐
  │ Métodos:           │──────────▶│ rex              │
  │   ladrar()         │           │ nombre="Rex"     │
  │   sentarse()       │           │ raza="Pastor"    │
  └────────────────────┘           └──────────────────┘
```

---

## Atributos y Métodos

### Tipos de atributos

| Tipo | Pertenece a | Acceso | Ejemplo |
|------|-------------|--------|---------|
| De instancia | Cada objeto | `self.nombre` | Nombre del perro |
| De clase | La clase (compartido) | `Perro.total` | Contador total |

### Tipos de métodos

| Decorador | Primer param | Acceso | Uso |
|-----------|--------------|--------|-----|
| (ninguno) | `self` | Instancia y clase | Operaciones normales |
| `@classmethod` | `cls` | Solo clase | Factory methods |
| `@staticmethod` | (ninguno) | Ninguno | Utilidades relacionadas |

---

## Encapsulamiento

Python usa **convenciones** en vez de restricciones fuertes:

| Prefijo | Significado | Ejemplo | Acceso |
|---------|-------------|---------|--------|
| (sin prefijo) | Público | `self.nombre` | Libre |
| `_` | Protegido (convención) | `self._edad` | "No toques desde fuera" |
| `__` | Privado (name mangling) | `self.__saldo` | `obj._Clase__saldo` |

### @property — Getters/Setters pythónicos

```python
class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor
```

---

## Herencia

```
        Animal
       /      \
    Perro     Gato
      |
  PerroGuía
```

```python
class Animal:
    def hablar(self):
        raise NotImplementedError

class Perro(Animal):
    def hablar(self):
        return "¡Guau!"

class Gato(Animal):
    def hablar(self):
        return "¡Miau!"
```

### super() — Llamar al método de la clase padre

```python
class PerroGuia(Perro):
    def __init__(self, nombre, certificado):
        super().__init__(nombre)  # Llama a Perro.__init__
        self.certificado = certificado
```

### MRO — Method Resolution Order

Python usa el algoritmo C3 para resolver herencia múltiple:

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
# D → B → C → A → object
```

---

## Polimorfismo

Diferentes clases responden al mismo mensaje (método) de forma distinta.

```python
animales = [Perro("Rex"), Gato("Michi")]
for animal in animales:
    print(animal.hablar())  # Cada uno responde diferente
```

### Duck Typing

"Si camina como pato y grazna como pato, es un pato."

Python no requiere herencia para polimorfismo — solo que el objeto
tenga los métodos/atributos esperados.

---

## Magic Methods

Métodos especiales con doble guión bajo que Python llama automáticamente.

| Método | Cuándo se llama | Ejemplo |
|--------|-----------------|---------|
| `__init__` | Al crear instancia | `obj = Clase()` |
| `__str__` | `str(obj)` / `print(obj)` | Representación legible |
| `__repr__` | `repr(obj)` / en REPL | Representación técnica |
| `__eq__` | `obj1 == obj2` | Igualdad |
| `__lt__` | `obj1 < obj2` | Menor que |
| `__len__` | `len(obj)` | Longitud |
| `__getitem__` | `obj[key]` | Acceso por índice |
| `__contains__` | `x in obj` | Pertenencia |
| `__add__` | `obj1 + obj2` | Suma |
| `__iter__` | `for x in obj` | Iteración |
| `__call__` | `obj()` | Llamar como función |
| `__enter__/__exit__` | `with obj` | Context manager |

---

## Clases Abstractas

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

# forma = Forma()  # TypeError: no se puede instanciar
```

---

## Dataclasses

Desde Python 3.7, `@dataclass` genera automáticamente `__init__`, `__repr__`,
`__eq__` y más.

```python
from dataclasses import dataclass

@dataclass
class Punto:
    x: float
    y: float

p = Punto(3, 4)  # No necesitas escribir __init__
```

---

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| Olvidar `self` | Método sin primer parámetro self | `def metodo(self, ...)` |
| Mutable compartido | Atributo de clase mutable | Inicializar en `__init__` |
| `super()` mal usado | No pasar argumentos correctos | `super().__init__(args)` |
| `__str__` vs `__repr__` | No implementar ambos | `__repr__` para debugging, `__str__` para usuario |
| Herencia diamante | Conflicto en herencia múltiple | Verificar MRO, usar super() |

---

## Ejercicios

### Nivel 1
1. Crea una clase `Rectangulo` con ancho y alto, métodos `area()` y `perimetro()`.
2. Implementa `__str__` y `__repr__` para la clase Rectángulo.
3. Crea una clase `CuentaBancaria` con depósito, retiro y consulta de saldo.

### Nivel 2
4. Crea una jerarquía: `Vehiculo` → `Auto`, `Moto`, `Camion`. Cada uno con `info()`.
5. Implementa `__eq__` y `__lt__` para una clase `Fraccion`.
6. Crea una clase `Pila` (stack) con `push`, `pop`, `peek`, `len()` y soporte para `in`.

### Nivel 3
7. Diseña un sistema de figuras geométricas con clases abstractas: `Circulo`, `Rectangulo`, `Triangulo`, todos con `area()` y `perimetro()`.
8. Implementa una clase `Vector` con operaciones: suma, resta, producto punto, magnitud, usando magic methods.
9. Usa `@dataclass` para modelar un sistema de biblioteca (Libro, Autor, Préstamo).

### Nivel 4
10. Implementa el patrón Observer usando POO.
11. Crea una clase `Matrix` con soporte para suma, multiplicación, transposición e indexación.
