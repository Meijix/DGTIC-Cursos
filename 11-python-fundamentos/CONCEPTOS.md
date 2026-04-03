# 11 — Python Fundamentos: Vision General del Modulo

## Objetivo

Este modulo cubre los fundamentos de Python desde cero hasta la construccion
de proyectos completos. Esta organizado en 10 secciones progresivas que
llevan al estudiante desde variables y tipos basicos hasta testing y
proyectos integradores.

---

## Mapa de Progresion

```
  01 Basicos               Variables, operadores, strings, condicionales, ciclos
       │
       ▼
  02 Estructuras de Datos  Listas, tuplas, diccionarios, sets, comprehensions
       │
       ▼
  03 Funciones Avanzadas   Closures, lambdas, *args/**kwargs, type hints
       │
       ▼
  04 POO                   Clases, herencia, polimorfismo, magic methods, dataclasses
       │
       ▼
  05 Modulos y Paquetes    Imports, paquetes, entornos virtuales, pip
       │
       ▼
  06 Archivos e I/O        Lectura/escritura, CSV, JSON, pathlib
       │
       ▼
  07 Decoradores y         Decoradores con argumentos, generadores, yield,
     Generadores           itertools, lazy evaluation
       │
       ▼
  08 Manejo de Errores     try/except, EAFP vs LBYL, excepciones propias, logging
       │
       ▼
  09 Testing               unittest, pytest, fixtures, mocking, TDD, coverage
       │
       ▼
  10 Proyectos             Gestor de tareas, analizador de datos, API CLI
     Integradores          (combinan todas las secciones anteriores)
```

---

## Filosofia de Python: El Zen

Python tiene una filosofia de diseno clara, accesible con `import this`.
Los principios mas relevantes para este modulo:

| Principio | Seccion donde se aplica |
|-----------|------------------------|
| Lo simple es mejor que lo complejo | 01 Basicos |
| Legibilidad cuenta | Todas (f-strings, nombres descriptivos) |
| Deberia haber una manera obvia de hacerlo | 02 Comprehensions vs loops |
| Los errores nunca deben pasar en silencio | 08 Manejo de errores |
| Si la implementacion es facil de explicar, es buena idea | 03 Funciones |
| Los espacios de nombres son una gran idea | 05 Modulos y paquetes |
| Explicito es mejor que implicito | 04 POO (self explicito) |
| Practicidad le gana a la pureza | 07 Decoradores, duck typing |

---

## Tabla Comparativa de Conceptos Clave

### Estructuras de datos (seccion 02)

| Estructura | Ordenada | Mutable | Duplicados | Acceso | Uso tipico |
|------------|----------|---------|------------|--------|------------|
| `list` | Si | Si | Si | Indice | Coleccion general |
| `tuple` | Si | No | Si | Indice | Datos fijos, retornos multiples |
| `dict` | Si* | Si | Claves no | Clave | Mapeo clave-valor |
| `set` | No | Si | No | N/A | Unicidad, operaciones de conjuntos |
| `frozenset` | No | No | No | N/A | Sets como claves de dict |
| `str` | Si | No | Si | Indice | Texto |

*Los diccionarios mantienen orden de insercion desde Python 3.7+.

### Paradigmas de funciones (secciones 03 y 07)

| Concepto | Que es | Cuando usarlo |
|----------|--------|---------------|
| Funcion regular | Bloque reutilizable con `def` | Logica general |
| Lambda | Funcion anonima de una linea | Callbacks cortos, `sorted(key=...)` |
| Closure | Funcion que captura variables de su entorno | Fabricas de funciones, estado encapsulado |
| Decorador | Funcion que envuelve otra funcion | Logging, cache, validacion, permisos |
| Generador | Funcion con `yield` (lazy) | Secuencias grandes, pipelines de datos |

### Manejo de errores vs validacion (seccion 08)

| Estilo | Nombre | Filosofia | Ejemplo |
|--------|--------|-----------|---------|
| EAFP | Es mas facil pedir perdon que permiso | Intenta y captura la excepcion | `try: x[0]` / `except IndexError` |
| LBYL | Mira antes de saltar | Verifica antes de actuar | `if len(x) > 0: x[0]` |

Python favorece EAFP. Usa `try/except` en vez de verificar todo con `if`.

### Testing (seccion 09)

| Framework | Estilo | Ventaja principal | Desventaja |
|-----------|--------|-------------------|------------|
| `unittest` | Clases (xUnit) | Incluido en Python, sin instalar nada | Verbose, requiere herencia |
| `pytest` | Funciones simples | Menos codigo, mejor output, plugins | Dependencia externa |

---

## Cuando Usar Cada Caracteristica

### Para almacenar datos

