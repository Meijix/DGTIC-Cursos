# 03 — Funciones y Genericos

## Funciones Tipadas

En TypeScript, las funciones declaran los tipos de sus parametros y su retorno.

```typescript
function suma(a: number, b: number): number {
  return a + b;
}
```

El tipo de retorno se puede inferir, pero es buena practica declararlo
en funciones publicas y complejas.

## Formas de Declarar Funciones

```
  // Declaracion clasica
  function saludar(nombre: string): string {
    return `Hola, ${nombre}`;
  }

  // Arrow function
  const duplicar = (n: number): number => n * 2;

  // Tipo de funcion como variable
  let operacion: (a: number, b: number) => number;
  operacion = (a, b) => a + b;

  // Interface para funcion
  interface Comparador {
    (a: string, b: string): number;
  }
```

## Parametros Opcionales y Default

```
  function crear(nombre: string, edad?: number): string {
    //                              ^
    //                     opcional (puede ser undefined)
    return edad ? `${nombre} (${edad})` : nombre;
  }

  function saludar(nombre: string, saludo: string = "Hola"): string {
    //                                       ^
    //                              valor por defecto
    return `${saludo}, ${nombre}!`;
  }

  ┌─────────────────────────────────────────────────────────┐
  │ Opcionales van DESPUES de los obligatorios              │
  │ Default no necesita ? — ya tiene un valor si se omite   │
  └─────────────────────────────────────────────────────────┘
```

## Rest Parameters

Reciben un numero variable de argumentos como array.

```typescript
function sumarTodos(...numeros: number[]): number {
  return numeros.reduce((acc, n) => acc + n, 0);
}

sumarTodos(1, 2, 3, 4, 5); // 15
```

## Function Overloads

Permiten que una funcion acepte diferentes combinaciones de parametros.

```
  // Firmas de overload (sin cuerpo)
  function buscar(id: number): Usuario;
  function buscar(email: string): Usuario;
  function buscar(filtro: FiltroAvanzado): Usuario[];

  // Implementacion (con cuerpo)
  function buscar(criterio: number | string | FiltroAvanzado): Usuario | Usuario[] {
    // logica de implementacion
  }

  ┌─────────────────────────────────────────────────────────┐
  │ Las firmas definen las combinaciones validas.           │
  │ La implementacion debe manejar TODOS los casos.         │
  │ Solo las firmas son visibles para quien usa la funcion. │
  └─────────────────────────────────────────────────────────┘
```

## Que son los Genericos

Los genericos permiten crear funciones, interfaces y clases que trabajan
con **cualquier tipo** sin perder la informacion de tipo.

```
  SIN genericos:                  CON genericos:
  function primero(arr: any[])    function primero<T>(arr: T[]): T
    → retorna any                   → retorna el tipo exacto

  primero([1,2,3])  → any        primero([1,2,3])  → number
  primero(["a"])    → any        primero(["a"])     → string
```

## Sintaxis de Genericos

```
  function identidad<T>(valor: T): T {
    return valor;
  }
           │
           └── T es un "parametro de tipo"
               Se reemplaza con el tipo real al usar la funcion

  identidad<string>("hola");   // T = string
  identidad<number>(42);       // T = number
  identidad("hola");           // TS infiere T = string
```

## Genericos con Multiples Parametros

```typescript
function par<K, V>(clave: K, valor: V): [K, V] {
  return [clave, valor];
}

par<string, number>("edad", 25);  // [string, number]
par("nombre", "Ana");             // [string, string] (inferido)
```

## Restricciones (Constraints)

Limitan los tipos que puede aceptar un generico.

```
  function largo<T extends { length: number }>(item: T): number {
    return item.length;
  }
                   │
                   └── T DEBE tener la propiedad .length

  largo("hola");       // OK: string tiene .length
  largo([1, 2, 3]);   // OK: array tiene .length
  largo(42);           // ERROR: number no tiene .length
```

## Interfaces Genericas

```typescript
interface Respuesta<T> {
  datos: T;
  exito: boolean;
  mensaje: string;
}

interface Paginado<T> {
  items: T[];
  pagina: number;
  totalPaginas: number;
}

// Uso:
let resp: Respuesta<string[]> = {
  datos: ["a", "b"],
  exito: true,
  mensaje: "OK"
};
```

## Diagrama: Genericos en Accion

```
  Definicion:                       Uso:
  ┌──────────────────────┐         ┌─────────────────────────┐
  │ function filtrar<T>( │         │ filtrar<number>(         │
  │   arr: T[],          │  ──▶    │   [1,2,3,4,5],          │
  │   pred: (x:T)=>bool  │         │   n => n > 3            │
  │ ): T[]               │         │ )                       │
  └──────────────────────┘         │ // retorna number[]     │
                                   └─────────────────────────┘
  T es abstracto                   T se reemplaza con number
  (funciona con cualquier tipo)    (todo queda tipado)
```

## Valores por Defecto en Genericos

```typescript
interface ContenedorAPI<T = any> {
  datos: T;
  timestamp: number;
}

let c1: ContenedorAPI<string> = { datos: "hola", timestamp: Date.now() };
let c2: ContenedorAPI = { datos: 42, timestamp: Date.now() }; // T = any
```

## keyof con Genericos

```typescript
function obtener<T, K extends keyof T>(obj: T, clave: K): T[K] {
  return obj[clave];
}

const usuario = { nombre: "Ana", edad: 25 };
obtener(usuario, "nombre");  // tipo: string
obtener(usuario, "edad");    // tipo: number
// obtener(usuario, "x");    // ERROR: "x" no es key de usuario
```

## Cuando Usar Genericos

- Funciones que operan sobre diferentes tipos sin perder informacion de tipo
- Contenedores y colecciones reutilizables (listas, colas, pilas, mapas)
- Respuestas de API donde el tipo de datos varia
- Funciones de utilidad (filtrar, mapear, buscar) que deben ser genericas
- Cuando usarias `any` pero quieres mantener la seguridad de tipos
