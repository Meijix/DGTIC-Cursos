# TypeScript — Conceptos Generales

## Que es TypeScript

TypeScript es un **superconjunto tipado de JavaScript** desarrollado por Microsoft.
Agrega un sistema de tipos estatico que se verifica en tiempo de compilacion,
pero al final se compila a JavaScript puro que ejecuta cualquier navegador o runtime.

```
TypeScript = JavaScript + Sistema de Tipos + Compilador
```

## Por que usar TypeScript en lugar de JavaScript

1. **Deteccion temprana de errores** — Los errores de tipo se encuentran antes de ejecutar
2. **Mejor autocompletado** — Los editores entienden la estructura de tus datos
3. **Refactorizacion segura** — Renombrar una propiedad actualiza todas las referencias
4. **Documentacion viva** — Los tipos actuan como documentacion que nunca se desactualiza
5. **Escalabilidad** — Indispensable en proyectos grandes con multiples desarrolladores

## Comparacion TypeScript vs JavaScript

```
┌──────────────────────┬─────────────────────┬─────────────────────┐
│ Caracteristica       │ JavaScript          │ TypeScript          │
├──────────────────────┼─────────────────────┼─────────────────────┤
│ Tipado               │ Dinamico            │ Estatico + Dinamico │
│ Errores de tipo      │ En ejecucion        │ En compilacion      │
│ Autocompletado       │ Limitado            │ Completo            │
│ Compilacion          │ No necesita         │ tsc -> .js          │
│ Curva de aprendizaje │ Baja                │ Media               │
│ Archivos             │ .js                 │ .ts / .tsx          │
│ Ejecucion directa    │ Si (navegador/Node) │ No (necesita tsc)   │
│ Interfaces           │ No existen          │ Si                  │
│ Enums                │ No nativos          │ Si                  │
│ Genericos            │ No                  │ Si                  │
│ Ecosistema           │ npm completo        │ npm + @types        │
│ Adopcion empresarial │ Universal           │ Creciendo rapido    │
└──────────────────────┴─────────────────────┴─────────────────────┘
```

## Sistema de Tipos

TypeScript utiliza un sistema de tipos **estructural** (no nominal). Esto significa
que la compatibilidad de tipos se determina por la **estructura** de los datos,
no por el nombre del tipo.

```
┌─────────────────────────────────────────────┐
│           SISTEMA DE TIPOS                  │
├─────────────────────────────────────────────┤
│                                             │
│  Tipos Primitivos    Tipos Compuestos       │
│  ├── string          ├── Array<T>           │
│  ├── number          ├── Tuple              │
│  ├── boolean         ├── Object / Interface │
│  ├── null            ├── Union (A | B)      │
│  ├── undefined       ├── Intersection (A&B) │
│  ├── symbol          └── Enum               │
│  ├── bigint                                 │
│  └── void / never    Tipos Avanzados        │
│                      ├── Generics<T>        │
│                      ├── Utility Types      │
│                      ├── Mapped Types        │
│                      ├── Conditional Types   │
│                      └── Template Literals   │
└─────────────────────────────────────────────┘
```

## Flujo de Compilacion

TypeScript no se ejecuta directamente. Debe compilarse a JavaScript mediante
el compilador `tsc` (TypeScript Compiler).

```
                    FLUJO DE COMPILACION

  codigo.ts          tsc (compilador)         codigo.js
 ┌───────────┐      ┌──────────────┐        ┌───────────┐
 │ TypeScript │ ──▶  │  1. Parsear  │  ──▶   │ JavaScript│
 │  (.ts)     │      │  2. Verificar│        │  (.js)    │
 │            │      │     tipos    │        │           │
 │ interface  │      │  3. Emitir   │        │ Sin tipos │
 │ tipos      │      │     JS       │        │ ES5/ES6+  │
 │ genericos  │      │              │        │           │
 └───────────┘      └──────────────┘        └───────────┘
                           │
                    ┌──────┴──────┐
                    │ tsconfig.json│
                    │ Configuracion│
                    │ del proyecto │
                    └─────────────┘

  Si hay errores de tipo:
  ┌────────────────────────────────────────┐
  │  Error TS2322: Type 'string' is not    │
  │  assignable to type 'number'.          │
  │  codigo.ts(5,3)                        │
  └────────────────────────────────────────┘
  El compilador reporta ANTES de ejecutar.
```

## Instalacion y Primeros Pasos

```bash
# Instalar TypeScript globalmente
npm install -g typescript

# Verificar version
tsc --version

# Inicializar proyecto con tsconfig.json
tsc --init

# Compilar un archivo
tsc archivo.ts

# Compilar en modo watch (recompila al guardar)
tsc --watch
```

## Estructura del Modulo

```
23-typescript/
├── CONCEPTOS.md          <-- Este archivo
├── CHEATSHEET.md         <-- Referencia rapida general
├── index.html            <-- Pagina de navegacion
├── 01-tipos-basicos/     <-- Tipos primitivos y anotaciones
├── 02-interfaces-types/  <-- Interfaces vs type aliases
├── 03-funciones-genericos/ <-- Funciones tipadas y genericos
├── 04-clases-poo/        <-- Clases y POO con tipos
├── 05-modulos-config/    <-- Configuracion y modulos ES
├── 06-tipos-avanzados/   <-- Utility types y tipos condicionales
└── 07-proyecto/          <-- Proyecto integrador
```

## Cuando Usar TypeScript

- **SI** — Proyectos medianos/grandes con multiples desarrolladores
- **SI** — APIs y backends con Node.js donde la estructura de datos importa
- **SI** — Aplicaciones frontend con React, Angular o Vue
- **SI** — Librerias publicas que necesitan buena DX (developer experience)
- **DEPENDE** — Scripts pequenos y prototipos rapidos (puede ser excesivo)
- **NO** — Si el equipo no tiene disposicion de aprender la sintaxis adicional
