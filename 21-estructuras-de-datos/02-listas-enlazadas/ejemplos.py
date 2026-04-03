"""
Listas Enlazadas en Python
===========================
Una lista enlazada es una estructura de datos lineal donde cada elemento
(nodo) contiene un valor y una referencia al siguiente nodo. A diferencia
de los arrays, los nodos no se almacenan en posiciones contiguas de memoria,
lo que permite inserciones y eliminaciones en O(1) si se tiene la referencia.
"""


# =============================================================================
# 1. Lista simplemente enlazada
# =============================================================================
class Nodo:
    """Nodo para lista simplemente enlazada."""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    """Lista simplemente enlazada con operaciones basicas."""
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, dato):
        """Agrega un nodo al final de la lista. O(n)"""
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def agregar_al_inicio(self, dato):
        """Agrega un nodo al inicio de la lista. O(1)"""
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def eliminar(self, dato):
        """Elimina la primera ocurrencia del dato. O(n)"""
        if not self.cabeza:
            return False
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return True
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                return True
            actual = actual.siguiente
        return False

    def buscar(self, dato):
        """Busca un dato y retorna su posicion (o -1). O(n)"""
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1

    def invertir(self):
        """Invierte la lista in-place. O(n)"""
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior

    def mostrar(self):
        """Retorna representacion visual de la lista."""
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(elementos) + " -> None"

    def __len__(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador


# Demostrar lista simplemente enlazada
print("=" * 60)
print("1. LISTA SIMPLEMENTE ENLAZADA")
print("=" * 60)

lista = ListaEnlazada()
for ciudad in ["CDMX", "Guadalajara", "Monterrey", "Puebla"]:
    lista.agregar_al_final(ciudad)
    print(f"  Agregar al final '{ciudad}': {lista.mostrar()}")

lista.agregar_al_inicio("Cancun")
print(f"  Agregar al inicio 'Cancun': {lista.mostrar()}")

print(f"  Longitud: {len(lista)}")

pos = lista.buscar("Monterrey")
print(f"  Buscar 'Monterrey': posicion {pos}")

lista.eliminar("Guadalajara")
print(f"  Eliminar 'Guadalajara': {lista.mostrar()}")

lista.invertir()
print(f"  Lista invertida: {lista.mostrar()}")


# =============================================================================
# 2. Lista doblemente enlazada (bonus)
# =============================================================================
class NodoDoble:
    """Nodo para lista doblemente enlazada."""
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None


class ListaDobleEnlazada:
    """Lista doblemente enlazada."""
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamano = 0

    def agregar_al_final(self, dato):
        """Agrega al final en O(1)."""
        nuevo = NodoDoble(dato)
        if not self.cola:
            self.cabeza = self.cola = nuevo
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.tamano += 1

    def agregar_al_inicio(self, dato):
        """Agrega al inicio en O(1)."""
        nuevo = NodoDoble(dato)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.tamano += 1

    def eliminar_del_final(self):
        """Elimina el ultimo nodo en O(1)."""
        if not self.cola:
            return None
        dato = self.cola.dato
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        self.tamano -= 1
        return dato

    def mostrar_adelante(self):
        """Recorre de cabeza a cola."""
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)

    def mostrar_reversa(self):
        """Recorre de cola a cabeza."""
        elementos = []
        actual = self.cola
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.anterior
        return " <-> ".join(elementos)


print("\n" + "=" * 60)
print("2. LISTA DOBLEMENTE ENLAZADA")
print("=" * 60)

doble = ListaDobleEnlazada()
for num in [10, 20, 30, 40, 50]:
    doble.agregar_al_final(num)

print(f"  Recorrido adelante: {doble.mostrar_adelante()}")
print(f"  Recorrido reversa:  {doble.mostrar_reversa()}")

doble.agregar_al_inicio(5)
print(f"  Agregar 5 al inicio: {doble.mostrar_adelante()}")

eliminado = doble.eliminar_del_final()
print(f"  Eliminar del final ({eliminado}): {doble.mostrar_adelante()}")
print(f"  Tamano: {doble.tamano}")

# Complejidad de operaciones
print("\n" + "=" * 60)
print("RESUMEN DE COMPLEJIDAD")
print("=" * 60)
print("  Lista Simple:")
print("    Insercion al inicio: O(1)")
print("    Insercion al final:  O(n)  [O(1) con referencia a cola]")
print("    Busqueda:            O(n)")
print("    Eliminacion:         O(n)")
print("  Lista Doble:")
print("    Insercion inicio/final: O(1)")
print("    Eliminacion inicio/final: O(1)")
print("    Busqueda: O(n)")
