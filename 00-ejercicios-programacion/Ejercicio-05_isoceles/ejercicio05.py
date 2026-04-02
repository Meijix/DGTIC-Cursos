# =============================================================================
# EJERCICIO 05 - Perimetro de un Triangulo Isosceles
# =============================================================================
# OBJETIVO: Calcular el perimetro de un triangulo isosceles.
# Un triangulo isosceles tiene 2 lados iguales y 1 base diferente.
# Perimetro = base + (2 * lado_igual)
#
# CONCEPTOS CLAVE que aprenderas en este ejercicio:
#   - Funciones con dos parametros
#   - Validacion de multiples entradas (una por una)
#   - Diferencia entre parametros posicionales
#   - Formulas geometricas con multiples variables
#
# PROGRESION: Extiende el Ejercicio 04 agregando un segundo parametro
# a la funcion. Ahora debemos validar DOS entradas del usuario, no una.
# Observa como el patron de validacion con while se REPITE para cada dato.
# =============================================================================

# --- FUNCION CON DOS PARAMETROS ---
# A diferencia del equilatero (1 parametro), aqui necesitamos 2:
#   base -> la longitud de la base (lado diferente)
#   lado -> la longitud de los 2 lados iguales
#
# IMPORTANTE SOBRE EL ORDEN DE PARAMETROS:
# Al llamar la funcion, los argumentos se asignan en orden:
#   calcular_perimetro(5, 8) -> base=5, lado=8
# Si inviertes el orden, el resultado sera diferente e incorrecto.
def calcular_perimetro(base, lado):
    # Formula: base + lado_izquierdo + lado_derecho
    # Como ambos lados son iguales: base + 2 * lado
    perimetro = base + (2 * lado)
    return perimetro
    # NOTA: Los parentesis en (2 * lado) no son necesarios porque
    # la multiplicacion tiene mayor precedencia que la suma.
    # Pero los parentesis mejoran la LEGIBILIDAD del codigo.


# --- ENTRADA Y VALIDACION DE MULTIPLES DATOS ---
# Observa el patron que se repite para cada dato:
#   1. Pedir el dato con float(input(...))
#   2. Validar con while
#   3. Repetir si no es valido
#
# Este patron es identico al del Ejercicio 04 pero se aplica DOS veces.
# En el Ejercicio 06 (escaleno), se aplicara TRES veces.
# Cuando ves codigo repetido, es señal de que podrias crear una funcion
# auxiliar para evitar la repeticion.
print("Perimetro de un triangulo isosceles")

base = float(input("Ingrese la longitud de la base: "))
while base < 0:
    print("La longitud de la base no puede ser negativa")
    base = float(input("Ingrese una longitud valida: "))

lado = float(input("Ingrese la longitud de los lados iguales: "))
while lado < 0:
    print("La longitud de los lados iguales no puede ser negativa")
    lado = float(input("Ingrese una longitud valida: "))

# --- RESULTADO ---
# Aqui combinamos un f-string largo con la llamada a la funcion.
# NOTA: Las lineas muy largas pueden ser dificiles de leer.
# Python permite dividir una linea larga usando parentesis:
#   print(
#       f"El perimetro del triangulo isosceles con base {base} "
#       f"y lados de longitud {lado} es:",
#       calcular_perimetro(base, lado)
#   )
# Las cadenas adyacentes se concatenan automaticamente en Python.
print(f"El perimetro del triangulo isosceles con base de longitud {base} y lados iguales de longitud {lado} es:", calcular_perimetro(base, lado))

# =============================================================================
# NOTAS ADICIONALES PARA EL ESTUDIANTE:
#
# 1. TRIANGULO ISOSCELES: Tiene 2 lados iguales. Los angulos de la base
#    tambien son iguales. "Iso" = igual, "sceles" = piernas.
#
# 2. LIMITACION: Este programa no verifica que las medidas formen un
#    triangulo valido. En el Ejercicio 09 aprenderemos la "desigualdad
#    del triangulo" para validar esto.
#    Ejemplo invalido: base=100, lado=1 (no forma triangulo).
#
# 3. CODIGO REPETIDO: Nota como el bloque de validacion (pedir + while)
#    se repite casi identico para cada dato. En proyectos reales,
#    crearias una funcion como:
#       def pedir_longitud(mensaje):
#           valor = float(input(mensaje))
#           while valor < 0:
#               valor = float(input("Ingrese una longitud valida: "))
#           return valor
#    Esto elimina la duplicacion y hace el codigo mas limpio.
# =============================================================================
