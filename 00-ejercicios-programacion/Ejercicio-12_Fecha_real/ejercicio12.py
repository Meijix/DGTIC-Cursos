# =============================================================================
# EJERCICIO 12 - Validacion de Fecha Real
# =============================================================================
# OBJETIVO: Recibir un dia, mes y año, y determinar si la fecha es real
# (valida) o no. Debe considerar años bisiestos para febrero.
#
# CONCEPTOS CLAVE que aprenderas en este ejercicio:
#   - Reutilizacion de funciones de ejercicios anteriores
#   - Logica condicional compleja con multiples niveles
#   - Operador 'in' para verificar pertenencia a una lista
#   - Variables bandera (flags): 'status' y 'bisiesto'
#   - Diseño de validacion de datos del mundo real
#
# PROGRESION: Este ejercicio COMBINA los ejercicios 10 (bisiesto) y 11
# (meses) en un programa mas complejo. Es el primer ejercicio que
# reutiliza codigo de ejercicios anteriores, demostrando el poder
# de las funciones. La complejidad logica aumenta significativamente
# con multiples niveles de if anidados.
# =============================================================================

# --- REUTILIZACION DE FUNCIONES ---
# Esta es EXACTAMENTE la funcion del Ejercicio 10.
# En un proyecto real, la importariamos desde un modulo:
#   from ejercicio10 import es_bisiesto
# Aqui la copiamos directamente para que el programa funcione de forma
# independiente.
#
# NOTA: El concepto de MODULOS e IMPORTACIONES se vera mas adelante.
# Por ahora, copiar la funcion demuestra por que es util tener
# funciones bien definidas: puedes reutilizarlas facilmente.
def es_bisiesto(año: int) -> bool:
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    else:
        return False


# --- FUNCION PRINCIPAL DE VALIDACION ---
# Esta funcion recibe dia, mes y año, y verifica si la combinacion
# forma una fecha real del calendario gregoriano.
#
# ESTRATEGIA DE VALIDACION (de lo general a lo especifico):
#   1. Verificar que el año sea valido (>= 1)
#   2. Verificar que el mes sea valido (1-12)
#   3. Verificar que el dia sea valido segun el mes:
#      - Febrero: 28 o 29 dias (depende de si es bisiesto)
#      - Meses de 31 dias: enero, marzo, mayo, julio, agosto, octubre, diciembre
#      - Meses de 30 dias: abril, junio, septiembre, noviembre
def es_fecha_real(dia, mes, año):
    # --- VARIABLE BANDERA (FLAG) ---
    # 'status' empieza como True y se cambia a False si se detecta
    # alguna condicion invalida. Al final, retornamos status.
    #
    # PATRON "CULPABLE HASTA DEMOSTRAR LO CONTRARIO" vs
    # "INOCENTE HASTA DEMOSTRAR LO CONTRARIO":
    #   - Aqui asumimos que la fecha ES valida (True) y buscamos razones para invalidarla.
    #   - Alternativa: asumir False e ir verificando cada condicion.
    # Ambos patrones son validos; la eleccion depende del problema.
    status = True
    bisiesto = False

    # --- VALIDACION DEL AÑO Y MES ---
    # Primero verificamos las condiciones mas generales.
    # Guardamos las condiciones en variables con nombres descriptivos
    # para hacer el codigo mas legible.
    cond_mes_invalid = (mes < 1 or mes > 12)
    cond_ano_invalid = (año < 1)

    if cond_ano_invalid:
        status = False
        print("Año invalido")

    if cond_mes_invalid:
        status = False
        print("Mes invalido")

    # --- VALIDACION DE FEBRERO (caso especial) ---
    # Febrero es el unico mes cuyo numero de dias depende del año.
    # En año bisiesto: 29 dias. En año normal: 28 dias.
    if mes == 2:
        # Aqui reutilizamos la funcion es_bisiesto() del Ejercicio 10.
        # NOTA: La comparacion '== True' es redundante:
        #   if es_bisiesto(año) == True:  -> funciona pero es verboso
        #   if es_bisiesto(año):          -> forma pythonica (preferida)
        # Ambas hacen lo mismo, pero la segunda es mas limpia.
        if es_bisiesto(año) == True:
            bisiesto = True
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")

        # Verificar el rango de dias segun si es bisiesto o no
        if bisiesto == True:
            if dia < 1 or dia > 29:
                status = False
                print("Dia invalido")
        else:
            if dia < 1 or dia > 28:
                status = False
                print("Dia invalido")

    # --- OPERADOR 'in' CON LISTAS ---
    # 'mes in [1,3,5,7,8,10,12]' verifica si el valor de 'mes'
    # esta contenido en la lista.
    #
    # Es equivalente a:
    #   mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12
    # Pero MUCHO mas corto y legible.
    #
    # 'in' funciona con listas, tuplas, strings, diccionarios y sets:
    #   "a" in "hola"           -> False
    #   "o" in "hola"           -> True
    #   3 in [1, 2, 3, 4]      -> True
    #   "x" in {"x": 1, "y": 2} -> True (busca en las llaves)
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        # Meses con 31 dias
        if dia < 1 or dia > 31:
            status = False
            print("Dia invalido")

    # --- MESES DE 30 DIAS ---
    # Si no es febrero (2) ni un mes de 31 dias, es un mes de 30 dias.
    # Estos son: abril (4), junio (6), septiembre (9), noviembre (11).
    else:
        if dia < 1 or dia > 30:
            status = False
            print("Dia invalido")

    return status


# --- PROGRAMA PRINCIPAL ---
# Pedimos los tres componentes de la fecha.
# NOTA: Aqui no hay validacion con while para cada entrada.
# La funcion es_fecha_real() se encarga de validar la combinacion completa.
year = int(input("Ingrese el año: "))
month = int(input("Ingrese el mes: "))
day = int(input("Ingrese el dia: "))

# Llamamos a la funcion con los argumentos en el orden correcto: dia, mes, año.
# ERROR POTENCIAL: Si confundes el orden (año, mes, dia), la validacion fallara.
# MEJORA: Usar argumentos nombrados para evitar confusion:
#   es_fecha_real(dia=day, mes=month, año=year)
print("Es fecha real?", es_fecha_real(day, month, year))

# =============================================================================
# NOTAS ADICIONALES PARA EL ESTUDIANTE:
#
# 1. COMPLEJIDAD CRECIENTE: Este es el ejercicio con la logica mas compleja
#    hasta ahora. Combina funciones reutilizadas, condicionales anidados,
#    el operador 'in' con listas, y variables bandera.
#
# 2. PRUEBAS RECOMENDADAS:
#    - 29/02/2024 -> True (2024 es bisiesto)
#    - 29/02/2023 -> False (2023 no es bisiesto)
#    - 31/04/2023 -> False (abril tiene 30 dias)
#    - 31/01/2023 -> True (enero tiene 31 dias)
#    - 00/01/2023 -> False (dia 0 no existe)
#    - 15/13/2023 -> False (mes 13 no existe)
#
# 3. MEJORA: La funcion podria retornar solo True/False sin imprimir
#    mensajes. Las funciones "puras" (sin efectos secundarios) son
#    mas faciles de reutilizar y probar.
#
# 4. MODULO datetime DE PYTHON:
#    Python tiene un modulo integrado para fechas:
#      from datetime import date
#      try:
#          date(2024, 2, 29)  # Valida automaticamente
#      except ValueError:
#          print("Fecha invalida")
#    Pero el objetivo de este ejercicio es entender la LOGICA detras.
# =============================================================================
