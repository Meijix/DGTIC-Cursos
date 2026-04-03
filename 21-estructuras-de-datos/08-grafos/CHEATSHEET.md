# Cheatsheet — Grafos

## Diagrama rapido

```
NO DIRIGIDO:           DIRIGIDO:              PONDERADO:
  A ─── B                A ──► B                A ──3── B
  |   / |                |   ╱ ↑                |      |
  |  /  |                ▼  ╱  |               1|     2|
  C ─── D                C ──► D                C ──4── D

Lista de adyacencia:              Matriz de adyacencia:
  {                                  A  B  C  D
    "A": ["B", "C"],             A [ 0  1  1  0 ]
    "B": ["A", "C", "D"],       B [ 1  0  1  1 ]
    "C": ["A", "B", "D"],       C [ 1  1  0  1 ]
    "D": ["B", "C"]             D [ 0  1  1  0 ]
  }

┌──────────────────┬────────────────┬──────────────┐
│ Criterio         │ Lista adj.     │ Matriz       │
├──────────────────┼────────────────┼──────────────┤
│ Espacio          │ O(V + E)       │ O(V^2)       │
│ Verificar arista │ O(grado)       │ O(1)         │
│ Listar vecinos   │ O(grado)       │ O(V)         │
│ Grafo disperso   │ Mejor opcion   │ Desperdicia  │
│ Grafo denso      │ Funciona       │ Mejor opcion │
└──────────────────┴────────────────┴──────────────┘
```

## Operaciones — O(?)

```
┌──────────────────────┬──────────────────┐
│ Operacion            │ Complejidad      │
├──────────────────────┼──────────────────┤
│ BFS / DFS            │   O(V + E)       │
│ Dijkstra (con heap)  │ O((V+E) log V)   │
│ Topological sort     │   O(V + E)       │
│ Agregar arista       │   O(1)           │
└──────────────────────┴──────────────────┘
```

## Python en 30 segundos

```python
from collections import deque

grafo = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C"]}

# BFS — Busqueda en anchura (camino mas corto sin pesos)
def bfs(grafo, inicio):
    visitados, cola = {inicio}, deque([inicio])
    while cola:
        nodo = cola.popleft()
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)

# DFS — Busqueda en profundidad (detectar ciclos, recorrer todo)
def dfs(grafo, nodo, visitados=None):
    if visitados is None: visitados = set()
    visitados.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)

# Dijkstra — camino mas corto con pesos positivos
import heapq
def dijkstra(grafo_p, inicio):
    dist = {v: float('inf') for v in grafo_p}
    dist[inicio] = 0
    heap = [(0, inicio)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for vecino, peso in grafo_p[u]:
            if d + peso < dist[vecino]:
                dist[vecino] = d + peso
                heapq.heappush(heap, (d + peso, vecino))
    return dist
```

## Problemas clasicos

- **Camino mas corto**: BFS (sin pesos), Dijkstra (pesos +), Bellman-Ford (pesos negativos).
- **Detectar ciclos**: DFS con estados (blanco/gris/negro) en dirigidos.
- **Componentes conexos**: DFS/BFS desde cada nodo no visitado.
- **Orden topologico**: solo en DAGs; DFS + pila o algoritmo de Kahn.

## Cuando usar / Cuando NO usar

- **Usar** para modelar redes (sociales, rutas, dependencias).
- **Usar lista adj.** para grafos dispersos (mayoria de casos reales).
- **Usar matriz** si el grafo es denso o necesitas verificar aristas en O(1).
- **NO usar** si la relacion es estrictamente jerarquica (usa arbol).
- **NO usar** matriz con millones de nodos y pocas aristas (memoria O(V^2)).

## Errores clasicos

- **Olvidar `visitados`**: BFS/DFS sin set de visitados entra en bucle infinito con ciclos.
- **Confundir dirigido con no dirigido**: en no dirigido agrega ambas aristas (A→B y B→A).
- **Usar Dijkstra con pesos negativos**: da resultados incorrectos. Usa Bellman-Ford.
- **Orden topologico en grafo con ciclos**: no existe. Verifica que sea DAG primero.
- **Olvidar nodos sin aristas**: incluyelos en el dict como `"E": []`.
