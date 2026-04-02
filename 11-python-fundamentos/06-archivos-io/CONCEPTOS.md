# 06 — Archivos e I/O

## Índice

1. [Abrir y Cerrar Archivos](#abrir-y-cerrar-archivos)
2. [Modos de Apertura](#modos-de-apertura)
3. [Lectura de Archivos](#lectura-de-archivos)
4. [Escritura de Archivos](#escritura-de-archivos)
5. [Context Managers (with)](#context-managers-with)
6. [Archivos CSV](#archivos-csv)
7. [Archivos JSON](#archivos-json)
8. [pathlib — Rutas Modernas](#pathlib)
9. [Codificación (Encoding)](#codificación-encoding)
10. [Errores Comunes](#errores-comunes)
11. [Ejercicios](#ejercicios)

---

## Abrir y Cerrar Archivos

```python
# Forma básica (NO recomendada — hay que cerrar manualmente)
f = open("archivo.txt", "r")
contenido = f.read()
f.close()

# Forma RECOMENDADA — context manager
with open("archivo.txt", "r") as f:
    contenido = f.read()
# El archivo se cierra automáticamente al salir del bloque
```

---

## Modos de Apertura

| Modo | Descripción | Si no existe | Si existe |
|------|-------------|-------------|-----------|
| `"r"` | Lectura (default) | Error | Lee |
| `"w"` | Escritura | Crea | **Sobrescribe** |
| `"a"` | Append (agregar) | Crea | Agrega al final |
| `"x"` | Creación exclusiva | Crea | Error |
| `"r+"` | Lectura y escritura | Error | Lee/escribe |
| `"w+"` | Escritura y lectura | Crea | Sobrescribe |
| `"b"` | Modo binario | — | — |
| `"t"` | Modo texto (default) | — | — |

Combinaciones comunes: `"rb"` (leer binario), `"wb"` (escribir binario).

---

## Lectura de Archivos

```python
with open("archivo.txt", "r", encoding="utf-8") as f:
    # Leer TODO el contenido como string
    todo = f.read()

    # Leer UNA línea
    linea = f.readline()

    # Leer TODAS las líneas como lista
    lineas = f.readlines()

    # Iterar línea por línea (más eficiente en memoria)
    for linea in f:
        print(linea.strip())
```

---

## Escritura de Archivos

```python
with open("salida.txt", "w", encoding="utf-8") as f:
    f.write("Primera línea\n")
    f.write("Segunda línea\n")

    # Escribir múltiples líneas
    lineas = ["Línea 3\n", "Línea 4\n"]
    f.writelines(lineas)

    # print también puede escribir a archivos
    print("Línea 5", file=f)
```

---

## Context Managers (with)

```
  with open("archivo.txt") as f:
       │                        │
       ▼                        ▼
  f.__enter__()            f.__exit__()
  (abre el archivo)        (cierra el archivo)
       │                        ▲
       │    ┌──────────────┐    │
       └──▶ │ Tu código    │────┘
            │ f.read()     │
            └──────────────┘
```

Ventajas:
- El archivo se cierra **siempre**, incluso si hay una excepción
- Código más limpio y seguro
- Funciona con cualquier objeto que implemente `__enter__` y `__exit__`

---

## Archivos CSV

```python
import csv

# Leer
with open("datos.csv", newline="", encoding="utf-8") as f:
    lector = csv.reader(f)
    for fila in lector:
        print(fila)  # Lista de strings

# Leer como diccionarios
with open("datos.csv", newline="", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        print(fila["nombre"], fila["edad"])

# Escribir
with open("salida.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nombre", "edad"])
    escritor.writerow(["Ana", 25])
```

---

## Archivos JSON

```python
import json

# Leer JSON desde archivo
with open("datos.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

# Escribir JSON a archivo
with open("salida.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)

# Convertir entre string JSON y objetos Python
json_str = json.dumps({"nombre": "Ana"}, ensure_ascii=False)
obj = json.loads(json_str)
```

---

## pathlib

Módulo moderno (Python 3.4+) para manejar rutas de archivos.
Es orientado a objetos y **multiplataforma**.

```python
from pathlib import Path

# Crear rutas
ruta = Path("carpeta") / "subcarpeta" / "archivo.txt"

# Información
ruta.name        # "archivo.txt"
ruta.stem        # "archivo"
ruta.suffix      # ".txt"
ruta.parent      # Path("carpeta/subcarpeta")
ruta.exists()    # bool
ruta.is_file()   # bool
ruta.is_dir()    # bool

# Leer y escribir directamente
contenido = ruta.read_text(encoding="utf-8")
ruta.write_text("contenido", encoding="utf-8")

# Listar archivos
for archivo in Path(".").glob("*.py"):
    print(archivo)
```

### pathlib vs os.path

| os.path (antiguo) | pathlib (moderno) |
|--------------------|-------------------|
| `os.path.join("a", "b")` | `Path("a") / "b"` |
| `os.path.exists(ruta)` | `ruta.exists()` |
| `os.path.basename(ruta)` | `ruta.name` |
| `os.path.splitext(ruta)` | `ruta.suffix` |
| `os.listdir(ruta)` | `ruta.iterdir()` |

---

## Codificación (Encoding)

**Siempre especifica `encoding="utf-8"`** al abrir archivos de texto.

```python
# BIEN
with open("archivo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()

# MAL (depende del sistema operativo)
with open("archivo.txt", "r") as f:
    contenido = f.read()
```

| Encoding | Descripción |
|----------|-------------|
| `utf-8` | El estándar para todo texto moderno |
| `ascii` | Solo caracteres ingleses (0-127) |
| `latin-1` | Europa occidental (256 caracteres) |
| `utf-16` | Usado por Windows internamente |

---

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `FileNotFoundError` | El archivo no existe | Verificar ruta, usar `Path.exists()` |
| `UnicodeDecodeError` | Encoding incorrecto | Especificar `encoding="utf-8"` |
| Archivo no se cierra | No usar `with` | Siempre usar context manager |
| Datos perdidos con `"w"` | `"w"` sobrescribe | Usar `"a"` para agregar |
| `newline=""` en CSV | Doble salto de línea | Siempre poner en Windows |
| Ruta con backslash | `\n` se interpreta como escape | Usar raw string `r"C:\..."` |

---

## Ejercicios

### Nivel 1
1. Lee un archivo de texto y cuenta las líneas, palabras y caracteres.
2. Escribe un programa que copie el contenido de un archivo a otro.
3. Lee un archivo línea por línea y numera cada línea.

### Nivel 2
4. Lee un archivo CSV de estudiantes y calcula promedios.
5. Convierte un archivo CSV a JSON y viceversa.
6. Implementa un sistema de log que agregue entradas a un archivo.

### Nivel 3
7. Usa `pathlib` para listar recursivamente todos los archivos `.py` de un directorio.
8. Crea un programa que monitoree un archivo y muestre nuevas líneas (como `tail -f`).
9. Implementa un sistema de caché que guarde datos en JSON.
