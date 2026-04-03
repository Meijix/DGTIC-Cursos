# TypeScript — Cheatsheet General

## Tipos Basicos

```typescript
let texto: string = "hola";
let edad: number = 25;
let activo: boolean = true;
let lista: number[] = [1, 2, 3];
let tupla: [string, number] = ["edad", 25];
let cualquiera: any = "sin verificar";
let seguro: unknown = "verificar antes de usar";
let nada: void = undefined;       // funciones sin retorno
let imposible: never;              // funciones que nunca retornan
```

## Interfaces vs Type Aliases

```
┌──────────────────────┬─────────────────────┬─────────────────────┐
│ Caracteristica       │ interface           │ type                │
├──────────────────────┼─────────────────────┼─────────────────────┤
│ Objetos              │ Si                  │ Si                  │
│ Extends / herencia   │ extends             │ & (interseccion)    │
│ Declaration merging  │ Si                  │ No                  │
│ Unions               │ No                  │ Si (A | B)          │
│ Primitivos           │ No                  │ Si                  │
│ Tuplas               │ No (indirecto)      │ Si                  │
│ Computed properties  │ No                  │ Si                  │
│ Recomendacion        │ Para APIs publicas  │ Para tipos internos │
└──────────────────────┴─────────────────────┴─────────────────────┘
```

## Genericos — Sintaxis Rapida

```typescript
// Funcion generica
function identidad<T>(valor: T): T { return valor; }

// Interface generica
interface Caja<T> { contenido: T; }

// Con restriccion
function largo<T extends { length: number }>(item: T): number {
  return item.length;
}

// Multiples parametros
function par<K, V>(clave: K, valor: V): [K, V] {
  return [clave, valor];
}
```

## Utility Types

```
┌───────────────────┬──────────────────────────────────────────┐
│ Utility Type      │ Que hace                                 │
├───────────────────┼──────────────────────────────────────────┤
│ Partial<T>        │ Todas las propiedades opcionales         │
│ Required<T>       │ Todas las propiedades obligatorias       │
│ Readonly<T>       │ Todas las propiedades solo lectura       │
│ Pick<T, K>        │ Solo las propiedades K de T              │
│ Omit<T, K>        │ Todas excepto las propiedades K          │
│ Record<K, V>      │ Objeto con claves K y valores V          │
│ Exclude<U, E>     │ Quita E de la union U                    │
│ Extract<U, E>     │ Extrae E de la union U                   │
│ NonNullable<T>    │ Quita null y undefined de T              │
│ ReturnType<F>     │ Tipo de retorno de la funcion F          │
│ Parameters<F>     │ Tupla con los tipos de parametros de F   │
│ Awaited<T>        │ Tipo que resuelve una Promise<T>         │
└───────────────────┴──────────────────────────────────────────┘
```

## tsconfig.json — Opciones Esenciales

```jsonc
{
  "compilerOptions": {
    // -- Salida --
    "target": "ES2020",          // Version JS de salida
    "module": "ESNext",          // Sistema de modulos
    "outDir": "./dist",          // Carpeta de salida
    "rootDir": "./src",          // Carpeta fuente

    // -- Verificacion estricta --
    "strict": true,              // Activa TODAS las verificaciones
    "noImplicitAny": true,       // Error si se infiere any
    "strictNullChecks": true,    // null/undefined requieren manejo

    // -- Modulos --
    "moduleResolution": "node",  // Resolucion estilo Node
    "esModuleInterop": true,     // Compatibilidad CommonJS/ESM
    "resolveJsonModule": true,   // Importar .json

    // -- Calidad --
    "noUnusedLocals": true,      // Error en variables sin usar
    "noUnusedParameters": true,  // Error en parametros sin usar
    "declaration": true          // Generar archivos .d.ts
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

## Type Guards Rapidos

```typescript
// typeof (primitivos)
if (typeof x === "string") { /* x es string aqui */ }

// instanceof (clases)
if (x instanceof Date) { /* x es Date aqui */ }

// in (propiedades)
if ("nombre" in obj) { /* obj tiene .nombre aqui */ }

// Custom type guard
function esString(x: unknown): x is string {
  return typeof x === "string";
}
```

## Patrones Comunes

```typescript
// Tipo union discriminada
type Resultado =
  | { ok: true; datos: string }
  | { ok: false; error: string };

// Asercion de tipo (usar con cuidado)
const input = document.getElementById("mi-input") as HTMLInputElement;

// Non-null assertion (usar con cuidado)
const elemento = document.getElementById("app")!;

// Optional chaining + nullish coalescing
const nombre = usuario?.perfil?.nombre ?? "Anonimo";
```
