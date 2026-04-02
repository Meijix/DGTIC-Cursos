# =============================================================================
# EJERCICIO 15 - Juego de Volados (Coin Flip con Apuestas)
# =============================================================================
# OBJETIVO: Simular un juego de volados (lanzar moneda) contra la computadora.
# El juego tiene 3 rondas con sistema de apuestas.
#
# REGLAS:
#   1. Ambos jugadores (usuario y computadora) inician con $500
#   2. En cada ronda, ambos apuestan entre $20 y $100
#   3. El jugador elige AGUILA o SOL
#   4. La computadora elige automaticamente el lado opuesto
#   5. Se lanza la moneda (aleatorio)
#   6. El ganador se lleva ambas apuestas
#   7. Despues de 3 rondas, quien tenga mas dinero gana
#
# CONCEPTOS CLAVE que aprenderas en este ejercicio:
#   - Manejo de estado del juego (variables que cambian entre rondas)
#   - try/except para manejo de errores de entrada
#   - Multiples funciones trabajando juntas
#   - Modulo time para efectos de espera
#   - Ciclo de juego (game loop)
#   - Diseño de programas interactivos complejos
#
# PROGRESION: Este es el ejercicio mas complejo del modulo. Combina
# TODOS los conceptos anteriores: funciones, validacion, ciclos,
# condicionales, modulos (random, time), y agrega manejo de errores
# con try/except y gestion de estado del juego.
# =============================================================================

# --- IMPORTACIONES ---
# random: para generar la apuesta de la computadora y el resultado del volado
# time: para agregar pausas dramaticas (time.sleep)
import random
import time

# =============================================================================
# FUNCIONES
# =============================================================================

# --- FUNCION: obtener_apuesta ---
# Pide al jugador su apuesta con validacion robusta.
# Recibe el dinero actual del jugador para verificar que no apueste mas
# de lo que tiene.
#
# PATRON: while True + try/except + return
# Este es un patron MUY comun en Python para pedir entrada validada:
#   1. while True: crea un ciclo infinito
#   2. try/except: maneja errores si el usuario ingresa texto
#   3. if valido: return (sale del ciclo si la entrada es correcta)
#   4. else: muestra error y el ciclo repite (pide de nuevo)
#
# COMPARACION CON EJERCICIOS ANTERIORES:
# Antes usabamos: num = int(input(...)); while num < 1: ...
# Eso falla si el usuario escribe "abc" (ValueError en int()).
# El patron try/except es MAS ROBUSTO: atrapa esos errores.
def obtener_apuesta(dinero):
    # --- while True (CICLO INFINITO CONTROLADO) ---
    # El ciclo se repite "para siempre" hasta que un 'return' lo termine.
    # Esto garantiza que la funcion SIEMPRE devolvera una apuesta valida.
    #
    # ADVERTENCIA: Un while True sin condicion de salida crearia un
    # ciclo infinito real (el programa nunca terminaria). Aqui la
    # condicion de salida es el 'return' dentro del if.
    while True:
        # --- try/except (MANEJO DE EXCEPCIONES) ---
        # 'try' intenta ejecutar el codigo.
        # Si ocurre un error del tipo especificado en 'except', Python
        # NO detiene el programa, sino que ejecuta el bloque except.
        #
        # TIPOS COMUNES DE EXCEPCIONES:
        #   ValueError    -> int("abc"), float("xyz")
        #   TypeError     -> "texto" + 5 (tipos incompatibles)
        #   ZeroDivisionError -> 10 / 0
        #   IndexError    -> lista[100] (indice fuera de rango)
        #   KeyError      -> diccionario["clave_inexistente"]
        #   FileNotFoundError -> open("archivo_que_no_existe.txt")
        #
        # SINTAXIS:
        #   try:
        #       codigo_que_puede_fallar
        #   except TipoDeError:
        #       que_hacer_si_falla
        #   except OtroTipoDeError:
        #       que_hacer_si_falla_de_otra_forma
        #   finally:
        #       esto_se_ejecuta_SIEMPRE (con o sin error)
        try:
            apuesta = int(input(f"Ingrese su apuesta entre 20 y 100: "))
            # Validacion de rango Y de fondos disponibles
            # La apuesta debe ser:
            #   - Mayor o igual a 20
            #   - Menor o igual a 100
            #   - Menor o igual al dinero disponible del jugador
            if 20 <= apuesta <= 100 and apuesta <= dinero:
                return apuesta
            else:
                print("Ingrese una apuesta valida: ")
        except ValueError:
            # Si el usuario escribe "abc" en vez de un numero,
            # int() lanza un ValueError que atrapamos aqui.
            # En vez de que el programa se detenga con error,
            # mostramos un mensaje amigable y volvemos a pedir.
            print("Ingrese un numero valido: ")


