# =============================================================================
# EJERCICIO 09 - Teorema de la Desigualdad del Triangulo
# =============================================================================
# OBJETIVO: Determinar si tres segmentos de longitud a, b y c pueden
# formar un triangulo valido, usando el teorema de la desigualdad.
#
# TEOREMA: Tres segmentos forman un triangulo si Y SOLO SI:
#   a + b > c   Y   b + c > a   Y   c + a > b
# Es decir, la suma de dos lados SIEMPRE debe ser mayor que el tercero.
#
# CONCEPTOS CLAVE que aprenderas en este ejercicio:
#   - Funciones que retornan valores booleanos (True/False)
#   - Operadores logicos: 'and' (Y logico)
#   - Expresiones booleanas directas en return
#   - Validacion matematica de datos
#
# PROGRESION: Complementa los ejercicios de triangulos (04-07).
# Introduce el concepto de funciones que retornan booleanos, muy usadas
# para validaciones. Tambien muestra como evaluar multiples condiciones
# simultaneas con 'and'.
# =============================================================================

# --- FUNCION QUE RETORNA UN BOOLEANO ---
# Una funcion puede retornar True o False directamente.
# Esto es muy comun para funciones de VALIDACION o VERIFICACION.
#
# PATRON COMUN: Funciones que empiezan con "es_" o "tiene_" o "puede_"
# generalmente retornan True/False:
#   es_triangulo(), es_bisiesto(), es_par(), tiene_permiso(), puede_votar()
#
# NOTA SOBRE EL RETURN:
# La expresion 'a + b > c and b + c > a and c + a > b' se evalua
# completamente y devuelve True o False SIN necesidad de un if.
#
# FORMA LARGA EQUIVALENTE (menos elegante):
#   def es_triangulo(a, b, c):
#       if a + b > c and b + c > a and c + a > b:
#           return True
#       else:
#           return False
#
# FORMA CORTA (mas pythonica, la que usamos):
#   return expresion_booleana
# Siempre que puedas retornar la expresion directamente, hazlo.
# Es mas limpio y mas "pythonico" (idiomatico de Python).
def es_triangulo(a, b, c):
    # --- OPERADOR 'and' ---
    # 'and' requiere que TODAS las condiciones sean True.
    # Si alguna es False, todo el resultado es False.
    #
    # Tabla de verdad de 'and':
    #   True  and True  = True
    #   True  and False = False
    #   False and True  = False
    #   False and False = False
    #
    # EVALUACION EN CORTOCIRCUITO: Python evalua de izquierda a derecha.
    # Si la primera condicion es False, NO evalua las demas (ya sabe
    # que el resultado sera False). Esto es una optimizacion automatica.
    #
    # EJEMPLO:
    #   a=3, b=4, c=5: 3+4>5(True) and 4+5>3(True) and 5+3>4(True) -> True
    #   a=1, b=2, c=10: 1+2>10(False) -> False (no evalua las demas)
    return a + b > c and b + c > a and c + a > b


# --- PROGRAMA PRINCIPAL ---
# Pedimos las tres longitudes al usuario.
# NOTA: Aqui NO hay validacion con while (podria agregarse).
# Se asume que el usuario ingresara numeros positivos.
a = float(input("Ingrese la longitud del segmento a: "))
b = float(input("Ingrese la longitud del segmento b: "))
c = float(input("Ingrese la longitud del segmento c: "))

# --- IMPRIMIENDO BOOLEANOS ---
# print() muestra True o False tal cual.
# La funcion es_triangulo() retorna un booleano que print() convierte
# automaticamente a texto: "True" o "False".
#
# ALTERNATIVA mas amigable para el usuario:
#   if es_triangulo(a, b, c):
#       print("Si, los segmentos pueden formar un triangulo")
#   else:
#       print("No, los segmentos NO pueden formar un triangulo")
print("Es triangulo?", es_triangulo(a, b, c))

# =============================================================================
# NOTAS ADICIONALES PARA EL ESTUDIANTE:
#
# 1. POR QUE 3 CONDICIONES? No basta con verificar solo una.
#    Ejemplo: a=1, b=2, c=3
#      a + b > c -> 1+2 > 3 -> 3 > 3 -> False (no forma triangulo)
#    Pero si solo verificamos b + c > a -> 2+3 > 1 -> True (parece valido!)
#    Por eso necesitamos verificar LAS TRES combinaciones.
#
# 2. CASO LIMITE: Si a + b = c exactamente, NO es un triangulo sino
#    una linea recta (triangulo "degenerado"). Por eso usamos '>' y no '>='.
#
# 3. CONEXION CON EJERCICIOS ANTERIORES: Esta funcion podria integrarse
#    en los ejercicios 06 y 07 para validar que los lados ingresados
#    realmente formen un triangulo antes de calcular el perimetro.
#
# 4. RETO: Modifica el programa para que, si es triangulo, tambien
#    indique de que tipo es (equilatero, isosceles o escaleno).
#    Pista: compara los lados entre si con == y !=.
# =============================================================================
