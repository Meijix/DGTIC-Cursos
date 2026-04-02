"""
pathlib — Rutas Modernas en Python
=====================================
pathlib (Python 3.4+) proporciona una API orientada a objetos
para manejar rutas de archivos. Es el reemplazo moderno de os.path.

Ejecuta este archivo:
    python pathlib_ejemplo.py
"""

from pathlib import Path
import tempfile

# ============================================================
# 1. CREAR RUTAS
# ============================================================

print("=== CREAR RUTAS ===\n")

# Ruta relativa
ruta = Path("carpeta") / "subcarpeta" / "archivo.txt"
print(f"Ruta construida: {ruta}")

# Ruta absoluta del directorio actual
actual = Path.cwd()
print(f"Directorio actual: {actual}")

# Ruta home del usuario
home = Path.home()
print(f"Home: {home}")

# Desde string
ruta_str = Path("/usr/local/bin/python3")
print(f"Desde string: {ruta_str}")

# ============================================================
# 2. COMPONENTES DE UNA RUTA
# ============================================================

print("\n=== COMPONENTES ===\n")

archivo = Path("/home/usuario/documentos/informe_final.pdf")

print(f"Ruta completa:  {archivo}")
print(f".name:          {archivo.name}")          # informe_final.pdf
print(f".stem:          {archivo.stem}")          # informe_final
print(f".suffix:        {archivo.suffix}")        # .pdf
print(f".suffixes:      {archivo.suffixes}")      # ['.pdf']
print(f".parent:        {archivo.parent}")        # /home/usuario/documentos
print(f".parents[1]:    {archivo.parents[1]}")    # /home/usuario
print(f".parts:         {archivo.parts}")         # ('/', 'home', 'usuario', ...)
print(f".anchor:        {archivo.anchor}")        # /
print(f".is_absolute(): {archivo.is_absolute()}")  # True

# Múltiples extensiones
archivo_tar = Path("datos.tar.gz")
print(f"\n{archivo_tar}.suffixes: {archivo_tar.suffixes}")  # ['.tar', '.gz']

# Cambiar extensión
nueva = archivo.with_suffix(".docx")
print(f"Cambiar ext: {nueva}")

# Cambiar nombre
renombrada = archivo.with_name("borrador.pdf")
print(f"Cambiar nombre: {renombrada}")

# ============================================================
# 3. OPERACIONES CON EL SISTEMA DE ARCHIVOS
# ============================================================

print("\n=== OPERACIONES ===\n")

temp_dir = Path(tempfile.mkdtemp(prefix="python_pathlib_"))

# Crear directorios
(temp_dir / "proyecto" / "src" / "utils").mkdir(parents=True, exist_ok=True)
print(f"Directorios creados: {temp_dir / 'proyecto' / 'src' / 'utils'}")

# Crear y escribir archivos
readme = temp_dir / "proyecto" / "README.md"
readme.write_text("# Mi Proyecto\nDescripción aquí.", encoding="utf-8")
print(f"Archivo escrito: {readme}")

# Crear varios archivos de ejemplo
for nombre in ["main.py", "utils.py", "config.py"]:
    archivo = temp_dir / "proyecto" / "src" / nombre
    archivo.write_text(f"# {nombre}\nprint('Hola desde {nombre}')\n", encoding="utf-8")

# Leer archivo
contenido = readme.read_text(encoding="utf-8")
print(f"Contenido: {contenido[:30]}...")

# Verificar existencia
print(f"\n¿README existe? {readme.exists()}")
print(f"¿Es archivo? {readme.is_file()}")
print(f"¿Es directorio? {(temp_dir / 'proyecto').is_dir()}")

# Tamaño
print(f"Tamaño: {readme.stat().st_size} bytes")

# ============================================================
# 4. LISTAR ARCHIVOS
# ============================================================

print("\n=== LISTAR ARCHIVOS ===\n")

proyecto = temp_dir / "proyecto"

# iterdir() — contenido directo (no recursivo)
print("Contenido del directorio proyecto/:")
for item in sorted(proyecto.iterdir()):
    tipo = "DIR " if item.is_dir() else "FILE"
    print(f"  [{tipo}] {item.name}")

# glob() — buscar con patrón
print("\nArchivos .py en src/:")
for py_file in sorted((proyecto / "src").glob("*.py")):
    print(f"  {py_file.name}")

# rglob() — glob recursivo (busca en subdirectorios)
print("\nTodos los archivos (recursivo):")
for item in sorted(proyecto.rglob("*")):
    if item.is_file():
        relativa = item.relative_to(proyecto)
        print(f"  {relativa}")

# Buscar patrones específicos
print("\nArchivos .py y .md recursivos:")
for patron in ["**/*.py", "**/*.md"]:
    for item in sorted(proyecto.glob(patron)):
        print(f"  {item.relative_to(proyecto)}")

# ============================================================
# 5. COMPARACIÓN: os.path vs pathlib
# ============================================================

print("\n=== os.path vs pathlib ===\n")

import os

ruta = "/home/usuario/docs/archivo.txt"

# os.path (antiguo)
print("os.path:")
print(f"  basename:  {os.path.basename(ruta)}")
print(f"  dirname:   {os.path.dirname(ruta)}")
print(f"  splitext:  {os.path.splitext(ruta)}")
print(f"  join:      {os.path.join('/home', 'user', 'file.txt')}")

# pathlib (moderno)
p = Path(ruta)
print(f"\npathlib:")
print(f"  .name:     {p.name}")
print(f"  .parent:   {p.parent}")
print(f"  .suffix:   {p.suffix}")
print(f"  / :        {Path('/home') / 'user' / 'file.txt'}")

# ============================================================
# 6. EJEMPLO INTEGRADOR: ORGANIZADOR DE ARCHIVOS
# ============================================================

print("\n=== EJEMPLO: ORGANIZADOR DE ARCHIVOS ===\n")

# Crear archivos de prueba
desorden = temp_dir / "desorden"
desorden.mkdir(exist_ok=True)

archivos_test = [
    "foto1.jpg", "foto2.png", "documento.pdf", "notas.txt",
    "reporte.pdf", "vacaciones.jpg", "script.py", "datos.csv",
    "imagen.png", "resumen.txt", "app.py", "backup.csv",
]

for nombre in archivos_test:
    (desorden / nombre).write_text(f"Contenido de {nombre}", encoding="utf-8")


def organizar_por_extension(directorio):
    """Organiza archivos por extensión en subcarpetas."""
    directorio = Path(directorio)

    # Mapeo de extensiones a categorías
    categorias = {
        ".jpg": "imagenes", ".png": "imagenes", ".gif": "imagenes",
        ".pdf": "documentos", ".txt": "documentos", ".doc": "documentos",
        ".py": "codigo", ".js": "codigo", ".html": "codigo",
        ".csv": "datos", ".json": "datos", ".xml": "datos",
    }

    movidos = 0
    for archivo in directorio.iterdir():
        if archivo.is_file():
            categoria = categorias.get(archivo.suffix.lower(), "otros")
            destino_dir = directorio / categoria
            destino_dir.mkdir(exist_ok=True)

            destino = destino_dir / archivo.name
            archivo.rename(destino)
            movidos += 1
            print(f"  {archivo.name} → {categoria}/")

    return movidos


print(f"Organizando {desorden}:")
total = organizar_por_extension(desorden)
print(f"\n{total} archivos organizados.")

# Mostrar resultado
print("\nEstructura resultante:")
for item in sorted(desorden.rglob("*")):
    if item.is_file():
        print(f"  {item.relative_to(desorden)}")

print(f"\nArchivos creados en: {temp_dir}")
