"""
Tests con pytest — El Estandar de la Industria
=================================================
Los mismos tests de test_basico.py reescritos con pytest.
Nota como el codigo es mas simple, mas legible y mas pythonic.

Instalar pytest:
    pip install pytest

Ejecutar estos tests:
    pytest test_pytest.py
    pytest test_pytest.py -v    (verbose)
    pytest test_pytest.py -s    (mostrar prints)
"""

import pytest

# Importamos el modulo que vamos a testear
from calculadora import Calculadora


# ============================================================
# DIFERENCIA CLAVE: No necesitamos clase ni herencia
# ============================================================

# En pytest, un test es simplemente una funcion que empieza con test_.
# Usamos 'assert' nativo de Python en vez de self.assertEqual.

# ============================================================
# FIXTURE: reemplaza setUp de unittest
# ============================================================

@pytest.fixture
def calc():
    """
    Fixture que provee una Calculadora limpia para cada test.
    pytest inyecta automaticamente esta fixture como argumento
    cuando un test tiene un parametro con el mismo nombre.
    """
    return Calculadora()


# ============================================================
# TESTS DE SUMA
# ============================================================

def test_sumar_positivos(calc):
    """Sumar dos positivos retorna su suma."""
    # En pytest: simplemente 'assert'. Si falla, pytest muestra
    # exactamente que valores se compararon.
    assert calc.sumar(3, 5) == 8

def test_sumar_negativos(calc):
    """Sumar dos negativos retorna un negativo."""
    assert calc.sumar(-3, -5) == -8

def test_sumar_cero(calc):
    """Sumar cero no cambia el valor."""
    assert calc.sumar(7, 0) == 7
    assert calc.sumar(0, 7) == 7


# ============================================================
# TESTS DE RESTA
# ============================================================

def test_restar_basico(calc):
    """Resta basica de dos numeros."""
    assert calc.restar(10, 3) == 7

def test_restar_resultado_negativo(calc):
    """Restar un numero mayor produce resultado negativo."""
    resultado = calc.restar(3, 10)
    assert resultado < 0, f"Se esperaba negativo, se obtuvo {resultado}"
    # ^^ Mensaje personalizado en caso de fallo


# ============================================================
# TESTS DE MULTIPLICACION
# ============================================================

def test_multiplicar_basico(calc):
    """Multiplicacion basica."""
    assert calc.multiplicar(4, 5) == 20

def test_multiplicar_por_cero(calc):
    """Cualquier numero por cero es cero."""
    assert calc.multiplicar(999, 0) == 0

def test_multiplicar_por_uno(calc):
    """Cualquier numero por uno es si mismo."""
    assert calc.multiplicar(42, 1) == 42


# ============================================================
# TESTS DE DIVISION
# ============================================================

def test_dividir_basico(calc):
    """Division basica retorna resultado correcto."""
    assert calc.dividir(10, 2) == 5.0

def test_dividir_con_decimales(calc):
    """Division con resultado decimal."""
    resultado = calc.dividir(10, 3)
    # pytest.approx() es la alternativa a assertAlmostEqual
    assert resultado == pytest.approx(3.3333, rel=1e-3)

def test_dividir_por_cero_lanza_excepcion(calc):
    """
    Dividir por cero debe lanzar ZeroDivisionError.
    pytest.raises es la alternativa a assertRaises.
    """
    with pytest.raises(ZeroDivisionError):
        calc.dividir(10, 0)

def test_dividir_por_cero_mensaje(calc):
    """Verificar que el mensaje de error sea descriptivo."""
    with pytest.raises(ZeroDivisionError, match="cero"):
        # 'match' verifica que el mensaje contenga "cero" (regex)
        calc.dividir(10, 0)


# ============================================================
# TESTS DE HISTORIAL
# ============================================================

def test_historial_vacio_al_inicio(calc):
    """El historial comienza vacio."""
    assert len(calc.historial) == 0
    # Alternativa mas pythonica:
    assert not calc.historial

def test_historial_registra_operaciones(calc):
    """Cada operacion se agrega al historial."""
    calc.sumar(1, 2)
    calc.restar(5, 3)
    assert len(calc.historial) == 2

def test_ultimo_resultado_sin_operaciones(calc):
    """Sin operaciones, ultimo_resultado retorna None."""
    assert calc.ultimo_resultado() is None

def test_ultimo_resultado_despues_de_operacion(calc):
    """ultimo_resultado retorna el resultado mas reciente."""
    calc.sumar(3, 5)
    calc.multiplicar(2, 4)
    assert calc.ultimo_resultado() == 8

def test_limpiar_historial(calc):
    """limpiar_historial vacia la lista."""
    calc.sumar(1, 1)
    calc.sumar(2, 2)
    calc.limpiar_historial()
    assert calc.historial == []


# ============================================================
# TESTS CON VERIFICACIONES DIVERSAS
# ============================================================

def test_resultado_es_numerico(calc):
    """Los resultados deben ser numericos."""
    resultado = calc.sumar(3, 5)
    assert isinstance(resultado, (int, float))

def test_historial_contiene_operacion(calc):
    """El historial registra el tipo de operacion."""
    calc.sumar(1, 2)
    primera = calc.historial[0]
    assert "operacion" in primera
    assert primera["operacion"] == "suma"

def test_resultado_positivo(calc):
    """Verificar condiciones booleanas directamente."""
    resultado = calc.sumar(1, 1)
    assert resultado > 0
    assert not (resultado < 0)


# ============================================================
# COMPARACION: unittest vs pytest
# ============================================================

# ┌────────────────────────────┬────────────────────────────┐
# │        unittest            │          pytest             │
# ├────────────────────────────┼────────────────────────────┤
# │ class Test(TestCase):      │ def test_algo():           │
# │     def test_algo(self):   │     assert a == b          │
# │         self.assertEqual() │                            │
# ├────────────────────────────┼────────────────────────────┤
# │ def setUp(self):           │ @pytest.fixture            │
# │     self.calc = Calc()     │ def calc():                │
# │                            │     return Calc()           │
# ├────────────────────────────┼────────────────────────────┤
# │ self.assertRaises(Error)   │ pytest.raises(Error)       │
# ├────────────────────────────┼────────────────────────────┤
# │ self.assertAlmostEqual()   │ pytest.approx()            │
# ├────────────────────────────┼────────────────────────────┤
# │ python -m unittest         │ pytest                     │
# └────────────────────────────┴────────────────────────────┘
#
# Recomendacion: usa pytest para proyectos nuevos.
# unittest es util conocerlo porque lo encontraras en codigo existente.
