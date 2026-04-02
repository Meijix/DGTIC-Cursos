"""
Funciones de Orden Superior
=============================
Funciones que reciben otras funciones como argumento o retornan funciones.
Este concepto es fundamental para la programación funcional en Python.

Ejecuta este archivo:
    python funciones_orden_superior.py
"""

# ============================================================
# 1. FUNCIONES COMO OBJETOS DE PRIMERA CLASE
# ============================================================

print("=== FUNCIONES COMO OBJETOS ===\n")


def saludar(nombre):
    """Saluda a alguien."""
    return f"Hola, {nombre}"


def despedir(nombre):
    """Se despide de alguien."""
    return f"Adiós, {nombre}"


# Las funciones se pueden asignar a variables
mi_funcion = saludar
print(f"mi_funcion('Ana') = {mi_funcion('Ana')}")
print(f"Nombre de la función: {mi_funcion.__name__}")

# Se pueden almacenar en estructuras de datos
acciones = {
    "saludar": saludar,
    "despedir": despedir,
}

for accion, func in acciones.items():
    print(f"  {accion}('Luis') → {func('Luis')}")

# Se pueden poner en listas
funciones = [str.upper, str.lower, str.title]
texto = "hola MUNDO python"
for f in funciones:
    print(f"  {f.__name__}('{texto}') → '{f(texto)}'")

# ============================================================
# 2. FUNCIONES COMO ARGUMENTOS
# ============================================================

print("\n=== FUNCIONES COMO ARGUMENTOS ===\n")


def aplicar(funcion, datos):
    """Aplica una función a cada elemento de una lista."""
    return [funcion(x) for x in datos]


numeros = [1, -2, 3, -4, 5]
print(f"Datos: {numeros}")
print(f"Aplicar abs:       {aplicar(abs, numeros)}")
print(f"Aplicar str:       {aplicar(str, numeros)}")
print(f"Aplicar cuadrado:  {aplicar(lambda x: x**2, numeros)}")


def aplicar_y_filtrar(funcion, predicado, datos):
    """Aplica una función solo a elementos que cumplan el predicado."""
    return [funcion(x) if predicado(x) else x for x in datos]


resultado = aplicar_y_filtrar(
    funcion=lambda x: x * 2,
    predicado=lambda x: x > 0,
    datos=numeros
)
print(f"Duplicar solo positivos: {resultado}")

# ============================================================
# 3. FUNCIONES QUE RETORNAN FUNCIONES
# ============================================================

print("\n=== FUNCIONES QUE RETORNAN FUNCIONES ===\n")


def crear_multiplicador(factor):
    """Fábrica de funciones: crea multiplicadores."""
    def multiplicar(x):
        return x * factor
    return multiplicar


doble = crear_multiplicador(2)
triple = crear_multiplicador(3)
decimo = crear_multiplicador(0.1)

print(f"doble(5) = {doble(5)}")       # 10
print(f"triple(5) = {triple(5)}")     # 15
print(f"decimo(5) = {decimo(5)}")     # 0.5


def crear_formateador(prefijo, sufijo=""):
    """Fábrica de funciones de formateo."""
    def formatear(texto):
        return f"{prefijo}{texto}{sufijo}"
    return formatear


html_bold = crear_formateador("<b>", "</b>")
html_italic = crear_formateador("<i>", "</i>")
con_comillas = crear_formateador('"', '"')

print(f"\n{html_bold('importante')}")
print(f"{html_italic('énfasis')}")
print(f"{con_comillas('citado')}")

# ============================================================
# 4. CLOSURES (CLAUSURAS)
# ============================================================

print("\n=== CLOSURES ===\n")


def crear_contador(inicio=0):
    """Crea un contador con estado persistente usando closure."""
    cuenta = [inicio]  # Usamos lista para poder mutar en Python < 3

    def incrementar():
        cuenta[0] += 1
        return cuenta[0]

    def obtener():
        return cuenta[0]

    def reiniciar():
        cuenta[0] = inicio

    # Retornamos múltiples funciones que comparten el mismo estado
    return incrementar, obtener, reiniciar


inc, get, reset = crear_contador(0)
print(f"Incrementar: {inc()}")  # 1
print(f"Incrementar: {inc()}")  # 2
print(f"Incrementar: {inc()}")  # 3
print(f"Obtener: {get()}")      # 3
reset()
print(f"Después de reiniciar: {get()}")  # 0


