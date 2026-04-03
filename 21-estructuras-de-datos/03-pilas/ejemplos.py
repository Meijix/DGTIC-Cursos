"""
Pilas (Stacks) en Python
=========================
Una pila es una estructura de datos LIFO (Last In, First Out): el ultimo
elemento en entrar es el primero en salir. Es como una pila de platos:
solo puedes poner o quitar platos de la parte superior.
Operaciones principales: push (apilar), pop (desapilar), peek (ver tope).
"""


# =============================================================================
# 1. Implementacion de Pila usando lista
# =============================================================================
class Pila:
    """Pila implementada con una lista de Python."""
    def __init__(self):
        self._elementos = []

    def apilar(self, elemento):
        """Agrega un elemento al tope. O(1) amortizado."""
        self._elementos.append(elemento)

    def desapilar(self):
        """Remueve y retorna el elemento del tope. O(1)."""
        if self.esta_vacia():
            raise IndexError("La pila esta vacia")
        return self._elementos.pop()

    def tope(self):
        """Retorna el elemento del tope sin removerlo. O(1)."""
        if self.esta_vacia():
            raise IndexError("La pila esta vacia")
        return self._elementos[-1]

    def esta_vacia(self):
        """Verifica si la pila esta vacia. O(1)."""
        return len(self._elementos) == 0

    def tamano(self):
        """Retorna el numero de elementos. O(1)."""
        return len(self._elementos)

    def __repr__(self):
        return f"Pila({self._elementos})"


print("=" * 60)
print("1. OPERACIONES BASICAS DE PILA")
print("=" * 60)

pila = Pila()
for valor in [10, 20, 30, 40, 50]:
    pila.apilar(valor)
    print(f"  Apilar {valor}: {pila}")

print(f"  Tope: {pila.tope()}")
print(f"  Tamano: {pila.tamano()}")

while not pila.esta_vacia():
    print(f"  Desapilar: {pila.desapilar()} | Restante: {pila}")


# =============================================================================
# 2. Ejemplo practico: Verificar parentesis balanceados
# =============================================================================
def parentesis_balanceados(expresion):
    """
    Verifica si los parentesis, corchetes y llaves estan balanceados.
    Usa una pila para emparejar cada cierre con su apertura correspondiente.
    """
    pila = Pila()
    pares = {')': '(', ']': '[', '}': '{'}

    for caracter in expresion:
        if caracter in "([{":
            pila.apilar(caracter)
        elif caracter in ")]}":
            if pila.esta_vacia() or pila.tope() != pares[caracter]:
                return False
            pila.desapilar()

    return pila.esta_vacia()


print("\n" + "=" * 60)
print("2. PARENTESIS BALANCEADOS")
print("=" * 60)

expresiones = [
    "({[]})",
    "((()))",
    "{[()]}",
    "([)]",
    "(((",
    "(){}{[]()}",
]
for expr in expresiones:
    resultado = "Balanceado" if parentesis_balanceados(expr) else "NO balanceado"
    print(f'  "{expr}" -> {resultado}')


# =============================================================================
# 3. Ejemplo practico: Invertir cadena con pila
# =============================================================================
def invertir_cadena(cadena):
    """Invierte una cadena usando una pila."""
    pila = Pila()
    for caracter in cadena:
        pila.apilar(caracter)

    resultado = ""
    while not pila.esta_vacia():
        resultado += pila.desapilar()
    return resultado


print("\n" + "=" * 60)
print("3. INVERTIR CADENA CON PILA")
print("=" * 60)

textos = ["Hola Mundo", "Python", "UNAM"]
for texto in textos:
    print(f'  "{texto}" -> "{invertir_cadena(texto)}"')


# =============================================================================
# 4. Ejemplo practico: Conversion decimal a binario
# =============================================================================
def decimal_a_binario(numero):
    """
    Convierte un numero decimal a binario usando una pila.
    Se divide sucesivamente entre 2 y se apilan los residuos.
    """
    if numero == 0:
        return "0"

    pila = Pila()
    n = abs(numero)

    while n > 0:
        pila.apilar(n % 2)
        n //= 2

    binario = ""
    while not pila.esta_vacia():
        binario += str(pila.desapilar())

    return ("-" if numero < 0 else "") + binario


print("\n" + "=" * 60)
print("4. CONVERSION DECIMAL A BINARIO")
print("=" * 60)

decimales = [0, 5, 10, 42, 100, 255]
for dec in decimales:
    print(f"  {dec:>3} en decimal = {decimal_a_binario(dec):>9} en binario"
          f"  (verificacion: {bin(dec)})")


# =============================================================================
# 5. Ejemplo practico: Evaluar expresion postfija (notacion polaca inversa)
# =============================================================================
def evaluar_postfija(expresion):
    """
    Evalua una expresion en notacion postfija (RPN).
    Ejemplo: "3 4 + 2 *" = (3 + 4) * 2 = 14
    """
    pila = Pila()
    operadores = {'+', '-', '*', '/'}

    for token in expresion.split():
        if token in operadores:
            b = pila.desapilar()
            a = pila.desapilar()
            if token == '+': pila.apilar(a + b)
            elif token == '-': pila.apilar(a - b)
            elif token == '*': pila.apilar(a * b)
            elif token == '/': pila.apilar(a / b)
        else:
            pila.apilar(float(token))

    return pila.desapilar()


print("\n" + "=" * 60)
print("5. EVALUACION DE EXPRESION POSTFIJA (RPN)")
print("=" * 60)

expresiones_rpn = [
    ("3 4 +", "(3 + 4)"),
    ("3 4 + 2 *", "(3 + 4) * 2"),
    ("5 1 2 + 4 * + 3 -", "5 + (1+2)*4 - 3"),
]
for expr, infija in expresiones_rpn:
    resultado = evaluar_postfija(expr)
    print(f'  Postfija: "{expr}"')
    print(f'  Infija:   {infija} = {resultado:.0f}')
    print()

# Complejidad de operaciones
print("=" * 60)
print("RESUMEN DE COMPLEJIDAD")
print("=" * 60)
print("  Push (apilar):    O(1) amortizado")
print("  Pop (desapilar):  O(1)")
print("  Peek (tope):      O(1)")
print("  Busqueda:         O(n)")
