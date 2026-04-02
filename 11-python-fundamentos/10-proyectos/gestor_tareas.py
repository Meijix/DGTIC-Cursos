"""
Proyecto 1: Gestor de Tareas (TODO List)
==========================================
Aplicacion de linea de comandos para gestionar tareas pendientes.
Las tareas se guardan en un archivo JSON para persistencia.

Conceptos integrados:
  - Clases y POO (Tarea, GestorTareas)
  - Archivos y JSON (guardar/cargar)
  - Excepciones (manejo de errores)
  - Decoradores (logging)
  - Listas, diccionarios, f-strings

Ejecuta este archivo:
    python gestor_tareas.py
"""

import json
import os
import functools
from datetime import datetime

# ============================================================
# DECORADOR: Logging de operaciones
# ============================================================
# Integra seccion 07 (Decoradores). Cada operacion importante
# se registra automaticamente con este decorador.

def log_operacion(func):
    """Decorador que imprime un registro de cada operacion."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"  [LOG] {func.__name__} ejecutado correctamente")
        return resultado
    return wrapper


# ============================================================
# CLASE: Tarea
# ============================================================
# Integra seccion 04 (POO). Cada tarea es un objeto con atributos
# y metodos para convertirse a/desde diccionario (serializacion).

class Tarea:
    """Representa una tarea individual."""

    def __init__(self, titulo, descripcion="", completada=False, fecha=None):
        """
        Inicializa una tarea.

        Args:
            titulo: Nombre de la tarea (requerido).
            descripcion: Detalle opcional.
            completada: Estado de la tarea (por defecto False).
            fecha: Fecha de creacion (se genera automaticamente).
        """
        if not titulo or not titulo.strip():
            raise ValueError("El titulo de la tarea no puede estar vacio")

        self.titulo = titulo.strip()
        self.descripcion = descripcion.strip()
        self.completada = completada
        self.fecha = fecha or datetime.now().strftime("%Y-%m-%d %H:%M")

    def completar(self):
        """Marca la tarea como completada."""
        self.completada = True

    def a_diccionario(self):
        """
        Convierte la tarea a diccionario para poder guardarla en JSON.
        Integra seccion 02 (Diccionarios) y seccion 06 (JSON).
        """
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "completada": self.completada,
            "fecha": self.fecha,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """
        Crea una Tarea desde un diccionario (al cargar de JSON).
        Usa @classmethod como constructor alternativo (seccion 07).
        """
        return cls(
            titulo=datos["titulo"],
            descripcion=datos.get("descripcion", ""),
            completada=datos.get("completada", False),
            fecha=datos.get("fecha"),
        )

    def __str__(self):
        """Representacion legible de la tarea."""
        estado = "[x]" if self.completada else "[ ]"
        desc = f" — {self.descripcion}" if self.descripcion else ""
        return f"{estado} {self.titulo}{desc} ({self.fecha})"


# ============================================================
# CLASE: GestorTareas
# ============================================================
# Integra multiples secciones: POO, archivos, excepciones,
# listas, decoradores.

class GestorTareas:
    """Gestiona una coleccion de tareas con persistencia en JSON."""

    def __init__(self, ruta_archivo="tareas.json"):
        """
        Inicializa el gestor y carga tareas existentes.

        Args:
            ruta_archivo: Ruta al archivo JSON de persistencia.
        """
        self.ruta_archivo = ruta_archivo
        self.tareas = []
        self._cargar()

    def _cargar(self):
        """
        Carga tareas desde el archivo JSON.
        Integra seccion 06 (lectura de archivos) y seccion 08 (excepciones).
        """
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                self.tareas = [Tarea.desde_diccionario(d) for d in datos]
                print(f"  Cargadas {len(self.tareas)} tareas desde "
                      f"{self.ruta_archivo}")
        except FileNotFoundError:
            # Primera vez: el archivo no existe aun — es normal
            self.tareas = []
            print(f"  Archivo {self.ruta_archivo} no encontrado. "
                  f"Se creara al guardar.")
        except json.JSONDecodeError as e:
            # El archivo existe pero esta corrupto
            print(f"  Error al leer JSON: {e}. Iniciando con lista vacia.")
            self.tareas = []

    @log_operacion
    def guardar(self):
        """
        Guarda todas las tareas en el archivo JSON.
        Integra seccion 06 (escritura de archivos).
        """
        datos = [tarea.a_diccionario() for tarea in self.tareas]
        with open(self.ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)

    @log_operacion
    def agregar(self, titulo, descripcion=""):
        """Agrega una nueva tarea a la lista."""
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)
        self.guardar()
        return tarea

    @log_operacion
    def completar(self, indice):
        """
        Marca una tarea como completada por su indice.
        Integra seccion 08 (manejo de errores con indice invalido).
        """
        if not 0 <= indice < len(self.tareas):
            raise IndexError(
                f"Indice {indice} fuera de rango. "
                f"Hay {len(self.tareas)} tareas (0 a {len(self.tareas)-1})."
            )
        self.tareas[indice].completar()
        self.guardar()
        return self.tareas[indice]

    @log_operacion
    def eliminar(self, indice):
        """Elimina una tarea por su indice."""
        if not 0 <= indice < len(self.tareas):
            raise IndexError(f"Indice {indice} fuera de rango.")
        tarea = self.tareas.pop(indice)
        self.guardar()
        return tarea

    def listar(self, solo_pendientes=False):
        """
        Lista todas las tareas (o solo las pendientes).
        Integra seccion 02 (filtrado con comprehensions).
        """
        if solo_pendientes:
            filtradas = [t for t in self.tareas if not t.completada]
        else:
            filtradas = self.tareas

        if not filtradas:
            print("\n  No hay tareas.")
            return

        print(f"\n  {'TAREAS PENDIENTES' if solo_pendientes else 'TODAS LAS TAREAS'}")
        print("  " + "-" * 50)
        for i, tarea in enumerate(self.tareas):
            if solo_pendientes and tarea.completada:
                continue
            print(f"  {i}. {tarea}")

    def resumen(self):
        """
        Muestra un resumen del estado de las tareas.
        Integra seccion 03 (funciones como sum con generadores).
        """
        total = len(self.tareas)
        completadas = sum(1 for t in self.tareas if t.completada)
        pendientes = total - completadas

        print(f"\n  === RESUMEN ===")
        print(f"  Total: {total} | Completadas: {completadas} | "
              f"Pendientes: {pendientes}")
        if total > 0:
            porcentaje = (completadas / total) * 100
            barra = "#" * int(porcentaje // 5) + "-" * (20 - int(porcentaje // 5))
            print(f"  Progreso: [{barra}] {porcentaje:.0f}%")


# ============================================================
# INTERFAZ DE LINEA DE COMANDOS
# ============================================================

def mostrar_menu():
    """Muestra el menu de opciones."""
    print("""
  ╔════════════════════════════════════╗
  ║       GESTOR DE TAREAS            ║
  ╠════════════════════════════════════╣
  ║  1. Ver todas las tareas          ║
  ║  2. Ver tareas pendientes         ║
  ║  3. Agregar tarea                 ║
  ║  4. Completar tarea               ║
  ║  5. Eliminar tarea                ║
  ║  6. Ver resumen                   ║
  ║  0. Salir                         ║
  ╚════════════════════════════════════╝""")


def main():
    """
    Funcion principal que ejecuta el bucle interactivo.
    Integra seccion 08 (manejo de excepciones en input del usuario).
    """
    # Usamos un archivo temporal para la demo
    import tempfile
    ruta = os.path.join(tempfile.gettempdir(), "gestor_tareas_demo.json")
    gestor = GestorTareas(ruta)

    # Agregar tareas de ejemplo si esta vacio
    if not gestor.tareas:
        print("\n  Agregando tareas de ejemplo...")
        gestor.agregar("Estudiar Python", "Completar la seccion de testing")
        gestor.agregar("Hacer ejercicio", "Correr 30 minutos")
        gestor.agregar("Leer un libro", "Terminar el capitulo 5")
        gestor.agregar("Comprar viveres", "Frutas, verduras y pan")

    while True:
        mostrar_menu()
        try:
            opcion = input("\n  Elige una opcion: ").strip()
        except (EOFError, KeyboardInterrupt):
            # EOFError: cuando se ejecuta sin input interactivo
            # KeyboardInterrupt: cuando el usuario presiona Ctrl+C
            print("\n  Saliendo...")
            break

        if opcion == "1":
            gestor.listar()

        elif opcion == "2":
            gestor.listar(solo_pendientes=True)

        elif opcion == "3":
            try:
                titulo = input("  Titulo: ").strip()
                descripcion = input("  Descripcion (opcional): ").strip()
                tarea = gestor.agregar(titulo, descripcion)
                print(f"  Agregada: {tarea}")
            except ValueError as e:
                print(f"  Error: {e}")
            except EOFError:
                print("\n  Saliendo...")
                break

        elif opcion == "4":
            gestor.listar()
            try:
                idx = int(input("  Numero de tarea a completar: "))
                tarea = gestor.completar(idx)
                print(f"  Completada: {tarea}")
            except (ValueError, IndexError) as e:
                print(f"  Error: {e}")
            except EOFError:
                print("\n  Saliendo...")
                break

        elif opcion == "5":
            gestor.listar()
            try:
                idx = int(input("  Numero de tarea a eliminar: "))
                tarea = gestor.eliminar(idx)
                print(f"  Eliminada: {tarea}")
            except (ValueError, IndexError) as e:
                print(f"  Error: {e}")
            except EOFError:
                print("\n  Saliendo...")
                break

        elif opcion == "6":
            gestor.resumen()

        elif opcion == "0":
            print("  Hasta luego!")
            break

        else:
            print("  Opcion no valida. Intenta de nuevo.")

    # Limpiar archivo temporal de la demo
    if os.path.exists(ruta):
        os.remove(ruta)
        print(f"  Archivo temporal eliminado: {ruta}")


# ============================================================
# PUNTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
    main()
