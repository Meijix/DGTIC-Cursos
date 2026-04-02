# 09 — Testing en Python

## Indice

1. [Por que Testear](#por-que-testear)
2. [Piramide de Testing](#piramide-de-testing)
3. [Anatomia de un Test: Arrange-Act-Assert](#anatomia-de-un-test-arrange-act-assert)
4. [unittest — Framework Built-in](#unittest--framework-built-in)
5. [pytest — El Estandar de la Industria](#pytest--el-estandar-de-la-industria)
6. [Fixtures en pytest](#fixtures-en-pytest)
7. [Parametrize — Testing con Multiples Datos](#parametrize--testing-con-multiples-datos)
8. [Mocking — Simular Dependencias](#mocking--simular-dependencias)
9. [Coverage — Cobertura de Codigo](#coverage--cobertura-de-codigo)
10. [TDD — Test-Driven Development](#tdd--test-driven-development)
11. [Buenas Practicas](#buenas-practicas)
12. [Errores Comunes en Testing](#errores-comunes-en-testing)
13. [Ejercicios](#ejercicios)

---

## Por que Testear

Los tests son la red de seguridad de tu codigo. Sin tests, cada
cambio es una apuesta.

### Beneficios concretos

1. **Detectar bugs temprano**: Un bug encontrado en desarrollo cuesta
   100x menos que uno encontrado en produccion.

2. **Confianza para refactorizar**: Si tienes tests, puedes reorganizar
   el codigo sabiendo que no rompiste nada. Sin tests, refactorizar
   da miedo y el codigo se deteriora.

3. **Documentacion viva**: Los tests muestran COMO se usa el codigo.
   A diferencia de los comentarios, los tests no se desactualizan
   porque fallan si el codigo cambia.

4. **Diseno mejor**: Escribir tests te obliga a crear codigo modular,
   con dependencias claras y funciones puras. Si es dificil de testear,
   probablemente esta mal disenado.

5. **Ahorro de tiempo**: Parece contraproducitvo, pero escribir tests
   AHORRA tiempo a mediano plazo. Cada hora invertida en tests evita
   horas de debugging manual.

### Cuando NO testear

- Prototipos descartables (scripts de una sola vez).
- Codigo que solo llama a otros modulos ya testeados.
- Configuracion trivial.

La regla practica: **si el codigo va a produccion, necesita tests**.

---

## Piramide de Testing

```
                  ╱╲
                 ╱  ╲
                ╱ E2E╲          ← Pocos: lentos, fragiles, costosos
               ╱ tests ╲         Simulan usuario real (Selenium, Playwright)
              ╱──────────╲
             ╱ Integracion╲     ← Moderados: verifican que los modulos
            ╱    tests     ╲      trabajan bien JUNTOS (API, BD)
           ╱────────────────╲
          ╱   Tests Unitarios╲  ← MUCHOS: rapidos, aislados, baratos
         ╱    (unit tests)    ╲   Prueban funciones/clases individuales
        ╱──────────────────────╲
```

### Distribucion ideal

| Tipo | Cantidad | Velocidad | Costo | Que prueba |
|------|----------|-----------|-------|------------|
| **Unitario** | 70-80% | Milisegundos | Bajo | Funcion/clase individual |
| **Integracion** | 15-20% | Segundos | Medio | Modulos trabajando juntos |
| **E2E** | 5-10% | Minutos | Alto | Flujo completo del usuario |

**En este curso nos enfocamos en tests unitarios**, que son la base
de todo testing y los mas importantes de dominar.

---

## Anatomia de un Test: Arrange-Act-Assert

Todo test sigue el patron **AAA** (tambien llamado Given-When-Then):

```python
def test_suma_numeros_positivos():
    # ARRANGE (Preparar) — configurar los datos de entrada
    a = 3
    b = 5

    # ACT (Actuar) — ejecutar la operacion que queremos probar
    resultado = sumar(a, b)

    # ASSERT (Verificar) — confirmar que el resultado es correcto
    assert resultado == 8
```

```
  ┌─────────────────────────────────────────────┐
  │              ARRANGE (Given)                │
  │  Preparar datos, crear objetos, configurar  │
  ├─────────────────────────────────────────────┤
  │                ACT (When)                   │
  │  Ejecutar la accion que queremos probar     │
  ├─────────────────────────────────────────────┤
  │              ASSERT (Then)                  │
  │  Verificar que el resultado es el esperado  │
  └─────────────────────────────────────────────┘
```

**Reglas del patron AAA**:
- Un test debe probar UNA sola cosa.
- El bloque ACT deberia ser una sola linea.
- Si necesitas muchos asserts, probablemente son multiples tests.

---

## unittest — Framework Built-in

`unittest` viene incluido con Python. Esta inspirado en JUnit (Java)
y usa un estilo orientado a objetos.

### Estructura basica

```python
import unittest

class TestCalculadora(unittest.TestCase):
    """Cada clase de test hereda de TestCase."""

    def setUp(self):
        """Se ejecuta ANTES de cada test (preparacion)."""
        self.calc = Calculadora()

    def tearDown(self):
        """Se ejecuta DESPUES de cada test (limpieza)."""
        pass

    def test_suma(self):
        """Cada metodo de test DEBE empezar con 'test_'."""
        resultado = self.calc.sumar(3, 5)
        self.assertEqual(resultado, 8)

if __name__ == "__main__":
    unittest.main()
```

### Ejecutar tests

```bash
# Ejecutar un archivo de tests
python -m unittest test_basico.py

# Descubrir y ejecutar todos los tests
python -m unittest discover

# Con mas detalle (verbose)
python -m unittest -v test_basico.py
```

### Metodos assert de unittest

| Metodo | Verifica |
|--------|----------|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `bool(x) is True` |
| `assertFalse(x)` | `bool(x) is False` |
| `assertIs(a, b)` | `a is b` |
| `assertIsNot(a, b)` | `a is not b` |
| `assertIsNone(x)` | `x is None` |
| `assertIsNotNone(x)` | `x is not None` |
| `assertIn(a, b)` | `a in b` |
| `assertNotIn(a, b)` | `a not in b` |
| `assertIsInstance(a, b)` | `isinstance(a, b)` |
| `assertNotIsInstance(a, b)` | `not isinstance(a, b)` |
| `assertRaises(Error)` | Lanza la excepcion `Error` |
| `assertAlmostEqual(a, b)` | `round(a-b, 7) == 0` |
| `assertGreater(a, b)` | `a > b` |
| `assertGreaterEqual(a, b)` | `a >= b` |
| `assertLess(a, b)` | `a < b` |
| `assertRegex(s, r)` | `re.search(r, s)` |
| `assertCountEqual(a, b)` | Mismos elementos sin importar orden |

### setUp y tearDown

```python
class TestBaseDatos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Se ejecuta UNA vez antes de TODOS los tests de la clase."""
        cls.conexion = conectar_bd()

    def setUp(self):
        """Se ejecuta antes de CADA test."""
        self.conexion.begin_transaction()

    def tearDown(self):
        """Se ejecuta despues de CADA test."""
        self.conexion.rollback()

    @classmethod
    def tearDownClass(cls):
        """Se ejecuta UNA vez despues de TODOS los tests."""
        cls.conexion.close()
```

---

## pytest — El Estandar de la Industria

pytest es el framework de testing mas popular en Python.
Es mas simple, mas potente y mas extensible que unittest.

### Por que pytest es preferido

| Caracteristica | unittest | pytest |
|---------------|----------|--------|
| Asserts | `self.assertEqual(a, b)` | `assert a == b` |
| Clase requerida | Si (TestCase) | No (funciones simples) |
| Fixtures | setUp/tearDown | `@pytest.fixture` (mas flexible) |
| Parametrize | No built-in | `@pytest.mark.parametrize` |
| Plugins | Pocos | Cientos (cov, mock, django, asyncio...) |
| Output en fallo | Basico | Detallado con diff |
| Autodescubrimiento | `test_*.py` | `test_*.py` y `*_test.py` |

### Instalacion

```bash
pip install pytest
```

### Sintaxis basica

```python
# test_ejemplo.py — no necesita clase ni imports especiales

def test_suma():
    assert 1 + 1 == 2

def test_string():
    assert "hola".upper() == "HOLA"

def test_lista():
    lista = [1, 2, 3]
    assert 2 in lista
    assert len(lista) == 3

def test_excepcion():
    import pytest
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

### Ejecutar tests

```bash
# Ejecutar todos los tests
pytest

# Un archivo especifico
pytest test_ejemplo.py

# Un test especifico
pytest test_ejemplo.py::test_suma

# Con output detallado
pytest -v

# Mostrar prints
pytest -s

# Parar en el primer fallo
pytest -x

# Ejecutar solo tests que fallaron la ultima vez
pytest --lf

# Ejecutar tests que coincidan con un patron
pytest -k "suma or resta"
```

### Mensajes de error detallados

Cuando un assert falla, pytest muestra EXACTAMENTE que salio mal:

```
    def test_lista():
        resultado = [1, 2, 3]
>       assert resultado == [1, 2, 4]
E       AssertionError: assert [1, 2, 3] == [1, 2, 4]
E         At index 2 diff: 3 != 4
```

Esto es MUCHO mas util que el `AssertionError` generico de unittest.

---

## Fixtures en pytest

Las fixtures son funciones que proveen datos o recursos a los tests.
Son mas flexibles que setUp/tearDown de unittest.

### Fixture basica

```python
import pytest

@pytest.fixture
def calculadora():
    """Crea una instancia de Calculadora para cada test."""
    return Calculadora()

def test_suma(calculadora):
    # pytest inyecta automaticamente la fixture como argumento
    assert calculadora.sumar(3, 5) == 8
```

### Fixture con setup y teardown (yield)

```python
@pytest.fixture
def base_datos():
    """Setup: crear conexion. Teardown: cerrarla."""
    db = conectar()        # Setup
    yield db               # El test se ejecuta aqui
    db.close()             # Teardown (siempre se ejecuta)
```

### Scope (alcance)

```python
@pytest.fixture(scope="function")   # Default: nueva para cada test
@pytest.fixture(scope="class")      # Una por clase de tests
@pytest.fixture(scope="module")     # Una por archivo .py
@pytest.fixture(scope="session")    # Una para toda la sesion de tests
```

### conftest.py

Archivo especial donde defines fixtures compartidas entre archivos:

```
tests/
├── conftest.py          # Fixtures disponibles para todos los tests
├── test_usuarios.py
├── test_productos.py
└── sub_modulo/
    ├── conftest.py      # Fixtures solo para este subdirectorio
    └── test_pedidos.py
```

```python
# conftest.py
import pytest

@pytest.fixture
def usuario_ejemplo():
    return {"nombre": "Ana", "edad": 25, "email": "ana@test.com"}

@pytest.fixture
def lista_productos():
    return [
        {"id": 1, "nombre": "Laptop", "precio": 999},
        {"id": 2, "nombre": "Mouse", "precio": 25},
    ]
```

### Fixtures parametrizadas

```python
@pytest.fixture(params=["sqlite", "postgres", "mysql"])
def base_datos(request):
    """El test se ejecuta 3 veces, una por cada BD."""
    db = conectar(request.param)
    yield db
    db.close()
```

---

## Parametrize — Testing con Multiples Datos

`@pytest.mark.parametrize` ejecuta el mismo test con diferentes datos.
Es perfecto para probar multiples casos sin duplicar codigo.

```python
import pytest

@pytest.mark.parametrize("entrada, esperado", [
    (1, 1),
    (2, 4),
    (3, 9),
    (0, 0),
    (-2, 4),
])
def test_cuadrado(entrada, esperado):
    assert entrada ** 2 == esperado
```

Esto genera 5 tests independientes. Si uno falla, los demas siguen.

### Parametrize con IDs descriptivos

```python
@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
], ids=["positivos", "mixtos", "ceros"])
def test_suma(a, b, esperado):
    assert a + b == esperado
```

Output:
```
test_suma[positivos] PASSED
test_suma[mixtos] PASSED
test_suma[ceros] PASSED
```

### Parametrize anidado (producto cartesiano)

```python
@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [10, 20])
def test_multiplicar(x, y):
    # Se ejecuta 6 veces: (1,10), (1,20), (2,10), (2,20), (3,10), (3,20)
    assert x * y == x * y
```

---

## Mocking — Simular Dependencias

El mocking reemplaza partes del sistema con objetos simulados.
Es esencial para tests unitarios que no deben depender de
servicios externos (APIs, bases de datos, archivos).

### Cuando usar mocks

```
  ┌─────────────────────────────────────────────────┐
  │               Tu funcion                       │
  │                                                 │
  │   resultado = api_externa.obtener_datos()       │
  │                   │                             │
  │                   ▼                             │
  │           En testing: MOCK                      │
  │           (respuesta simulada)                  │
  │                                                 │
  │           En produccion: API REAL               │
  │           (llamada al servidor)                 │
  └─────────────────────────────────────────────────┘
```

**Usa mocks cuando**:
- La dependencia es externa (API, BD, sistema de archivos).
- La dependencia es lenta (red, disco).
- La dependencia es no determinista (fecha actual, random).
- Quieres probar casos dificiles de reproducir (errores de red).

**NO uses mocks cuando**:
- Puedes usar la implementacion real sin problemas.
- El mock haria el test trivial (solo prueba el mock, no tu codigo).

### unittest.mock — Herramientas principales

| Herramienta | Uso |
|-------------|-----|
| `Mock()` | Objeto que acepta cualquier atributo/llamada |
| `MagicMock()` | Mock con metodos magicos (__len__, __iter__, etc.) |
| `patch()` | Reemplaza un objeto real con un mock temporalmente |
| `patch.object()` | Reemplaza un atributo especifico de un objeto |
| `patch.dict()` | Reemplaza temporalmente un diccionario |

### Mock basico

```python
from unittest.mock import Mock, MagicMock

# Mock acepta cualquier llamada y retorna otro Mock
api = Mock()
api.obtener_usuario.return_value = {"nombre": "Ana", "edad": 25}

resultado = api.obtener_usuario(42)
# resultado == {"nombre": "Ana", "edad": 25}

# Verificar que se llamo correctamente
api.obtener_usuario.assert_called_once_with(42)
```

### patch — Reemplazar temporalmente

```python
from unittest.mock import patch

# Como decorador
@patch("mi_modulo.requests.get")
def test_obtener_clima(mock_get):
    mock_get.return_value.json.return_value = {"temp": 22}
    resultado = obtener_clima("CDMX")
    assert resultado["temp"] == 22

# Como context manager
def test_obtener_clima():
    with patch("mi_modulo.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"temp": 22}
        resultado = obtener_clima("CDMX")
        assert resultado["temp"] == 22
```

### Metodos de verificacion de Mock

```python
mock = Mock()
mock(1, 2, key="valor")

mock.assert_called()                        # Se llamo al menos una vez
mock.assert_called_once()                   # Se llamo exactamente una vez
mock.assert_called_with(1, 2, key="valor")  # Ultima llamada con estos args
mock.assert_called_once_with(1, 2, key="valor")  # Una vez con estos args
mock.assert_not_called()                    # Nunca se llamo

# Inspeccionar llamadas
mock.call_count                    # Numero de llamadas
mock.call_args                     # Argumentos de la ultima llamada
mock.call_args_list                # Lista de todas las llamadas
```

---

## Coverage — Cobertura de Codigo

La cobertura mide que porcentaje de tu codigo se ejecuta durante los tests.

### Instalacion

```bash
pip install pytest-cov
```

### Uso

```bash
# Reporte en consola
pytest --cov=mi_modulo

# Reporte HTML detallado
pytest --cov=mi_modulo --cov-report=html

# Fallar si la cobertura es menor a 80%
pytest --cov=mi_modulo --cov-fail-under=80
```

### Ejemplo de reporte

```
---------- coverage: platform darwin, python 3.11 ----------
Name                    Stmts   Miss  Cover
-------------------------------------------
calculadora.py             20      3    85%
validador.py               35     10    71%
-------------------------------------------
TOTAL                      55     13    76%
```

### Que significa la cobertura

```
  100% ── Todas las lineas se ejecutaron (no garantiza que sea correcto)
   80% ── Buen objetivo para la mayoria de proyectos
   60% ── Minimo aceptable
   < 50% ── Problematico
```

**Importante**: 100% de cobertura NO significa 0 bugs.
La cobertura mide que lineas se ejecutan, no que se prueban
todos los casos posibles. Pero baja cobertura SI indica
que hay codigo sin probar.

---

## TDD — Test-Driven Development

TDD es una metodologia donde escribes el test ANTES del codigo.

### Ciclo Red-Green-Refactor

```
  ┌──────────────────────────────────────────┐
  │                                          │
  │    1. RED: Escribir un test que FALLE    │
  │         │                                │
  │         ▼                                │
  │    2. GREEN: Escribir el codigo MINIMO   │
  │       para que el test pase              │
  │         │                                │
  │         ▼                                │
  │    3. REFACTOR: Mejorar el codigo        │
  │       manteniendo los tests verdes       │
  │         │                                │
  │         └──────────► Volver a 1          │
  │                                          │
  └──────────────────────────────────────────┘
```

### Ejemplo: Implementar una pila (Stack)

```python
# --- Paso 1: RED — escribir el test primero ---

def test_pila_vacia():
    pila = Pila()
    assert pila.esta_vacia() == True
    assert len(pila) == 0

# Este test FALLA porque Pila no existe aun.

# --- Paso 2: GREEN — codigo minimo para pasar ---

class Pila:
    def __init__(self):
        self._items = []

    def esta_vacia(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

# El test pasa. Ahora escribimos el siguiente test.

# --- Siguiente ciclo RED ---

def test_push_y_pop():
    pila = Pila()
    pila.push(42)
    assert not pila.esta_vacia()
    assert pila.pop() == 42
    assert pila.esta_vacia()

# --- GREEN ---

class Pila:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def esta_vacia(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

# --- REFACTOR: agregar manejo de errores ---

def test_pop_pila_vacia():
    pila = Pila()
    with pytest.raises(IndexError, match="pila vacia"):
        pila.pop()
```

### Beneficios de TDD

1. Codigo testeable por disenio (porque el test se escribe primero).
2. Cobertura alta natural (todo el codigo se escribio para un test).
3. Pasos pequenos — reduce la complejidad del problema.
4. Los tests son la especificacion — defines que debe hacer antes de como.

### Cuando usar TDD

- Logica de negocio compleja.
- Algoritmos y transformaciones de datos.
- APIs publicas de librerias.
- Cuando NO tienes claro como implementar algo.

### Cuando NO usar TDD estricto

- Prototipos exploratorios (primero descubre, luego testea).
- UI y presentacion (mejor tests E2E).
- Codigo que interactua mucho con I/O (complejo de mockear).

---

## Buenas Practicas

### Nombrado de tests

```python
# MAL: nombre vago
def test_1():
    ...

# BIEN: describe que se prueba y que se espera
def test_sumar_numeros_positivos_retorna_suma():
    ...

def test_dividir_por_cero_lanza_excepcion():
    ...

def test_usuario_sin_email_no_se_registra():
    ...
```

**Patron recomendado**: `test_[que]_[condicion]_[resultado esperado]`

### Independencia de tests

```python
# MAL: un test depende de otro
class TestOrden:
    def test_crear_orden(self):
        self.orden = crear_orden()      # Modifica estado compartido

    def test_agregar_item(self):
        self.orden.agregar(item)        # Depende de test_crear_orden

# BIEN: cada test se prepara independientemente
class TestOrden:
    def test_crear_orden(self):
        orden = crear_orden()
        assert orden is not None

    def test_agregar_item(self):
        orden = crear_orden()           # Crea su propia orden
        orden.agregar(item)
        assert len(orden.items) == 1
```

### Un test, un concepto

```python
# MAL: prueba demasiadas cosas
def test_calculadora():
    assert sumar(1, 2) == 3
    assert restar(5, 3) == 2
    assert multiplicar(4, 5) == 20
    assert dividir(10, 2) == 5

# BIEN: cada concepto en su propio test
def test_sumar():
    assert sumar(1, 2) == 3

def test_restar():
    assert restar(5, 3) == 2
```

### Tests rapidos

Los tests unitarios deben ser rapidos (milisegundos):
- No acceder a la red.
- No acceder a la base de datos.
- No acceder al sistema de archivos (o usar tmpdir).
- Usar mocks para dependencias externas.

### Tests deterministas

El mismo test debe dar el mismo resultado siempre:
- No depender de la hora actual (mockear `datetime.now`).
- No depender de random (usar seed o mockear).
- No depender de orden de ejecucion.

### Estructura de archivos

```
proyecto/
├── src/
│   ├── calculadora.py
│   ├── usuario.py
│   └── ...
├── tests/
│   ├── conftest.py           # Fixtures compartidas
│   ├── test_calculadora.py   # Tests para calculadora
│   ├── test_usuario.py       # Tests para usuario
│   └── ...
├── pytest.ini                # Configuracion de pytest
└── requirements-test.txt     # Dependencias de testing
```

---

## Errores Comunes en Testing

| Error | Problema | Solucion |
|-------|----------|----------|
| Tests dependientes | Un test falla y rompe otros | Cada test independiente con su setup |
| Demasiados mocks | El test solo prueba los mocks | Mockear solo dependencias externas |
| Tests fragiles | Fallan con cambios cosmeticos | Probar comportamiento, no implementacion |
| Tests lentos | Nadie los ejecuta | Optimizar o separar en suites |
| Ignorar tests rotos | `@skip` permanente | Arreglar o eliminar el test |
| Assert sin mensaje | No sabes por que fallo | `assert x == y, "mensaje descriptivo"` |
| Probar internos | Tests se rompen al refactorizar | Probar la interfaz publica |
| No testear edge cases | Bugs en los limites | Lista vacia, None, 0, negativo, maximo |
| Copy-paste tests | Dificil de mantener | Usar parametrize o fixtures |
| Tests que nunca fallan | `assert True` escondido | Revisar que el test realmente verifica algo |

### Edge cases a considerar siempre

```python
# Para numeros:
# - 0, 1, -1
# - Numeros muy grandes
# - float("inf"), float("nan")

# Para strings:
# - "" (vacio)
# - " " (solo espacios)
# - String muy largo
# - Caracteres especiales y unicode

# Para colecciones:
# - [] / {} / set() (vacio)
# - Un solo elemento
# - Muchos elementos
# - Duplicados

# Para objetos:
# - None
# - Tipo incorrecto
```

---

## Ejercicios

### Nivel 1
1. Escribe tests unittest para una funcion `es_palindromo(texto)`.
2. Reescribe los mismos tests con pytest (nota la diferencia en simplicity).
3. Usa `assertRaises` / `pytest.raises` para verificar que tu funcion
   lanza `TypeError` si recibe un numero en vez de un string.

### Nivel 2
4. Crea una fixture que provea un diccionario de configuracion para tests.
5. Usa `@pytest.mark.parametrize` para probar una funcion `calcular_iva(precio, tasa)`
   con al menos 8 combinaciones diferentes.
6. Escribe tests para una clase `Inventario` con metodos `agregar`, `remover`,
   `buscar`, `total`. Usa setUp/fixture para inicializar el inventario.

### Nivel 3
7. Mockea una llamada a `requests.get` para probar una funcion que
   consume una API externa. Prueba el caso exitoso y el de error.
8. Usa `patch` para mockear `datetime.now()` y probar una funcion
   que se comporta diferente segun la hora del dia.
9. Practica TDD: implementa una clase `Carrito` de compras paso a paso,
   escribiendo el test primero cada vez.

### Nivel 4
10. Configura pytest-cov y logra al menos 90% de cobertura en un modulo.
11. Crea un conftest.py con fixtures de diferentes scopes y verifica
    el orden de ejecucion.
12. Implementa un test de integracion que pruebe dos modulos trabajando
    juntos (por ejemplo, `Usuario` + `BaseDatos`).
