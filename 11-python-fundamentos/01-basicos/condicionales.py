"""
Condicionales en Python
========================
Estructuras de control que permiten ejecutar código
de forma selectiva según condiciones booleanas.

Ejecuta este archivo:
    python condicionales.py
"""

# ============================================================
# 1. IF / ELIF / ELSE BÁSICO
# ============================================================

print("=== IF / ELIF / ELSE ===\n")

temperatura = 28

if temperatura > 35:
    print("Hace mucho calor — quédate en casa")
elif temperatura > 25:
    print("Hace calor — lleva ropa ligera")
elif temperatura > 15:
    print("Clima templado — lleva una chaqueta ligera")
elif temperatura > 5:
    print("Hace frío — abrígate bien")
else:
    print("Hace mucho frío — extrema precauciones")

# Nota: solo se ejecuta el PRIMER bloque cuya condición sea True.
# Los demás se saltan, aunque también sean verdaderos.

# ============================================================
# 2. OPERADOR TERNARIO (EXPRESIÓN CONDICIONAL)
# ============================================================

print("\n=== OPERADOR TERNARIO ===\n")

edad = 20

# Sintaxis: valor_si_true if condicion else valor_si_false
estado = "mayor de edad" if edad >= 18 else "menor de edad"
print(f"Con {edad} años eres {estado}")

# Se puede usar en cualquier contexto que acepte una expresión
numeros = [1, -2, 3, -4, 5]
absolutos = [x if x >= 0 else -x for x in numeros]
print(f"Valores absolutos: {absolutos}")

# Ternario anidado (no recomendado para más de 2 niveles)
nota = 85
calificacion = "A" if nota >= 90 else "B" if nota >= 80 else "C" if nota >= 70 else "F"
print(f"Nota {nota} → Calificación: {calificacion}")

# ============================================================
# 3. TRUTHY Y FALSY EN CONDICIONALES
# ============================================================

print("\n=== TRUTHY Y FALSY ===\n")

# Python evalúa cualquier valor como booleano en un contexto condicional.
# No es necesario escribir: if len(lista) > 0:

# Forma pythónica:
lista = [1, 2, 3]
if lista:  # True si la lista NO está vacía
    print(f"La lista tiene {len(lista)} elementos")

lista_vacia = []
if not lista_vacia:  # True si la lista ESTÁ vacía
    print("La lista está vacía")

# Con strings
nombre = ""
nombre_display = nombre or "Anónimo"  # Cortocircuito como valor default
print(f"Nombre: {nombre_display}")

# Con None
resultado = None
if resultado is None:  # Siempre usar 'is' con None
    print("No hay resultado todavía")

# ============================================================
# 4. CONDICIONES COMPUESTAS
# ============================================================

print("\n=== CONDICIONES COMPUESTAS ===\n")

edad = 25
tiene_licencia = True
tiene_seguro = True

# Múltiples condiciones con and / or
if edad >= 18 and tiene_licencia and tiene_seguro:
    print("Puede conducir legalmente")

# Condiciones con paréntesis para claridad
es_fin_de_semana = True
es_feriado = False
hora = 10

if (es_fin_de_semana or es_feriado) and (8 <= hora <= 22):
    print("La tienda está abierta")

# Comparaciones encadenadas (más pythonico)
valor = 50
if 0 <= valor <= 100:
    print(f"{valor} está en el rango [0, 100]")

# ============================================================
# 5. MATCH-CASE (Python 3.10+)
# ============================================================

print("\n=== MATCH-CASE (Python 3.10+) ===\n")

# Equivalente mejorado de switch-case de otros lenguajes.
# NOTA: Requiere Python 3.10 o superior.

def clasificar_http(codigo):
    """Clasifica un código de estado HTTP."""
    match codigo:
        case 200:
            return "OK"
        case 301:
            return "Movido permanentemente"
        case 404:
            return "No encontrado"
        case 500:
            return "Error interno del servidor"
        case _:  # _ es el comodín (wildcard) — captura todo lo demás
            return f"Código desconocido: {codigo}"

for code in [200, 301, 404, 500, 418]:
    print(f"  HTTP {code}: {clasificar_http(code)}")

# --- Match con patrones más avanzados ---
def analizar_comando(comando):
    """Analiza comandos con pattern matching."""
    match comando.split():
        case ["salir"]:
            return "Saliendo del programa..."
        case ["ayuda"]:
            return "Comandos: salir, ayuda, buscar <término>"
        case ["buscar", termino]:
            return f"Buscando: '{termino}'"
        case ["buscar", *terminos]:  # Captura múltiples argumentos
            return f"Buscando: {' '.join(terminos)}"
        case [accion, *args]:
            return f"Comando desconocido: '{accion}' con args {args}"
        case _:
            return "Comando vacío"

