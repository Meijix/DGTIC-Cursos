# =============================================================================
# EJERCICIO 10 - Año Bisiesto
# =============================================================================
# OBJETIVO: Determinar si un año dado es bisiesto o no.
#
# REGLAS DE AÑO BISIESTO:
#   1. Si el año es divisible entre 4, PUEDE ser bisiesto.
#   2. PERO si es divisible entre 100, NO es bisiesto...
#   3. A MENOS QUE tambien sea divisible entre 400, SI es bisiesto.
#
# Ejemplos:
#   2024 -> bisiesto     (divisible entre 4, NO entre 100)
#   1900 -> NO bisiesto  (divisible entre 4 y 100, pero NO entre 400)
#   2000 -> bisiesto     (divisible entre 4, 100 Y 400)
#   2023 -> NO bisiesto  (no divisible entre 4)
#
# CONCEPTOS CLAVE que aprenderas en este ejercicio:
#   - Condicionales complejos con 'and' y 'or'
#   - Precedencia de operadores logicos
#   - Anotaciones de tipo (type hints): int, bool, ->
#   - Logica de reglas con excepciones
#
# PROGRESION: Sube significativamente la complejidad logica. La regla de
# año bisiesto requiere combinar multiples condiciones con and/or,
# lo cual es un excelente ejercicio de logica booleana.
# Esta funcion se reutilizara en el Ejercicio 12 (validacion de fechas).
# =============================================================================

# --- ANOTACIONES DE TIPO (TYPE HINTS) ---
# 'año: int' indica que el parametro 'año' deberia ser un entero.
# '-> bool' indica que la funcion retorna un booleano (True/False).
#
# IMPORTANTE: Las anotaciones de tipo en Python son solo INFORMATIVAS.
# Python NO impide que pases un float o string. Son una guia para
# el programador y herramientas de analisis estatico (como mypy).
#
# Ejemplos de anotaciones:
#   def saludar(nombre: str) -> str:
#   def sumar(a: int, b: int) -> int:
#   def es_valido(dato: float) -> bool:
def es_bisiesto(año: int) -> bool:
    # --- CONDICIONAL COMPLEJO ---
    # Vamos a desglosar la condicion paso a paso:
    #
    # año % 4 == 0              -> Es divisible entre 4?
    # año % 100 != 0            -> NO es divisible entre 100?
    # año % 400 == 0            -> Es divisible entre 400?
    #
    # La condicion completa:
    #   año % 4 == 0 AND (año % 100 != 0 OR año % 400 == 0)
    #
    # LECTURA EN ESPAÑOL:
    #   "Es bisiesto si es divisible entre 4 Y (no es divisible entre 100
    #    O es divisible entre 400)"
    #
    # PRECEDENCIA DE OPERADORES LOGICOS:
    #   1. not  (se evalua primero)
    #   2. and  (se evalua segundo)
    #   3. or   (se evalua ultimo)
    #
    # Por eso los parentesis en (año % 100 != 0 or año % 400 == 0) son
    # NECESARIOS. Sin ellos, 'and' se evaluaria antes que 'or' y la
    # logica seria incorrecta.
    #
    # VERIFICACION CON EJEMPLOS:
    #   año=2024: 2024%4==0(T) and (2024%100!=0(T) or 2024%400==0(F)) = T and T = True
    #   año=1900: 1900%4==0(T) and (1900%100!=0(F) or 1900%400==0(F)) = T and F = False
    #   año=2000: 2000%4==0(T) and (2000%100!=0(F) or 2000%400==0(T)) = T and T = True
    #   año=2023: 2023%4==0(F) and (...) = False (cortocircuito, no evalua el resto)
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    else:
        return False
    # FORMA MAS CORTA (mas pythonica):
    #   return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)
    # Retorna directamente la expresion booleana, como en el Ejercicio 09.


# --- PROGRAMA PRINCIPAL ---
año = int(input("Ingrese el año a evaluar: "))

# Llamamos a la funcion y mostramos el resultado.
# NOTA: es_bisiesto() devuelve True o False.
# Podriamos hacerlo mas legible:
#   if es_bisiesto(año):
#       print(f"El año {año} SI es bisiesto")
#   else:
#       print(f"El año {año} NO es bisiesto")
print(f"El año {año} es bisiesto?", es_bisiesto(año))

# =============================================================================
# NOTAS ADICIONALES PARA EL ESTUDIANTE:
#
# 1. FORMA ALTERNATIVA con if/elif anidados (mas explicita pero larga):
#    def es_bisiesto(año):
#        if año % 400 == 0:
#            return True          # Divisible entre 400 -> SI
#        elif año % 100 == 0:
#            return False         # Divisible entre 100 pero no 400 -> NO
#        elif año % 4 == 0:
#            return True          # Divisible entre 4 pero no 100 -> SI
#        else:
#            return False         # No divisible entre 4 -> NO
#
# 2. DATO HISTORICO: El calendario gregoriano fue introducido en 1582
#    por el Papa Gregorio XIII. Antes se usaba el calendario juliano
#    que solo tenia la regla de divisible entre 4.
#
# 3. REUTILIZACION: Esta funcion se usara en el Ejercicio 12 para
#    determinar si febrero tiene 28 o 29 dias al validar fechas.
#
# 4. RETO: Escribe un programa que liste todos los años bisiestos
#    entre 1900 y 2100.
# =============================================================================