# --- FUNCION: obtener_eleccion ---
# Pide al jugador que elija AGUILA (1) o SOL (0).
# Usa el mismo patron robusto: while True + try/except + return.
def obtener_eleccion():
    while True:
        try:
            eleccion = int(input("Elija 1-AGUILA o 0-SOL: "))
            # Solo acepta 0 o 1
            if 0 <= eleccion <= 1:
                return eleccion
            else:
                print("Ingrese una eleccion valida: ")
        except ValueError:
            print("Ingrese un numero valido: ")


# --- FUNCION: volado_tradicional ---
# Convierte el valor numerico (0 o 1) a texto legible ("SOL" o "AGUILA").
# Es una funcion de "traduccion" o "mapeo".
#
# ALTERNATIVAS:
#   1. Usando un diccionario:
#      def volado_tradicional(volado):
#          return {0: "SOL", 1: "AGUILA"}[volado]
#
#   2. Usando una lista:
#      def volado_tradicional(volado):
#          return ["SOL", "AGUILA"][volado]
#
#   3. Usando un operador ternario:
#      def volado_tradicional(volado):
#          return "AGUILA" if volado == 1 else "SOL"
def volado_tradicional(volado):
    if volado == 0:
        return "SOL"
    else:
        return "AGUILA"


# =============================================================================
# PROGRAMA PRINCIPAL - ESTADO INICIAL DEL JUEGO
# =============================================================================

# --- VARIABLES DE ESTADO ---
# El "estado" de un juego son todas las variables que describen la
# situacion actual. Aqui el estado incluye:
#   - Dinero de cada jugador
#   - Numero de ronda actual
#   - Numero total de rondas
#
# NOTA: En programacion de juegos mas avanzada, el estado se guarda
# en un diccionario o una clase (objeto):
#   estado = {"jugador_dinero": 500, "cpu_dinero": 500, "ronda": 1}
jugador_dinero = 500
computadora_dinero = 500

numero_ronda = 1
rondas_permitidas = 3

# --- MENSAJES DE BIENVENIDA ---
# time.sleep(segundos) pausa la ejecucion por el tiempo indicado.
# Esto crea un efecto dramatico, como si el programa estuviera "pensando".
#
# time.sleep() acepta decimales: time.sleep(0.5) pausa medio segundo.
#
# NOTA: En programas que no son interactivos (scripts de procesamiento),
# NUNCA uses time.sleep(). Solo es util para efectos visuales en
# programas interactivos como juegos.
print("Bienvenido al juego de volados")
time.sleep(1)
print("El juego tiene 3 rondas")
time.sleep(1)
print("Cada jugador inicia con 500")
time.sleep(1)
print("Que empiece el juego!")

