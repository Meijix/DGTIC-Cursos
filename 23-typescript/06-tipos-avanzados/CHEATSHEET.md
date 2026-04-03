# 06 — Tipos Avanzados — Cheatsheet

## Utility Types

```typescript
interface Usuario { id: number; nombre: string; email: string; }

Partial<Usuario>           // todas opcionales
Required<Usuario>          // todas obligatorias
Readonly<Usuario>          // todas readonly
Pick<Usuario, "id"|"nombre">  // solo id y nombre
Omit<Usuario, "email">    // todo excepto email
Record<string, number>     // { [k: string]: number }
```

## Exclude / Extract / NonNullable

```typescript
type T = "a" | "b" | "c" | "d";

Exclude<T, "a" | "b">     // "c" | "d"
Extract<T, "a" | "b">     // "a" | "b"

type Nullable = string | number | null | undefined;
NonNullable<Nullable>      // string | number
```

## ReturnType / Parameters / Awaited

```typescript
function crear(nombre: string, edad: number): { id: number } {
  return { id: 1 };
}

ReturnType<typeof crear>      // { id: number }
Parameters<typeof crear>      // [string, number]

type Datos = Awaited<Promise<string>>;  // string
```

## Mapped Types

```typescript
// Hacer todo opcional
type MiPartial<T> = { [K in keyof T]?: T[K] };

// Hacer todo readonly
type MiReadonly<T> = { readonly [K in keyof T]: T[K] };

// Hacer todo nullable
type Nullable<T> = { [K in keyof T]: T[K] | null };

// Renombrar keys con template literal
type Getter<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};
```

## Conditional Types

```typescript
type EsString<T> = T extends string ? true : false;

EsString<string>    // true
EsString<number>    // false

// Con infer
type RetornoDe<T> = T extends (...args: any[]) => infer R ? R : never;
type ElementoDe<T> = T extends (infer E)[] ? E : never;

RetornoDe<() => string>   // string
ElementoDe<number[]>      // number
```

## Template Literal Types

```typescript
type Evento = "click" | "focus" | "blur";
type Handler = `on${Capitalize<Evento>}`;
// "onClick" | "onFocus" | "onBlur"

type Metodo = "get" | "post" | "put" | "delete";
type Ruta = "/users" | "/posts";
type Endpoint = `${Uppercase<Metodo>} ${Ruta}`;
// "GET /users" | "GET /posts" | "POST /users" | ...
```

## String Utility Types

```typescript
Uppercase<"hola">       // "HOLA"
Lowercase<"HOLA">       // "hola"
Capitalize<"hola">      // "Hola"
Uncapitalize<"Hola">    // "hola"
```

## Type Guards

```typescript
// typeof
if (typeof x === "string") { /* string */ }

// instanceof
if (x instanceof Date) { /* Date */ }

// in
if ("nombre" in obj) { /* obj tiene nombre */ }

// Custom guard
function esNumero(x: unknown): x is number {
  return typeof x === "number";
}
```

## Discriminated Union

```typescript
type Forma =
  | { tipo: "circulo"; radio: number }
  | { tipo: "cuadrado"; lado: number };

function area(f: Forma): number {
  switch (f.tipo) {
    case "circulo": return Math.PI * f.radio ** 2;
    case "cuadrado": return f.lado ** 2;
  }
}
```

## satisfies (TS 5+)

```typescript
type Color = "rojo" | "verde" | "azul";
type Colores = Record<string, Color | Color[]>;

const palette = {
  primario: "rojo",
  secundario: ["verde", "azul"]
} satisfies Colores;
// palette.primario es tipo "rojo" (no Color | Color[])
```

## Tabla Rapida

```
┌─────────────────────┬─────────────────────────────────┐
│ Herramienta         │ Caso de uso                     │
├─────────────────────┼─────────────────────────────────┤
│ Partial<T>          │ Actualizaciones parciales       │
│ Required<T>         │ Asegurar completitud            │
│ Readonly<T>         │ Datos inmutables                │
│ Pick<T,K>           │ Subconjunto de propiedades      │
│ Omit<T,K>           │ Excluir propiedades             │
│ Record<K,V>         │ Diccionarios y mapas            │
│ Mapped type         │ Transformar tipos               │
│ Conditional type    │ Tipos dependientes              │
│ Template literal    │ Strings tipadas                 │
│ Type guard          │ Narrowing en runtime            │
│ infer               │ Extraer tipos internos          │
│ satisfies           │ Validar sin perder precision    │
└─────────────────────┴─────────────────────────────────┘
```
