"""
Excepciones en Python — try / except / else / finally
=======================================================
Las excepciones son el mecanismo de Python para manejar errores
en tiempo de ejecucion. En lugar de verificar cada posible error
antes de actuar (LBYL), Python prefiere intentar y manejar el
error si ocurre (EAFP).

Ejecuta este archivo:
    python excepciones.py
"""

# ============================================================
# 1. try / except BASICO
# ============================================================

print("=== try / except basico ===\n")

# Sin manejo de errores, esto DETIENE el programa:
# resultado = 10 / 0  # ZeroDivisionError

# Con try/except, capturamos el error y continuamos:
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero")

# El programa continua normalmente
print("El programa sigue ejecutandose\n")

# ============================================================
# 2. CAPTURAR LA EXCEPCION CON 'as'
# ============================================================

print("=== Capturar con 'as' ===\n")

try:
    numeros = [1, 2, 3]
    print(numeros[10])
except IndexError as e:
    # 'e' contiene el objeto excepcion con informacion del error
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Mensaje: {e}")
    print(f"Args: {e.args}")

# ============================================================
# 3. MULTIPLES except — ORDEN IMPORTA
# ============================================================

print("\n=== Multiples except ===\n")

def convertir_y_dividir(texto, divisor):
    """Demuestra captura de diferentes tipos de error."""
    try:
        numero = int(texto)
        resultado = numero / divisor
        return resultado
    except ValueError:
        # Se evalua primero: int("abc") falla
        print(f"  ValueError: '{texto}' no es un numero valido")
    except ZeroDivisionError:
        # Se evalua segundo: division entre 0
        print(f"  ZeroDivisionError: no se puede dividir entre 0")
    except (TypeError, AttributeError) as e:
        # Se pueden agrupar varios tipos en una tupla
        print(f"  {type(e).__name__}: {e}")
    return None

convertir_y_dividir("abc", 2)    # ValueError
convertir_y_dividir("10", 0)     # ZeroDivisionError
convertir_y_dividir("10", 2)     # Exito (retorna 5.0)

# IMPORTANTE: los except se evaluan en ORDEN.
# Si pones Exception primero, captura TODO y los demas nunca se ejecutan.
# Siempre pon las excepciones mas especificas primero.

# ============================================================
# 4. else — SOLO SI NO HUBO ERROR
# ============================================================

print("\n=== else (solo si no hubo error) ===\n")

def buscar_en_diccionario(diccionario, clave):
    """Demuestra el bloque else."""
    try:
        valor = diccionario[clave]
    except KeyError:
        print(f"  La clave '{clave}' no existe")
    else:
        # Este bloque se ejecuta SOLO si try termino sin error.
        # Ventaja: el codigo en else NO esta protegido por except,
        # asi que si falla aqui, el error se propaga normalmente.
        print(f"  Encontrado: {clave} = {valor}")
        return valor
    return None

datos = {"nombre": "Ana", "edad": 25}
buscar_en_diccionario(datos, "nombre")    # Exito -> else
buscar_en_diccionario(datos, "telefono")  # Error -> except

# ============================================================
# 5. finally — SIEMPRE SE EJECUTA
# ============================================================

print("\n=== finally (siempre se ejecuta) ===\n")

def leer_archivo(ruta):
    """
    finally garantiza que el recurso se libere, haya o no error.
    (En la practica, usamos 'with' que hace esto automaticamente.)
    """
    archivo = None
    try:
        archivo = open(ruta, "r")
        contenido = archivo.read()
        print(f"  Leido: {len(contenido)} caracteres")
    except FileNotFoundError:
        print(f"  Archivo no encontrado: {ruta}")
    except PermissionError:
        print(f"  Sin permisos para leer: {ruta}")
    finally:
        # Esto se ejecuta SIEMPRE, incluso si hay return en try
        if archivo is not None:
            archivo.close()
            print("  Archivo cerrado (en finally)")
        else:
            print("  No habia archivo que cerrar (en finally)")

leer_archivo("archivo_inexistente.txt")

# ============================================================
# 6. RE-RAISING — RELANZAR EXCEPCIONES
# ============================================================

print("\n=== Re-raising excepciones ===\n")

def procesar_dato(valor):
    """
    A veces quieres loggear el error pero dejarlo propagarse.
    Usa 'raise' sin argumentos para relanzar la excepcion original.
    """
    try:
        return int(valor)
    except ValueError:
        print(f"  [LOG] Error al procesar '{valor}'")
        raise   # Relanza la MISMA excepcion con su traceback original
        # NUNCA uses 'raise e' — eso reinicia el traceback

try:
    procesar_dato("no_es_numero")
except ValueError as e:
    print(f"  Capturado arriba: {e}")

# ============================================================
# 7. raise — LANZAR EXCEPCIONES MANUALMENTE
# ============================================================

print("\n=== raise (lanzar excepciones) ===\n")

def validar_edad(edad):
    """Lanza excepciones cuando los datos son invalidos."""
    if not isinstance(edad, int):
        raise TypeError(f"La edad debe ser int, recibio {type(edad).__name__}")
    if edad < 0:
        raise ValueError(f"La edad no puede ser negativa: {edad}")
    if edad > 150:
        raise ValueError(f"Edad no realista: {edad}")
    return edad

# Caso valido
print(f"  Edad valida: {validar_edad(25)}")

# Casos invalidos
for valor in ["veinticinco", -5, 200]:
    try:
        validar_edad(valor)
    except (TypeError, ValueError) as e:
        print(f"  Error para {valor!r}: {e}")

# ============================================================
# 8. ENCADENAMIENTO DE EXCEPCIONES (raise ... from ...)
# ============================================================

print("\n=== raise ... from ... (encadenamiento) ===\n")

def conectar_base_datos():
    """Simula un error de conexion."""
    raise ConnectionError("No se pudo conectar al servidor")

def obtener_usuario(user_id):
    """Envuelve errores de bajo nivel en excepciones de alto nivel."""
    try:
        conectar_base_datos()
    except ConnectionError as e:
        # 'from e' preserva la excepcion original como __cause__
        raise RuntimeError(f"Error al obtener usuario {user_id}") from e

try:
    obtener_usuario(42)
except RuntimeError as e:
    print(f"  Error: {e}")
    print(f"  Causa original: {e.__cause__}")

# ============================================================
# 9. EJEMPLO INTEGRADOR
# ============================================================

print("\n=== Ejemplo integrador: calculadora segura ===\n")

def calculadora(expresion):
    """
    Evalua una operacion simple del tipo 'numero operador numero'.
    Demuestra el flujo completo try/except/else/finally.
    """
    partes = expresion.split()
    try:
        a = float(partes[0])
        op = partes[1]
        b = float(partes[2])

        if op == "+":
            resultado = a + b
        elif op == "-":
            resultado = a - b
        elif op == "*":
            resultado = a * b
        elif op == "/":
            resultado = a / b
        else:
            raise ValueError(f"Operador desconocido: '{op}'")

    except IndexError:
        print(f"  Formato invalido: usa 'num op num' (ej: '5 + 3')")
    except ValueError as e:
        print(f"  Error de valor: {e}")
    except ZeroDivisionError:
        print(f"  Error: division entre cero")
    else:
        # Solo se ejecuta si todo salio bien
        print(f"  {expresion} = {resultado}")
        return resultado
    finally:
        print(f"  [LOG] Expresion procesada: '{expresion}'")

    return None

calculadora("10 + 5")
calculadora("8 / 0")
calculadora("abc + 3")
calculadora("7 % 2")
calculadora("solo_un_numero")