# =============================================================================
# CICLO PRINCIPAL DEL JUEGO (GAME LOOP)
# =============================================================================
# Este while controla las rondas del juego. Cada iteracion es una ronda.
# Es el patron "game loop": un ciclo que actualiza el estado del juego
# en cada iteracion hasta que se cumple una condicion de fin.
while numero_ronda <= rondas_permitidas:
    print(f"Ronda {numero_ronda}")

    # --- FASE 1: APUESTAS ---
    # Primero apuesta la computadora, luego el jugador.
    print("La computadora realiza su apuesta")

    # La computadora genera una apuesta aleatoria.
    computadora_apuesta = random.randint(20, 100)

    # --- LOGICA DE APUESTA DE LA COMPUTADORA ---
    # Se debe verificar que la computadora no apueste mas de lo que tiene.
    # min() devuelve el menor de dos valores:
    #   min(80, 500) = 80   (apuesta normal, tiene suficiente dinero)
    #   min(80, 50) = 50    (la apuesta se limita al dinero disponible)
    #
    # Luego se genera un nuevo random entre 20 y ese maximo ajustado.
    # Esto asegura que la apuesta siempre sea pagable.
    computadora_apuesta = min(computadora_apuesta, computadora_dinero)
    computadora_apuesta = random.randint(20, computadora_apuesta)

    # Restar la apuesta del dinero de la computadora
    computadora_dinero -= computadora_apuesta
    print(f"La computadora apuesta {computadora_apuesta}")

    # El jugador ingresa su apuesta (con validacion robusta)
    jugador_apuesta = obtener_apuesta(jugador_dinero)
    jugador_dinero -= jugador_apuesta

    # --- FASE 2: ELECCIONES ---
    # El jugador elige AGUILA o SOL.
    # La computadora SIEMPRE elige el lado OPUESTO.
    # Esto simplifica el juego: siempre hay un ganador y un perdedor.
    jugador_eleccion = obtener_eleccion()

    # --- LOGICA OPUESTA ---
    # Si el jugador elige 1 (AGUILA), la computadora elige 0 (SOL).
    # Si el jugador elige 0 (SOL), la computadora elige 1 (AGUILA).
    #
    # ALTERNATIVA mas corta usando operador ternario:
    #   computadora_eleccion = 0 if jugador_eleccion == 1 else 1
    #
    # ALTERNATIVA aun mas corta usando resta:
    #   computadora_eleccion = 1 - jugador_eleccion
    #   (Si jugador=1, computadora=0. Si jugador=0, computadora=1.)
    if jugador_eleccion == 1:
        print("El jugador eligio AGUILA")
        computadora_eleccion = 0
    else:
        print("El jugador eligio SOL")
        computadora_eleccion = 1

    print(f"La computadora eligio: {computadora_eleccion} que es {volado_tradicional(computadora_eleccion)}")

    # --- FASE 3: LANZAMIENTO ---
    # Se genera el resultado aleatorio: 0 (SOL) o 1 (AGUILA).
    print("Volando moneda...")
    time.sleep(3)  # Pausa dramatica de 3 segundos
    volado = random.randint(0, 1)
    print(f"Resultado del volado: {volado} que es {volado_tradicional(volado)}")

    # --- FASE 4: DETERMINAR GANADOR DE LA RONDA ---
    # Comparamos la eleccion del jugador con el resultado del volado.
    # El ganador se lleva AMBAS apuestas (la suya + la del rival).
    #
    # NOTA SOBRE EL FLUJO DE DINERO:
    # Al inicio de la ronda, ambos "ponen" su apuesta (se resta de su total).
    # El ganador recibe de vuelta SU apuesta + la del rival.
    # Esto equivale a: el ganador gana lo que aposto el perdedor.
    if jugador_eleccion == volado:
        print("Ganaste!")
        jugador_dinero += computadora_apuesta + jugador_apuesta
    else:
        print("Perdiste!")
        computadora_dinero += computadora_apuesta + jugador_apuesta

    # Mostrar el estado actual despues de cada ronda
    print(f"Computadora: {computadora_dinero}")
    print(f"Jugador: {jugador_dinero}")

    # Avanzar a la siguiente ronda
    # Sin esta linea, el while seria infinito (numero_ronda nunca cambia).
    numero_ronda += 1

# =============================================================================
# RESULTADO FINAL
# =============================================================================
# Despues de las 3 rondas, comparamos el dinero final.
# Hay tres resultados posibles: ganar, perder o empatar.
print("Fin del juego")
if jugador_dinero > computadora_dinero:
    print("Ganaste!")
elif jugador_dinero < computadora_dinero:
    print("Perdiste!")
else:
    print("Empate!")

print(f"Dinero total CPU: {computadora_dinero}")
print(f"Dinero total Jugador: {jugador_dinero}")

# =============================================================================
# NOTAS ADICIONALES PARA EL ESTUDIANTE:
#
# 1. MANEJO DE ESTADO: Este ejercicio muestra como las variables de estado
#    (dinero, ronda) se actualizan en cada iteracion del game loop.
#    Entender esto es fundamental para cualquier programa interactivo.
#
# 2. try/except: Es la forma "pythonica" de manejar errores. En vez de
#    verificar ANTES si algo puede fallar (LBYL: Look Before You Leap),
#    Python prefiere INTENTAR y MANEJAR el error (EAFP: Easier to Ask
#    Forgiveness than Permission).
#
# 3. MEJORAS SUGERIDAS:
#    - Permitir que el usuario elija cuantas rondas jugar
#    - Agregar un sistema de "doble o nada"
#    - Mostrar un historial de rondas al final
#    - Detectar cuando un jugador se queda sin dinero suficiente
#    - Agregar mas opciones de apuesta (todo o nada, mitad, etc.)
#
# 4. PATRON GAME LOOP: El ciclo while que controla las rondas es un
#    "game loop" simplificado. En juegos reales (videojuegos), el game
#    loop es mas complejo e incluye:
#      while juego_activo:
#          procesar_entrada()    # Leer teclado/mouse
#          actualizar_estado()   # Logica del juego
#          dibujar_pantalla()    # Renderizar graficos
#
# 5. RETO FINAL: Convierte este juego en un torneo donde el usuario
#    juega multiples partidas (cada una de 3 rondas) y se lleva un
#    registro de victorias/derrotas.
# =============================================================================
