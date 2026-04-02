# =============================================================================
# EJERCICIO 11 - Meses del Año
# =============================================================================
# OBJETIVO: Recibir un numero entero entre 0 y 11 y mostrar el mes
# correspondiente (0=Enero, 1=Febrero, ..., 11=Diciembre).
#
# CONCEPTOS CLAVE que aprenderas en este ejercicio:
#   - Listas en Python: definicion, acceso por indice
#   - Indices de listas (empiezan en 0, no en 1)
#   - Validacion de rango con comparaciones encadenadas
#   - Uso de listas como alternativa a if/elif largos
#
# PROGRESION: Introduce las LISTAS, una de las estructuras de datos
# mas importantes de Python. Tambien muestra un patron elegante:
# usar una lista como "tabla de busqueda" en lugar de escribir
# 12 condicionales if/elif.
# Esta logica se combinara con el Ejercicio 10 en el Ejercicio 12.
# =============================================================================

# --- LISTAS EN PYTHON ---
# Una lista es una coleccion ORDENADA de elementos.
# Se define con corchetes [] y los elementos se separan con comas.
#
# CARACTERISTICAS:
#   - Los indices empiezan en 0 (no en 1!)
#   - Se accede a un elemento con lista[indice]
#   - Las listas son MUTABLES (puedes cambiar sus elementos)
#   - Pueden contener elementos de cualquier tipo
#
# INDICES:
#   meses[0]  -> "Enero"
#   meses[1]  -> "Febrero"
#   meses[11] -> "Diciembre"
#   meses[12] -> ERROR: IndexError (fuera de rango)
#   meses[-1] -> "Diciembre" (los indices negativos cuentan desde el final)
#
# POR QUE INDICES DESDE 0?
# Es una convencion de la mayoria de lenguajes de programacion.
# Se basa en que el indice representa el "desplazamiento" desde el inicio.
# El primer elemento esta a 0 posiciones del inicio.
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# --- ENTRADA DEL USUARIO ---
# Se pide un numero entre 0 y 11 (los indices validos de la lista).
numero = int(input("Ingrese un numero entero entre 0 y 11: "))

# --- COMPARACION ENCADENADA ---
# Python permite escribir: 0 <= numero <= 11
# Esto es equivalente a: numero >= 0 and numero <= 11
# Pero la forma encadenada es mas legible y mas "pythonica".
#
# Otros ejemplos de comparaciones encadenadas:
#   1 < x < 10       -> x esta entre 1 y 10 (exclusivo)
#   0 <= y <= 100     -> y esta entre 0 y 100 (inclusivo)
#   a < b < c         -> b esta entre a y c
#
# ALTERNATIVA CON LISTA COMO TABLA DE BUSQUEDA:
# En vez de escribir 12 condicionales:
#   if numero == 0: print("Enero")
#   elif numero == 1: print("Febrero")
#   elif numero == 2: print("Marzo")
#   ...
# Usamos la lista y accedemos por indice. Es MUCHO mas elegante.
#
# ALTERNATIVA CON match/case (Python 3.10+):
#   match numero:
#       case 0: print("Enero")
#       case 1: print("Febrero")
#       ...
#       case _: print("Numero invalido")
# Pero la lista sigue siendo la solucion mas concisa.
if 0 <= numero <= 11:
    # Acceso directo al elemento por su indice.
    # Esto funciona porque los indices de la lista (0-11) coinciden
    # con los numeros que representan los meses.
    print(meses[numero])
else:
    print("El numero ingresado no es valido")

# =============================================================================
# NOTAS ADICIONALES PARA EL ESTUDIANTE:
#
# 1. INDICES BASE 0 vs BASE 1:
#    En este ejercicio, Enero=0 y Diciembre=11.
#    En la vida real, Enero es el mes 1 y Diciembre el mes 12.
#    El Ejercicio 12 usa la convencion "natural" (1-12), por lo que
#    accede con meses[mes - 1] para compensar la diferencia.
#
# 2. OTRAS OPERACIONES CON LISTAS:
#    len(meses)         -> 12 (numero de elementos)
#    meses.append("X")  -> agrega un elemento al final
#    meses[0] = "Jan"   -> cambia el primer elemento
#    "Marzo" in meses   -> True (verifica si existe)
#
# 3. ALTERNATIVA CON DICCIONARIO:
#    meses = {1: "Enero", 2: "Febrero", ..., 12: "Diciembre"}
#    Asi podrias usar indices del 1 al 12 directamente.
#
# 4. RETO: Modifica el programa para que use indices del 1 al 12
#    en lugar del 0 al 11 (mas intuitivo para el usuario).
# =============================================================================
