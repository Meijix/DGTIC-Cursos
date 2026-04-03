"""
Colas (Queues) en Python
=========================
Una cola es una estructura de datos FIFO (First In, First Out): el primer
elemento en entrar es el primero en salir. Es como una fila en el banco:
el primero que llega es el primero en ser atendido.
Operaciones principales: enqueue (encolar), dequeue (desencolar), peek (frente).
"""

from collections import deque
from queue import PriorityQueue


# =============================================================================
# 1. Implementacion de Cola desde cero
# =============================================================================
class Cola:
    """Cola implementada con una lista (para fines educativos)."""
    def __init__(self):
        self._elementos = []

    def encolar(self, elemento):
        """Agrega un elemento al final. O(1) amortizado."""
        self._elementos.append(elemento)

    def desencolar(self):
        """Remueve y retorna el elemento del frente. O(n) con lista."""
        if self.esta_vacia():
            raise IndexError("La cola esta vacia")
        return self._elementos.pop(0)

    def frente(self):
        """Retorna el elemento del frente sin removerlo."""
        if self.esta_vacia():
            raise IndexError("La cola esta vacia")
        return self._elementos[0]

    def esta_vacia(self):
        return len(self._elementos) == 0

    def tamano(self):
        return len(self._elementos)

    def __repr__(self):
        return f"Cola({self._elementos})"


print("=" * 60)
print("1. OPERACIONES BASICAS DE COLA")
print("=" * 60)

cola = Cola()
for cliente in ["Ana", "Beto", "Carlos", "Diana"]:
    cola.encolar(cliente)
    print(f"  Encolar '{cliente}': {cola}")

print(f"  Frente: {cola.frente()}")
print(f"  Tamano: {cola.tamano()}")

while not cola.esta_vacia():
    atendido = cola.desencolar()
    print(f"  Atender '{atendido}': {cola}")


# =============================================================================
# 2. Cola eficiente con deque
# =============================================================================
print("\n" + "=" * 60)
print("2. COLA EFICIENTE CON collections.deque")
print("=" * 60)

cola_deque = deque()
for tarea in ["Imprimir reporte", "Enviar correo", "Backup BD", "Limpiar cache"]:
    cola_deque.append(tarea)
    print(f"  Encolar: '{tarea}'")

print(f"  Cola completa: {list(cola_deque)}")

while cola_deque:
    tarea = cola_deque.popleft()  # O(1), mucho mas eficiente que list.pop(0)
    print(f"  Procesando: '{tarea}' | Pendientes: {len(cola_deque)}")


# =============================================================================
# 3. Ejemplo practico: Simulacion de cola de impresion
# =============================================================================
print("\n" + "=" * 60)
print("3. SIMULACION: COLA DE IMPRESION")
print("=" * 60)

cola_impresion = deque()
documentos = [
    ("Tesis.pdf", 45),
    ("Reporte.docx", 12),
    ("Foto.jpg", 3),
    ("Presentacion.pptx", 28),
    ("Factura.pdf", 5),
]

# Encolar todos los documentos
for nombre, paginas in documentos:
    cola_impresion.append((nombre, paginas))
    print(f"  Agregado a cola: {nombre} ({paginas} paginas)")

print(f"\n  Procesando cola de impresion...")
tiempo_total = 0
while cola_impresion:
    nombre, paginas = cola_impresion.popleft()
    tiempo = paginas * 0.5  # 0.5 seg por pagina
    tiempo_total += tiempo
    print(f"  Imprimiendo '{nombre}' ({paginas} pags, {tiempo:.1f}s)"
          f" | Pendientes: {len(cola_impresion)}")

print(f"  Tiempo total estimado: {tiempo_total:.1f} segundos")


# =============================================================================
# 4. Cola de prioridad
# =============================================================================
print("\n" + "=" * 60)
print("4. COLA DE PRIORIDAD (PriorityQueue)")
print("=" * 60)

cola_urgencias = PriorityQueue()

# (prioridad, nombre, descripcion) - menor numero = mayor prioridad
pacientes = [
    (3, "Juan", "Dolor de cabeza"),
    (1, "Maria", "Fractura de brazo"),
    (2, "Pedro", "Fiebre alta"),
    (1, "Ana", "Dificultad respiratoria"),
    (4, "Luis", "Revision general"),
]

for prioridad, nombre, desc in pacientes:
    cola_urgencias.put((prioridad, nombre, desc))
    print(f"  Registrar: {nombre} - {desc} (prioridad {prioridad})")

print(f"\n  Atendiendo pacientes por prioridad:")
while not cola_urgencias.empty():
    prioridad, nombre, desc = cola_urgencias.get()
    print(f"  [Prioridad {prioridad}] Atender a {nombre}: {desc}")


# =============================================================================
# 5. Ejemplo practico: Planificador Round Robin
# =============================================================================
print("\n" + "=" * 60)
print("5. SIMULACION: PLANIFICADOR ROUND ROBIN")
print("=" * 60)


class Proceso:
    def __init__(self, nombre, tiempo_total):
        self.nombre = nombre
        self.tiempo_restante = tiempo_total
        self.tiempo_total = tiempo_total

    def __repr__(self):
        return f"{self.nombre}({self.tiempo_restante}ms)"


# Crear procesos con distintos tiempos de ejecucion
procesos = deque([
    Proceso("Firefox", 8),
    Proceso("VSCode", 5),
    Proceso("Spotify", 3),
    Proceso("Terminal", 6),
])

quantum = 3  # Tiempo maximo por turno (en milisegundos)
tiempo_actual = 0
print(f"  Quantum: {quantum}ms")
print(f"  Procesos: {list(procesos)}")
print()

while procesos:
    proceso = procesos.popleft()
    tiempo_ejecucion = min(quantum, proceso.tiempo_restante)
    proceso.tiempo_restante -= tiempo_ejecucion
    tiempo_actual += tiempo_ejecucion

    estado = "COMPLETADO" if proceso.tiempo_restante == 0 else "pausado"
    print(f"  t={tiempo_actual:>2}ms | Ejecutar {proceso.nombre}"
          f" por {tiempo_ejecucion}ms -> {estado}"
          f" (restante: {proceso.tiempo_restante}ms)")

    if proceso.tiempo_restante > 0:
        procesos.append(proceso)  # Regresar a la cola

print(f"\n  Todos los procesos completados en {tiempo_actual}ms")

# Complejidad de operaciones
print("\n" + "=" * 60)
print("RESUMEN DE COMPLEJIDAD")
print("=" * 60)
print("  Cola con lista:")
print("    Encolar (append):      O(1) amortizado")
print("    Desencolar (pop(0)):   O(n)")
print("  Cola con deque:")
print("    Encolar (append):      O(1)")
print("    Desencolar (popleft):  O(1)")
print("  Cola de prioridad:")
print("    Encolar:   O(log n)")
print("    Desencolar: O(log n)")
