"""
Diccionarios en Python
=======================
Mapeos mutables de claves a valores. Desde Python 3.7+,
preservan el orden de inserción. Búsqueda por clave en O(1).

Ejecuta este archivo:
    python diccionarios.py
"""

# ============================================================
# 1. CREACIÓN DE DICCIONARIOS
# ============================================================

print("=== CREACIÓN ===\n")

# Literal (forma más común)
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "CDMX",
    "activo": True,
}

# Constructor dict()
persona2 = dict(nombre="Luis", edad=30, ciudad="GDL")

# Desde lista de pares
pares = [("a", 1), ("b", 2), ("c", 3)]
desde_pares = dict(pares)

# dict.fromkeys() — mismas claves con un valor inicial
plantilla = dict.fromkeys(["nombre", "edad", "email"], "pendiente")

# Diccionario vacío
vacio = {}

print(f"Literal:     {persona}")
print(f"Constructor: {persona2}")
print(f"Desde pares: {desde_pares}")
print(f"fromkeys:    {plantilla}")

# ============================================================
# 2. ACCESO A VALORES
# ============================================================

print("\n=== ACCESO ===\n")

config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "db": "postgres",
}

# Acceso directo con []
print(f"config['host'] = {config['host']}")

# CUIDADO: KeyError si la clave no existe
# print(config["timeout"])  # KeyError: 'timeout'

# Acceso seguro con .get()
print(f"config.get('timeout') = {config.get('timeout')}")           # None
print(f"config.get('timeout', 30) = {config.get('timeout', 30)}")   # 30 (default)

# Verificar existencia
print(f"\n'host' in config: {'host' in config}")          # True
print(f"'timeout' in config: {'timeout' in config}")      # False

# ============================================================
# 3. MODIFICACIÓN
# ============================================================

print("\n=== MODIFICACIÓN ===\n")

datos = {"a": 1, "b": 2}
print(f"Original: {datos}")

# Agregar o modificar
datos["c"] = 3
datos["a"] = 10
print(f"Agregar c, modificar a: {datos}")

# update() — fusionar con otro diccionario
datos.update({"d": 4, "b": 20})
print(f"update(d=4, b=20): {datos}")

# Operador | — fusión (Python 3.9+)
extra = {"e": 5, "f": 6}
fusionado = datos | extra
print(f"datos | extra: {fusionado}")

# |= — fusión in-place (Python 3.9+)
datos |= {"g": 7}
print(f"datos |= g=7: {datos}")

# setdefault() — insertar solo si NO existe
datos.setdefault("a", 999)   # No cambia porque "a" ya existe
datos.setdefault("h", 8)     # Sí inserta porque "h" no existe
print(f"setdefault: {datos}")

# ============================================================
# 4. ELIMINACIÓN
# ============================================================

print("\n=== ELIMINACIÓN ===\n")

d = {"a": 1, "b": 2, "c": 3, "d": 4}
print(f"Original: {d}")

# del — elimina o lanza KeyError
del d["a"]
print(f"del d['a']: {d}")

# pop() — elimina y devuelve el valor
valor = d.pop("b")
print(f"d.pop('b'): {d} (devolvió {valor})")

# pop() con default — no lanza error si no existe
valor = d.pop("xyz", "no existía")
print(f"d.pop('xyz', default): devolvió '{valor}'")

# popitem() — elimina y devuelve el último par (LIFO)
ultimo = d.popitem()
print(f"d.popitem(): {d} (eliminó {ultimo})")

# clear() — vacía el diccionario
d.clear()
print(f"d.clear(): {d}")

# ============================================================
# 5. ITERACIÓN
# ============================================================

print("\n=== ITERACIÓN ===\n")

frutas = {"manzana": 5, "pera": 3, "uva": 8, "kiwi": 2}

# Iterar sobre claves (por defecto)
print("Claves:")
for clave in frutas:
    print(f"  {clave}")

# Iterar sobre valores
print("\nValores:")
for valor in frutas.values():
    print(f"  {valor}")

# Iterar sobre pares (clave, valor) — LO MÁS COMÚN
print("\nPares (clave, valor):")
for fruta, cantidad in frutas.items():
    print(f"  {fruta}: {cantidad} unidades")

# Las vistas .keys(), .values(), .items() son dinámicas
claves = frutas.keys()
print(f"\nClaves antes: {list(claves)}")
frutas["mango"] = 4
print(f"Claves después de agregar: {list(claves)}")

# ============================================================
# 6. DICCIONARIOS ANIDADOS
# ============================================================

