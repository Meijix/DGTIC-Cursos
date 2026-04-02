# =============================================================================
# EJERCICIO 08 - Tablas de Multiplicar
# =============================================================================
# OBJETIVO: Recibir un numero del usuario e imprimir su tabla de multiplicar
# del 2 al 10.
# Ejemplo: Si el usuario ingresa 7, imprime: 7x2=14, 7x3=21, ..., 7x10=70
#
# CONCEPTOS CLAVE que aprenderas en este ejercicio:
#   - Funciones que NO retornan valor (solo imprimen)
#   - f-strings con expresiones aritmeticas dentro de las llaves
#   - Diferencia entre funciones que retornan vs funciones que imprimen
#   - Ciclo for con range() para generar multiplicadores
#
# PROGRESION: Este ejercicio es mas corto que los anteriores pero introduce
# un concepto importante: funciones que realizan ACCIONES (imprimir) en
# lugar de CALCULAR Y RETORNAR valores. Tambien muestra que puedes poner
# expresiones matematicas directamente dentro de f-strings.
# =============================================================================

# --- FUNCION SIN RETURN ---
# Esta funcion imprime la tabla pero NO devuelve ningun valor.
# Cuando una funcion no tiene 'return', devuelve None automaticamente.
#
# DIFERENCIA IMPORTANTE:
#   def calcular(x):   -> Calcula y RETORNA el resultado (para usarlo despues)
#       return x * 2
#
#   def mostrar(x):    -> Muestra el resultado en pantalla (efecto secundario)
#       print(x * 2)
#
# CUANDO USAR CADA UNA:
#   - Usa return cuando necesitas el resultado para otra operacion
#   - Usa print cuando solo quieres mostrar informacion al usuario
#
# En este caso, la funcion solo necesita MOSTRAR la tabla, no devolver nada.
def tabla_multiplicar(numero):
    # range(2, 11) genera: 2, 3, 4, 5, 6, 7, 8, 9, 10
    # Recordatorio: el limite superior (11) NO se incluye.
    for i in range(2, 11):
        # --- EXPRESIONES DENTRO DE f-strings ---
        # Dentro de las llaves {} puedes poner CUALQUIER expresion valida:
        #   {numero}       -> el valor de la variable
        #   {numero * i}   -> el resultado de la multiplicacion
        #   {len("hola")}  -> el resultado de una funcion (4)
        #
        # Python evalua la expresion y coloca el resultado en el string.
        # Esto es muy poderoso y evita crear variables temporales.
        #
        # SIN f-strings, tendrias que escribir:
        #   print(str(numero) + " x " + str(i) + " = " + str(numero * i))
        # Que es mucho mas largo y dificil de leer.
        print(f"{numero} x {i} = {numero * i}")


# --- PROGRAMA PRINCIPAL ---
# Pedimos el numero y llamamos a la funcion.
# NOTA: No hay validacion aqui. Las tablas de multiplicar funcionan
# con cualquier numero, incluyendo negativos y cero.
#
# OBSERVACION: La llamada tabla_multiplicar(numero) NO se pasa a print()
# porque la funcion ya imprime internamente. Si hicieras:
#   print(tabla_multiplicar(numero))
# Se imprimiria la tabla Y luego "None" (el retorno implicito).
numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

# =============================================================================
# NOTAS ADICIONALES PARA EL ESTUDIANTE:
#
# 1. PRUEBA CON DISTINTOS VALORES:
#    - Ingresa 5: deberia imprimir 5x2=10, 5x3=15, ..., 5x10=50
#    - Ingresa 0: todas las multiplicaciones daran 0
#    - Ingresa -3: dara resultados negativos (-6, -9, ..., -30)
#
# 2. MEJORAS SUGERIDAS:
#    - Permitir que el usuario elija el rango (no solo 2-10)
#    - Agregar validacion para limitar a numeros positivos
#    - Mostrar multiples tablas en un solo ciclo
#
# 3. RETO: Modifica el programa para que imprima las tablas del 1 al 10
#    en formato de tabla (matriz), alineando los numeros.
#    Pista: usa print(f"{valor:4d}") para alinear a 4 caracteres.
#
# 4. NOTA SOBRE EFICIENCIA: La multiplicacion numero * i se calcula
#    "al vuelo" dentro del f-string. No se guarda en ninguna variable.
#    Esto es perfectamente eficiente para operaciones simples.
# =============================================================================
