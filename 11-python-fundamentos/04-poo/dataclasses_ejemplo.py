"""
Dataclasses en Python
======================
Desde Python 3.7, @dataclass genera automáticamente __init__,
__repr__, __eq__ y más. Ideal para clases que principalmente
almacenan datos.

Ejecuta este archivo:
    python dataclasses_ejemplo.py
"""

from dataclasses import dataclass, field, asdict, astuple
from typing import ClassVar

# ============================================================
# 1. DATACLASS BÁSICA
# ============================================================

print("=== DATACLASS BÁSICA ===\n")


@dataclass
class Punto:
    """Un punto en 2D. @dataclass genera __init__, __repr__, __eq__."""
    x: float
    y: float


# __init__ generado automáticamente
p1 = Punto(3, 4)
p2 = Punto(3, 4)
p3 = Punto(1, 2)

print(f"p1 = {p1}")               # __repr__ generado
print(f"p1 == p2: {p1 == p2}")    # __eq__ generado: compara campo a campo
print(f"p1 == p3: {p1 == p3}")

# ============================================================
# 2. VALORES POR DEFECTO
# ============================================================

print("\n=== VALORES POR DEFECTO ===\n")


@dataclass
class Configuracion:
    """Configuración con valores por defecto."""
    host: str = "localhost"
    port: int = 8080
    debug: bool = False
    workers: int = 4


# Se pueden crear con defaults parciales
cfg1 = Configuracion()
cfg2 = Configuracion(host="0.0.0.0", debug=True)

print(f"Default:      {cfg1}")
print(f"Personalizado: {cfg2}")

# ============================================================
# 3. FIELD() — CONTROL AVANZADO
# ============================================================

print("\n=== FIELD() ===\n")


@dataclass
class Estudiante:
    """Estudiante con control avanzado de campos."""
    nombre: str
    matricula: str
    # Campos con default factory (para mutables)
    calificaciones: list[float] = field(default_factory=list)
    # Campo excluido de __repr__
    _cache: dict = field(default_factory=dict, repr=False)
    # Campo excluido de __init__ y __repr__
    _promedio_cache: float | None = field(default=None, init=False, repr=False)

    # Variable de clase (no es un campo)
    total: ClassVar[int] = 0

    def __post_init__(self):
        """Se ejecuta después del __init__ generado."""
        Estudiante.total += 1

    @property
    def promedio(self) -> float:
        if not self.calificaciones:
            return 0.0
        if self._promedio_cache is None:
            self._promedio_cache = sum(self.calificaciones) / len(self.calificaciones)
        return self._promedio_cache

    def agregar_calificacion(self, calif: float):
        self.calificaciones.append(calif)
        self._promedio_cache = None  # Invalidar cache


e1 = Estudiante("Ana", "A001", [95, 88, 92])
e2 = Estudiante("Luis", "A002")

print(f"e1 = {e1}")
print(f"e2 = {e2}")
print(f"Promedio e1: {e1.promedio:.2f}")

e2.agregar_calificacion(85)
e2.agregar_calificacion(90)
print(f"Promedio e2: {e2.promedio:.2f}")
print(f"Total estudiantes: {Estudiante.total}")

# ============================================================
# 4. FROZEN (INMUTABLE)
# ============================================================

print("\n=== FROZEN (INMUTABLE) ===\n")


@dataclass(frozen=True)
class Color:
    """Color inmutable — no se pueden modificar sus campos."""
    rojo: int
    verde: int
    azul: int

    def __post_init__(self):
        # Validación en frozen dataclass
        for campo, valor in [("rojo", self.rojo), ("verde", self.verde), ("azul", self.azul)]:
            if not 0 <= valor <= 255:
                raise ValueError(f"{campo} debe estar entre 0 y 255, recibido: {valor}")

    @property
    def hex(self) -> str:
        return f"#{self.rojo:02x}{self.verde:02x}{self.azul:02x}"


rojo = Color(255, 0, 0)
azul = Color(0, 0, 255)

print(f"Rojo: {rojo} → {rojo.hex}")
print(f"Azul: {azul} → {azul.hex}")

# No se puede modificar:
# rojo.rojo = 128  # FrozenInstanceError

# Al ser inmutable, es hashable → puede ser clave de dict o elemento de set
colores = {rojo: "rojo", azul: "azul"}
print(f"colores[Color(255,0,0)] = {colores[Color(255, 0, 0)]}")

# ============================================================
# 5. ORDEN (@dataclass(order=True))
# ============================================================

