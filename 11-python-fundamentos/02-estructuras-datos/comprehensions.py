"""
Comprehensions en Python
=========================
Sintaxis concisa y expresiva para crear listas, diccionarios
y sets a partir de iterables. Una de las características más
"pythónicas" del lenguaje.

Ejecuta este archivo:
    python comprehensions.py
"""

# ============================================================
# 1. LIST COMPREHENSION — BÁSICO
# ============================================================

print("=== LIST COMPREHENSION ===\n")

# Sintaxis: [expresion for variable in iterable]

# Forma clásica con ciclo
cuadrados_loop = []
for x in range(10):
    cuadrados_loop.append(x ** 2)

# Equivalente con comprehension (más conciso y rápido)
cuadrados = [x ** 2 for x in range(10)]
print(f"Cuadrados: {cuadrados}")

# Más ejemplos básicos
mayusculas = [nombre.upper() for nombre in ["ana", "luis", "eva"]]
print(f"Mayúsculas: {mayusculas}")

longitudes = [len(palabra) for palabra in ["Python", "es", "genial"]]
print(f"Longitudes: {longitudes}")

# ============================================================
# 2. LIST COMPREHENSION CON FILTRO
# ============================================================

print("\n=== CON FILTRO (if) ===\n")

# Sintaxis: [expresion for variable in iterable if condicion]

pares = [x for x in range(20) if x % 2 == 0]
print(f"Pares 0-19: {pares}")

# Solo strings que empiezan con 'p'
palabras = ["python", "java", "perl", "javascript", "php", "go"]
con_p = [p for p in palabras if p.startswith("p")]
print(f"Empiezan con 'p': {con_p}")

# Filtrar None y valores falsy
datos = [1, None, 2, "", 3, 0, 4, False, 5]
limpios = [x for x in datos if x is not None and x != ""]
print(f"Sin None ni vacíos: {limpios}")

# Solo truthy
truthy = [x for x in datos if x]
print(f"Solo truthy: {truthy}")

# ============================================================
# 3. LIST COMPREHENSION CON IF-ELSE
# ============================================================

print("\n=== CON IF-ELSE ===\n")

# Cuando queremos transformar (no filtrar), el if-else va ANTES del for
# Sintaxis: [expr_true if condicion else expr_false for variable in iterable]

par_impar = ["par" if x % 2 == 0 else "impar" for x in range(8)]
print(f"Par/Impar: {par_impar}")

# Reemplazar negativos por cero
numeros = [3, -1, 5, -8, 2, -4, 7]
positivos = [x if x > 0 else 0 for x in numeros]
print(f"Sin negativos: {positivos}")

# Aplicar descuento selectivo
precios = [100, 250, 50, 300, 75]
con_descuento = [p * 0.9 if p > 200 else p for p in precios]
print(f"Con descuento (>200): {con_descuento}")

# ============================================================
# 4. COMPREHENSIONS ANIDADAS
# ============================================================

print("\n=== COMPREHENSIONS ANIDADAS ===\n")

# --- Aplanar una lista de listas ---
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plana = [elem for fila in matriz for elem in fila]
print(f"Matriz:  {matriz}")
print(f"Aplanada: {plana}")

# Equivalente con ciclos:
# plana = []
# for fila in matriz:
#     for elem in fila:
#         plana.append(elem)

# --- Crear una matriz ---
filas, cols = 3, 4
matriz_nueva = [[0 for _ in range(cols)] for _ in range(filas)]
print(f"\nMatriz 3x4 de ceros: {matriz_nueva}")

# --- Producto cartesiano ---
colores = ["rojo", "azul"]
tallas = ["S", "M", "L"]
combinaciones = [(color, talla) for color in colores for talla in tallas]
print(f"\nCombinaciones: {combinaciones}")

# --- Aplanar con filtro ---
datos = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
positivos_planos = [x for fila in datos for x in fila if x > 0]
print(f"Positivos (aplanado): {positivos_planos}")

# ============================================================
# 5. DICT COMPREHENSION
# ============================================================

print("\n=== DICT COMPREHENSION ===\n")

# Sintaxis: {clave: valor for variable in iterable}

# Cuadrados
cuadrados_dict = {x: x**2 for x in range(1, 6)}
print(f"Cuadrados: {cuadrados_dict}")

# Desde dos listas con zip
nombres = ["Ana", "Luis", "Eva"]
edades = [25, 30, 22]
personas = {nombre: edad for nombre, edad in zip(nombres, edades)}
print(f"Personas: {personas}")

# Invertir un diccionario
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
print(f"Invertido: {invertido}")

# Filtrar un diccionario
precios = {"manzana": 15, "pera": 25, "uva": 40, "kiwi": 60, "naranja": 20}
caros = {fruta: precio for fruta, precio in precios.items() if precio > 20}
print(f"Caros (>$20): {caros}")

# Transformar valores
con_iva = {fruta: round(precio * 1.16, 2) for fruta, precio in precios.items()}
print(f"Con IVA (16%): {con_iva}")

