# 08 — Manejo de Errores y Excepciones

## Indice

1. [Jerarquia de Excepciones](#jerarquia-de-excepciones)
2. [try / except / else / finally](#try--except--else--finally)
3. [EAFP vs LBYL](#eafp-vs-lbyl)
4. [Excepciones Personalizadas](#excepciones-personalizadas)
5. [Logging](#logging)
6. [Context Managers](#context-managers)
7. [Errores Comunes](#errores-comunes)
8. [Ejercicios](#ejercicios)

---

## Jerarquia de Excepciones

Todas las excepciones heredan de `BaseException`. Las que normalmente
capturamos heredan de `Exception`.

```
BaseException
├── SystemExit                    # sys.exit()
├── KeyboardInterrupt             # Ctrl+C
├── GeneratorExit                 # gen.close()
└── Exception                     # ← Base de TODAS las excepciones comunes
    ├── ArithmeticError
    │   ├── ZeroDivisionError     # division / 0
    │   ├── OverflowError         # numero demasiado grande
    │   └── FloatingPointError
    ├── AttributeError            # obj.atributo_inexistente
    ├── EOFError                  # input() sin datos
    ├── ImportError
    │   └── ModuleNotFoundError   # import modulo_inexistente
    ├── LookupError
    │   ├── IndexError            # lista[999]
    │   └── KeyError              # dict["clave_inexistente"]
    ├── NameError
    │   └── UnboundLocalError     # variable local no asignada
    ├── OSError
    │   ├── FileNotFoundError     # open("no_existe.txt")
    │   ├── PermissionError       # sin permisos
    │   ├── FileExistsError       # archivo ya existe (modo 'x')
    │   ├── IsADirectoryError     # operacion de archivo en directorio
    │   └── ConnectionError
    │       ├── ConnectionRefusedError
    │       └── ConnectionResetError
    ├── RuntimeError
    │   ├── NotImplementedError   # metodo abstracto no implementado
    │   └── RecursionError        # limite de recursion
    ├── StopIteration             # iterador agotado
    ├── TypeError                 # tipo incorrecto
    ├── ValueError                # valor incorrecto (tipo correcto)
    │   └── UnicodeError
    │       ├── UnicodeDecodeError
    │       └── UnicodeEncodeError
    └── Warning
        ├── DeprecationWarning
        ├── FutureWarning
        └── UserWarning
```

**Regla de oro**: nunca captures `BaseException` a menos que sepas
exactamente lo que haces. Captura `Exception` o, mejor aun, la
excepcion especifica.

---

## try / except / else / finally

```
  ┌──────────────────────────────────┐
  │           try:                   │
  │     codigo que puede fallar      │──── Si hay error ──┐
  ├──────────────────────────────────┤                     │
  │           except TipoError:      │◄────────────────────┘
  │     manejar el error             │
  ├──────────────────────────────────┤
  │           else:                  │◄── Solo si NO hubo error
  │     codigo si todo salio bien    │
  ├──────────────────────────────────┤
  │           finally:               │◄── SIEMPRE se ejecuta
  │     limpieza (cerrar archivos)   │    (haya o no error)
  └──────────────────────────────────┘
```

### Flujo detallado

```python
try:
    resultado = operacion()
except ValueError as e:
    # Se ejecuta SOLO si ocurre ValueError
    print(f"Error de valor: {e}")
except (TypeError, KeyError) as e:
    # Puedes capturar multiples tipos
    print(f"Error de tipo o clave: {e}")
except Exception as e:
    # Captura generica (ultimo recurso)
    print(f"Error inesperado: {e}")
else:
    # Se ejecuta SOLO si no hubo excepcion
    print(f"Exito: {resultado}")
finally:
    # Se ejecuta SIEMPRE (haya o no error)
    print("Limpieza completada")
```

### Reglas importantes

1. `except` sin tipo captura TODO (mala practica).
2. `else` se ejecuta solo si `try` termino sin excepcion.
3. `finally` se ejecuta SIEMPRE, incluso si hay `return` en `try`.
4. Los `except` se evaluan en orden — pon los mas especificos primero.
5. `as e` guarda la excepcion en variable para inspeccionarla.

---

## EAFP vs LBYL

Dos filosofias para manejar errores:

### LBYL — Look Before You Leap (Mira antes de saltar)

```python
# Verificar ANTES de actuar
if "clave" in diccionario:
    valor = diccionario["clave"]
else:
    valor = "default"
```

### EAFP — Easier to Ask Forgiveness than Permission (Pedir perdon)

```python
# Actuar y manejar el error si ocurre
try:
    valor = diccionario["clave"]
except KeyError:
    valor = "default"
```

**Python favorece EAFP** porque:
- Es mas legible en la mayoria de los casos.
- Es mas seguro ante condiciones de carrera (race conditions).
- Es mas rapido cuando el error es raro (el camino feliz no paga costo).

Usa LBYL cuando verificar sea barato y el error sea comun.
Usa EAFP cuando verificar sea costoso o el error sea raro.

---

## Excepciones Personalizadas

Crea tus propias excepciones cuando las built-in no describen bien el error.

```python
class ErrorDeValidacion(Exception):
    """Error al validar datos de entrada."""

    def __init__(self, campo, valor, mensaje):
        self.campo = campo
        self.valor = valor
        self.mensaje = mensaje
        super().__init__(f"{campo}: {mensaje} (valor: {valor!r})")

# Jerarquia personalizada
class ErrorDeAplicacion(Exception):
    """Base para todos los errores de la aplicacion."""

class ErrorDeAutenticacion(ErrorDeAplicacion):
    """Error al autenticar un usuario."""

class ErrorDeAutorizacion(ErrorDeAplicacion):
    """Error de permisos insuficientes."""
```

**Buenas practicas**:
- Hereda siempre de `Exception` (nunca de `BaseException`).
- Crea una excepcion base para tu aplicacion.
- Nombre descriptivo terminando en `Error` o `Exception`.
- Agrega atributos utiles (campo, codigo, contexto).
- Documenta cuando y por que se lanza.

---

## Logging

El modulo `logging` es la forma profesional de registrar eventos.
**Nunca uses print() para logs en produccion.**

### Niveles de logging

```
  Nivel        Valor   Uso
  ──────────── ─────   ─────────────────────────────────────
  DEBUG          10     Informacion detallada para diagnostico
  INFO           20     Confirmacion de que todo funciona bien
  WARNING        30     Algo inesperado, pero el programa sigue
  ERROR          40     Error grave, alguna funcionalidad fallo
  CRITICAL       50     Error fatal, el programa puede terminar
```

```
  DEBUG ──▶ INFO ──▶ WARNING ──▶ ERROR ──▶ CRITICAL
  (mas detalle)                           (mas grave)
```

### Configuracion basica

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

logger.debug("Variable x = 42")
logger.info("Servidor iniciado en puerto 8080")
logger.warning("Disco al 90%% de capacidad")
logger.error("No se pudo conectar a la BD")
logger.critical("Sistema de archivos corrupto")
```

### Handlers (donde van los logs)

| Handler | Destino |
|---------|---------|
| StreamHandler | Consola (stderr) |
| FileHandler | Archivo |
| RotatingFileHandler | Archivo con rotacion por tamanio |
| TimedRotatingFileHandler | Archivo con rotacion por tiempo |
| SMTPHandler | Email |
| HTTPHandler | Servidor HTTP |

---

## Context Managers

Los context managers garantizan que los recursos se liberen correctamente,
incluso si ocurre un error. Se usan con la sentencia `with`.

### Protocolo: `__enter__` y `__exit__`

```python
class MiContextManager:
    def __enter__(self):
        # Adquirir recurso
        print("Abriendo recurso")
        return self  # Lo que se asigna con 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Liberar recurso (SIEMPRE se ejecuta)
        print("Cerrando recurso")
        # Retornar True suprime la excepcion
        # Retornar False (o None) la propaga
        return False
```

### Con `contextlib.contextmanager`

```python
from contextlib import contextmanager

@contextmanager
def mi_recurso():
    # Setup (equivale a __enter__)
    print("Abriendo")
    recurso = "datos"
    try:
        yield recurso     # Lo que se asigna con 'as'
    finally:
        # Teardown (equivale a __exit__)
        print("Cerrando")
```

### Usos comunes

```python
# Archivos (el mas comun)
with open("archivo.txt") as f:
    contenido = f.read()
# El archivo se cierra automaticamente

# Locks en hilos
import threading
lock = threading.Lock()
with lock:
    # Seccion critica protegida
    pass

# Medir tiempo
import time
from contextlib import contextmanager

@contextmanager
def cronometro(nombre):
    inicio = time.perf_counter()
    yield
    duracion = time.perf_counter() - inicio
    print(f"{nombre}: {duracion:.4f}s")
```

---

## Errores Comunes

| Error | Causa | Solucion |
|-------|-------|----------|
| `except:` sin tipo | Captura TODO incluido Ctrl+C | Siempre especificar tipo |
| Silenciar errores | `except: pass` | Al menos loggear el error |
| `except Exception as e: print(e)` | Pierde el traceback | Usar `logging.exception()` |
| Capturar demasiado pronto | try/except en cada linea | Dejar que los errores suban |
| Usar excepciones para flujo | Excepciones como if/else | Usar condicionales normales |
| No limpiar recursos | Abrir sin cerrar | Usar `with` (context managers) |
| Re-raise incorrecto | `raise e` en vez de `raise` | `raise` sin argumento preserva traceback |
| Excepcion en finally | Error en bloque finally | Mantener finally simple |

---

## Ejercicios

### Nivel 1
1. Escribe una funcion `dividir(a, b)` que maneje `ZeroDivisionError`.
2. Crea un try/except/else/finally que abra un archivo, lea su contenido,
   y garantice que se cierre incluso si hay error.
3. Maneja `ValueError` al convertir input del usuario a entero.

### Nivel 2
4. Crea excepciones personalizadas para un sistema bancario:
   `SaldoInsuficiente`, `CuentaNoEncontrada`, `MontoInvalido`.
5. Implementa un context manager `TempDir` que cree un directorio
   temporal y lo elimine al salir del `with`.
6. Configura logging con dos handlers: consola (WARNING+) y archivo (DEBUG+).

### Nivel 3
7. Crea un decorador `@manejar_errores` que capture excepciones,
   las loggee y retorne un valor por defecto.
8. Implementa un context manager `Transaccion` para una base de datos
   simple (diccionario) que haga rollback si ocurre un error.
9. Escribe una funcion que use `ExceptionGroup` (Python 3.11+)
   para reportar multiples errores a la vez.

### Nivel 4
10. Combina excepciones personalizadas, logging y context managers
    para crear un mini-framework de procesamiento de archivos robusto.
