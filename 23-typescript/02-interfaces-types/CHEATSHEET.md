# 02 — Interfaces y Types — Cheatsheet

## Definir una Interface

```typescript
interface Usuario {
  nombre: string;
  edad: number;
  email?: string;          // opcional
  readonly id: number;     // solo lectura
}
```

## Definir un Type Alias

```typescript
type Punto = { x: number; y: number };
type ID = string | number;
type Estado = "activo" | "inactivo" | "pendiente";
type Coordenadas = [number, number];
```

## Extender Interface

```typescript
interface Animal { nombre: string; }
interface Perro extends Animal { raza: string; }

// Multiple herencia
interface PerroGuia extends Animal, Perro { certificado: boolean; }
```

## Extender Type (Interseccion)

```typescript
type Animal = { nombre: string };
type Mascota = Animal & { duenio: string };
// Resultado: { nombre: string; duenio: string }
```

## Union Types

```typescript
type StringONumero = string | number;
type Semaforo = "rojo" | "amarillo" | "verde";
type Dado = 1 | 2 | 3 | 4 | 5 | 6;

function mostrar(valor: string | number): void {
  if (typeof valor === "string") { /* es string */ }
  else { /* es number */ }
}
```

## Interseccion Types

```typescript
type A = { x: number };
type B = { y: number };
type AB = A & B;  // { x: number; y: number }
```

## Propiedades Opcionales

```typescript
interface Config {
  host: string;
  puerto?: number;       // puede ser number | undefined
  debug?: boolean;
}

let cfg: Config = { host: "localhost" }; // OK, puerto y debug omitidos
```

## Readonly

```typescript
interface Inmutable {
  readonly id: number;
  readonly nombre: string;
}

let obj: Inmutable = { id: 1, nombre: "test" };
// obj.id = 2;  // ERROR: Cannot assign to 'id' because it is read-only
```

## Index Signatures

```typescript
interface Diccionario {
  [clave: string]: string;
}

interface NumerosPorNombre {
  [nombre: string]: number;
}
```

## Tipos Literales

```typescript
type Rol = "admin" | "editor" | "lector";
type HttpStatus = 200 | 301 | 404 | 500;
type Verdad = true;

let rol: Rol = "admin";      // OK
// let rol2: Rol = "otro";   // ERROR
```

## Declaration Merging (solo interface)

```typescript
interface Ventana { titulo: string; }
interface Ventana { ancho: number; }
// Resultado: Ventana = { titulo: string; ancho: number }
```

## Union Discriminada

```typescript
type Exito = { tipo: "exito"; datos: string };
type Error = { tipo: "error"; mensaje: string };
type Resultado = Exito | Error;

function manejar(r: Resultado): string {
  switch (r.tipo) {
    case "exito": return r.datos;
    case "error": return r.mensaje;
  }
}
```

## Tabla Rapida

```
┌───────────────────┬───────────────┬───────────────┐
│ Necesidad         │ Usar          │ Sintaxis      │
├───────────────────┼───────────────┼───────────────┤
│ Forma de objeto   │ interface     │ interface X{} │
│ Union de tipos    │ type          │ A | B         │
│ Interseccion      │ type          │ A & B         │
│ Alias primitivo   │ type          │ type X = str  │
│ Herencia objeto   │ interface     │ extends       │
│ Tupla             │ type          │ [A, B]        │
│ Merging           │ interface     │ declarar 2x   │
│ API publica       │ interface     │ interface X{} │
└───────────────────┴───────────────┴───────────────┘
```
