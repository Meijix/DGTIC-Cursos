"""
Grafos en Python
=================
Un grafo es una estructura de datos compuesta por vertices (nodos) y
aristas (conexiones). Puede ser dirigido o no dirigido, ponderado o
no ponderado. Es la estructura mas versatil para modelar relaciones:
redes sociales, mapas, dependencias, etc.
Aqui implementamos un grafo con lista de adyacencia.
"""

from collections import deque
import heapq


# =============================================================================
# 1. Grafo no dirigido con lista de adyacencia
# =============================================================================
class Grafo:
    """Grafo no dirigido implementado con lista de adyacencia."""
    def __init__(self):
        self.adyacencia = {}

    def agregar_vertice(self, vertice):
        """Agrega un vertice al grafo."""
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = []

    def agregar_arista(self, origen, destino):
        """Agrega una arista no dirigida entre dos vertices."""
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.adyacencia[origen].append(destino)
        self.adyacencia[destino].append(origen)

    def bfs(self, inicio):
        """Busqueda en anchura (Breadth-First Search). O(V + E)."""
        visitados = set()
        cola = deque([inicio])
        visitados.add(inicio)
        orden = []

        while cola:
            vertice = cola.popleft()
            orden.append(vertice)
            for vecino in self.adyacencia[vertice]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        return orden

    def dfs(self, inicio):
        """Busqueda en profundidad (Depth-First Search). O(V + E)."""
        visitados = set()
        orden = []
        self._dfs_recursivo(inicio, visitados, orden)
        return orden

    def _dfs_recursivo(self, vertice, visitados, orden):
        visitados.add(vertice)
        orden.append(vertice)
        for vecino in self.adyacencia[vertice]:
            if vecino not in visitados:
                self._dfs_recursivo(vecino, visitados, orden)

    def existe_camino(self, origen, destino):
        """Verifica si existe un camino entre dos vertices usando BFS."""
        if origen not in self.adyacencia or destino not in self.adyacencia:
            return False
        visitados = set()
        cola = deque([origen])
        visitados.add(origen)

        while cola:
            vertice = cola.popleft()
            if vertice == destino:
                return True
            for vecino in self.adyacencia[vertice]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        return False

    def detectar_ciclo(self):
        """Detecta si el grafo no dirigido contiene un ciclo."""
        visitados = set()

        for vertice in self.adyacencia:
            if vertice not in visitados:
                if self._ciclo_dfs(vertice, visitados, None):
                    return True
        return False

    def _ciclo_dfs(self, vertice, visitados, padre):
        visitados.add(vertice)
        for vecino in self.adyacencia[vertice]:
            if vecino not in visitados:
                if self._ciclo_dfs(vecino, visitados, vertice):
                    return True
            elif vecino != padre:
                return True
        return False

    def mostrar(self):
        """Muestra la lista de adyacencia."""
        for vertice in sorted(self.adyacencia.keys()):
            vecinos = sorted(self.adyacencia[vertice])
            print(f"    {vertice}: {vecinos}")


# =============================================================================
# Demostrar grafo basico
# =============================================================================
print("=" * 60)
print("1. GRAFO NO DIRIGIDO - OPERACIONES BASICAS")
print("=" * 60)

grafo = Grafo()
aristas = [
    ("CDMX", "Puebla"), ("CDMX", "Queretaro"), ("CDMX", "Toluca"),
    ("Puebla", "Oaxaca"), ("Queretaro", "Guadalajara"),
    ("Guadalajara", "Monterrey"), ("Toluca", "Morelia"),
    ("Morelia", "Guadalajara"),
]

print("  Agregando aristas (ciudades conectadas):")
for origen, destino in aristas:
    grafo.agregar_arista(origen, destino)
    print(f"    {origen} <-> {destino}")

print(f"\n  Lista de adyacencia:")
grafo.mostrar()

# BFS y DFS
print(f"\n  BFS desde CDMX: {grafo.bfs('CDMX')}")
print(f"  DFS desde CDMX: {grafo.dfs('CDMX')}")


# =============================================================================
# 2. Verificar caminos y detectar ciclos
# =============================================================================
print("\n" + "=" * 60)
print("2. CAMINOS Y CICLOS")
print("=" * 60)

print(f"  Existe camino CDMX -> Monterrey: {grafo.existe_camino('CDMX', 'Monterrey')}")
print(f"  Existe camino Oaxaca -> Toluca: {grafo.existe_camino('Oaxaca', 'Toluca')}")

