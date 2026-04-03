# 05 — Modulos y Configuracion — Cheatsheet

## tsconfig.json Minimo Recomendado

```jsonc
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "declaration": true,
    "sourceMap": true,
    "skipLibCheck": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

## Import / Export

```typescript
// Named export
export function sumar(a: number, b: number): number { return a + b; }
export const PI = 3.14159;
export interface Config { host: string; port: number; }

// Named import
import { sumar, PI, Config } from "./utils.js";

// Default export
export default class Logger { }
import Logger from "./logger.js";

// Import todo
import * as Utils from "./utils.js";

// Re-export
export { sumar } from "./utils.js";
export * from "./utils.js";
```

## Import/Export Solo de Tipos

```typescript
// Solo importa el tipo (eliminado en compilacion)
import type { Config } from "./tipos.js";

// Export solo tipo
export type { Config };
export type MiTipo = string | number;
```

## Opciones de target

```
┌───────────┬─────────────────────────────────┐
│ Target    │ Soporte                         │
├───────────┼─────────────────────────────────┤
│ ES5       │ IE11+ (muy legacy)              │
│ ES6/ES2015│ Clases, arrow functions, let    │
│ ES2018    │ async/await, rest/spread        │
│ ES2020    │ Optional chaining, BigInt       │
│ ES2022    │ Top-level await, #private       │
│ ESNext    │ Ultimo estandar disponible      │
└───────────┴─────────────────────────────────┘
```

## Opciones de module

```
┌───────────────┬─────────────────────────────┐
│ Module        │ Uso                         │
├───────────────┼─────────────────────────────┤
│ CommonJS      │ Node.js legacy (require)    │
│ ES6/ES2015    │ ES Modules basicos          │
│ ESNext        │ Bundlers modernos, Node 18+ │
│ Node16/NodeNext│ Node.js con ESM nativo     │
└───────────────┴─────────────────────────────┘
```

## Opciones Strict (individuales)

```
┌─────────────────────────┬────────────────────┐
│ Opcion                  │ Efecto             │
├─────────────────────────┼────────────────────┤
│ noImplicitAny           │ No inferir any     │
│ strictNullChecks        │ Manejar null/undef │
│ strictFunctionTypes     │ Tipos fn estrictos │
│ strictPropertyInit      │ Inicializar props  │
│ noImplicitThis          │ this explicito     │
│ alwaysStrict            │ Emitir "use strict"│
└─────────────────────────┴────────────────────┘
```

## Declaration Files (.d.ts)

```typescript
// tipos-globales.d.ts
declare module "mi-libreria-sin-tipos" {
  export function hacerAlgo(x: string): number;
  export const VERSION: string;
}

// Ampliar tipos existentes
declare global {
  interface Window {
    miVariable: string;
  }
}
```

## @types Comunes

```bash
npm i -D @types/node        # APIs de Node.js
npm i -D @types/express      # Express.js
npm i -D @types/react        # React
npm i -D @types/lodash       # Lodash
npm i -D @types/jest         # Jest testing
```

## Comandos tsc

```bash
tsc                    # Compilar segun tsconfig.json
tsc --init             # Crear tsconfig.json
tsc --watch            # Recompilar al detectar cambios
tsc --noEmit           # Solo verificar tipos, no generar JS
tsc archivo.ts         # Compilar un archivo especifico
tsc --showConfig       # Mostrar config efectiva
```

## Path Aliases

```jsonc
// tsconfig.json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@utils/*": ["src/utils/*"],
      "@models/*": ["src/models/*"]
    }
  }
}
```

```typescript
// Usar en codigo
import { sumar } from "@utils/math.js";
```

## Tabla Rapida — Archivos

```
┌──────────────┬──────────────────────────────────────┐
│ Extension    │ Proposito                            │
├──────────────┼──────────────────────────────────────┤
│ .ts          │ Codigo TypeScript                    │
│ .tsx         │ TypeScript con JSX (React)           │
│ .d.ts        │ Solo declaraciones de tipos          │
│ .js          │ JavaScript compilado                 │
│ .js.map      │ Source map para debugging            │
│ tsconfig.json│ Configuracion del proyecto           │
└──────────────┴──────────────────────────────────────┘
```
