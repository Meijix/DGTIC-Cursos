# 03 — Funciones y Genericos — Cheatsheet

## Funciones Tipadas

```typescript
// Declaracion
function suma(a: number, b: number): number { return a + b; }

// Arrow
const duplicar = (n: number): number => n * 2;

// Tipo de funcion
type Operacion = (a: number, b: number) => number;
let op: Operacion = (a, b) => a * b;
```

## Parametros Opcionales y Default

```typescript
function crear(nombre: string, edad?: number): string { ... }
function saludar(nombre: string, saludo = "Hola"): string { ... }
```

## Rest Parameters

```typescript
function sumarTodos(...nums: number[]): number {
  return nums.reduce((a, b) => a + b, 0);
}
```

## Overloads

```typescript
function buscar(id: number): Usuario;
function buscar(email: string): Usuario;
function buscar(criterio: number | string): Usuario {
  // implementacion
}
```

## Genericos — Basico

```typescript
function identidad<T>(valor: T): T { return valor; }
identidad<string>("hola");  // explicito
identidad(42);              // inferido: T = number
```

## Genericos — Multiples Parametros

```typescript
function par<K, V>(clave: K, valor: V): [K, V] {
  return [clave, valor];
}
```

## Genericos — Restricciones

```typescript
// T debe tener .length
function largo<T extends { length: number }>(item: T): number {
  return item.length;
}

// K debe ser clave de T
function obtener<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
```

## Interface Generica

```typescript
interface Respuesta<T> {
  datos: T;
  exito: boolean;
  mensaje: string;
}

let r: Respuesta<string[]> = { datos: ["a"], exito: true, mensaje: "ok" };
```

## Type Generico

```typescript
type Resultado<T> = { ok: true; valor: T } | { ok: false; error: string };
type Par<A, B> = [A, B];
type Nullable<T> = T | null;
```

## Valor Default en Genericos

```typescript
interface Caja<T = string> { contenido: T; }
let c: Caja = { contenido: "hola" };      // T = string
let d: Caja<number> = { contenido: 42 };  // T = number
```

## Funcion Generica con Callback

```typescript
function mapear<T, U>(arr: T[], fn: (item: T) => U): U[] {
  return arr.map(fn);
}

mapear([1, 2, 3], n => n.toString());  // string[]
```

## Patrones Comunes

```typescript
// Promise generica
async function fetchDatos<T>(url: string): Promise<T> {
  const resp = await fetch(url);
  return resp.json() as T;
}

// Funcion fabrica
function crearArray<T>(item: T, cantidad: number): T[] {
  return Array(cantidad).fill(item);
}

// Restriccion con interface
interface Identificable { id: number; }
function buscarPorId<T extends Identificable>(items: T[], id: number): T | undefined {
  return items.find(item => item.id === id);
}
```

## Tabla Rapida

```
┌────────────────────┬──────────────────────────────────┐
│ Patron             │ Sintaxis                         │
├────────────────────┼──────────────────────────────────┤
│ Generico simple    │ <T>                              │
│ Dos parametros     │ <K, V>                           │
│ Con restriccion    │ <T extends Tipo>                 │
│ Con keyof          │ <T, K extends keyof T>           │
│ Con default        │ <T = string>                     │
│ En interface       │ interface X<T> { prop: T }       │
│ En type            │ type X<T> = { prop: T }          │
│ En funcion         │ function fn<T>(x: T): T          │
│ En arrow           │ const fn = <T>(x: T): T => x    │
└────────────────────┴──────────────────────────────────┘
```
