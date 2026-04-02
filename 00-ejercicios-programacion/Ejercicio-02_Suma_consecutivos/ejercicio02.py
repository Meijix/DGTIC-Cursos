# =============================================================================
# EJERCICIO 02 - Suma de Numeros Consecutivos
# =============================================================================
# OBJETIVO: Recibir un numero entre 1 y 50 del usuario y sumar todos los
# numeros consecutivos desde 1 hasta ese numero.
# Ejemplo: Si el usuario ingresa 5, la suma es 1+2+3+4+5 = 15.
#
# CONCEPTOS CLAVE que aprenderas en este ejercicio:
#   - Funciones: def, parametros, return
#   - Entrada del usuario: input() e int()
#   - Validacion con ciclo 'while'
#   - Acumuladores (variable que acumula sumas)
#   - Operador de asignacion compuesta: +=
#
# PROGRESION: Este ejercicio introduce FUNCIONES y VALIDACION DE ENTRADA,
# dos conceptos fundamentales que se reutilizan en todos los ejercicios
# siguientes. Tambien se introduce input() para recibir datos del usuario.
# =============================================================================

# --- FUNCIONES EN PYTHON ---
# Una funcion es un bloque de codigo reutilizable que:
#   1. Tiene un NOMBRE descriptivo
#   2. Puede recibir PARAMETROS (datos de entrada)
#   3. Puede RETORNAR un resultado con 'return'
#
# SINTAXIS:
#   def nombre_funcion(parametro1, parametro2):
#       # codigo de la funcion
#       return resultado
#
# POR QUE usamos funciones?
#   - Evitar repetir codigo (DRY: Don't Repeat Yourself)
#   - Organizar el programa en partes mas pequeñas y comprensibles
#   - Facilitar las pruebas: puedes probar la funcion sola
#   - Reutilizar: puedes llamar la funcion muchas veces con datos distintos
#
# NOTA SOBRE NOMBRES: En Python, los nombres de funciones usan
# snake_case (palabras_separadas_por_guiones_bajos), NO camelCase.
def suma_consecutiva(numero):
    # --- ACUMULADOR ---
    # Un acumulador es una variable que va sumando valores en cada iteracion.
    # SIEMPRE se inicializa en 0 antes del ciclo.
    # ERROR COMUN: Olvidar inicializar el acumulador, lo que causa un NameError.
    suma = 0

    # range(1, numero + 1) genera: 1, 2, 3, ..., numero
    # Recordatorio: range() NO incluye el ultimo valor, por eso usamos numero + 1.
    #
    # DATO MATEMATICO: La suma de 1 hasta N tambien se puede calcular con
    # la formula de Gauss: N * (N + 1) / 2
    # Ejemplo: suma de 1 a 100 = 100 * 101 / 2 = 5050
    # Aqui usamos el ciclo para practicar, pero la formula es mas eficiente.
    for i in range(1, numero + 1):
        # '+=' es el operador de asignacion compuesta.
        # 'suma += i' es equivalente a 'suma = suma + i'
        # Otros operadores similares: -=, *=, /=, //=, %=
        suma += i

    # 'return' devuelve el resultado al lugar donde se llamo la funcion.
    # Sin 'return', la funcion devuelve None (nada) por defecto.
    # ERROR COMUN: Usar print() dentro de la funcion en vez de return.
    #   - print() MUESTRA el valor en pantalla pero NO lo devuelve.
    #   - return DEVUELVE el valor para que pueda usarse despues.
    return suma


# --- ENTRADA DEL USUARIO: input() ---
# input() siempre devuelve un STRING (texto), nunca un numero.
# Para usarlo como numero, debemos convertirlo:
#   int(input(...))   -> convierte a entero (sin decimales)
#   float(input(...)) -> convierte a flotante (con decimales)
#
# ERROR COMUN: Olvidar la conversion.
#   num = input("Numero: ")  # num es "5" (texto), no 5 (numero)
#   num + 1                  # ERROR: no puedes sumar texto + numero
#
# ADVERTENCIA: Si el usuario escribe letras en vez de numeros,
# int() lanzara un ValueError. En ejercicios posteriores veremos
# como manejar esto con try/except.
num = int(input("Ingrese un numero entre 1 y 50: "))

# --- VALIDACION CON WHILE ---
# El ciclo 'while' repite el bloque de codigo MIENTRAS la condicion sea True.
# Aqui lo usamos como un "guardian": no dejamos continuar al programa
# hasta que el usuario ingrese un valor valido.
#
# COMO FUNCIONA:
#   1. Si num esta entre 1 y 50, la condicion es False -> NO entra al while
#   2. Si num esta fuera de rango, la condicion es True -> pide de nuevo
#   3. Sigue pidiendo hasta que el usuario ingrese algo valido
#
# OPERADORES LOGICOS:
#   'or'  -> True si AL MENOS UNA condicion es verdadera
#   'and' -> True si AMBAS condiciones son verdaderas
#   'not' -> Invierte el valor (True -> False, False -> True)
#
# ALTERNATIVA mas legible:
#   while not (1 <= num <= 50):
# Python permite comparaciones encadenadas: 1 <= num <= 50
# que es equivalente a: num >= 1 and num <= 50
while num < 1 or num > 50:
    print("El numero ingresado no es valido")
    num = int(input("Ingrese un numero entre 1 y 50: "))

# --- LLAMADA A LA FUNCION ---
# Aqui llamamos a suma_consecutiva(num). El valor de 'num' se pasa como
# argumento al parametro 'numero' de la funcion.
# El resultado que devuelve 'return' se pasa directamente a print().
#
# NOTA: print() puede recibir multiples argumentos separados por comas.
# Los separa automaticamente con un espacio.
#   print("Hola", "mundo")  -> "Hola mundo"
#   print("Total:", 100)    -> "Total: 100"
print("La suma de sus consecutivos es:", suma_consecutiva(num))

# =============================================================================
# NOTAS ADICIONALES PARA EL ESTUDIANTE:
#
# 1. PATRON DE VALIDACION: El patron "pedir -> validar con while -> repedir"
#    es MUY comun en programacion. Lo veras en casi todos los ejercicios.
#
# 2. PRUEBA: Llama a suma_consecutiva(10) mentalmente. El resultado debe ser 55.
#    Verifica: 1+2+3+4+5+6+7+8+9+10 = 55
#
# 3. RETO: Modifica la funcion para que tambien funcione con numeros negativos.
#    Ejemplo: suma_consecutiva(-3) deberia sumar -3 + -2 + -1 + 0 = -6
# =============================================================================
