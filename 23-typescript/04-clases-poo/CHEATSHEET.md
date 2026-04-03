# 04 — Clases y POO — Cheatsheet

## Clase Basica

```typescript
class Persona {
  nombre: string;
  edad: number;

  constructor(nombre: string, edad: number) {
    this.nombre = nombre;
    this.edad = edad;
  }

  saludar(): string {
    return `Hola, soy ${this.nombre}`;
  }
}
```

## Shorthand Constructor

```typescript
class Persona {
  constructor(
    public nombre: string,
    public edad: number,
    private _id: number
  ) {}
}
// Equivale a declarar propiedades + asignar en constructor
```

## Modificadores de Acceso

```typescript
class Ejemplo {
  public visible: string;          // accesible desde cualquier lugar
  protected heredable: string;     // clase + subclases
  private interno: string;         // solo esta clase
  readonly fijo: string;           // no se puede reasignar
}
```

## Herencia

```typescript
class Animal {
  constructor(public nombre: string) {}
  mover(): string { return `${this.nombre} se mueve`; }
}

class Perro extends Animal {
  ladrar(): string { return "Guau!"; }
  // hereda: nombre, mover()
}
```

## Clase Abstracta

```typescript
abstract class Forma {
  abstract area(): number;           // sin implementacion
  describir(): string {              // con implementacion
    return `Area: ${this.area()}`;
  }
}

class Circulo extends Forma {
  constructor(public radio: number) { super(); }
  area(): number { return Math.PI * this.radio ** 2; }
}
```

## Implements

```typescript
interface Serializable { toJSON(): string; }
interface Validable { esValido(): boolean; }

class Usuario implements Serializable, Validable {
  constructor(public nombre: string, public email: string) {}
  toJSON(): string { return JSON.stringify(this); }
  esValido(): boolean { return this.email.includes("@"); }
}
```

## Miembros Estaticos

```typescript
class MathUtil {
  static PI = 3.14159;
  static cuadrado(n: number): number { return n * n; }
}

MathUtil.PI;           // 3.14159
MathUtil.cuadrado(5);  // 25
```

## Getters y Setters

```typescript
class Cuenta {
  private _saldo: number = 0;

  get saldo(): number { return this._saldo; }

  set saldo(valor: number) {
    if (valor < 0) throw new Error("Saldo negativo");
    this._saldo = valor;
  }
}
```

## Override de Metodos

```typescript
class Animal {
  hablar(): string { return "..."; }
}

class Gato extends Animal {
  override hablar(): string { return "Miau"; }
}
```

## Clase Generica

```typescript
class Caja<T> {
  private items: T[] = [];
  agregar(item: T): void { this.items.push(item); }
  obtener(i: number): T { return this.items[i]; }
}

const cajaStr = new Caja<string>();
const cajaNum = new Caja<number>();
```

## Tabla Rapida

```
┌──────────────────┬──────────────────────────────────┐
│ Concepto         │ Sintaxis                         │
├──────────────────┼──────────────────────────────────┤
│ Clase            │ class X { }                      │
│ Herencia         │ class Y extends X { }            │
│ Abstracta        │ abstract class X { }             │
│ Implementar      │ class X implements I { }         │
│ Estatico         │ static metodo(): T { }           │
│ Getter           │ get prop(): T { }                │
│ Setter           │ set prop(v: T) { }               │
│ Readonly         │ readonly prop: T                 │
│ Override         │ override metodo(): T { }         │
│ Super            │ super() / super.metodo()         │
└──────────────────┴──────────────────────────────────┘
```
