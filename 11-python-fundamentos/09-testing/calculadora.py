"""
Calculadora — Modulo para Testear
====================================
Este modulo implementa una calculadora simple que sera utilizada
como sujeto de prueba en los archivos test_*.py de esta seccion.

Es intencionalmente simple para enfocarnos en COMO testear,
no en la logica del codigo.

Uso:
    from calculadora import Calculadora

    calc = Calculadora()
    calc.sumar(3, 5)       # 8
    calc.dividir(10, 3)    # 3.333...
    calc.dividir(10, 0)    # ZeroDivisionError
"""


class Calculadora:
    """Calculadora basica con las 4 operaciones fundamentales."""

    def __init__(self):
        self.historial = []

    def sumar(self, a, b):
        """Retorna la suma de a y b."""
        resultado = a + b
        self._registrar("suma", a, b, resultado)
        return resultado

    def restar(self, a, b):
        """Retorna la resta de a menos b."""
        resultado = a - b
        self._registrar("resta", a, b, resultado)
        return resultado

    def multiplicar(self, a, b):
        """Retorna el producto de a por b."""
        resultado = a * b
        self._registrar("multiplicacion", a, b, resultado)
        return resultado

    def dividir(self, a, b):
        """
        Retorna la division de a entre b.
        Lanza ZeroDivisionError si b es cero.
        """
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        resultado = a / b
        self._registrar("division", a, b, resultado)
        return resultado

    def _registrar(self, operacion, a, b, resultado):
        """Registra la operacion en el historial."""
        self.historial.append({
            "operacion": operacion,
            "a": a,
            "b": b,
            "resultado": resultado,
        })

    def limpiar_historial(self):
        """Limpia el historial de operaciones."""
        self.historial.clear()

    def ultimo_resultado(self):
        """Retorna el resultado de la ultima operacion, o None."""
        if not self.historial:
            return None
        return self.historial[-1]["resultado"]
