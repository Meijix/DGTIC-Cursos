"""
Arboles Binarios de Busqueda (BST) en Python
==============================================
Un arbol binario de busqueda es una estructura jerarquica donde cada nodo
tiene como maximo dos hijos. Para cada nodo, todos los valores en el
subarbol izquierdo son menores y todos en el derecho son mayores.
Esto permite busqueda, insercion y eliminacion en O(log n) promedio.
"""


# =============================================================================
# 1. Nodo y Arbol Binario de Busqueda
# =============================================================================
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBST:
    """Arbol Binario de Busqueda con operaciones completas."""
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        """Inserta un valor en el arbol. O(log n) promedio."""
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, valor)
        return nodo

    def buscar(self, valor):
        """Busca un valor en el arbol. O(log n) promedio."""
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)
        return self._buscar_recursivo(nodo.derecho, valor)

    def eliminar(self, valor):
        """Elimina un valor del arbol. O(log n) promedio."""
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return None
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, valor)
        else:
            # Caso 1: nodo hoja o con un solo hijo
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo
            # Caso 2: nodo con dos hijos - buscar sucesor inorden
            sucesor = self._minimo_nodo(nodo.derecho)
            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.valor)
        return nodo

    def _minimo_nodo(self, nodo):
        actual = nodo
        while actual.izquierdo:
            actual = actual.izquierdo
        return actual

    # Recorridos
    def inorden(self):
        """Recorrido inorden: izq -> raiz -> der (orden ascendente)."""
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.derecho, resultado)

    def preorden(self):
        """Recorrido preorden: raiz -> izq -> der."""
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    def _preorden(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden(nodo.izquierdo, resultado)
            self._preorden(nodo.derecho, resultado)

    def postorden(self):
        """Recorrido postorden: izq -> der -> raiz."""
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado

    def _postorden(self, nodo, resultado):
        if nodo:
            self._postorden(nodo.izquierdo, resultado)
            self._postorden(nodo.derecho, resultado)
            resultado.append(nodo.valor)

    def minimo(self):
        """Retorna el valor minimo del arbol."""
        if not self.raiz:
            return None
        return self._minimo_nodo(self.raiz).valor

    def maximo(self):
        """Retorna el valor maximo del arbol."""
        if not self.raiz:
            return None
        actual = self.raiz
        while actual.derecho:
            actual = actual.derecho
        return actual.valor

    def imprimir_arbol(self):
        """Imprime una representacion visual del arbol."""
        lineas = []
        self._construir_visual(self.raiz, "", True, lineas)
        return "\n".join(lineas)

    def _construir_visual(self, nodo, prefijo, es_ultimo, lineas):
        if nodo is not None:
            conector = "`-- " if es_ultimo else "|-- "
            lineas.append(prefijo + conector + str(nodo.valor))
            nuevo_prefijo = prefijo + ("    " if es_ultimo else "|   ")
            # Mostrar hijos: derecho primero (arriba), izquierdo despues (abajo)
            if nodo.izquierdo or nodo.derecho:
                self._construir_visual(nodo.derecho, nuevo_prefijo, False, lineas)
                self._construir_visual(nodo.izquierdo, nuevo_prefijo, True, lineas)


# =============================================================================
# Demostrar operaciones del BST
# =============================================================================
print("=" * 60)
print("1. ARBOL BINARIO DE BUSQUEDA - OPERACIONES")
print("=" * 60)

arbol = ArbolBST()
valores = [50, 30, 70, 20, 40, 60, 80, 10, 35, 45]

print("  Insertando valores:", valores)
for v in valores:
    arbol.insertar(v)

print(f"\n  Estructura del arbol:")
for linea in arbol.imprimir_arbol().split("\n"):
    print(f"    {linea}")

print(f"\n  Recorrido inorden (ascendente):  {arbol.inorden()}")
print(f"  Recorrido preorden:              {arbol.preorden()}")
print(f"  Recorrido postorden:             {arbol.postorden()}")

print(f"\n  Minimo: {arbol.minimo()}")
print(f"  Maximo: {arbol.maximo()}")

print(f"\n  Buscar 40: {arbol.buscar(40)}")
print(f"  Buscar 99: {arbol.buscar(99)}")

# Eliminar nodos
print(f"\n  Eliminar 20 (hoja):")
arbol.eliminar(20)
print(f"  Inorden: {arbol.inorden()}")

print(f"  Eliminar 30 (nodo con dos hijos):")
arbol.eliminar(30)
print(f"  Inorden: {arbol.inorden()}")

print(f"\n  Arbol despues de eliminaciones:")
for linea in arbol.imprimir_arbol().split("\n"):
    print(f"    {linea}")


# =============================================================================
# 2. Validar si un arbol es BST valido
# =============================================================================
def es_bst_valido(nodo, minimo=float('-inf'), maximo=float('inf')):
    """
    Verifica si un arbol binario cumple la propiedad de BST.
    Cada nodo debe estar dentro del rango (minimo, maximo).
    """
    if nodo is None:
        return True
    if nodo.valor <= minimo or nodo.valor >= maximo:
        return False
    return (es_bst_valido(nodo.izquierdo, minimo, nodo.valor) and
            es_bst_valido(nodo.derecho, nodo.valor, maximo))


print("\n" + "=" * 60)
print("2. VALIDAR BST")
print("=" * 60)

# BST valido
print(f"  Arbol actual es BST valido: {es_bst_valido(arbol.raiz)}")

# Crear un arbol invalido manualmente
raiz_invalida = Nodo(10)
raiz_invalida.izquierdo = Nodo(5)
raiz_invalida.derecho = Nodo(15)
raiz_invalida.izquierdo.derecho = Nodo(12)  # Viola la propiedad: 12 > 10
print(f"  Arbol invalido (12 en subarbol izquierdo de 10): "
      f"{es_bst_valido(raiz_invalida)}")

# Complejidad de operaciones
print("\n" + "=" * 60)
print("RESUMEN DE COMPLEJIDAD")
print("=" * 60)
print("  Busqueda:    O(log n) promedio, O(n) peor caso")
print("  Insercion:   O(log n) promedio, O(n) peor caso")
print("  Eliminacion: O(log n) promedio, O(n) peor caso")
print("  Recorridos:  O(n)")
print("  El peor caso ocurre con arboles degenerados (tipo lista)")
