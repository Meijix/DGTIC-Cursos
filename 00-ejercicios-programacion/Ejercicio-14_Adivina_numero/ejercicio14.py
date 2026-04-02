# =============================================================================
# EJERCICIO 14 - Adivina el Numero
# =============================================================================
# OBJETIVO: Juego donde el programa genera un numero aleatorio entre 1 y 100,
# y el usuario tiene 5 intentos para adivinarlo. El programa da pistas
# de si el numero es mayor o menor.
#
# CONCEPTOS CLAVE que aprenderas en este ejercicio:
#   - Modulo 'random' e importaciones (import)
#   - random.randint() para numeros aleatorios
#   - Ciclo while con contador de intentos
#   - Sentencia 'break' para salir de un ciclo prematuramente
#   - Clausula 'else' en un while (poco comun pero poderosa)
#   - Diseño de un juego interactivo simple
#
# PROGRESION: Primer ejercicio tipo "juego". Introduce el modulo random,
# la importacion de modulos, el break para salir de ciclos, y la
# poco conocida clausula while/else. Es un salto hacia programas
# interactivos y dinamicos.
# =============================================================================

# --- IMPORTACION DE MODULOS ---
# 'import random' hace disponibles las funciones del modulo 'random'.
# Un MODULO es un archivo de Python con funciones y variables que puedes
# reutilizar. Python incluye muchos modulos integrados (built-in):
#   random   -> numeros aleatorios
#   math     -> funciones matematicas (sqrt, sin, cos, pi)
#   datetime -> fechas y horas
#   os       -> interaccion con el sistema operativo
#   json     -> leer/escribir archivos JSON
#
# FORMAS DE IMPORTAR:
#   import random                 -> Usa: random.randint(1, 100)
#   from random import randint    -> Usa: randint(1, 100)  (sin prefijo)
#   from random import *          -> Importa TODO (no recomendado)
#
# BUENA PRACTICA: Importar con 'import modulo' y usar 'modulo.funcion()'
# hace el codigo mas claro sobre de donde viene cada funcion.
import random

# --- random.randint(a, b) ---
# Genera un numero ENTERO aleatorio entre a y b, INCLUYENDO ambos.
# A diferencia de range(), randint() SI incluye el limite superior.
#   random.randint(1, 100)  -> puede ser 1, 2, 3, ..., 99, 100
#   random.randint(1, 6)    -> simula un dado de 6 caras
#
# NOTA: Cada vez que ejecutas el programa, se genera un numero DIFERENTE.
# Si quisieras resultados reproducibles (para pruebas), usarias:
#   random.seed(42)  -> siempre generara la misma secuencia
numero_a_adivinar = random.randint(1, 100)

# --- CONTADOR DE INTENTOS ---
# Inicializamos en 0 y lo incrementamos en cada intento.
# El ciclo continua mientras intentos < 5 (permite 5 intentos: 0,1,2,3,4).
intentos = 0

# Mensajes de bienvenida al juego
print("Adivina el numero entre 1 y 100")
print("Tienes 5 intentos")
print("Buena suerte!")

# --- CICLO DEL JUEGO ---
# El while se ejecuta mientras queden intentos (intentos < 5).
# Cada iteracion es un intento del jugador.
while intentos < 5:
    # Incrementar el contador al inicio de cada intento.
    # Despues de esta linea: intento 1, 2, 3, 4 o 5.
    intentos += 1

    # Pedir el numero al usuario
    # NOTA: No hay validacion del rango (1-100) ni manejo de errores
    # si el usuario ingresa texto. Podrias mejorarlo con try/except.
    numero_ingresado = int(input("Ingrese un numero: "))

    # --- PISTAS: BUSQUEDA BINARIA GUIADA ---
    # El programa indica si el numero es mayor o menor.
    # Con esta informacion, el jugador puede usar una estrategia
    # de "busqueda binaria": siempre adivinar el numero del medio
    # del rango posible.
    #
    # Ejemplo de estrategia optima:
    #   Rango: 1-100, adivina 50 -> "mayor" -> Rango: 51-100
    #   Rango: 51-100, adivina 75 -> "menor" -> Rango: 51-74
    #   Rango: 51-74, adivina 62 -> "mayor" -> Rango: 63-74
    #   ...
    # Con busqueda binaria, 7 intentos bastan para cualquier numero del 1-100.
    # Con 5 intentos, no siempre es posible ganar.
    if numero_ingresado < numero_a_adivinar:
        print("Intenta un numero mayor")
    elif numero_ingresado > numero_a_adivinar:
        print("Intenta un numero menor")
    else:
        # --- ADIVINASTE! ---
        print(f"GANASTE! El numero a adivinar era {numero_a_adivinar}")
        print(f"Se necesitaron {intentos} intentos para adivinar el numero")
        # --- BREAK ---
        # 'break' sale INMEDIATAMENTE del ciclo while.
        # Sin break, el ciclo seguiria pidiendo intentos aun despues de ganar.
        #
        # IMPORTANTE: Cuando break termina un while, la clausula 'else'
        # del while NO se ejecuta. Solo se ejecuta si el while termina
        # "naturalmente" (cuando la condicion se vuelve False).
        break

# --- CLAUSULA else DEL while ---
# Esta es una caracteristica UNICA de Python que muchos desconocen.
# El 'else' de un while se ejecuta SOLO cuando el ciclo termina
# porque la condicion se volvio False (fin natural).
# NO se ejecuta si el ciclo termino con 'break'.
#
# LOGICA EN ESTE JUEGO:
#   - Si el jugador adivina: break -> el else NO se ejecuta
#   - Si se agotan los 5 intentos: el while termina naturalmente -> else SE ejecuta
#
# OTROS USOS DE while/else:
#   - Buscar un elemento: si lo encuentras, break. Si no, el else indica "no encontrado".
#   - Reintentos: si funciona, break. Si no, el else indica "todos los reintentos fallaron".
else:
    print(f"PERDISTE! El numero a adivinar era {numero_a_adivinar}")

# =============================================================================
# NOTAS ADICIONALES PARA EL ESTUDIANTE:
#
# 1. BREAK, CONTINUE Y PASS:
#    break    -> Sale del ciclo inmediatamente
#    continue -> Salta a la siguiente iteracion (ignora el resto del bloque)
#    pass     -> No hace nada (placeholder para bloques vacios)
#
# 2. while/else vs for/else:
#    Ambos ciclos (while y for) pueden tener clausula else.
#    La logica es la misma: else se ejecuta si NO hubo break.
#
# 3. MEJORAS SUGERIDAS:
#    - Agregar try/except para manejar entrada invalida
#    - Validar que el numero este entre 1 y 100
#    - Mostrar cuantos intentos quedan en cada turno
#    - Permitir al usuario elegir la dificultad (rango y numero de intentos)
#
# 4. RETO: Invierte el juego. El usuario piensa un numero y la
#    computadora intenta adivinarlo usando busqueda binaria.
#    La computadora siempre ganara en 7 intentos o menos!
# =============================================================================
