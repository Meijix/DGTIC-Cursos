# 04 — Clases y Programacion Orientada a Objetos

## Clases en TypeScript vs JavaScript

TypeScript agrega **tipos, modificadores de acceso y clases abstractas**
al sistema de clases de JavaScript, acercandolo a lenguajes como Java o C#.

```
┌──────────────────────┬─────────────────────┬─────────────────────┐
│ Caracteristica       │ JavaScript          │ TypeScript          │
├──────────────────────┼─────────────────────┼─────────────────────┤
│ Clases               │ Si (ES6+)           │ Si                  │
│ Herencia             │ Si (extends)        │ Si (extends)        │
│ public/private       │ # privado (ES2022)  │ public/private/prot │
│ Interfaces           │ No                  │ implements          │
│ Clases abstractas    │ No                  │ abstract            │
│ Tipos en propiedades │ No                  │ Si                  │
│ readonly             │ No nativo           │ Si                  │
│ Parametros shorthand │ No                  │ Si (constructor)    │
└──────────────────────┴─────────────────────┴─────────────────────┘
```

## Clase Basica con Tipos

```typescript
class Persona {
  nombre: string;
  edad: number;

  constructor(nombre: string, edad: number) {
    this.nombre = nombre;
    this.edad = edad;
  }

  presentarse(): string {
    return `Soy ${this.nombre}, tengo ${this.edad} anios`;
  }
}
```

## Shorthand del Constructor

TypeScript permite declarar y asignar propiedades directamente en el constructor.

```
  // Sin shorthand (verbose):          // Con shorthand (compacto):
  class Persona {                      class Persona {
    nombre: string;                      constructor(
    edad: number;                          public nombre: string,
                                           public edad: number
    constructor(nombre: string,          ) {}
                edad: number) {        }
      this.nombre = nombre;
      this.edad = edad;
    }
  }

  Ambos producen exactamente la misma clase.
```

## Modificadores de Acceso

```
┌────────────────┬───────────┬────────────┬──────────────┐
│ Modificador    │ Clase     │ Subclase   │ Exterior     │
├────────────────┼───────────┼────────────┼──────────────┤
│ public         │ Si        │ Si         │ Si           │
│ protected      │ Si        │ Si         │ No           │
│ private        │ Si        │ No         │ No           │
│ readonly       │ Si (leer) │ Si (leer)  │ Si (leer)    │
└────────────────┴───────────┴────────────┴──────────────┘

  public    — accesible desde cualquier lugar (por defecto)
  protected — solo dentro de la clase y sus subclases
  private   — solo dentro de la propia clase
  readonly  — se puede leer pero no reasignar despues del constructor
```

## Diagrama de Acceso

```
  ┌──────────────────────────────────────────┐
  │  class Animal                            │
  │  ┌─────────────────────────────────┐     │
  │  │ public nombre     ←───────── acceso externo OK    │
  │  │ protected especie ←───────── subclase OK, externo NO │
  │  │ private _id       ←───────── solo esta clase      │
  │  └─────────────────────────────────┘     │
  │                                          │
  │  class Perro extends Animal              │
  │  ┌─────────────────────────────────┐     │
  │  │ this.nombre   ✓ (public)        │     │
  │  │ this.especie  ✓ (protected)     │     │
  │  │ this._id      ✗ (private)       │     │
  │  └─────────────────────────────────┘     │
  └──────────────────────────────────────────┘
```

## Herencia (extends)

```typescript
class Animal {
  constructor(public nombre: string) {}

  mover(distancia: number): string {
    return `${this.nombre} se movio ${distancia}m`;
  }
}

class Perro extends Animal {
  ladrar(): string {
    return `${this.nombre} dice: Guau!`;
  }
}
```

## Clases Abstractas

No se pueden instanciar directamente. Definen un contrato que las subclases
deben implementar.

```
  abstract class Forma {
    abstract calcularArea(): number;   // SIN implementacion
    abstract calcularPerimetro(): number;

    describir(): string {              // CON implementacion
      return `Area: ${this.calcularArea()}`;
    }
  }

  // const f = new Forma();  // ERROR: no se puede instanciar

  class Circulo extends Forma {
    constructor(public radio: number) { super(); }

    calcularArea(): number {           // DEBE implementar
      return Math.PI * this.radio ** 2;
    }
    calcularPerimetro(): number {
      return 2 * Math.PI * this.radio;
    }
  }
```

## Implements (interface como contrato)

Una clase puede **implementar** una o mas interfaces.

```
  interface Serializable {
    serializar(): string;
  }

  interface Imprimible {
    imprimir(): void;
  }

  class Documento implements Serializable, Imprimible {
    constructor(public contenido: string) {}

    serializar(): string {       // obligatorio por Serializable
      return JSON.stringify({ contenido: this.contenido });
    }

    imprimir(): void {           // obligatorio por Imprimible
      console.log(this.contenido);
    }
  }

  ┌──────────────────────────────────────────────────────┐
  │ implements = "esta clase CUMPLE este contrato"       │
  │ La clase DEBE tener todos los metodos de la interface│
  └──────────────────────────────────────────────────────┘
```

## Miembros Estaticos

Pertenecen a la clase, no a las instancias.

```typescript
class Contador {
  static total: number = 0;

  constructor() {
    Contador.total++;
  }

  static obtenerTotal(): number {
    return Contador.total;
  }
}

new Contador();
new Contador();
Contador.obtenerTotal(); // 2
```

## Getters y Setters

```typescript
class Temperatura {
  private _celsius: number;

  constructor(celsius: number) {
    this._celsius = celsius;
  }

  get fahrenheit(): number {
    return this._celsius * 9/5 + 32;
  }

  set fahrenheit(f: number) {
    this._celsius = (f - 32) * 5/9;
  }
}
```

## Cuando Usar Cada Patron

- **Clases simples** — Objetos con estado y comportamiento relacionado
- **abstract** — Familia de clases con comportamiento comun pero detalles diferentes
- **implements** — Asegurar que una clase cumple un contrato especifico
- **private** — Datos internos que no deben ser accesibles desde fuera
- **protected** — Datos que las subclases necesitan pero el exterior no
- **static** — Contadores, fabricas, metodos de utilidad sin estado de instancia
- **readonly** — Propiedades que se asignan una vez y no cambian