# Agregar un vertice aislado
grafo.agregar_vertice("Cancun")
print(f"  Existe camino CDMX -> Cancun: {grafo.existe_camino('CDMX', 'Cancun')}")

print(f"  El grafo contiene ciclo: {grafo.detectar_ciclo()}")

# Grafo sin ciclo (arbol)
arbol = Grafo()
arbol.agregar_arista("A", "B")
arbol.agregar_arista("A", "C")
arbol.agregar_arista("B", "D")
print(f"  Grafo tipo arbol (A-B, A-C, B-D) contiene ciclo: {arbol.detectar_ciclo()}")


# =============================================================================
# 3. Grafo ponderado con algoritmo de Dijkstra
# =============================================================================
class GrafoPonderado:
    """Grafo ponderado para encontrar caminos mas cortos."""
    def __init__(self):
        self.adyacencia = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = []

    def agregar_arista(self, origen, destino, peso):
        """Agrega una arista con peso (no dirigida)."""
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.adyacencia[origen].append((destino, peso))
        self.adyacencia[destino].append((origen, peso))

    def dijkstra(self, inicio):
        """
        Algoritmo de Dijkstra: encuentra la distancia minima desde
        un vertice a todos los demas. O((V + E) log V) con heap.
        """
        distancias = {v: float('inf') for v in self.adyacencia}
        distancias[inicio] = 0
        previos = {v: None for v in self.adyacencia}
        # Min-heap: (distancia, vertice)
        heap = [(0, inicio)]

        while heap:
            dist_actual, vertice = heapq.heappop(heap)

            if dist_actual > distancias[vertice]:
                continue  # Ya encontramos un camino mas corto

            for vecino, peso in self.adyacencia[vertice]:
                nueva_dist = dist_actual + peso
                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
                    previos[vecino] = vertice
                    heapq.heappush(heap, (nueva_dist, vecino))

        return distancias, previos

    def camino_mas_corto(self, inicio, destino):
        """Retorna el camino mas corto y su distancia."""
        distancias, previos = self.dijkstra(inicio)

        if distancias[destino] == float('inf'):
            return None, float('inf')

        camino = []
        actual = destino
        while actual is not None:
            camino.append(actual)
            actual = previos[actual]
        camino.reverse()

        return camino, distancias[destino]


print("\n" + "=" * 60)
print("3. GRAFO PONDERADO - DIJKSTRA")
print("=" * 60)

mapa = GrafoPonderado()
rutas = [
    ("CDMX", "Puebla", 130), ("CDMX", "Queretaro", 220),
    ("CDMX", "Toluca", 65), ("Puebla", "Oaxaca", 340),
    ("Queretaro", "Guadalajara", 290), ("Toluca", "Morelia", 245),
    ("Morelia", "Guadalajara", 310), ("Guadalajara", "Monterrey", 700),
    ("Queretaro", "Monterrey", 740),
]

print("  Rutas (distancias en km):")
for origen, destino, km in rutas:
    mapa.agregar_arista(origen, destino, km)
    print(f"    {origen} <-> {destino}: {km} km")

# Dijkstra desde CDMX
distancias, _ = mapa.dijkstra("CDMX")
print(f"\n  Distancias minimas desde CDMX:")
for ciudad, dist in sorted(distancias.items(), key=lambda x: x[1]):
    print(f"    CDMX -> {ciudad}: {dist} km")

# Camino mas corto especifico
camino, dist = mapa.camino_mas_corto("CDMX", "Monterrey")
print(f"\n  Camino mas corto CDMX -> Monterrey:")
print(f"    Ruta: {' -> '.join(camino)}")
print(f"    Distancia total: {dist} km")

camino2, dist2 = mapa.camino_mas_corto("Oaxaca", "Guadalajara")
print(f"\n  Camino mas corto Oaxaca -> Guadalajara:")
print(f"    Ruta: {' -> '.join(camino2)}")
print(f"    Distancia total: {dist2} km")

# Complejidad de operaciones
print("\n" + "=" * 60)
print("RESUMEN DE COMPLEJIDAD (V=vertices, E=aristas)")
print("=" * 60)
print("  Agregar vertice:  O(1)")
print("  Agregar arista:   O(1)")
print("  BFS:              O(V + E)")
print("  DFS:              O(V + E)")
print("  Dijkstra (heap):  O((V + E) log V)")
print("  Detectar ciclo:   O(V + E)")
print("  Espacio:          O(V + E)")