# Con nonlocal (Python 3+)
def crear_acumulador(inicial=0):
    """Acumulador usando nonlocal."""
    total = inicial

    def agregar(valor):
        nonlocal total
        total += valor
        return total

    return agregar


acc = crear_acumulador(100)
print(f"\nAcumular 10: {acc(10)}")    # 110
print(f"Acumular 20: {acc(20)}")      # 130
print(f"Acumular -5: {acc(-5)}")      # 125

# ============================================================
# 5. MAP, FILTER, REDUCE
# ============================================================

print("\n=== MAP, FILTER, REDUCE ===\n")

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Números: {numeros}")

# --- map: transformar cada elemento ---
cuadrados = list(map(lambda x: x**2, numeros))
print(f"map(x²):    {cuadrados}")

# map con múltiples iterables
a = [1, 2, 3]
b = [10, 20, 30]
sumas = list(map(lambda x, y: x + y, a, b))
print(f"map(+, a, b): {sumas}")

# --- filter: filtrar elementos ---
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"filter(par): {pares}")

# filter con None — elimina valores falsy
mezclados = [0, 1, "", "hola", None, True, False, [], [1]]
truthy = list(filter(None, mezclados))
print(f"filter(None): {truthy}")

# --- reduce: acumular a un solo valor ---
suma = reduce(lambda acc, x: acc + x, numeros)
print(f"reduce(+):   {suma}")

producto = reduce(lambda acc, x: acc * x, numeros)
print(f"reduce(*):   {producto}")

# reduce con valor inicial
con_inicial = reduce(lambda acc, x: acc + x, numeros, 100)
print(f"reduce(+, inicio=100): {con_inicial}")

# Encontrar el máximo con reduce
maximo = reduce(lambda a, b: a if a > b else b, numeros)
print(f"reduce(max): {maximo}")

# ============================================================
# 6. COMPOSICIÓN DE FUNCIONES
# ============================================================

print("\n=== COMPOSICIÓN ===\n")


def componer(*funciones):
    """Compone múltiples funciones: componer(f, g, h)(x) = f(g(h(x)))."""
    def composicion(x):
        resultado = x
        for f in reversed(funciones):
            resultado = f(resultado)
        return resultado
    return composicion


# Ejemplo: limpiar un string
limpiar = componer(
    str.strip,
    str.lower,
    lambda s: s.replace("  ", " ")
)

texto_sucio = "  HOLA   MUNDO  Python  "
print(f"Original: '{texto_sucio}'")
print(f"Limpio:   '{limpiar(texto_sucio)}'")


# Pipeline (más intuitivo: izquierda a derecha)
def pipeline(dato, *funciones):
    """Aplica funciones en orden: pipeline(x, f, g, h) = h(g(f(x)))."""
    resultado = dato
    for f in funciones:
        resultado = f(resultado)
    return resultado


resultado = pipeline(
    "  HOLA MUNDO  ",
    str.strip,
    str.lower,
    str.title,
)
print(f"Pipeline: '{resultado}'")

# Con reduce
def pipeline_reduce(dato, funciones):
    return reduce(lambda acc, f: f(acc), funciones, dato)


resultado2 = pipeline_reduce(
    [3, 1, 4, 1, 5, 9],
    [sorted, list.copy, lambda lst: lst[:3]]
)
print(f"Pipeline con reduce: {resultado2}")

# ============================================================
# 7. SORTED CON KEY (EJEMPLO PRÁCTICO)
# ============================================================

print("\n=== SORTED CON KEY ===\n")

# sorted y .sort() aceptan una función key

estudiantes = [
    ("Ana", 9.2),
    ("Luis", 8.5),
    ("Eva", 9.8),
    ("Carlos", 7.3),
]

# Ordenar por calificación (descendente)
por_calif = sorted(estudiantes, key=lambda e: e[1], reverse=True)
print("Por calificación:")
for nombre, calif in por_calif:
    print(f"  {nombre}: {calif}")

# Ordenar strings ignorando mayúsculas
palabras = ["banana", "Apple", "cherry", "Date"]
por_nombre = sorted(palabras, key=str.lower)
print(f"\nOrdenadas (case-insensitive): {por_nombre}")

# Ordenar por múltiples criterios
datos = [("Ana", 25), ("Luis", 25), ("Eva", 22), ("Carlos", 22)]
por_edad_nombre = sorted(datos, key=lambda x: (x[1], x[0]))
print(f"Por edad, luego nombre: {por_edad_nombre}")