```
  ¿Necesitas modificar los datos?
       │
  Si ──┤── ¿Necesitas clave-valor?
       │        │
       │   Si ──┘──▶ dict
       │   No ──┘──▶ ¿Necesitas unicidad?
       │                  │
       │             Si ──┘──▶ set
       │             No ──┘──▶ list
       │
  No ──┘── ¿Es un registro con campos fijos?
              │
         Si ──┘──▶ namedtuple o dataclass(frozen=True)
         No ──┘──▶ tuple
```

### Para organizar logica

```
  ¿La logica necesita estado propio?
       │
  Si ──┘──▶ Clase (POO, seccion 04)
       │
  No ──┘── ¿Es una transformacion pura?
              │
         Si ──┘──▶ Funcion pura (seccion 03)
         No ──┘──▶ ¿Necesitas modificar comportamiento de otra funcion?
                       │
                  Si ──┘──▶ Decorador (seccion 07)
                  No ──┘──▶ Funcion regular
```

### Para procesar datos grandes

```
  ¿Los datos caben en memoria?
       │
  Si ──┘──▶ List comprehension (seccion 02)
  No ──┘──▶ Generador + itertools (seccion 07)
```

---

## Resumen por Seccion

### 01 — Basicos
Fundamento de todo: variables con tipado dinamico, operadores, strings
(inmutables, slicing, f-strings), condicionales (`if/elif/else`,
`match-case`), ciclos (`for`, `while`, `enumerate`, `zip`).

### 02 — Estructuras de Datos
Las cuatro estructuras fundamentales: listas, tuplas, diccionarios y sets.
Comprehensions como forma pytonica de transformar datos. Mutabilidad
como concepto central para evitar bugs.

### 03 — Funciones Avanzadas
Funciones como objetos de primera clase. Closures y lambdas. Funciones
de orden superior (`map`, `filter`, `sorted`). `*args` y `**kwargs`
para flexibilidad. Type hints para documentar tipos.

### 04 — Programacion Orientada a Objetos
Clases, herencia (simple y multiple con MRO), polimorfismo y duck typing.
Encapsulamiento por convencion (`_protegido`, `__privado`). Magic methods
para integrar clases con la sintaxis de Python. `@dataclass` para reducir
boilerplate.

### 05 — Modulos y Paquetes
Organizacion del codigo en modulos (.py) y paquetes (directorios con
`__init__.py`). Sistema de imports. Entornos virtuales (`venv`) para
aislar dependencias. `pip` para instalar paquetes de PyPI.

### 06 — Archivos e I/O
Lectura y escritura de archivos de texto y binarios. Context managers
(`with`) para manejo seguro de recursos. Formatos CSV y JSON.
`pathlib` como alternativa moderna a `os.path`.

### 07 — Decoradores y Generadores
Decoradores: envolver funciones para agregar comportamiento (logging,
cache, timing). Generadores: producir valores bajo demanda con `yield`
para procesar datos sin cargar todo en memoria. `itertools` para
operaciones avanzadas sobre iterables.

### 08 — Manejo de Errores
Jerarquia de excepciones de Python. Estructura `try/except/else/finally`.
Filosofia EAFP. Excepciones personalizadas para dominios especificos.
Modulo `logging` para registro profesional. Context managers propios.

### 09 — Testing
Piramide de testing (unitarios, integracion, E2E). Patron AAA
(Arrange-Act-Assert). `unittest` (built-in) y `pytest` (estandar de
la industria). Fixtures, parametrize y mocking. Cobertura de codigo.
Metodologia TDD (Red-Green-Refactor).

### 10 — Proyectos Integradores
Tres proyectos que combinan todos los conceptos: gestor de tareas
(POO + JSON + excepciones), analizador de datos (archivos + funciones),
y proyecto CLI (modulos + testing + decoradores).

---

## Prerequisitos y Herramientas

| Herramienta | Para que | Seccion |
|-------------|----------|---------|
| Python 3.10+ | Interprete | Todas |
| Editor/IDE (VS Code) | Escribir codigo | Todas |
| Terminal | Ejecutar scripts | Todas |
| `venv` | Entornos virtuales | 05+ |
| `pip` | Instalar paquetes | 05+ |
| `pytest` | Testing | 09 |
| `pytest-cov` | Cobertura | 09 |

---

## Ruta de Estudio Recomendada

Para principiantes absolutos, seguir el orden 01 a 10 secuencialmente.
Para quienes ya programan en otro lenguaje:

1. Revisar rapidamente 01-02 (sintaxis y estructuras).
2. Profundizar en 03 (funciones avanzadas son el corazon de Python).
3. Estudiar 04 (POO en Python difiere de Java/C++).
4. Ir directo a 07-08 (decoradores y errores son patrones diarios).
5. Completar con 09 (testing es indispensable en codigo profesional).
6. Aplicar todo en 10 (proyectos).
