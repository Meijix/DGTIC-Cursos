"""
Heaps (Monticulos) en Python
==============================
Un heap es un arbol binario completo que satisface la propiedad de heap:
- Min-Heap: el padre siempre es menor o igual que sus hijos.
- Max-Heap: el padre siempre es mayor o igual que sus hijos.
Es la estructura ideal para colas de prioridad y para obtener
el minimo/maximo en O(1) con inserciones/eliminaciones en O(log n).
Python provee el modulo 'heapq' que implementa un min-heap.
"""

import heapq


# =============================================================================
# 1. Uso del modulo heapq
# =============================================================================
print("=" * 60)
print("1. MODULO heapq - OPERACIONES BASICAS")
print("=" * 60)

# Crear un heap a partir de una lista
numeros = [35, 10, 27, 5, 18, 42, 3, 15]
print(f"  Lista original: {numeros}")

heapq.heapify(numeros)  # Convierte la lista en heap in-place O(n)
print(f"  Despues de heapify: {numeros}")
print(f"  Minimo (raiz): {numeros[0]}")

# Push: insertar un elemento O(log n)
heapq.heappush(numeros, 1)
print(f"  Despues de push(1): {numeros}")

# Pop: extraer el minimo O(log n)
minimo = heapq.heappop(numeros)
print(f"  Pop (extraer minimo={minimo}): {numeros}")

# Pushpop: push + pop en una sola operacion (mas eficiente)
resultado = heapq.heappushpop(numeros, 20)
print(f"  Pushpop(20), salio {resultado}: {numeros}")

# nlargest y nsmallest
datos = [64, 25, 12, 22, 11, 90, 45, 33]
print(f"\n  Datos: {datos}")
print(f"  3 mas grandes: {heapq.nlargest(3, datos)}")
print(f"  3 mas pequenos: {heapq.nsmallest(3, datos)}")

# Extraer todos en orden
heap_copia = datos[:]
heapq.heapify(heap_copia)
ordenados = []
while heap_copia:
    ordenados.append(heapq.heappop(heap_copia))
print(f"  Extraidos en orden (heapsort): {ordenados}")


# =============================================================================
# 2. Implementacion de MinHeap desde cero
# =============================================================================
class MinHeap:
    """Implementacion de Min-Heap usando un arreglo."""
    def __init__(self):
        self.heap = []

    def _padre(self, i):
        return (i - 1) // 2

    def _hijo_izq(self, i):
        return 2 * i + 1

    def _hijo_der(self, i):
        return 2 * i + 2

    def _intercambiar(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _subir(self, i):
        """Sube un elemento hasta restaurar la propiedad de heap."""
        while i > 0 and self.heap[i] < self.heap[self._padre(i)]:
            self._intercambiar(i, self._padre(i))
            i = self._padre(i)

    def _bajar(self, i):
        """Baja un elemento hasta restaurar la propiedad de heap."""
        tamano = len(self.heap)
        menor = i
        izq = self._hijo_izq(i)
        der = self._hijo_der(i)

        if izq < tamano and self.heap[izq] < self.heap[menor]:
            menor = izq
        if der < tamano and self.heap[der] < self.heap[menor]:
            menor = der

        if menor != i:
            self._intercambiar(i, menor)
            self._bajar(menor)

    def insertar(self, valor):
        """Inserta un elemento. O(log n)."""
        self.heap.append(valor)
        self._subir(len(self.heap) - 1)

    def extraer_minimo(self):
        """Extrae y retorna el minimo. O(log n)."""
        if not self.heap:
            raise IndexError("El heap esta vacio")
        minimo = self.heap[0]
        ultimo = self.heap.pop()
        if self.heap:
            self.heap[0] = ultimo
            self._bajar(0)
        return minimo

    def minimo(self):
        """Retorna el minimo sin extraerlo. O(1)."""
        if not self.heap:
            raise IndexError("El heap esta vacio")
        return self.heap[0]

    def tamano(self):
        return len(self.heap)

    def __repr__(self):
        return f"MinHeap({self.heap})"


print("\n" + "=" * 60)
print("2. MINHEAP IMPLEMENTADO DESDE CERO")
print("=" * 60)

mi_heap = MinHeap()
valores = [15, 10, 20, 8, 25, 5, 30]
for v in valores:
    mi_heap.insertar(v)
    print(f"  Insertar {v:>2}: {mi_heap}")

print(f"\n  Minimo actual: {mi_heap.minimo()}")
print(f"  Extrayendo en orden:")
while mi_heap.tamano() > 0:
    print(f"    Extraer minimo: {mi_heap.extraer_minimo()} | {mi_heap}")


# =============================================================================
# 3. Ejemplo practico: K elementos mas grandes
# =============================================================================
print("\n" + "=" * 60)
print("3. ENCONTRAR K ELEMENTOS MAS GRANDES")
print("=" * 60)


def k_mas_grandes(lista, k):
    """
    Encuentra los k elementos mas grandes usando un min-heap de tamano k.
    Complejidad: O(n log k) - mas eficiente que ordenar cuando k << n.
    """
    # Mantener un min-heap de tamano k
    heap = lista[:k]
    heapq.heapify(heap)

    for num in lista[k:]:
        if num > heap[0]:  # Si es mayor que el menor del heap
            heapq.heapreplace(heap, num)  # Reemplazar el menor

    return sorted(heap, reverse=True)


datos = [23, 65, 12, 3, 87, 45, 33, 91, 17, 56, 72, 8]
k = 4
print(f"  Datos: {datos}")
print(f"  Los {k} mas grandes: {k_mas_grandes(datos, k)}")


# =============================================================================
# 4. Ejemplo practico: Mezclar K listas ordenadas
# =============================================================================
print("\n" + "=" * 60)
print("4. MEZCLAR K LISTAS ORDENADAS")
print("=" * 60)


def mezclar_k_listas(listas):
    """
    Mezcla k listas ordenadas en una sola lista ordenada.
    Usa un heap para siempre extraer el menor elemento disponible.
    Complejidad: O(N log k), donde N = total de elementos, k = num listas.
    """
    resultado = []
    # El heap almacena tuplas: (valor, indice_lista, indice_elemento)
    heap = []

    for i, lista in enumerate(listas):
        if lista:
            heapq.heappush(heap, (lista[0], i, 0))

    while heap:
        valor, lista_idx, elem_idx = heapq.heappop(heap)
        resultado.append(valor)

        # Si hay mas elementos en esa lista, agregar el siguiente
        if elem_idx + 1 < len(listas[lista_idx]):
            siguiente = listas[lista_idx][elem_idx + 1]
            heapq.heappush(heap, (siguiente, lista_idx, elem_idx + 1))

    return resultado


listas_ordenadas = [
    [1, 5, 9, 13],
    [2, 6, 10],
    [3, 4, 7, 11, 12],
    [8, 14, 15],
]

print("  Listas ordenadas:")
for i, lista in enumerate(listas_ordenadas):
    print(f"    Lista {i}: {lista}")

mezclada = mezclar_k_listas(listas_ordenadas)
print(f"  Resultado mezclado: {mezclada}")

# Complejidad de operaciones
print("\n" + "=" * 60)
print("RESUMEN DE COMPLEJIDAD")
print("=" * 60)
print("  Obtener minimo/maximo: O(1)")
print("  Insertar:              O(log n)")
print("  Extraer minimo/maximo: O(log n)")
print("  Heapify (construir):   O(n)")
print("  Heapsort:              O(n log n)")
