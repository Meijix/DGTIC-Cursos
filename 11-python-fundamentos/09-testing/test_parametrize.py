"""
Parametrize — Probar Multiples Casos con Un Solo Test
========================================================
@pytest.mark.parametrize ejecuta el mismo test con diferentes
datos de entrada. Elimina la duplicacion de tests y hace facil
agregar nuevos casos.

Ejecutar estos tests:
    pytest test_parametrize.py -v
"""

import pytest
from calculadora import Calculadora


# ============================================================
# 1. PARAMETRIZE BASICO
# ============================================================

@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),       # Caso basico: positivos
    (0, 0, 0),       # Caso borde: ceros
    (-1, -1, -2),    # Negativos
    (-1, 1, 0),      # Mixto
    (100, 200, 300), # Numeros grandes
    (0.1, 0.2, 0.3), # Flotantes (cuidado con precision)
])
def test_sumar(a, b, esperado):
    """
    Este test se ejecuta 6 VECES, una por cada tupla de parametros.
    Si uno falla, los demas siguen ejecutandose.
    """
    calc = Calculadora()
    resultado = calc.sumar(a, b)
    assert resultado == pytest.approx(esperado)
    # pytest.approx maneja la imprecision de flotantes


# ============================================================
# 2. PARAMETRIZE CON IDS DESCRIPTIVOS
# ============================================================

@pytest.mark.parametrize("a, b, esperado", [
    (10, 2, 5.0),
    (7, 2, 3.5),
    (1, 3, 0.3333),
    (-10, 2, -5.0),
    (0, 5, 0.0),
], ids=[
    "division_exacta",
    "resultado_decimal",
    "tercio",
    "dividendo_negativo",
    "cero_entre_algo",
])
def test_dividir(a, b, esperado):
    """
    Los ids aparecen en el output de pytest -v:
        test_dividir[division_exacta] PASSED
        test_dividir[resultado_decimal] PASSED
        test_dividir[tercio] PASSED
    Hacen el reporte mas legible que los valores por defecto.
    """
    calc = Calculadora()
    resultado = calc.dividir(a, b)
    assert resultado == pytest.approx(esperado, rel=1e-3)


# ============================================================
# 3. PARAMETRIZE PARA EXCEPCIONES
# ============================================================

@pytest.mark.parametrize("a, b", [
    (1, 0),
    (0, 0),
    (-5, 0),
    (999999, 0),
])
def test_dividir_por_cero(a, b):
    """Todos los casos de division por cero deben lanzar excepcion."""
    calc = Calculadora()
    with pytest.raises(ZeroDivisionError):
        calc.dividir(a, b)


# ============================================================
# 4. PARAMETRIZE CON MULTIPLES OPERACIONES
# ============================================================

@pytest.mark.parametrize("operacion, a, b, esperado", [
    ("sumar", 3, 5, 8),
    ("sumar", -1, 1, 0),
    ("restar", 10, 3, 7),
    ("restar", 0, 5, -5),
    ("multiplicar", 4, 5, 20),
    ("multiplicar", -2, 3, -6),
    ("dividir", 10, 2, 5.0),
    ("dividir", 7, 2, 3.5),
], ids=lambda params: f"{params}" if isinstance(params, str) else None)
def test_operacion_generica(operacion, a, b, esperado):
    """
    Un solo test parametrizado que prueba TODAS las operaciones.
    Usa getattr para llamar al metodo dinamicamente.
    """
    calc = Calculadora()
    metodo = getattr(calc, operacion)
    resultado = metodo(a, b)
    assert resultado == pytest.approx(esperado)


# ============================================================
# 5. PARAMETRIZE ANIDADO (PRODUCTO CARTESIANO)
# ============================================================

@pytest.mark.parametrize("a", [1, 5, 10, -3])
@pytest.mark.parametrize("b", [1, 2, 0.5])
def test_multiplicar_producto_cartesiano(a, b):
    """
    Dos decoradores @parametrize generan el PRODUCTO CARTESIANO.
    Con 4 valores de 'a' y 3 de 'b', se generan 12 tests:
        (1,1), (1,2), (1,0.5), (5,1), (5,2), (5,0.5), ...

    Util para probar todas las combinaciones posibles.
    """
    calc = Calculadora()
    resultado = calc.multiplicar(a, b)
    assert resultado == a * b


# ============================================================
# 6. PARAMETRIZE CON FUNCIONES PURAS
# ============================================================

def es_palindromo(texto):
    """Verifica si un texto es palindromo (ignora mayusculas y espacios)."""
    limpio = texto.lower().replace(" ", "")
    return limpio == limpio[::-1]

@pytest.mark.parametrize("texto, esperado", [
    ("ana", True),
    ("Oso", True),
    ("Anita lava la tina", True),
    ("Python", False),
    ("", True),                     # String vacio es palindromo
    ("a", True),                    # Un solo caracter es palindromo
    ("ab", False),
    ("aba", True),
    ("abba", True),
    ("reconocer", True),
], ids=lambda x: repr(x) if isinstance(x, str) else None)
def test_es_palindromo(texto, esperado):
    """Probar palindromos con muchos casos de forma compacta."""
    assert es_palindromo(texto) == esperado


# ============================================================
# 7. PARAMETRIZE CON pytest.param Y MARKERS
# ============================================================

@pytest.mark.parametrize("entrada, esperado", [
    pytest.param(2, 4, id="cuadrado_de_2"),
    pytest.param(0, 0, id="cuadrado_de_0"),
    pytest.param(-3, 9, id="cuadrado_de_negativo"),
    pytest.param(0.5, 0.25, id="cuadrado_de_fraccion"),
    pytest.param(
        1000000, 1000000000000,
        id="numero_grande",
        marks=pytest.mark.slow,    # Marcar tests especificos
    ),
])
def test_cuadrado(entrada, esperado):
    """
    pytest.param permite dar id y marks a casos individuales.
    Puedes filtrar con: pytest -m "not slow"
    """
    assert entrada ** 2 == pytest.approx(esperado)
