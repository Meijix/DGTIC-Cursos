# =============================================================================
# EJERCICIO 04 - Perimetro de un Triangulo Equilatero
# =============================================================================
# OBJETIVO: Calcular el perimetro de un triangulo equilatero.
# Un triangulo equilatero tiene los 3 lados IGUALES.
# Perimetro = lado * 3
#
# CONCEPTOS CLAVE que aprenderas en este ejercicio:
#   - Funciones con un solo parametro
#   - Aplicacion de formulas geometricas simples
#   - Validacion de datos (longitudes no pueden ser negativas)
#   - Combinar f-strings con print() y llamadas a funciones
#
# PROGRESION: Inicia una serie de 4 ejercicios sobre triangulos (04-07).
# Cada uno agrega complejidad: primero 1 lado, luego 2, luego 3,
# y finalmente un programa que unifica los tres tipos.
# Este patron de "construir incrementalmente" es clave en programacion.
# =============================================================================

# --- FUNCION PARA CALCULAR EL PERIMETRO ---
# Recibe UN solo parametro porque los 3 lados son iguales.
# El perimetro de un equilatero es simplemente lado * 3.
#
# NOTA SOBRE DISEÑO: Aunque la operacion es simple (lado * 3),
# encapsularla en una funcion tiene ventajas:
#   1. El nombre de la funcion documenta lo que hace
#   2. Si la formula cambia, solo modificas un lugar
#   3. Puedes reutilizarla en otros programas (como el Ejercicio 07)
def calcular_perimetro(lado):
    perimetro = lado * 3
    return perimetro
    # EQUIVALENTE MAS CORTO: return lado * 3


# --- INTERACCION CON EL USUARIO ---
# print() sin f-string: simplemente muestra texto fijo.
# Es util para titulos o mensajes que no necesitan variables.
print("Perimetro de un triangulo equilatero")

# Pedimos la longitud del lado con float() porque las medidas
# pueden tener decimales (ej: 5.7 cm).
longitud_lado = float(input("Ingrese la longitud de uno de los lados: "))

# --- VALIDACION ---
# Las longitudes fisicas no pueden ser negativas.
# NOTA: Aqui se usa '< 0', lo que permite el valor 0.
# Un lado de longitud 0 no tiene sentido geometrico.
# Seria mejor usar '<= 0' para prohibirlo.
#
# MEJORA SUGERIDA:
#   while longitud_lado <= 0:
#       print("La longitud debe ser mayor a 0")
#       longitud_lado = float(input("Ingrese una longitud valida: "))
while longitud_lado < 0:
    print("La longitud del lado no puede ser negativa")
    longitud_lado = float(input("Ingrese una longitud valida: "))

# --- COMBINANDO f-strings CON LLAMADAS A FUNCIONES ---
# Aqui se combinan dos formas de pasar datos a print():
#   1. Un f-string con variables interpoladas: f"...{longitud_lado}..."
#   2. Una coma seguida de una llamada a funcion: calcular_perimetro(...)
#
# print() recibe ambos como argumentos separados por coma.
# La coma agrega un espacio automatico entre los dos elementos.
#
# ALTERNATIVA usando solo f-string:
#   print(f"El perimetro del triangulo equilatero con lados de longitud {longitud_lado} es: {calcular_perimetro(longitud_lado)}")
print(f"El perimetro del triangulo equilatero con lados de longitud {longitud_lado} es:", calcular_perimetro(longitud_lado))

# =============================================================================
# NOTAS ADICIONALES PARA EL ESTUDIANTE:
#
# 1. TRIANGULO EQUILATERO: Todos sus lados miden lo mismo y todos sus
#    angulos miden 60 grados. Es el triangulo "mas simetrico".
#
# 2. COMPARACION CON EL SIGUIENTE EJERCICIO: En el Ejercicio 05 (isosceles),
#    la funcion necesitara DOS parametros porque tiene dos medidas distintas.
#
# 3. RETO: Agrega el calculo del AREA del triangulo equilatero.
#    Formula: area = (sqrt(3) / 4) * lado^2
#    Necesitaras: import math y math.sqrt()
# =============================================================================
