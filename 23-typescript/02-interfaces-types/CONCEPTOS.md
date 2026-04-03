# 02 — Interfaces y Type Aliases

## Que son las Interfaces

Una **interface** define la forma (shape) de un objeto: que propiedades tiene
y de que tipo es cada una. Es un contrato que los objetos deben cumplir.

```typescript
interface Usuario {
  nombre: string;
  edad: number;
  email: string;
}
```

## Que son los Type Aliases

Un **type alias** crea un nombre para cualquier tipo: objetos, uniones,
intersecciones, primitivos, tuplas, etc.

```typescript
type Punto = { x: number; y: number };
type ID = string | number;
type Color = "rojo" | "verde" | "azul";
```

## Comparacion: interface vs type

```
┌──────────────────────┬─────────────────────┬─────────────────────┐
│ Capacidad            │ interface           │ type                │
├──────────────────────┼─────────────────────┼─────────────────────┤
│ Definir objetos      │ Si                  │ Si                  │
│ Extender/heredar     │ extends             │ & (interseccion)    │
│ Declaration merging  │ Si (se fusionan)    │ No (error)          │
│ Tipos union          │ No                  │ Si (A | B)          │
│ Tipos primitivos     │ No                  │ Si (type ID = string)│
│ Tuplas directas      │ No                  │ Si                  │
│ implements en clase  │ Si                  │ Si (si es objeto)   │
│ Computed properties  │ No                  │ Si                  │
│ Rendimiento (tsc)    │ Ligeramente mejor   │ Normal              │
└──────────────────────┴─────────────────────┴─────────────────────┘
```

### Regla general

- Usa **interface** para definir formas de objetos y APIs publicas
- Usa **type** para uniones, intersecciones, primitivos y tipos complejos

## Propiedades Opcionales y Readonly

```
  interface Producto {
    nombre: string;            // obligatoria
    precio: number;            // obligatoria
    descripcion?: string;      // OPCIONAL (puede ser undefined)
    readonly id: number;       // SOLO LECTURA (no se puede reasignar)
  }

  ┌────────────────────────────────────────────┐
  │  ?  = La propiedad puede no existir        │
  │  readonly = No se puede modificar despues  │
  │             de la creacion del objeto       │
  └────────────────────────────────────────────┘
```

## Extender Interfaces

Las interfaces pueden **heredar** propiedades de otras interfaces.

```
  interface Animal {               interface Mascota extends Animal {
    nombre: string;          ──▶     duenio: string;
    edad: number;                  }
  }
                                   // Mascota tiene: nombre, edad, duenio

  Se puede extender de multiples:
  interface PerroGuia extends Animal, Mascota {
    certificado: string;
  }
```

## Extender con Types (Interseccion)

Los type aliases usan `&` para combinar tipos.

```
  type Animal = { nombre: string; edad: number };
  type Mascota = Animal & { duenio: string };

  // Equivale a:
  // { nombre: string; edad: number; duenio: string }
```

## Tipos Union (|)

Un valor puede ser de **uno u otro** tipo.

```
  type Resultado = string | number;
  type Estado = "activo" | "inactivo" | "pendiente";

  ┌──────────────────────────────────────────────┐
  │  A | B  =  "El valor es A  O  es B"         │
  │                                              │
  │  function mostrar(id: string | number) {     │
  │    // id puede ser string O number           │
  │    // Necesitas type guard para usar metodos │
  │  }                                           │
  └──────────────────────────────────────────────┘
```

## Tipos Interseccion (&)

Un valor debe cumplir **ambos** tipos simultaneamente.

```
  type ConNombre = { nombre: string };
  type ConEdad = { edad: number };
  type Persona = ConNombre & ConEdad;

  ┌──────────────────────────────────────────────┐
  │  A & B  =  "El valor es A  Y  tambien B"    │
  │                                              │
  │  let p: Persona = {                          │
  │    nombre: "Ana",   // de ConNombre          │
  │    edad: 25         // de ConEdad            │
  │  };                                          │
  └──────────────────────────────────────────────┘
```

## Tipos Literales

Un tipo literal restringe el valor a una **constante exacta**.

```
  type Direccion = "norte" | "sur" | "este" | "oeste";
  type Dado = 1 | 2 | 3 | 4 | 5 | 6;
  type Respuesta = true | false;

  let rumbo: Direccion = "norte";   // OK
  let rumbo2: Direccion = "arriba"; // ERROR
```

## Declaration Merging (solo interfaces)

Si declaras la misma interface dos veces, TypeScript las **fusiona**.

```
  interface Config { host: string; }
  interface Config { puerto: number; }

  // Resultado: Config = { host: string; puerto: number; }
```

Esto es util para extender tipos de librerias externas. Los type aliases
**no** soportan esto: declarar el mismo type dos veces causa un error.

## Index Signatures

Permite definir objetos con claves dinamicas.

```
  interface Diccionario {
    [clave: string]: number;
  }

  let precios: Diccionario = {
    manzana: 15,
    pera: 20,
    uva: 35
  };
```

## Diagrama de Decision

```
  Necesitas definir un tipo?
       │
       ├── Es un objeto/contrato? ──▶ interface
       │
       ├── Es una union (A | B)? ──▶ type
       │
       ├── Es un primitivo con alias? ──▶ type
       │
       ├── Necesitas declaration merging? ──▶ interface
       │
       └── Tipo complejo / mapeado? ──▶ type
```

## Cuando Usar Cada Uno

- **interface** — Objetos, clases que implementan contratos, APIs publicas
- **type** — Uniones, intersecciones, tuplas, tipos complejos, alias de primitivos
- **readonly** — Datos que no deben cambiar (configs, IDs, constantes)
- **?** (opcional) — Propiedades que pueden no existir (formularios parciales)
- **Union literal** — Conjuntos cerrados de valores conocidos (estados, roles)