# Contar frecuencia de caracteres
texto = "mississippi"
frecuencia = {c: texto.count(c) for c in set(texto)}
print(f"Frecuencia en '{texto}': {frecuencia}")

# ============================================================
# 6. SET COMPREHENSION
# ============================================================

print("\n=== SET COMPREHENSION ===\n")

# Sintaxis: {expresion for variable in iterable}

# Vocales en un texto
texto = "el murcielago tiene todas las vocales"
vocales = {c for c in texto.lower() if c in "aeiou"}
print(f"Vocales en el texto: {vocales}")

# Longitudes únicas
palabras = ["hola", "mundo", "casa", "perro", "gato", "sol"]
longitudes_unicas = {len(p) for p in palabras}
print(f"Longitudes únicas: {longitudes_unicas}")

# Residuos módulo 5
residuos = {x % 5 for x in range(100)}
print(f"Residuos mod 5: {residuos}")

# ============================================================
# 7. GENERATOR EXPRESSION (EXPRESIÓN GENERADORA)
# ============================================================

print("\n=== GENERATOR EXPRESSION ===\n")

# Sintaxis: (expresion for variable in iterable)
# Es como una list comprehension pero LAZY: no crea toda la lista en memoria

# List comprehension: crea la lista completa en memoria
suma_lista = sum([x**2 for x in range(1000000)])

# Generator expression: calcula uno a uno, usa memoria constante
suma_gen = sum(x**2 for x in range(1000000))

print(f"Suma de cuadrados (1M): {suma_gen}")

# La diferencia importa con datos grandes
import sys
lista = [x for x in range(10000)]
generador = (x for x in range(10000))
print(f"\nMemoria lista:     {sys.getsizeof(lista)} bytes")
print(f"Memoria generador: {sys.getsizeof(generador)} bytes")

# El generador se agota después de una iteración
gen = (x**2 for x in range(5))
print(f"\nPrimeros del generador: {next(gen)}, {next(gen)}, {next(gen)}")
print(f"Resto: {list(gen)}")  # Solo quedan 2

# Uso práctico: verificar si ALGÚN/TODO cumple condición
numeros = [2, 4, 6, 8, 10]
todos_pares = all(x % 2 == 0 for x in numeros)
print(f"\n¿Todos pares? {todos_pares}")

algun_mayor_5 = any(x > 5 for x in numeros)
print(f"¿Alguno > 5? {algun_mayor_5}")

# ============================================================
# 8. CUÁNDO USAR Y CUÁNDO NO
# ============================================================

print("\n=== BUENAS PRÁCTICAS ===\n")

# BIEN: Comprehension simple y legible
nombres = ["  Ana  ", "  Luis  ", "  Eva  "]
limpios = [nombre.strip() for nombre in nombres]
print(f"Limpiar nombres: {limpios}")

# BIEN: Filtro simple
mayores = [e for e in [15, 22, 8, 30, 17] if e >= 18]
print(f"Mayores de edad: {mayores}")

# MAL: Demasiado complejo — mejor usar un ciclo
# resultado = [
#     f(x) if g(x) > 0 else h(x)
#     for sublista in lista_anidada
#     for x in sublista
#     if x is not None and isinstance(x, int) and x > threshold
# ]

# BIEN: Cuando la lógica es compleja, usa un ciclo explícito
def procesar_datos(datos_anidados):
    """Ejemplo de cuándo un ciclo es mejor que una comprehension."""
    resultado = []
    for sublista in datos_anidados:
        for x in sublista:
            if x is None:
                continue
            if not isinstance(x, (int, float)):
                continue
            valor = x ** 2 if x > 0 else abs(x)
            resultado.append(valor)
    return resultado

datos = [[1, None, -3], [4, "texto", 6], [None, 8, -2]]
print(f"Procesados: {procesar_datos(datos)}")

# ============================================================
# 9. EJEMPLO INTEGRADOR: PROCESAMIENTO DE DATOS
# ============================================================

print("\n=== EJEMPLO INTEGRADOR ===\n")

# Datos de ventas: (producto, cantidad, precio_unitario)
ventas = [
    ("laptop", 5, 15000),
    ("mouse", 50, 250),
    ("teclado", 30, 800),
    ("monitor", 10, 5000),
    ("cable USB", 100, 50),
    ("webcam", 20, 1200),
    ("audífonos", 35, 600),
]

# Total por producto
totales = {prod: cant * precio for prod, cant, precio in ventas}
print("Ventas totales por producto:")
for prod, total in sorted(totales.items(), key=lambda x: x[1], reverse=True):
    print(f"  {prod:<12s}: ${total:>10,}")

# Productos con ventas > $20,000
grandes = {prod: total for prod, total in totales.items() if total > 20_000}
print(f"\nVentas > $20,000: {grandes}")

# Resumen
total_general = sum(totales.values())
promedio = total_general / len(totales)
producto_estrella = max(totales, key=totales.get)

print(f"\nTotal general: ${total_general:,}")
print(f"Promedio por producto: ${promedio:,.0f}")
print(f"Producto estrella: {producto_estrella} (${totales[producto_estrella]:,})")
