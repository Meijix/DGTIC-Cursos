"""
Fixtures en pytest — Preparar Datos para Tests
=================================================
Las fixtures son funciones que proveen datos, objetos o recursos
a los tests. Son la forma de pytest de hacer setup/teardown
de manera flexible y reutilizable.

Instalar pytest:
    pip install pytest

Ejecutar estos tests:
    pytest test_fixtures.py -v
    pytest test_fixtures.py -v -s   (para ver los prints del ciclo de vida)
"""

import pytest
import os
import tempfile

from calculadora import Calculadora


# ============================================================
# 1. FIXTURE BASICA — Retorna un objeto
# ============================================================

@pytest.fixture
def calc():
    """
    Fixture que provee una Calculadora limpia.
    Por defecto, scope='function': se ejecuta para CADA test.
    """
    return Calculadora()

def test_suma_con_fixture(calc):
    """pytest inyecta 'calc' automaticamente al ver el parametro."""
    assert calc.sumar(2, 3) == 5

def test_historial_independiente(calc):
    """Cada test recibe una calculadora NUEVA (limpia)."""
    # Este historial esta vacio aunque el test anterior hizo una suma
    assert len(calc.historial) == 0
    calc.sumar(1, 1)
    assert len(calc.historial) == 1


# ============================================================
# 2. FIXTURE CON SETUP Y TEARDOWN (yield)
# ============================================================

@pytest.fixture
def archivo_temporal():
    """
    Fixture que crea un archivo temporal y lo elimina al final.
    - Todo ANTES de yield es SETUP.
    - Lo que se hace yield es lo que recibe el test.
    - Todo DESPUES de yield es TEARDOWN (siempre se ejecuta).
    """
    # SETUP: crear archivo temporal
    ruta = os.path.join(tempfile.gettempdir(), "test_fixture.txt")
    with open(ruta, "w") as f:
        f.write("datos de prueba\n")
        f.write("segunda linea\n")
    print(f"\n  [SETUP] Archivo creado: {ruta}")

    yield ruta    # <-- El test se ejecuta aqui, recibe la ruta

    # TEARDOWN: limpiar (se ejecuta SIEMPRE, incluso si el test falla)
    if os.path.exists(ruta):
        os.remove(ruta)
        print(f"  [TEARDOWN] Archivo eliminado: {ruta}")

def test_leer_archivo_temporal(archivo_temporal):
    """Usa la fixture que crea/elimina el archivo."""
    assert os.path.exists(archivo_temporal)
    with open(archivo_temporal) as f:
        contenido = f.read()
    assert "datos de prueba" in contenido

def test_contar_lineas(archivo_temporal):
    """Otro test que usa el mismo archivo temporal."""
    with open(archivo_temporal) as f:
        lineas = f.readlines()
    assert len(lineas) == 2


# ============================================================
# 3. FIXTURE QUE USA OTRA FIXTURE
# ============================================================

@pytest.fixture
def calc_con_historial(calc):
    """
    Las fixtures pueden usar otras fixtures como dependencias.
    Esta fixture recibe 'calc' y le agrega operaciones previas.
    """
    calc.sumar(10, 20)
    calc.restar(50, 30)
    calc.multiplicar(3, 4)
    return calc

def test_historial_tiene_tres_operaciones(calc_con_historial):
    """Verifica que la fixture preparo el historial."""
    assert len(calc_con_historial.historial) == 3

def test_ultimo_resultado_es_multiplicacion(calc_con_historial):
    """El ultimo resultado deberia ser 3 * 4 = 12."""
    assert calc_con_historial.ultimo_resultado() == 12


# ============================================================
# 4. SCOPE — Controlar el ciclo de vida
# ============================================================

# scope="function" (default): nueva instancia para cada test
# scope="class":   una instancia por clase de tests
# scope="module":  una instancia por archivo .py
# scope="session": una instancia para TODA la sesion de pytest

