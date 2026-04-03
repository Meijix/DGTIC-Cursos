# 01 — Tipos Basicos — Cheatsheet

## Primitivos

```typescript
let nombre: string = "Ana";
let edad: number = 30;
let activo: boolean = true;
let nulo: null = null;
let indefinido: undefined = undefined;
let simbolo: symbol = Symbol("id");
let grande: bigint = 100n;
```

## Arrays

```typescript
let numeros: number[] = [1, 2, 3];
let palabras: Array<string> = ["hola", "mundo"];
let mixto: (string | number)[] = ["uno", 2];
let readonly: readonly number[] = [1, 2, 3]; // no se puede modificar
```

## Tuplas

```typescript
let par: [string, number] = ["edad", 25];
let triple: [number, string, boolean] = [1, "ok", true];
let etiquetada: [nombre: string, edad: number] = ["Ana", 30];
```

## Enums

```typescript
// Numerico (auto-incremental)
enum Color { Rojo, Verde, Azul }        // 0, 1, 2
let c: Color = Color.Verde;             // 1

// String
enum Estado { Activo = "ACTIVO", Inactivo = "INACTIVO" }

// Const enum (eliminado en compilacion)
const enum Dir { Norte, Sur, Este, Oeste }
```

## Tipos Especiales

```typescript
// any — sin verificacion (evitar)
let x: any = "cualquier cosa";
x = 42; x = true; x.metodo(); // todo permitido

// unknown — seguro, requiere verificacion
let y: unknown = obtenerDato();
if (typeof y === "string") { y.toUpperCase(); }

// void — sin retorno util
function log(msg: string): void { console.log(msg); }

// never — nunca retorna
function fallo(msg: string): never { throw new Error(msg); }
```

## Anotaciones vs Inferencia

```typescript
// Explicita (anotacion)
let a: number = 10;
function suma(x: number, y: number): number { return x + y; }

// Inferida (TypeScript deduce el tipo)
let b = 10;                    // number
let c = "hola";               // string
let d = [1, 2, 3];            // number[]
const e = "literal";          // tipo literal "literal"
```

## Aserciones de Tipo

```typescript
let valor: unknown = "hola mundo";

// Forma 1: as
let largo1 = (valor as string).length;

// Forma 2: angulos (no usar en JSX/TSX)
let largo2 = (<string>valor).length;
```

## Type Narrowing Basico

```typescript
function procesar(valor: string | number): string {
  if (typeof valor === "string") {
    return valor.toUpperCase();    // TS sabe que es string
  }
  return valor.toFixed(2);        // TS sabe que es number
}
```

## Tabla Rapida — any vs unknown

```
┌──────────────┬───────────────────┬───────────────────┐
│ Operacion    │ any               │ unknown           │
├──────────────┼───────────────────┼───────────────────┤
│ Asignar a    │ Cualquier tipo    │ Solo any/unknown  │
│ Leer prop    │ Si (sin error)    │ No (error)        │
│ Llamar()     │ Si (sin error)    │ No (error)        │
│ Operadores   │ Si (sin error)    │ No (error)        │
│ Con guard    │ No necesita       │ Si, obligatorio   │
│ Seguridad    │ Ninguna           │ Alta              │
└──────────────┴───────────────────┴───────────────────┘
```
