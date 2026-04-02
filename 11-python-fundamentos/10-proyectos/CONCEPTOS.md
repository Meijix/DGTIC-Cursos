# 10 — Proyectos Integradores

## Descripcion

Esta seccion contiene tres proyectos que integran los conceptos
aprendidos a lo largo del curso. Cada proyecto combina multiples
temas para resolver un problema practico.

---

## Proyecto 1: Gestor de Tareas (`gestor_tareas.py`)

**Que hace**: Aplicacion de linea de comandos para gestionar una lista
de tareas pendientes (TODO list) con persistencia en archivo JSON.

**Conceptos integrados**:
- **Clases y POO** (seccion 04): Clase `Tarea` y `GestorTareas`
- **Archivos y JSON** (seccion 06): Guardar/cargar tareas en JSON
- **Excepciones** (seccion 08): Manejo de errores de archivo y validacion
- **Decoradores** (seccion 07): Logging de operaciones
- **Listas y diccionarios** (seccion 02): Almacenar y filtrar tareas
- **Strings y formato** (seccion 01): Presentacion en consola
- **Funciones** (seccion 03): Modularizacion del codigo

**Como ejecutar**:
```bash
python gestor_tareas.py
```

---

## Proyecto 2: Analizador de Texto (`analizador_texto.py`)

**Que hace**: Herramienta que analiza un archivo de texto y muestra
estadisticas: frecuencia de palabras, palabras unicas, lineas, etc.

**Conceptos integrados**:
- **Diccionarios** (seccion 02): Frecuencia de palabras
- **Conjuntos (sets)** (seccion 02): Palabras unicas
- **Comprehensions** (seccion 02): Filtrado y transformacion
- **Archivos** (seccion 06): Lectura de archivos de texto
- **Funciones** (seccion 03): Organizacion modular
- **Strings** (seccion 01): Limpieza y procesamiento de texto
- **Excepciones** (seccion 08): Manejo de archivos no encontrados

**Como ejecutar**:
```bash
python analizador_texto.py                # Usa texto de ejemplo
python analizador_texto.py archivo.txt    # Analiza un archivo
```

---

## Proyecto 3: Cliente de API del Clima (`api_clima.py`)

**Que hace**: Consulta el clima actual de cualquier ciudad usando
la API gratuita de wttr.in (no requiere API key).

**Conceptos integrados**:
- **Modulos** (seccion 05): urllib, json
- **Excepciones** (seccion 08): Manejo de errores de red
- **Diccionarios** (seccion 02): Parseo de JSON
- **Strings y f-strings** (seccion 01): Formato de salida
- **Funciones** (seccion 03): Organizacion del codigo
- **Context managers** (seccion 08): Manejo de conexiones

**Como ejecutar**:
```bash
python api_clima.py                # Modo interactivo
python api_clima.py "Mexico City"  # Ciudad como argumento
```

---

## Sugerencias para Seguir Practicando

Despues de estudiar estos proyectos, intenta:

1. **Agregar tests** a cada proyecto (seccion 09).
2. **Extender funcionalidad**: prioridades en tareas, graficas de
   frecuencia, pronostico de varios dias.
3. **Combinar proyectos**: un gestor de tareas que envie el clima
   como recordatorio diario.
4. **Crear tu propio proyecto** que integre al menos 5 secciones
   del curso.
