# Grafos (Graphs)

## Que es

Un **grafo** es una estructura de datos que modela **relaciones entre objetos**. Consiste en un conjunto de **vertices** (nodos) conectados por **aristas** (edges). Los grafos son la estructura mas general y flexible: las listas, arboles y hasta las tablas hash pueden verse como casos especiales de grafos.

## Diagrama

### Grafo no dirigido

```
    [A]───────[B]
     |  \      |
     |    \    |
     |      \  |
    [D]───────[C]
     |
    [E]

Vertices: {A, B, C, D, E}
Aristas:  {(A,B), (A,C), (A,D), (B,C), (C,D), (D,E)}
```

### Grafo dirigido (digrafo)

```
    [A]──────►[B]
     │  \      │
     │    \    │
     ▼     ▼   ▼
    [D]◄──────[C]
     │
     ▼
    [E]

Las flechas indican la direccion permitida.
A→B existe, pero B→A no.
```

### Grafo ponderado (con pesos)

```
    [A]───5───[B]
     |  \      |
     2    3    7
     |      \  |
    [D]───1───[C]
     |
     4
     |
    [E]

Los numeros representan el costo/distancia de cada arista.
```

## Representaciones en memoria

### Matriz de adyacencia

```
      A  B  C  D  E
  A [ 0  1  1  1  0 ]
  B [ 1  0  1  0  0 ]
  C [ 1  1  0  1  0 ]
  D [ 1  0  1  0  1 ]
  E [ 0  0  0  1  0 ]

Espacio: O(V^2)
Verificar arista: O(1)
Buena para: grafos densos
```

### Lista de adyacencia

```
  A → [B, C, D]
  B → [A, C]
  C → [A, B, D]
  D → [A, C, E]
  E → [D]

Espacio: O(V + E)
Verificar arista: O(grado del vertice)
Buena para: grafos dispersos (la mayoria de casos reales)
```

### Comparacion

```
                    Matriz          Lista
Espacio             O(V^2)          O(V + E)
Verificar arista    O(1)            O(grado)
Obtener vecinos     O(V)            O(grado)
Agregar arista      O(1)            O(1)
Agregar vertice     O(V^2)*         O(1)
Mejor para          Grafos densos   Grafos dispersos
```
*Requiere redimensionar la matriz.

## Operaciones principales

| Operacion            | Complejidad        | Descripcion                         |
|----------------------|--------------------|-------------------------------------|
| BFS                  | O(V + E)           | Recorrido por amplitud              |
| DFS                  | O(V + E)           | Recorrido por profundidad           |
| Dijkstra             | O((V+E) log V)     | Camino mas corto (pesos positivos)  |
| Bellman-Ford         | O(V * E)           | Camino mas corto (pesos negativos)  |
| Componentes conexas  | O(V + E)           | Encontrar grupos conectados         |
| Deteccion de ciclos  | O(V + E)           | Verificar si existe un ciclo        |

## Como funciona

### BFS (Busqueda por Amplitud) - usa cola

```
Inicio: A

Nivel 0:  [A]
          / | \
Nivel 1: [B][C][D]         Cola: A → B,C,D → C,D → D → E
          |     |
Nivel 2: (ya visitados) [E]

Orden de visita: A, B, C, D, E
Encuentra el camino mas corto (en grafos sin peso).
```

```
BFS paso a paso:
  Cola: [A]          Visitados: {A}
  Saca A, agrega B,C,D
  Cola: [B, C, D]    Visitados: {A, B, C, D}
  Saca B, C ya visitado
  Cola: [C, D]       Visitados: {A, B, C, D}
  Saca C, vecinos ya visitados
  Cola: [D]          Visitados: {A, B, C, D}
  Saca D, agrega E
  Cola: [E]          Visitados: {A, B, C, D, E}
  Saca E, vecino D ya visitado
  Cola: []           Fin
```

### DFS (Busqueda por Profundidad) - usa pila/recursion

```
Inicio: A

   [A]
    ↓
   [B]
    ↓
   [C]
    ↓
   [D]
    ↓
   [E]

Orden de visita: A, B, C, D, E
Explora tan profundo como sea posible antes de retroceder.
Util para: deteccion de ciclos, ordenamiento topologico.
```

### Camino mas corto (Dijkstra)

```
Encontrar camino mas corto de A a E:

    [A]───5───[B]
     |  \      |
     2    3    7
     |      \  |
    [D]───1───[C]
     |
     4
     |
    [E]

Paso a paso:
  dist[A]=0, dist[otros]=infinito
  Visitar A: dist[D]=2, dist[C]=3, dist[B]=5
  Visitar D: dist[E]=2+4=6, dist[C]=min(3, 2+1)=3
  Visitar C: dist[B]=min(5, 3+7)=5
  Visitar B: (nada mejora)
  Visitar E: fin

Camino mas corto A→E: A → D → E, costo = 6
```

## Cuando usarla

**Usar grafos cuando:**
- Los datos tienen relaciones complejas (no solo jerarquicas)
- Necesitas modelar redes (sociales, de transporte, computadoras)
- El problema involucra caminos, conexiones o dependencias
- Necesitas detectar ciclos o componentes conectados

**Elegir la representacion:**
- **Matriz de adyacencia**: grafo denso, necesitas verificar aristas frecuentemente
- **Lista de adyacencia**: grafo disperso, necesitas recorrer vecinos frecuentemente

**BFS vs DFS:**
- **BFS**: camino mas corto (sin pesos), explorar por niveles
- **DFS**: deteccion de ciclos, ordenamiento topologico, laberintos

## Casos de uso en el mundo real

- **Redes sociales**: personas son vertices, amistades son aristas
- **GPS/Mapas**: intersecciones son vertices, calles son aristas con peso (distancia)
- **Internet**: routers y enlaces de red
- **Dependencias**: orden de compilacion, instalacion de paquetes (topological sort)
- **Recomendaciones**: "personas que tambien compraron..."
- **Deteccion de fraude**: patrones inusuales en grafos de transacciones

## Errores comunes

1. **No marcar nodos como visitados**: en BFS y DFS, olvidar marcar nodos visitados produce ciclos infinitos.
2. **Usar Dijkstra con pesos negativos**: Dijkstra no funciona con aristas de peso negativo. Usar Bellman-Ford.
3. **Confundir dirigido con no dirigido**: en un grafo dirigido, la arista A→B no implica B→A. Asegurate de agregar ambas si el grafo es no dirigido.
4. **Elegir la representacion incorrecta**: una matriz de adyacencia para un grafo disperso de 10,000 nodos desperdicia mucha memoria (100 millones de celdas).
5. **Asumir que el grafo es conexo**: en problemas reales, los grafos pueden tener multiples componentes desconectadas. Verificar antes de asumir que existe camino entre dos nodos.
