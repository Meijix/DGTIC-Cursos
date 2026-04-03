# 01 — Tipos Basicos en TypeScript

## Que son los tipos

Los tipos definen la **forma y naturaleza** de los datos. TypeScript verifica
que los valores asignados correspondan con el tipo declarado, detectando
errores antes de ejecutar el codigo.

## Tipos Primitivos

```
┌─────────────┬──────────────────────────────────────────────┐
│ Tipo        │ Descripcion                                  │
├─────────────┼──────────────────────────────────────────────┤
│ string      │ Texto: "hola", 'mundo', `template`          │
│ number      │ Numeros: 42, 3.14, 0xFF, NaN, Infinity      │
│ boolean     │ Logico: true, false                          │
│ null        │ Ausencia intencional de valor                │
│ undefined   │ Variable declarada pero sin asignar          │
│ symbol      │ Identificador unico e inmutable              │
│ bigint      │ Enteros arbitrariamente grandes: 9007n       │
└─────────────┴──────────────────────────────────────────────┘
```

## Tipos Especiales de TypeScript

```
┌─────────────┬──────────────────────────────────────────────┐
│ Tipo        │ Descripcion                                  │
├─────────────┼──────────────────────────────────────────────┤
│ any         │ Desactiva la verificacion de tipos           │
│ unknown     │ Seguro: requiere verificacion antes de usar  │
│ void        │ Funcion que no retorna valor util            │
│ never       │ Funcion que NUNCA retorna (error / infinito) │
└─────────────┴──────────────────────────────────────────────┘
```

## Anotaciones de Tipo vs Inferencia

TypeScript puede **inferir** tipos automaticamente, pero tambien puedes
declararlos explicitamente con **anotaciones**.

```
  Anotacion explicita          Inferencia automatica
  ─────────────────            ──────────────────────
  let x: number = 5;          let x = 5;  // TS infiere number
  let s: string = "hola";     let s = "hola"; // TS infiere string
```

### Cuando usar anotaciones explicitas

- Parametros de funciones (siempre)
- Variables sin valor inicial
- Tipos de retorno en funciones publicas
- Cuando la inferencia no es suficientemente precisa

### Cuando confiar en la inferencia

- Variables con valor inicial claro
- Retorno obvio de funciones simples
- Resultados de operaciones aritmeticas

## Arrays y Tuplas

```
  Arrays (todos los elementos del mismo tipo):
  ┌──────────────────────────────────────────┐
  │ let nums: number[] = [1, 2, 3];         │
  │ let strs: Array<string> = ["a", "b"];   │
  └──────────────────────────────────────────┘

  Tuplas (longitud y tipos fijos por posicion):
  ┌──────────────────────────────────────────┐
  │ let par: [string, number] = ["edad", 25];│
  │ // par[0] es string, par[1] es number   │
  └──────────────────────────────────────────┘
```

## Enums

Los enums permiten definir un conjunto de constantes con nombre.

```
  enum Direccion {         Resultado compilado (JS):
    Norte,    // 0         var Direccion;
    Sur,      // 1         Direccion[0] = "Norte";
    Este,     // 2         Direccion["Norte"] = 0;
    Oeste     // 3         ...
  }
```

### Tipos de enum

- **Numerico** — Valores auto-incrementales (por defecto)
- **String** — Cada miembro tiene un valor string explicito
- **const enum** — Se elimina en compilacion, solo quedan los valores

## any vs unknown

```
  any                              unknown
  ───                              ───────
  Desactiva verificacion           Requiere verificacion
  Permite CUALQUIER operacion      Bloquea operaciones sin guard
  Usar solo como ultimo recurso    Preferir sobre any

  let a: any = "hola";            let b: unknown = "hola";
  a.metodo();  // OK (peligroso)  b.metodo();  // ERROR
  a + 1;       // OK (peligroso)  if (typeof b === "string") {
                                    b.toUpperCase(); // OK
                                  }
```

## void y never

```
  void — la funcion retorna pero sin valor util:
  function saludar(): void {
    console.log("Hola");
    // return undefined; (implicito)
  }

  never — la funcion NUNCA retorna:
  function error(msg: string): never {
    throw new Error(msg);       // siempre lanza
  }
  function infinito(): never {
    while (true) { }            // nunca termina
  }
```

## Diagrama de Jerarquia de Tipos

```
                    unknown  (supertipo de todo)
                       │
          ┌────────────┼────────────┐
          │            │            │
       string       number      boolean  ...objetos, arrays
          │            │            │
          └────────────┼────────────┘
                       │
                     never  (subtipo de todo)
```

`unknown` acepta cualquier valor. `never` no acepta ningun valor.
Todo tipo es asignable a `unknown`, y `never` es asignable a todo tipo.

## Cuando Usar Cada Tipo

- **string, number, boolean** — Siempre que puedas ser especifico
- **unknown** — Datos externos (API, input del usuario) antes de validar
- **any** — Solo al migrar JS a TS o con librerias sin tipos
- **void** — Retorno de funciones que solo producen efectos secundarios
- **never** — Funciones que lanzan errores o entran en loops infinitos
- **tuplas** — Cuando la posicion de cada elemento tiene significado fijo
- **enums** — Conjuntos cerrados de opciones conocidas en compilacion
