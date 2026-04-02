# =============================================================================
# EJERCICIO 06 - Perimetro de un Triangulo Escaleno
# =============================================================================
# OBJETIVO: Calcular el perimetro de un triangulo escaleno.
# Un triangulo escaleno tiene los 3 lados de DIFERENTE longitud.
# Perimetro = lado1 + lado2 + lado3
#
# CONCEPTOS CLAVE que aprenderas en este ejercicio:
#   - Funciones con tres parametros
#   - Validacion con '<= 0' vs '< 0' (prohibir el cero)
#   - Repeticion de patrones de validacion
#   - Preparacion para la unificacion en el Ejercicio 07
#
# PROGRESION: Extiende los ejercicios 04 y 05. Ahora la funcion recibe
# 3 parametros y se validan 3 entradas. Observa como el codigo de
# validacion se repite 3 veces, lo cual refuerza la necesidad de
# crear funciones auxiliares para evitar repeticion.
# =============================================================================

# --- FUNCION CON TRES PARAMETROS ---
# Cada lado tiene un nombre distinto: lado1, lado2, lado3.
# El perimetro es simplemente la suma de los tres.
#
# NOTA SOBRE CONVENCIONES DE NOMBRES:
# Usamos lado1, lado2, lado3 con numeros porque los tres son
# equivalentes (no hay "base" ni "lados iguales" como en el isosceles).
# En otros contextos podrias usar: lado_a, lado_b, lado_c.
def calcular_perimetro(lado1, lado2, lado3):
    perimetro = lado1 + lado2 + lado3
    return perimetro
    # ALTERNATIVA: return lado1 + lado2 + lado3
    # OTRA ALTERNATIVA usando sum() con una lista:
    #   return sum([lado1, lado2, lado3])


# --- VALIDACION MEJORADA: '<= 0' en lugar de '< 0' ---
# A diferencia de los ejercicios 04 y 05 que usan '< 0',
# aqui se usa '<= 0' (menor O IGUAL a cero).
# Esto PROHIBE el valor 0, que es correcto porque un lado
# de longitud 0 no tiene sentido fisico.
#
# COMPARACION:
#   while lado1 < 0:   -> permite 0 (incorrecto geometricamente)
#   while lado1 <= 0:  -> prohibe 0 (correcto geometricamente)
print("Perimetro de un triangulo escaleno")

lado1 = float(input("Ingrese la longitud del lado 1: "))
while lado1 <= 0:
    lado1 = float(input("Ingrese una longitud valida para el lado 1: "))

lado2 = float(input("Ingrese la longitud del lado 2: "))
while lado2 <= 0:
    lado2 = float(input("Ingrese una longitud valida para el lado 2: "))

lado3 = float(input("Ingrese la longitud del lado 3: "))
while lado3 <= 0:
    lado3 = float(input("Ingrese una longitud valida para el lado 3: "))

# --- RESULTADO ---
# Observa el f-string con multiples variables interpoladas.
# Cada {variable} se reemplaza por su valor actual.
print(f"El perimetro del triangulo escaleno con lados {lado1},{lado2}, {lado3} es:", calcular_perimetro(lado1, lado2, lado3))

# =============================================================================
# NOTAS ADICIONALES PARA EL ESTUDIANTE:
#
# 1. TRIANGULO ESCALENO: Todos sus lados son diferentes y todos sus
#    angulos son diferentes. "Escaleno" viene del griego "desigual".
#
# 2. CODIGO REPETIDO (x3): El patron pedir+validar se repite 3 veces.
#    Si tuvieras un poligono de 10 lados, tendrias que repetirlo 10 veces!
#    Solucion: crear una funcion auxiliar o usar una lista:
#
#    lados = []
#    for i in range(3):
#        lado = float(input(f"Ingrese la longitud del lado {i+1}: "))
#        while lado <= 0:
#            lado = float(input(f"Longitud valida para lado {i+1}: "))
#        lados.append(lado)
#    perimetro = sum(lados)
#
# 3. LIMITACION: No se verifica la desigualdad del triangulo.
#    Ejemplo: lados 1, 2, 100 pasan la validacion pero NO forman
#    un triangulo. El Ejercicio 09 aborda esta validacion.
#
# 4. SIGUIENTE PASO: El Ejercicio 07 unifica los tres tipos de
#    triangulos en un solo programa, usando menus y condicionales.
# =============================================================================
