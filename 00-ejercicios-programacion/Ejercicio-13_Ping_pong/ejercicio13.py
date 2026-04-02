# =============================================================================
# EJERCICIO 13 - Ping Pong (FizzBuzz)
# =============================================================================
# OBJETIVO: Imprimir los numeros del 1 al 100, pero:
#   - Si es multiplo de 3: imprimir "ping" en lugar del numero
#   - Si es multiplo de 5: imprimir "pong" en lugar del numero
#   - Si es multiplo de 3 Y 5: imprimir "ping pong"
#   - Si no es multiplo de ninguno: imprimir el numero normal
#
# NOTA: Este es el clasico problema "FizzBuzz", uno de los ejercicios
# de programacion mas famosos del mundo. Se usa frecuentemente en
# entrevistas de trabajo como filtro basico.
#
# CONCEPTOS CLAVE que aprenderas en este ejercicio:
#   - El ORDEN de las condiciones en if/elif/else importa
#   - Encapsular logica en una funcion
#   - Combinacion de operador modulo (%) con condicionales
#   - Logica de prioridades: lo MAS ESPECIFICO primero
#
# PROGRESION: Combina conceptos de ejercicios anteriores (for, modulo,
# if/elif/else) en un patron clasico. Introduce la idea de que el
# ORDEN de las condiciones afecta el resultado.
# =============================================================================

# --- FUNCION ping_pong() ---
# Encapsulamos toda la logica en una funcion. Esto permite:
#   1. Llamarla cuantas veces necesitemos
#   2. Eventualmente parametrizarla (cambiar el rango, los multiplos, etc.)
#   3. Mantener el programa principal limpio
def ping_pong():
    # range(1, 101) genera numeros del 1 al 100.
    for i in range(1, 101):
        # --- ORDEN DE CONDICIONES (CRITICO!) ---
        # La condicion para multiplos de 3 Y 5 DEBE ir PRIMERO.
        #
        # POR QUE? Porque un numero que es multiplo de 3 y 5 (como 15)
        # TAMBIEN es multiplo de 3. Si ponemos la condicion de "multiplo de 3"
        # primero, 15 entraria ahi y nunca llegaria a "multiplo de 3 y 5".
        #
        # ORDEN INCORRECTO (BUG):
        #   if i % 3 == 0:          <- 15 entra aqui!
        #       print("ping")       <- Imprime "ping" en vez de "ping pong"
        #   elif i % 3 == 0 and i % 5 == 0:
        #       print("ping pong")  <- NUNCA se ejecuta para 15
        #
        # ORDEN CORRECTO (lo que usamos):
        #   if i % 3 == 0 and i % 5 == 0:  <- Lo mas especifico PRIMERO
        #   elif i % 3 == 0:                <- Luego las condiciones parciales
        #   elif i % 5 == 0:
        #   else:                           <- El caso por defecto al final
        #
        # REGLA GENERAL: En una cadena if/elif, coloca las condiciones
        # mas ESPECIFICAS primero y las mas GENERALES despues.

        # Verificar si es multiplo de AMBOS (3 y 5)
        # Un numero es multiplo de 3 y 5 si es multiplo de 15 (3*5=15).
        # ALTERNATIVA: if i % 15 == 0:  (mas eficiente, misma logica)
        if i % 3 == 0 and i % 5 == 0:
            print("ping pong")

        # Verificar si es multiplo solo de 3
        elif i % 3 == 0:
            print("ping")

        # Verificar si es multiplo solo de 5
        elif i % 5 == 0:
            print("pong")

        # Si no es multiplo de ninguno, imprimir el numero
        else:
            print(i)


# --- LLAMADA A LA FUNCION ---
# Una sola linea para ejecutar todo el programa.
# Nota que la funcion no recibe parametros ni retorna valor.
ping_pong()

# =============================================================================
# NOTAS ADICIONALES PARA EL ESTUDIANTE:
#
# 1. FIZZBUZZ EN ENTREVISTAS: Este problema (conocido como FizzBuzz) es
#    tan clasico que se ha convertido en un filtro basico en entrevistas
#    de programacion. La clave esta en el ORDEN de las condiciones.
#
# 2. LOS MULTIPLOS DE 3 Y 5 (del 1 al 100) son:
#    Solo de 3: 3, 6, 9, 12, 18, 21, 24, 27, 33, 36, ...
#    Solo de 5: 5, 10, 20, 25, 35, 40, 50, 55, 65, 70, ...
#    De ambos (15): 15, 30, 45, 60, 75, 90
#
# 3. ALTERNATIVAS CREATIVAS:
#    a) Usando strings acumulados:
#       resultado = ""
#       if i % 3 == 0: resultado += "ping "
#       if i % 5 == 0: resultado += "pong"
#       print(resultado or i)
#
#    b) Usando un diccionario:
#       reglas = {3: "ping", 5: "pong"}
#
# 4. RETO: Parametriza la funcion para que reciba el rango y las reglas:
#    ping_pong(1, 100, {3: "ping", 5: "pong"})
#    Asi podrias agregar mas reglas facilmente.
# =============================================================================