comandos = ["salir", "ayuda", "buscar python", "buscar hola mundo", "crear archivo.txt"]
print()
for cmd in comandos:
    print(f"  '{cmd}' → {analizar_comando(cmd)}")

# --- Match con guardas (guards) ---
def clasificar_numero(n):
    """Clasifica un número usando match con guardas."""
    match n:
        case 0:
            return "cero"
        case n if n > 0:
            return "positivo"
        case n if n < 0:
            return "negativo"

for num in [0, 42, -7]:
    print(f"  {num} es {clasificar_numero(num)}")

# ============================================================
# 6. PATRONES COMUNES CON CONDICIONALES
# ============================================================

print("\n=== PATRONES COMUNES ===\n")

# --- Validación de entrada ---
def validar_edad(entrada):
    """Valida que la entrada sea una edad válida."""
    if not entrada.isdigit():
        return "Error: debe ser un número"
    edad = int(entrada)
    if not (0 <= edad <= 150):
        return "Error: edad fuera de rango"
    return f"Edad válida: {edad}"

for test in ["25", "abc", "-5", "200", "0"]:
    print(f"  validar_edad('{test}') → {validar_edad(test)}")

# --- Diccionario como switch (alternativa pre-3.10) ---
def calcular(a, operador, b):
    """Calculadora usando diccionario como switch."""
    operaciones = {
        "+": lambda: a + b,
        "-": lambda: a - b,
        "*": lambda: a * b,
        "/": lambda: a / b if b != 0 else "Error: división por cero",
    }
    if operador not in operaciones:
        return f"Operador '{operador}' no válido"
    return operaciones[operador]()

print(f"\n  5 + 3 = {calcular(5, '+', 3)}")
print(f"  10 / 0 = {calcular(10, '/', 0)}")
print(f"  7 ^ 2 = {calcular(7, '^', 2)}")

# --- Asignación condicional con walrus ---
import random
random.seed(123)

print("\n--- Walrus en condicional ---")
datos = [random.randint(1, 100) for _ in range(10)]
print(f"Datos: {datos}")

if (maximo := max(datos)) > 80:
    print(f"El máximo ({maximo}) supera el umbral de 80")
else:
    print(f"El máximo ({maximo}) está dentro del rango")

# ============================================================
# 7. EJEMPLO INTEGRADOR: AÑO BISIESTO
# ============================================================

print("\n=== EJEMPLO: AÑO BISIESTO ===\n")


def es_bisiesto(anio):
    """
    Un año es bisiesto si:
    - Es divisible entre 4
    - EXCEPTO si es divisible entre 100
    - A MENOS QUE también sea divisible entre 400

    Ejemplos:
    - 2024: divisible entre 4, no entre 100 → bisiesto
    - 1900: divisible entre 4 y 100, no entre 400 → NO bisiesto
    - 2000: divisible entre 4, 100 y 400 → bisiesto
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


anios_test = [2000, 1900, 2024, 2023, 2100, 1600]
for anio in anios_test:
    resultado = "SÍ" if es_bisiesto(anio) else "NO"
    print(f"  {anio}: {resultado} es bisiesto")

# ============================================================
# 8. EJEMPLO INTEGRADOR: CLASIFICADOR DE TRIÁNGULOS
# ============================================================

print("\n=== EJEMPLO: CLASIFICADOR DE TRIÁNGULOS ===\n")


def clasificar_triangulo(a, b, c):
    """Clasifica un triángulo según sus lados."""
    # Primero verificar que los lados formen un triángulo válido
    # (la suma de dos lados debe ser mayor al tercero)
    lados = sorted([a, b, c])

    if lados[0] <= 0:
        return "Inválido: los lados deben ser positivos"

    if lados[0] + lados[1] <= lados[2]:
        return "Inválido: no forma un triángulo"

    # Clasificar por lados
    if a == b == c:
        tipo = "Equilátero"
    elif a == b or b == c or a == c:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"

    # Verificar si es rectángulo (Pitágoras)
    if abs(lados[0]**2 + lados[1]**2 - lados[2]**2) < 1e-9:
        tipo += " rectángulo"

    return tipo


triangulos = [(3, 3, 3), (3, 4, 5), (5, 5, 3), (2, 3, 4), (1, 2, 10), (-1, 2, 3)]
for lados in triangulos:
    print(f"  {lados} → {clasificar_triangulo(*lados)}")
