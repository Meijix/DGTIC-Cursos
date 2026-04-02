"""
Tests con unittest — Framework Built-in de Python
====================================================
unittest es el framework de testing incluido con Python.
Usa un estilo orientado a objetos: cada grupo de tests es una clase
que hereda de unittest.TestCase.

Ejecutar estos tests:
    python -m unittest test_basico.py
    python -m unittest test_basico.py -v   (verbose)
"""

import unittest

# Importamos el modulo que vamos a testear
from calculadora import Calculadora


class TestCalculadoraBasico(unittest.TestCase):
    """
    Tests basicos de la calculadora.
    Cada metodo que empiece con 'test_' se ejecuta como un test.
    """

    def setUp(self):
        """
        Se ejecuta ANTES de cada test.
        Aqui preparamos lo que necesitamos (patron Arrange).
        Esto garantiza que cada test empiece con una calculadora limpia.
        """
        self.calc = Calculadora()

    def tearDown(self):
        """
        Se ejecuta DESPUES de cada test.
        Aqui hacemos limpieza si es necesario.
        En este caso no hay nada que limpiar, pero es bueno conocerlo.
        """
        pass

    # --------------------------------------------------------
    # TESTS DE SUMA
    # --------------------------------------------------------

    def test_sumar_positivos(self):
        """Sumar dos numeros positivos retorna su suma."""
        resultado = self.calc.sumar(3, 5)
        self.assertEqual(resultado, 8)

    def test_sumar_negativos(self):
        """Sumar dos numeros negativos retorna un negativo."""
        resultado = self.calc.sumar(-3, -5)
        self.assertEqual(resultado, -8)

    def test_sumar_cero(self):
        """Sumar cero no cambia el valor."""
        self.assertEqual(self.calc.sumar(7, 0), 7)
        self.assertEqual(self.calc.sumar(0, 7), 7)

    # --------------------------------------------------------
    # TESTS DE RESTA
    # --------------------------------------------------------

    def test_restar_basico(self):
        """Resta basica de dos numeros."""
        self.assertEqual(self.calc.restar(10, 3), 7)

    def test_restar_resultado_negativo(self):
        """Restar un numero mayor produce resultado negativo."""
        resultado = self.calc.restar(3, 10)
        self.assertLess(resultado, 0)  # Verifica que es menor que 0

    # --------------------------------------------------------
    # TESTS DE MULTIPLICACION
    # --------------------------------------------------------

    def test_multiplicar_basico(self):
        """Multiplicacion basica."""
        self.assertEqual(self.calc.multiplicar(4, 5), 20)

    def test_multiplicar_por_cero(self):
        """Cualquier numero por cero es cero."""
        self.assertEqual(self.calc.multiplicar(999, 0), 0)

    def test_multiplicar_por_uno(self):
        """Cualquier numero por uno es si mismo."""
        self.assertEqual(self.calc.multiplicar(42, 1), 42)

    # --------------------------------------------------------
    # TESTS DE DIVISION
    # --------------------------------------------------------

    def test_dividir_basico(self):
        """Division basica retorna resultado correcto."""
        resultado = self.calc.dividir(10, 2)
        self.assertEqual(resultado, 5.0)

    def test_dividir_con_decimales(self):
        """Division con resultado decimal."""
        resultado = self.calc.dividir(10, 3)
        # assertAlmostEqual compara con precision limitada
        # (por defecto 7 decimales, ideal para floats)
        self.assertAlmostEqual(resultado, 3.3333333, places=5)

    def test_dividir_por_cero_lanza_excepcion(self):
        """
        Dividir por cero debe lanzar ZeroDivisionError.
        assertRaises verifica que se lance la excepcion correcta.
        """
        # Forma 1: como context manager (recomendada)
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(10, 0)

    def test_dividir_por_cero_mensaje(self):
        """Verificar que el mensaje de error sea descriptivo."""
        with self.assertRaises(ZeroDivisionError) as context:
            self.calc.dividir(10, 0)
        # Verificar que el mensaje contiene texto esperado
        self.assertIn("cero", str(context.exception))

    # --------------------------------------------------------
    # TESTS DE HISTORIAL
    # --------------------------------------------------------

    def test_historial_vacio_al_inicio(self):
        """El historial comienza vacio."""
        self.assertEqual(len(self.calc.historial), 0)

    def test_historial_registra_operaciones(self):
        """Cada operacion se agrega al historial."""
        self.calc.sumar(1, 2)
        self.calc.restar(5, 3)
        self.assertEqual(len(self.calc.historial), 2)

    def test_ultimo_resultado_sin_operaciones(self):
        """Sin operaciones, ultimo_resultado retorna None."""
        self.assertIsNone(self.calc.ultimo_resultado())

    def test_ultimo_resultado_despues_de_operacion(self):
        """ultimo_resultado retorna el resultado mas reciente."""
        self.calc.sumar(3, 5)
        self.calc.multiplicar(2, 4)
        self.assertEqual(self.calc.ultimo_resultado(), 8)

    def test_limpiar_historial(self):
        """limpiar_historial vacia la lista."""
        self.calc.sumar(1, 1)
        self.calc.sumar(2, 2)
        self.calc.limpiar_historial()
        self.assertEqual(len(self.calc.historial), 0)

    # --------------------------------------------------------
    # TESTS CON assertTrue, assertFalse, assertIn
    # --------------------------------------------------------

    def test_resultado_es_numerico(self):
        """Los resultados deben ser numericos."""
        resultado = self.calc.sumar(3, 5)
        self.assertIsInstance(resultado, (int, float))

    def test_historial_contiene_operacion(self):
        """El historial registra el tipo de operacion."""
        self.calc.sumar(1, 2)
        primera = self.calc.historial[0]
        self.assertIn("operacion", primera)
        self.assertEqual(primera["operacion"], "suma")

    def test_resultado_positivo(self):
        """assertTrue verifica que una condicion sea verdadera."""
        resultado = self.calc.sumar(1, 1)
        self.assertTrue(resultado > 0)
        self.assertFalse(resultado < 0)


# ============================================================
# EJECUTAR TESTS
# ============================================================

# Esto permite ejecutar con: python test_basico.py
if __name__ == "__main__":
    unittest.main()
