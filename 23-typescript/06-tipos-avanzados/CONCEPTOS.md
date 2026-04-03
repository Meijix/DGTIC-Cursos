# 06 — Tipos Avanzados

## Utility Types

TypeScript incluye tipos de utilidad integrados que transforman otros tipos.
Son herramientas fundamentales para evitar repeticion.

```
┌───────────────────┬──────────────────────────────────────────┐
│ Utility Type      │ Que hace                                 │
├───────────────────┼──────────────────────────────────────────┤
│ Partial<T>        │ Todas las propiedades de T opcionales    │
│ Required<T>       │ Todas las propiedades de T obligatorias  │
│ Readonly<T>       │ Todas las propiedades de T solo lectura  │
│ Pick<T, K>        │ Solo las propiedades K de T              │
│ Omit<T, K>        │ Todas las propiedades de T excepto K     │
│ Record<K, V>      │ Objeto con claves K y valores V          │
│ Exclude<U, E>     │ Quita los tipos E de la union U          │
│ Extract<U, E>     │ Extrae los tipos E de la union U         │
│ NonNullable<T>    │ Quita null y undefined de T              │
│ ReturnType<F>     │ Tipo de retorno de la funcion F          │
│ Parameters<F>     │ Tupla con tipos de parametros de F       │
│ Awaited<T>        │ Tipo que resuelve Promise<T>             │
└───────────────────┴──────────────────────────────────────────┘
```

## Partial y Required

```
  interface Usuario {
    nombre: string;
    email: string;
    edad: number;
  }

  Partial<Usuario> =                Required<Partial<Usuario>> =
  {                                 {
    nombre?: string;    (todas       nombre: string;    (todas
    email?: string;      opcionales)  email: string;      obligatorias)
    edad?: number;                   edad: number;
  }                                 }

  Caso de uso:
  - Partial → Actualizar parcialmente (solo los campos que cambian)
  - Required → Asegurar que un tipo parcial este completo
```

## Pick y Omit

```
  interface Usuario {
    id: number;
    nombre: string;
    email: string;
    password: string;
  }

  Pick<Usuario, "id" | "nombre">     Omit<Usuario, "password">
  =                                  =
  {                                  {
    id: number;                        id: number;
    nombre: string;                    nombre: string;
  }                                    email: string;
                                     }

  Caso de uso:
  - Pick → Seleccionar solo lo necesario (respuestas de API)
  - Omit → Excluir campos sensibles (password, tokens)
```

## Record

Crea un tipo de objeto con claves y valores definidos.

```
  Record<string, number>   =  { [key: string]: number }
  Record<"a"|"b"|"c", boolean>  =  { a: boolean; b: boolean; c: boolean }

  Caso de uso: Diccionarios, mapas de configuracion, tablas de busqueda
```

## Mapped Types

Permiten transformar las propiedades de un tipo existente.

```
  // Asi funciona internamente Partial:
  type MiPartial<T> = {
    [K in keyof T]?: T[K];
  };

  // Hacer todo readonly:
  type MiReadonly<T> = {
    readonly [K in keyof T]: T[K];
  };

  // Hacer todo nullable:
  type Nullable<T> = {
    [K in keyof T]: T[K] | null;
  };

  ┌──────────────────────────────────────────────────────┐
  │ [K in keyof T]  = "para cada propiedad K de T"      │
  │ T[K]            = "el tipo de esa propiedad"         │
  │ ?:              = "hazla opcional"                   │
  │ readonly        = "hazla solo lectura"               │
  └──────────────────────────────────────────────────────┘
```

## Conditional Types

Seleccionan un tipo basado en una condicion.

```
  type EsString<T> = T extends string ? "si" : "no";

  EsString<string>   // "si"
  EsString<number>   // "no"
  EsString<"hola">   // "si" (literal string extiende string)

  Sintaxis:
  ┌──────────────────────────────────────────┐
  │ T extends U ? TipoVerdadero : TipoFalso │
  └──────────────────────────────────────────┘
```

### infer — Extraer tipos dentro de conditional types

```
  type RetornoDe<T> = T extends (...args: any[]) => infer R ? R : never;

  RetornoDe<() => string>          // string
  RetornoDe<(x: number) => boolean>  // boolean

  infer R = "captura el tipo de retorno y llamalo R"
```

## Template Literal Types

Crean tipos string a partir de combinaciones.

```
  type Color = "rojo" | "verde" | "azul";
  type Tamano = "sm" | "md" | "lg";

  type ClaseCSS = `${Tamano}-${Color}`;
  // = "sm-rojo" | "sm-verde" | "sm-azul"
  //  | "md-rojo" | "md-verde" | "md-azul"
  //  | "lg-rojo" | "lg-verde" | "lg-azul"

  TypeScript genera TODAS las combinaciones posibles.
```

### Utility types para strings

```
  Uppercase<"hola">     // "HOLA"
  Lowercase<"HOLA">     // "hola"
  Capitalize<"hola">    // "Hola"
  Uncapitalize<"Hola">  // "hola"
```

## Type Guards

Mecanismos para reducir (narrow) el tipo de una variable.

```
  1. typeof — para primitivos
     if (typeof x === "string") { /* x es string */ }

  2. instanceof — para clases
     if (x instanceof Date) { /* x es Date */ }

  3. in — para verificar propiedades
     if ("nombre" in obj) { /* obj tiene .nombre */ }

  4. Custom type guard — funcion con retorno "x is Tipo"
     function esString(x: unknown): x is string {
       return typeof x === "string";
     }
```

## Diagrama: Flujo de Type Guards

```
  valor: string | number | null
       │
       ├── typeof === "string" ──▶ valor: string
       │
       ├── typeof === "number" ──▶ valor: number
       │
       └── valor === null ──▶ valor: null

  En cada rama, TypeScript sabe exactamente el tipo.
```

## Custom Type Guard — Patron Completo

```typescript
interface Perro {
  tipo: "perro";
  ladrar(): void;
}

interface Gato {
  tipo: "gato";
  ronronear(): void;
}

type Mascota = Perro | Gato;

function esPerro(mascota: Mascota): mascota is Perro {
  return mascota.tipo === "perro";
}

function manejarMascota(m: Mascota): void {
  if (esPerro(m)) {
    m.ladrar();    // TypeScript sabe que es Perro
  } else {
    m.ronronear(); // TypeScript sabe que es Gato
  }
}
```

## Cuando Usar Cada Herramienta

- **Partial** — Formularios de edicion, actualizaciones parciales
- **Pick/Omit** — Respuestas de API, vistas parciales de datos
- **Record** — Diccionarios, mapas de configuracion
- **Mapped types** — Transformaciones sistematicas de tipos
- **Conditional types** — Librerias que necesitan tipos dependientes
- **Template literals** — Sistemas de CSS, rutas de API tipadas
- **Type guards** — Siempre que manejes uniones de tipos
