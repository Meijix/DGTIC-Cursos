# 05 — Modulos y Configuracion

## tsconfig.json

El archivo `tsconfig.json` es el centro de configuracion de un proyecto TypeScript.
Define como el compilador `tsc` procesa y verifica el codigo.

```bash
# Generar tsconfig.json con opciones por defecto
tsc --init
```

## Estructura de tsconfig.json

```
  tsconfig.json
  ┌─────────────────────────────────────────────────────────┐
  │ {                                                       │
  │   "compilerOptions": {                                  │
  │     // Opciones del compilador (la seccion principal)   │
  │   },                                                    │
  │   "include": [...],    // Que archivos compilar         │
  │   "exclude": [...],    // Que archivos ignorar          │
  │   "extends": "...",    // Heredar de otro tsconfig      │
  │   "references": [...]  // Project references            │
  │ }                                                       │
  └─────────────────────────────────────────────────────────┘
```

## Opciones Principales de compilerOptions

### Target y Module

```
┌───────────────────┬──────────────────────────────────────────┐
│ Opcion            │ Descripcion                              │
├───────────────────┼──────────────────────────────────────────┤
│ target            │ Version JS de salida (ES5, ES6, ES2020+)│
│ module            │ Sistema de modulos (CommonJS, ESNext)    │
│ moduleResolution  │ Como resolver imports (node, bundler)    │
│ outDir            │ Carpeta de salida para .js compilados    │
│ rootDir           │ Carpeta raiz de archivos fuente          │
│ lib               │ Librerias de tipos incluidas (DOM, etc.) │
└───────────────────┴──────────────────────────────────────────┘
```

### Modo Estricto (strict)

```
  "strict": true   activa TODAS estas verificaciones:

  ┌─────────────────────────┬────────────────────────────────┐
  │ Opcion individual       │ Que hace                       │
  ├─────────────────────────┼────────────────────────────────┤
  │ noImplicitAny           │ Error si se infiere any        │
  │ strictNullChecks        │ null/undefined deben manejarse │
  │ strictFunctionTypes     │ Tipos de funcion mas estrictos │
  │ strictBindCallApply     │ Verifica bind/call/apply       │
  │ strictPropertyInit      │ Props deben inicializarse      │
  │ noImplicitThis          │ Error si this es any           │
  │ alwaysStrict            │ Emite "use strict" en JS       │
  └─────────────────────────┴────────────────────────────────┘

  RECOMENDACION: Siempre usa "strict": true en proyectos nuevos.
```

### Opciones de Calidad

```
┌─────────────────────────┬──────────────────────────────────┐
│ Opcion                  │ Que hace                         │
├─────────────────────────┼──────────────────────────────────┤
│ noUnusedLocals          │ Error en variables sin usar      │
│ noUnusedParameters      │ Error en parametros sin usar     │
│ noImplicitReturns       │ Error si falta return en rama    │
│ noFallthroughCasesInSwitch│ Error en case sin break/return │
│ exactOptionalProperties │ Diferencia undefined de omitido  │
└─────────────────────────┴──────────────────────────────────┘
```

## tsconfig.json Recomendado

```jsonc
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "esModuleInterop": true,
    "resolveJsonModule": true,
    "declaration": true,
    "sourceMap": true,
    "skipLibCheck": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "**/*.test.ts"]
}
```

## ES Modules en TypeScript

TypeScript usa la misma sintaxis de import/export que ES Modules.

```
  // ── archivo: utils.ts ──
  export function sumar(a: number, b: number): number {
    return a + b;
  }
  export const PI = 3.14159;

  // ── archivo: main.ts ──
  import { sumar, PI } from "./utils.js";
  //                              ^^^
  //  En TS con moduleResolution "node16" o "bundler"
  //  se usa .js en el import (porque el .ts se compilara a .js)

  console.log(sumar(1, 2));
```

### Tipos de Export

```
  // Named exports
  export function foo() { }
  export const BAR = 42;

  // Default export
  export default class MiClase { }

  // Re-export
  export { foo } from "./otro-modulo.js";
  export * from "./todo.js";

  // Export de tipo (eliminado en compilacion)
  export type { MiTipo } from "./tipos.js";
  export interface MiInterface { }
```

## Declaration Files (.d.ts)

Los archivos `.d.ts` contienen solo **declaraciones de tipos** sin codigo ejecutable.
Sirven para describir la forma de librerias JavaScript.

```
  ┌──────────────────────────────────────────────────────┐
  │  libreria.js (JavaScript puro, sin tipos)            │
  │  ┌──────────────────────────────────────────┐        │
  │  │ function sumar(a, b) { return a + b; }  │        │
  │  └──────────────────────────────────────────┘        │
  │                                                      │
  │  libreria.d.ts (tipos para TypeScript)               │
  │  ┌──────────────────────────────────────────┐        │
  │  │ declare function sumar(a: number,        │        │
  │  │                         b: number): number;│       │
  │  └──────────────────────────────────────────┘        │
  │                                                      │
  │  TypeScript combina ambos para verificar tipos.      │
  └──────────────────────────────────────────────────────┘
```

### Generar .d.ts automaticamente

```bash
# En tsconfig.json:
# "declaration": true
# "declarationDir": "./types"

tsc   # genera .js + .d.ts
```

## Paquetes @types

Muchas librerias JS populares tienen tipos mantenidos por la comunidad
en el repositorio DefinitelyTyped, disponibles como paquetes `@types/`.

```bash
# Instalar tipos para librerias sin tipos nativos
npm install --save-dev @types/node
npm install --save-dev @types/express
npm install --save-dev @types/lodash

# Librerias modernas ya incluyen tipos (.d.ts dentro del paquete)
# No necesitan @types: axios, zod, prisma, etc.
```

```
  ┌────────────────────────────────────────────────────────┐
  │ Si la libreria tiene tipos incluidos:                  │
  │   npm install libreria          (solo esto)            │
  │                                                        │
  │ Si NO tiene tipos:                                     │
  │   npm install libreria                                 │
  │   npm install --save-dev @types/libreria               │
  │                                                        │
  │ Si no existe @types:                                   │
  │   Crear un archivo .d.ts local con las declaraciones   │
  └────────────────────────────────────────────────────────┘
```

## Estructura Tipica de Proyecto

```
  mi-proyecto/
  ├── tsconfig.json       <-- Configuracion
  ├── package.json
  ├── src/                <-- Codigo fuente TS
  │   ├── index.ts
  │   ├── utils.ts
  │   └── types/
  │       └── global.d.ts  <-- Tipos personalizados
  ├── dist/               <-- JS compilado (generado por tsc)
  │   ├── index.js
  │   └── utils.js
  └── node_modules/
```

## Cuando Usar Cada Opcion

- **strict: true** — Siempre, en todo proyecto nuevo
- **target: ES2020+** — Para la mayoria de proyectos modernos
- **module: ESNext** — Con bundlers (Vite, webpack) o Node 18+
- **module: CommonJS** — Proyectos Node.js legacy
- **declaration: true** — Si publicas una libreria
- **sourceMap: true** — Para debug en desarrollo
- **skipLibCheck: true** — Acelera compilacion, omite verificar .d.ts
