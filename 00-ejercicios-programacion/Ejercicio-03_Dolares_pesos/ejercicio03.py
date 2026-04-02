# =============================================================================
# EJERCICIO 03 - Convertidor de Dolares a Pesos
# =============================================================================
# OBJETIVO: Recibir un monto en dolares y una tasa de cambio, luego
# calcular y mostrar el equivalente en pesos mexicanos.
#
# CONCEPTOS CLAVE que aprenderas en este ejercicio:
#   - Funciones con multiples parametros
#   - Tipo float (numeros con decimales)
#   - Diferencia entre int() y float()
#   - Validacion de multiples entradas
#   - Operaciones aritmeticas basicas
#
# PROGRESION: Amplia el Ejercicio 02 introduciendo float() para manejar
# decimales (esencial para dinero) y funciones con mas de un parametro.
# =============================================================================

# --- FUNCION CON DOS PARAMETROS ---
# Esta funcion recibe DOS valores: el monto y la tasa de cambio.
# Cuando una funcion necesita multiples datos para trabajar, los
# separamos con comas en la definicion.
#
# BUENA PRACTICA: Los nombres de los parametros deben ser descriptivos.
# 'monto_dolares' y 'tasa_cambio' son mucho mejor que 'x' y 'y'.
#
# NOTA SOBRE ALCANCE (SCOPE):
# Las variables dentro de una funcion son LOCALES: solo existen dentro
# de la funcion. 'monto_pesos' NO existe fuera de esta funcion.
# Esto significa que puedes tener variables con el mismo nombre en
# distintas funciones sin que se afecten entre si.
def convertir_pesos(monto_dolares, tasa_cambio):

    # La conversion es una simple multiplicacion.
    # Ejemplo: 100 dolares * 17.50 pesos/dolar = 1750.00 pesos
    monto_pesos = monto_dolares * tasa_cambio
    return monto_pesos
    # EQUIVALENTE MAS CORTO (sin variable intermedia):
    #   return monto_dolares * tasa_cambio
    # Ambas formas son validas. La variable intermedia hace el codigo
    # mas legible, pero para operaciones simples puedes retornar directamente.


# --- float() vs int() ---
# int()   -> Convierte a numero ENTERO (sin decimales): int("42") = 42
# float() -> Convierte a numero con DECIMALES: float("17.50") = 17.50
#
# Usamos float() aqui porque el dinero casi siempre tiene centavos.
#   int("17.50")    -> ERROR! int() no puede convertir un string con punto decimal
#   float("17.50")  -> 17.5 (funciona correctamente)
#   int(17.50)      -> 17 (si ya es numero, trunca los decimales)
#
# PRECISION DE FLOTANTES (concepto avanzado):
# Los numeros flotantes tienen limitaciones de precision.
#   0.1 + 0.2 = 0.30000000000000004 (no exactamente 0.3)
# Para aplicaciones financieras reales, se usa el modulo 'decimal'.
# Para este ejercicio educativo, float() es suficiente.
monto_dolares = float(input("Ingrese el monto en dolares: "))

# Validacion: el monto no puede ser negativo.
# NOTA: Aqui se permite 0 (monto = 0 es valido, simplemente da 0 pesos).
# Cambia '< 0' a '<= 0' si quieres prohibir el cero tambien.
while monto_dolares < 0:
    print("El monto no puede ser negativo")
    monto_dolares = float(input("Ingrese el monto en dolares: "))

tasa_cambio = float(input("Ingrese la tasa de cambio actual: "))

# Validacion: la tasa de cambio tampoco puede ser negativa.
# NOTA: Una tasa de cambio de 0 no tiene sentido economico, pero
# el programa lo permite. Podrias mejorar la validacion con '<= 0'.
while tasa_cambio < 0:
    print("La tasa de cambio no puede ser negativa")
    tasa_cambio = float(input("Ingrese la tasa de cambio actual: "))

# --- LLAMADA A FUNCION CON MULTIPLES ARGUMENTOS ---
# Los argumentos se pasan en el MISMO ORDEN que los parametros de la definicion.
#   convertir_pesos(monto_dolares, tasa_cambio)
#                   ^              ^
#                   parametro 1    parametro 2
#
# ERROR COMUN: Pasar los argumentos en orden incorrecto.
# Si accidentalmente escribes convertir_pesos(tasa_cambio, monto_dolares),
# el resultado sera incorrecto sin que Python muestre un error.
#
# ALTERNATIVA con argumentos nombrados (keyword arguments):
#   convertir_pesos(tasa_cambio=17.50, monto_dolares=100)
# Con argumentos nombrados, el orden no importa.
print("El monto en pesos es:", convertir_pesos(monto_dolares, tasa_cambio))

# =============================================================================
# NOTAS ADICIONALES PARA EL ESTUDIANTE:
#
# 1. PATRON REPETIDO: Observa que la validacion con while es identica
#    a la del Ejercicio 02. Este patron se repite mucho: pedir -> validar.
#
# 2. MEJORA SUGERIDA: Podrias crear una funcion 'pedir_numero_positivo()'
#    que encapsule el patron de validacion, evitando repetir codigo.
#
# 3. RETO: Agrega una segunda conversion de pesos a euros, reutilizando
#    la misma funcion con una tasa de cambio diferente.
#
# 4. DATO: La tasa de cambio USD/MXN fluctua diariamente.
#    A marzo 2025, ronda los 17-20 pesos por dolar.
# =============================================================================
