"""
Tablas Hash (Hash Tables) en Python
=====================================
Una tabla hash es una estructura que mapea claves a valores usando una
funcion hash. Permite busqueda, insercion y eliminacion en O(1) promedio.
Python implementa esto nativamente con el tipo 'dict'.
Aqui implementamos una desde cero para entender el funcionamiento interno.
"""


# =============================================================================
# 1. Implementacion de Tabla Hash con encadenamiento
# =============================================================================
class TablaHash:
    """
    Tabla hash con resolucion de colisiones por encadenamiento.
    Cada posicion del arreglo contiene una lista de pares (clave, valor).
    """
    def __init__(self, capacidad=8):
        self.capacidad = capacidad
        self.tamano = 0
        self.cubetas = [[] for _ in range(capacidad)]

    def _hash(self, clave):
        """Funcion hash: convierte la clave en un indice."""
        if isinstance(clave, str):
            # Hash simple para cadenas: suma de valores ASCII ponderada
            valor = sum(ord(c) * (i + 1) for i, c in enumerate(clave))
            return valor % self.capacidad
        return hash(clave) % self.capacidad

    def poner(self, clave, valor):
        """Inserta o actualiza un par clave-valor. O(1) promedio."""
        indice = self._hash(clave)
        cubeta = self.cubetas[indice]

        # Buscar si la clave ya existe
        for i, (c, v) in enumerate(cubeta):
            if c == clave:
                cubeta[i] = (clave, valor)  # Actualizar
                return

        cubeta.append((clave, valor))  # Insertar
        self.tamano += 1

        # Redimensionar si el factor de carga supera 0.75
        if self.tamano / self.capacidad > 0.75:
            self._redimensionar()

    def obtener(self, clave):
        """Obtiene el valor asociado a una clave. O(1) promedio."""
        indice = self._hash(clave)
        for c, v in self.cubetas[indice]:
            if c == clave:
                return v
        raise KeyError(f"Clave '{clave}' no encontrada")

    def eliminar(self, clave):
        """Elimina un par clave-valor. O(1) promedio."""
        indice = self._hash(clave)
        cubeta = self.cubetas[indice]
        for i, (c, v) in enumerate(cubeta):
            if c == clave:
                cubeta.pop(i)
                self.tamano -= 1
                return v
        raise KeyError(f"Clave '{clave}' no encontrada")

    def contiene(self, clave):
        """Verifica si una clave existe. O(1) promedio."""
        indice = self._hash(clave)
        return any(c == clave for c, v in self.cubetas[indice])

    def _redimensionar(self):
        """Duplica la capacidad y redistribuye todos los elementos."""
        capacidad_anterior = self.capacidad
        self.capacidad *= 2
        cubetas_antiguas = self.cubetas
        self.cubetas = [[] for _ in range(self.capacidad)]
        self.tamano = 0

        for cubeta in cubetas_antiguas:
            for clave, valor in cubeta:
                self.poner(clave, valor)

        print(f"    [Redimensionar: {capacidad_anterior} -> {self.capacidad}]")

    def mostrar(self):
        """Muestra el estado interno de la tabla."""
        for i, cubeta in enumerate(self.cubetas):
            if cubeta:
                elementos = ", ".join(f"{c}: {v}" for c, v in cubeta)
                print(f"    [{i}]: {elementos}")
            else:
                print(f"    [{i}]: vacia")


# =============================================================================
# Demostrar operaciones basicas
# =============================================================================
print("=" * 60)
print("1. OPERACIONES BASICAS DE TABLA HASH")
print("=" * 60)

tabla = TablaHash(capacidad=4)

datos = [("nombre", "Carlos"), ("edad", 28), ("ciudad", "CDMX"),
         ("carrera", "Computacion")]
for clave, valor in datos:
    tabla.poner(clave, valor)
    print(f"  Poner('{clave}', '{valor}') -> hash={tabla._hash(clave)}")

print(f"\n  Estado interno (capacidad={tabla.capacidad}):")
tabla.mostrar()

print(f"\n  obtener('nombre'): {tabla.obtener('nombre')}")
print(f"  contiene('edad'): {tabla.contiene('edad')}")
print(f"  contiene('telefono'): {tabla.contiene('telefono')}")

tabla.eliminar("ciudad")
print(f"  Despues de eliminar('ciudad'):")
tabla.mostrar()


# =============================================================================
# 2. Colisiones en accion
# =============================================================================
print("\n" + "=" * 60)
print("2. MANEJO DE COLISIONES")
print("=" * 60)

tabla_col = TablaHash(capacidad=4)
palabras = ["hola", "adios", "casa", "mesa", "silla", "perro", "gato", "sol"]

for p in palabras:
    indice = tabla_col._hash(p)
    tabla_col.poner(p, len(p))
    print(f"  '{p}' -> hash={indice}")

print(f"\n  Estado interno (pueden verse colisiones en misma cubeta):")
tabla_col.mostrar()


# =============================================================================
# 3. Comparacion con dict de Python
# =============================================================================
print("\n" + "=" * 60)
print("3. COMPARACION CON dict DE PYTHON")
print("=" * 60)

# El dict de Python es una tabla hash optimizada en C
directorio = {
    "Ana": "555-0001",
    "Beto": "555-0002",
    "Carlos": "555-0003",
}

directorio["Diana"] = "555-0004"  # Insertar
print(f"  Directorio: {directorio}")
print(f"  Buscar 'Carlos': {directorio['Carlos']}")
print(f"  'Beto' en directorio: {'Beto' in directorio}")

del directorio["Ana"]  # Eliminar
print(f"  Despues de eliminar 'Ana': {directorio}")

# Iterar
print("  Recorrer pares:")
for nombre, telefono in directorio.items():
    print(f"    {nombre}: {telefono}")


# =============================================================================
# 4. Ejemplo practico: Contar frecuencia de palabras
# =============================================================================
print("\n" + "=" * 60)
print("4. EJEMPLO: FRECUENCIA DE PALABRAS")
print("=" * 60)

texto = """
el gato negro y el perro blanco jugaban en el parque
el gato corria y el perro ladraba mientras el sol brillaba
"""


def contar_frecuencia(texto):
    """Cuenta la frecuencia de cada palabra usando nuestra tabla hash."""
    frecuencia = TablaHash(capacidad=16)
    palabras = texto.lower().split()

    for palabra in palabras:
        if frecuencia.contiene(palabra):
            frecuencia.poner(palabra, frecuencia.obtener(palabra) + 1)
        else:
            frecuencia.poner(palabra, 1)

    return frecuencia


freq = contar_frecuencia(texto)

# Mostrar resultados ordenados por frecuencia usando dict de Python
resultados = {}
for cubeta in freq.cubetas:
    for palabra, conteo in cubeta:
        resultados[palabra] = conteo

print("  Frecuencia de palabras (ordenada):")
for palabra, conteo in sorted(resultados.items(), key=lambda x: -x[1]):
    barra = "#" * conteo
    print(f"    {palabra:<12} {conteo:>2} {barra}")

# Complejidad de operaciones
print("\n" + "=" * 60)
print("RESUMEN DE COMPLEJIDAD")
print("=" * 60)
print("  Insercion:    O(1) promedio, O(n) peor caso")
print("  Busqueda:     O(1) promedio, O(n) peor caso")
print("  Eliminacion:  O(1) promedio, O(n) peor caso")
print("  Espacio:      O(n)")
print("  El peor caso ocurre cuando todas las claves colisionan")
