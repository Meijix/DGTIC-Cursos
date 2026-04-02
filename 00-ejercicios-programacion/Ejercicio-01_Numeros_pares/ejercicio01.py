# =============================================================================
# EJERCICIO 01 - Numeros Pares del 0 al 100
# =============================================================================
# OBJETIVO: Imprimir todos los numeros pares entre 0 y 100.
#
# CONCEPTOS CLAVE que aprenderas en este ejercicio:
#   - Variables y asignacion de valores
#   - El ciclo 'for' y la funcion range()
#   - El operador modulo (%)
#   - Condicionales con 'if'
#   - La funcion print() y f-strings
#
# PROGRESION: Este es el primer ejercicio. Aqui se introducen los fundamentos
# mas basicos de Python: variables, ciclos y condicionales.
# =============================================================================

# --- VARIABLES ---
# En Python, una variable se crea simplemente asignando un valor con '='.
# No necesitas declarar el tipo (como en Java o C). Python lo deduce solo.
# Esto se llama "tipado dinamico".
#
# Aqui definimos el rango de numeros que queremos evaluar.
# Usamos nombres descriptivos: 'start' y 'end' en lugar de 'a' y 'b'.
# BUENA PRACTICA: Siempre usa nombres de variables que describan su proposito.
start = 0
end = 100

# --- f-strings (formatted string literals) ---
# Las f-strings se crean poniendo 'f' antes de las comillas.
# Dentro de las llaves {} puedes poner cualquier expresion de Python.
# Ejemplo: f"Hola {nombre}" inserta el valor de la variable 'nombre'.
#
# ALTERNATIVAS para formatear texto:
#   print("Los numeros pares entre " + str(start) + " y " + str(end))  # Concatenacion
#   print("Los numeros pares entre {} y {}".format(start, end))          # .format()
#   print("Los numeros pares entre %d y %d" % (start, end))             # Estilo antiguo
# Las f-strings (Python 3.6+) son la forma mas moderna y legible.
print(f"Los numeros pares entre {start} y {end} son: ")

# --- CICLO FOR con range() ---
# 'for i in range(start, end)' recorre los numeros desde 'start' hasta 'end - 1'.
#
# IMPORTANTE: range() NO incluye el ultimo numero.
#   range(0, 100) genera: 0, 1, 2, 3, ..., 98, 99  (no incluye 100)
#   Si quisieras incluir el 100, usarias range(0, 101).
#
# range() puede recibir 1, 2 o 3 argumentos:
#   range(10)        -> 0, 1, 2, ..., 9         (solo fin)
#   range(2, 10)     -> 2, 3, 4, ..., 9         (inicio, fin)
#   range(0, 10, 2)  -> 0, 2, 4, 6, 8           (inicio, fin, paso)
#
# ALTERNATIVA MAS EFICIENTE para este problema:
#   for i in range(start, end + 1, 2):   # Paso de 2, solo genera pares
#       print(i)
# Esa version evita revisar cada numero, pero aqui usamos el modulo para
# aprender como funciona el operador %.
for i in range(start, end):

    # --- OPERADOR MODULO (%) ---
    # El operador '%' devuelve el RESIDUO de una division entera.
    # Ejemplos:
    #   10 % 2 = 0   (10 / 2 = 5, residuo 0)  -> ES PAR
    #   7 % 2 = 1    (7 / 2 = 3, residuo 1)    -> ES IMPAR
    #   15 % 3 = 0   (15 / 3 = 5, residuo 0)   -> ES MULTIPLO DE 3
    #
    # REGLA: Si numero % 2 == 0, el numero es par.
    #
    # ERROR COMUN: Confundir '%' (modulo) con '/' (division).
    #   10 / 2 = 5.0   (division normal, siempre devuelve float)
    #   10 // 2 = 5     (division entera, devuelve int)
    #   10 % 2 = 0      (modulo, devuelve el residuo)
    if i % 2 == 0:
        print(i)

# =============================================================================
# NOTAS ADICIONALES PARA EL ESTUDIANTE:
#
# 1. INDENTACION: En Python, la indentacion (espacios al inicio) es
#    OBLIGATORIA. El codigo dentro de un 'for' o 'if' DEBE estar indentado.
#    Se recomienda usar 4 espacios (no tabulaciones).
#
# 2. PRUEBA MODIFICANDO: Cambia 'start' y 'end' para ver que pasa.
#    Intenta imprimir los numeros impares (i % 2 != 0).
#
# 3. RETO: Intenta resolver esto usando range(0, 101, 2) sin el if.
# =============================================================================