print("\n=== ORDENAMIENTO ===\n")


@dataclass(order=True)
class Version:
    """Versión semántica con ordenamiento automático."""
    # Los campos se comparan en orden de declaración
    major: int
    minor: int
    patch: int

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"


versiones = [
    Version(2, 0, 0),
    Version(1, 9, 1),
    Version(1, 10, 0),
    Version(1, 9, 0),
    Version(3, 0, 1),
]

print(f"Versiones ordenadas: {sorted(versiones)}")
print(f"Última: {max(versiones)}")
print(f"1.9.0 < 1.9.1: {Version(1,9,0) < Version(1,9,1)}")

# ============================================================
# 6. CONVERSIÓN A DICT Y TUPLE
# ============================================================

print("\n=== CONVERSIÓN ===\n")


@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int
    categoria: str = "general"


producto = Producto("Laptop", 15000, 10, "electrónica")

# Convertir a diccionario
como_dict = asdict(producto)
print(f"Como dict: {como_dict}")

# Convertir a tupla
como_tuple = astuple(producto)
print(f"Como tuple: {como_tuple}")

# Útil para serialización JSON
import json
json_str = json.dumps(como_dict, ensure_ascii=False)
print(f"Como JSON: {json_str}")

# ============================================================
# 7. HERENCIA CON DATACLASSES
# ============================================================

print("\n=== HERENCIA ===\n")


@dataclass
class PersonaBase:
    nombre: str
    edad: int


@dataclass
class EmpleadoData(PersonaBase):
    puesto: str = "Sin asignar"
    salario: float = 0.0


emp = EmpleadoData("Ana García", 30, "Desarrolladora", 45000)
print(f"Empleado: {emp}")
print(f"Es PersonaBase: {isinstance(emp, PersonaBase)}")

# ============================================================
# 8. EJEMPLO INTEGRADOR: SISTEMA DE TAREAS
# ============================================================

print("\n=== EJEMPLO: SISTEMA DE TAREAS ===\n")

from datetime import datetime, timedelta
from enum import Enum


class Prioridad(Enum):
    BAJA = 1
    MEDIA = 2
    ALTA = 3
    URGENTE = 4


@dataclass(order=True)
class Tarea:
    """Tarea con prioridad y fecha límite."""
    # sort_index se usa para ordenamiento pero no para init/repr
    sort_index: tuple = field(init=False, repr=False)

    titulo: str
    prioridad: Prioridad = Prioridad.MEDIA
    completada: bool = False
    fecha_limite: datetime | None = None
    etiquetas: list[str] = field(default_factory=list)

    def __post_init__(self):
        # Ordenar por: prioridad (desc), fecha límite (asc)
        fecha_sort = self.fecha_limite or datetime.max
        self.sort_index = (-self.prioridad.value, fecha_sort)

    def completar(self):
        self.completada = True

    @property
    def vencida(self) -> bool:
        if self.fecha_limite and not self.completada:
            return datetime.now() > self.fecha_limite
        return False

    def __str__(self):
        estado = "[x]" if self.completada else "[ ]"
        prioridad = self.prioridad.name
        fecha = self.fecha_limite.strftime("%Y-%m-%d") if self.fecha_limite else "sin fecha"
        tags = f" [{', '.join(self.etiquetas)}]" if self.etiquetas else ""
        return f"{estado} [{prioridad}] {self.titulo} (hasta {fecha}){tags}"


# Crear tareas
tareas = [
    Tarea("Estudiar Python", Prioridad.ALTA,
          fecha_limite=datetime.now() + timedelta(days=7),
          etiquetas=["estudio", "python"]),
    Tarea("Comprar víveres", Prioridad.BAJA,
          fecha_limite=datetime.now() + timedelta(days=1)),
    Tarea("Entregar proyecto", Prioridad.URGENTE,
          fecha_limite=datetime.now() + timedelta(hours=3),
          etiquetas=["trabajo"]),
    Tarea("Leer libro", Prioridad.MEDIA),
    Tarea("Ejercicio", Prioridad.MEDIA,
          fecha_limite=datetime.now() + timedelta(days=1)),
]

# Completar una tarea
tareas[3].completar()

# Ordenar por prioridad (gracias a order=True y sort_index)
print("Tareas ordenadas por prioridad:")
for tarea in sorted(tareas):
    print(f"  {tarea}")

# Resumen
pendientes = [t for t in tareas if not t.completada]
completadas = [t for t in tareas if t.completada]
print(f"\nPendientes: {len(pendientes)}, Completadas: {len(completadas)}")