print("\n=== DICCIONARIOS ANIDADOS ===\n")

empresa = {
    "nombre": "TechCorp",
    "empleados": {
        "E001": {
            "nombre": "Ana",
            "puesto": "Desarrolladora",
            "habilidades": ["Python", "SQL", "Git"]
        },
        "E002": {
            "nombre": "Luis",
            "puesto": "DevOps",
            "habilidades": ["Docker", "Linux", "AWS"]
        },
    },
    "direccion": {
        "calle": "Av. Principal 123",
        "ciudad": "CDMX",
    }
}

# Acceso profundo
print(f"Empresa: {empresa['nombre']}")
print(f"Empleado E001: {empresa['empleados']['E001']['nombre']}")
print(f"Habilidades E001: {empresa['empleados']['E001']['habilidades']}")
print(f"Ciudad: {empresa['direccion']['ciudad']}")

# Acceso seguro profundo (evitar KeyError en cadena)
# Opción 1: get encadenado
resultado = empresa.get("empleados", {}).get("E003", {}).get("nombre", "No encontrado")
print(f"\nEmpleado E003: {resultado}")

# ============================================================
# 7. PATRONES COMUNES
# ============================================================

print("\n=== PATRONES COMUNES ===\n")

# --- Contar frecuencias ---
texto = "el gato y el perro y el pájaro"
frecuencias = {}
for palabra in texto.split():
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
print(f"Frecuencias: {frecuencias}")

# Forma más elegante con Counter
from collections import Counter
freq = Counter(texto.split())
print(f"Con Counter: {dict(freq)}")
print(f"Más comunes: {freq.most_common(2)}")

# --- Agrupar por categoría ---
personas = [
    ("Ana", "Ingeniería"),
    ("Luis", "Marketing"),
    ("Eva", "Ingeniería"),
    ("Carlos", "Marketing"),
    ("Diana", "Ingeniería"),
]

por_depto = {}
for nombre, depto in personas:
    por_depto.setdefault(depto, []).append(nombre)
print(f"\nPor departamento: {por_depto}")

# Con defaultdict (más elegante)
from collections import defaultdict
por_depto2 = defaultdict(list)
for nombre, depto in personas:
    por_depto2[depto].append(nombre)
print(f"Con defaultdict: {dict(por_depto2)}")

# --- Invertir un diccionario ---
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
print(f"\nOriginal:  {original}")
print(f"Invertido: {invertido}")

# ============================================================
# 8. DICT COMPREHENSION
# ============================================================

print("\n=== DICT COMPREHENSION ===\n")

# Cuadrados
cuadrados = {x: x**2 for x in range(1, 6)}
print(f"Cuadrados: {cuadrados}")

# Filtrar un diccionario
precios = {"manzana": 15, "pera": 25, "uva": 40, "kiwi": 60}
caros = {fruta: precio for fruta, precio in precios.items() if precio > 20}
print(f"Caros (>$20): {caros}")

# Transformar claves y valores
mayusculas = {k.upper(): v for k, v in precios.items()}
print(f"Claves en mayúsculas: {mayusculas}")

# ============================================================
# 9. EJEMPLO INTEGRADOR: SISTEMA DE CALIFICACIONES
# ============================================================

print("\n=== EJEMPLO: SISTEMA DE CALIFICACIONES ===\n")

calificaciones = {
    "Ana":    {"mate": 95, "física": 88, "prog": 92},
    "Luis":   {"mate": 72, "física": 68, "prog": 85},
    "Eva":    {"mate": 100, "física": 95, "prog": 98},
    "Carlos": {"mate": 60, "física": 55, "prog": 70},
}

# Promedios por alumno
print("Promedios por alumno:")
promedios = {}
for alumno, materias in calificaciones.items():
    promedio = sum(materias.values()) / len(materias)
    promedios[alumno] = promedio
    estado = "Aprobado" if promedio >= 70 else "Reprobado"
    print(f"  {alumno:<8s}: {promedio:.1f} — {estado}")

# Mejor alumno
mejor = max(promedios, key=promedios.get)
print(f"\nMejor alumno: {mejor} ({promedios[mejor]:.1f})")

# Promedios por materia
materias_set = set()
for materias in calificaciones.values():
    materias_set.update(materias.keys())

print("\nPromedios por materia:")
for materia in sorted(materias_set):
    notas = [cal[materia] for cal in calificaciones.values()]
    promedio = sum(notas) / len(notas)
    print(f"  {materia:<8s}: {promedio:.1f}")
