# =============================================================================
# EJERCICIO 07 - Perimetro de Cualquier Triangulo (Unificado)
# =============================================================================
# OBJETIVO: Programa que calcula el perimetro de un triangulo segun su tipo
# (equilatero, isosceles o escaleno). El usuario elige el tipo mediante
# un menu y el programa solicita los datos necesarios.
#
# CONCEPTOS CLAVE que aprenderas en este ejercicio:
#   - Menus interactivos con el usuario
#   - Funciones que llaman a otras funciones
#   - Condicionales multiples: if / elif / else
#   - Diseño de programas mas complejos
#   - Recursion implicita (una funcion que se llama a si misma indirectamente)
#
# PROGRESION: Este ejercicio UNIFICA los ejercicios 04, 05 y 06 en un
# solo programa. Es un salto importante en complejidad: combina menus,
# condicionales y validacion en una estructura mas grande.
# Aprende a descomponer un problema grande en funciones mas pequeñas.
# =============================================================================

# --- FUNCION PRINCIPAL DE CALCULO ---
# Esta funcion recibe la opcion del menu y ejecuta la logica correspondiente.
# Internamente solicita los datos necesarios segun el tipo de triangulo.
#
# NOTA SOBRE DISEÑO: Esta funcion hace dos cosas:
#   1. Pide datos al usuario (input)
#   2. Calcula el perimetro
# En diseño profesional, separarfamos estas responsabilidades.
# Pero para un ejercicio educativo, es una buena forma de ver como
# los condicionales dirigen el flujo del programa.
def calcular_perimetro(opcion):

    # --- IF / ELIF / ELSE ---
    # Estructura de decision multiple. Python evalua las condiciones en orden:
    #   1. Si opcion == 1, ejecuta el bloque del equilatero
    #   2. Si no, revisa si opcion == 2 (isosceles)
    #   3. Si no, revisa si opcion == 3 (escaleno)
    #   4. Si ninguna se cumple, ejecuta el 'else'
    #
    # IMPORTANTE: Solo se ejecuta UN bloque. Una vez que encuentra una
    # condicion verdadera, ignora todas las demas.

    # --- Opcion 1: Triangulo equilatero ---
    if opcion == 1:
        long_lado = float(input("Ingrese la longitud de uno de los lados del triangulo equilatero: "))
        # Validacion: el lado debe ser mayor a 0
        while long_lado <= 0:
            print("La longitud del lado debe ser mayor a 0")
            long_lado = float(input("Ingrese la longitud de uno de los lados del triangulo equilatero: "))
        perimetro = long_lado * 3

    # --- Opcion 2: Triangulo isosceles ---
    elif opcion == 2:
        base = float(input("Ingrese la longitud de la base: "))
        while base <= 0:
            print("La longitud de la base debe ser mayor a 0")
            base = float(input("Ingrese la longitud de la base: "))
        lado = float(input("Ingrese la longitud de los lados iguales: "))
        while lado <= 0:
            print("La longitud de los lados iguales debe ser mayor a 0")
            lado = float(input("Ingrese la longitud de los lados iguales: "))
        perimetro = base + 2 * lado

    # --- Opcion 3: Triangulo escaleno ---
    elif opcion == 3:
        lado1 = float(input("Ingrese la longitud del lado 1: "))
        while lado1 <= 0:
            print("La longitud del lado debe ser mayor a 0")
            lado1 = float(input("Ingrese la longitud del lado 1: "))

        lado2 = float(input("Ingrese la longitud del lado 2: "))
        while lado2 <= 0:
            print("La longitud del lado debe ser mayor a 0")
            lado2 = float(input("Ingrese la longitud del lado 2: "))

        lado3 = float(input("Ingrese la longitud del lado 3: "))
        while lado3 <= 0:
            print("La longitud del lado debe ser mayor a 0")
            lado3 = float(input("Ingrese la longitud del lado 3: "))

        perimetro = lado1 + lado2 + lado3

    # --- Opcion invalida ---
    # Si el usuario ingresa un numero que no es 1, 2 ni 3.
    # NOTA: Aqui se llama a tipo_triangulo() para volver a mostrar el menu.
    # Esto crea una especie de "recursion indirecta":
    #   calcular_perimetro() -> tipo_triangulo() -> calcular_perimetro()
    #
    # ADVERTENCIA: Este enfoque puede causar problemas si el usuario
    # ingresa muchas opciones invalidas (cada llamada ocupa memoria).
    # Una mejor solucion seria usar un ciclo while en el programa principal:
    #   tipo_actual = tipo_triangulo()
    #   while tipo_actual not in [1, 2, 3]:
    #       print("Opcion invalida")
    #       tipo_actual = tipo_triangulo()
    else:
        print("Opcion invalida")
        tipo_triangulo()

    return perimetro


# --- FUNCION DE MENU ---
# Esta funcion muestra las opciones disponibles y devuelve la eleccion.
# Separar el menu en su propia funcion es buena practica porque:
#   1. Mantiene el codigo organizado
#   2. Permite reutilizar el menu facilmente
#   3. Hace el programa principal mas legible
#
# NOTA SOBRE ORDEN DE DEFINICION:
# En Python, las funciones deben estar DEFINIDAS antes de ser LLAMADAS.
# Aqui tipo_triangulo() se define despues de calcular_perimetro(),
# pero funciona porque ambas se llaman al final del programa (lineas 94-96).
# Lo que importa es que esten definidas ANTES de la primera llamada.
def tipo_triangulo():
    print("Ingresa el numero correspondiente a tu tipo de triangulo")
    print("1. Triangulo equilatero")
    print("2. Triangulo isoceles")
    print("3. Triangulo escaleno")
    opcion = int(input("Ingrese el tipo de triangulo: "))
    return opcion


# --- PROGRAMA PRINCIPAL ---
# Aqui es donde se ejecuta el programa. Primero muestra el menu,
# luego calcula el perimetro segun la opcion elegida.
#
# FLUJO DEL PROGRAMA:
#   1. tipo_triangulo() muestra el menu y devuelve la opcion
#   2. La opcion se guarda en 'tipo_actual'
#   3. calcular_perimetro(tipo_actual) ejecuta la logica correspondiente
#   4. El resultado se muestra con print()
tipo_actual = tipo_triangulo()
print("El perimetro del triangulo es: ", calcular_perimetro(tipo_actual))

# =============================================================================
# NOTAS ADICIONALES PARA EL ESTUDIANTE:
#
# 1. UNIFICACION: Este ejercicio demuestra como combinar ejercicios
#    anteriores en un programa mas grande. En proyectos reales,
#    frecuentemente se construyen programas grandes a partir de
#    piezas mas pequeñas que ya funcionan.
#
# 2. MEJORA SUGERIDA: Agrega validacion al menu principal con un while
#    para que solo acepte opciones 1, 2 o 3, sin usar recursion.
#
# 3. CONCEPTO AVANZADO (match/case): En Python 3.10+, puedes reemplazar
#    la cadena if/elif/else con match/case:
#      match opcion:
#          case 1: ...
#          case 2: ...
#          case 3: ...
#          case _: print("Opcion invalida")
#    Lo veremos en el Ejercicio 11.
#
# 4. RETO: Agrega una opcion 4 que permita al usuario salir del programa,
#    y un ciclo que permita calcular multiples perimetros sin reiniciar.
# =============================================================================