@pytest.fixture(scope="module")
def recurso_costoso():
    """
    Fixture con scope='module': se crea UNA vez para todo el archivo.
    Ideal para recursos costosos (conexiones BD, cargar datasets).
    """
    print("\n  [SETUP MODULE] Creando recurso costoso...")
    datos = list(range(100_000))  # Simula algo costoso
    yield datos
    print("\n  [TEARDOWN MODULE] Liberando recurso costoso...")

def test_recurso_tiene_datos(recurso_costoso):
    """Primer test que usa el recurso (se crea aqui)."""
    assert len(recurso_costoso) == 100_000

def test_recurso_empieza_en_cero(recurso_costoso):
    """Segundo test que usa el MISMO recurso (no se vuelve a crear)."""
    assert recurso_costoso[0] == 0


# ============================================================
# 5. FIXTURE CON DATOS COMPLEJOS
# ============================================================

@pytest.fixture
def usuario_ejemplo():
    """Provee un diccionario de usuario para tests."""
    return {
        "nombre": "Ana Garcia",
        "email": "ana@ejemplo.com",
        "edad": 28,
        "activo": True,
        "roles": ["usuario", "editor"],
    }

@pytest.fixture
def lista_productos():
    """Provee una lista de productos para tests."""
    return [
        {"id": 1, "nombre": "Laptop", "precio": 15999.00, "stock": 10},
        {"id": 2, "nombre": "Mouse", "precio": 299.00, "stock": 50},
        {"id": 3, "nombre": "Teclado", "precio": 599.00, "stock": 0},
    ]

def test_usuario_tiene_campos_requeridos(usuario_ejemplo):
    """Verifica la estructura del usuario."""
    campos = ["nombre", "email", "edad", "activo"]
    for campo in campos:
        assert campo in usuario_ejemplo

def test_usuario_tiene_roles(usuario_ejemplo):
    """Verifica que el usuario tiene al menos un rol."""
    assert len(usuario_ejemplo["roles"]) > 0

def test_productos_con_stock(lista_productos):
    """Filtra productos con stock disponible."""
    con_stock = [p for p in lista_productos if p["stock"] > 0]
    assert len(con_stock) == 2

def test_producto_mas_caro(lista_productos):
    """Encuentra el producto con mayor precio."""
    mas_caro = max(lista_productos, key=lambda p: p["precio"])
    assert mas_caro["nombre"] == "Laptop"


# ============================================================
# 6. conftest.py — FIXTURES COMPARTIDAS
# ============================================================

# En un proyecto real, las fixtures compartidas van en conftest.py:
#
# tests/
# ├── conftest.py          ← fixtures disponibles para TODOS los tests
# │   @pytest.fixture
# │   def db():
# │       return conectar_bd()
# │
# ├── test_usuarios.py     ← puede usar db() sin importar nada
# ├── test_productos.py    ← tambien puede usar db()
# └── sub_modulo/
#     ├── conftest.py      ← fixtures ADICIONALES solo para este dir
#     └── test_pedidos.py  ← tiene acceso a ambos conftest.py
#
# pytest descubre conftest.py automaticamente. No necesitas importarlo.


# ============================================================
# 7. FIXTURE CON tmp_path (built-in de pytest)
# ============================================================

def test_escribir_archivo(tmp_path):
    """
    tmp_path es una fixture BUILT-IN de pytest que provee un
    directorio temporal unico para cada test. Se limpia automaticamente.
    """
    # tmp_path es un objeto pathlib.Path
    archivo = tmp_path / "datos.txt"
    archivo.write_text("contenido de prueba", encoding="utf-8")

    assert archivo.exists()
    assert archivo.read_text(encoding="utf-8") == "contenido de prueba"

def test_multiples_archivos(tmp_path):
    """Crear varios archivos en el directorio temporal."""
    for i in range(3):
        archivo = tmp_path / f"archivo_{i}.txt"
        archivo.write_text(f"contenido {i}")

    archivos = list(tmp_path.iterdir())
    assert len(archivos) == 3
