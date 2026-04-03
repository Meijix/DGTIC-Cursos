// ============================================================================
// 04 — CLASES Y PROGRAMACION ORIENTADA A OBJETOS
// ============================================================================
// Compilar: tsc ejemplos.ts
// Ejecutar: node ejemplos.js
// ============================================================================


// ----------------------------------------------------------------------------
// 1. CLASE BASICA CON SHORTHAND CONSTRUCTOR
// ----------------------------------------------------------------------------

class Persona {
  constructor(
    public nombre: string,
    public edad: number,
    private _email: string
  ) {}

  presentarse(): string {
    return `Soy ${this.nombre}, tengo ${this.edad} anios`;
  }

  get email(): string {
    return this._email;
  }

  set email(nuevoEmail: string) {
    if (!nuevoEmail.includes("@")) {
      throw new Error("Email invalido");
    }
    this._email = nuevoEmail;
  }
}

const ana = new Persona("Ana", 28, "ana@ejemplo.com");

console.log("=== Clase Basica ===");
console.log(ana.presentarse());
console.log(`Email: ${ana.email}`);


// ----------------------------------------------------------------------------
// 2. MODIFICADORES DE ACCESO
// ----------------------------------------------------------------------------

class CuentaBancaria {
  public titular: string;
  private _saldo: number;
  protected _numeroCuenta: string;
  readonly fechaCreacion: Date;

  constructor(titular: string, saldoInicial: number) {
    this.titular = titular;
    this._saldo = saldoInicial;
    this._numeroCuenta = this.generarNumeroCuenta();
    this.fechaCreacion = new Date();
  }

  // Metodo publico
  public depositar(monto: number): void {
    if (monto <= 0) throw new Error("Monto debe ser positivo");
    this._saldo += monto;
    console.log(`  Deposito de $${monto}. Nuevo saldo: $${this._saldo}`);
  }

  public retirar(monto: number): void {
    if (monto > this._saldo) throw new Error("Fondos insuficientes");
    this._saldo -= monto;
    console.log(`  Retiro de $${monto}. Nuevo saldo: $${this._saldo}`);
  }

  get saldo(): number {
    return this._saldo;
  }

  // Metodo privado — solo accesible dentro de esta clase
  private generarNumeroCuenta(): string {
    return `CTA-${Math.random().toString(36).substring(2, 10).toUpperCase()}`;
  }
}

console.log("\n=== Modificadores de Acceso ===");
const cuenta = new CuentaBancaria("Carlos", 1000);
cuenta.depositar(500);
cuenta.retirar(200);
console.log(`  Saldo final: $${cuenta.saldo}`);
// cuenta._saldo;  // ERROR: Property '_saldo' is private


// ----------------------------------------------------------------------------
// 3. HERENCIA
// ----------------------------------------------------------------------------

class Animal {
  constructor(
    public nombre: string,
    protected especie: string
  ) {}

  mover(distancia: number): string {
    return `${this.nombre} (${this.especie}) se movio ${distancia}m`;
  }

  describir(): string {
    return `${this.nombre} es un(a) ${this.especie}`;
  }
}

class Perro extends Animal {
  constructor(nombre: string, public raza: string) {
    super(nombre, "Canino");  // llama al constructor padre
  }

  ladrar(): string {
    return `${this.nombre} dice: Guau! Guau!`;
  }

  // Override — sobreescribe el metodo padre
  override mover(distancia: number): string {
    return `${this.nombre} corrio ${distancia}m (raza: ${this.raza})`;
  }
}

class Pez extends Animal {
  constructor(nombre: string, public aguaDulce: boolean) {
    super(nombre, "Pez");
  }

  override mover(distancia: number): string {
    const tipo = this.aguaDulce ? "agua dulce" : "agua salada";
    return `${this.nombre} nado ${distancia}m en ${tipo}`;
  }
}

console.log("\n=== Herencia ===");
const max = new Perro("Max", "Labrador");
console.log(max.describir());
console.log(max.ladrar());
console.log(max.mover(50));

const nemo = new Pez("Nemo", false);
console.log(nemo.describir());
console.log(nemo.mover(100));


// ----------------------------------------------------------------------------
// 4. CLASES ABSTRACTAS
// No se pueden instanciar, definen contratos para subclases
// ----------------------------------------------------------------------------

abstract class Forma {
  constructor(public color: string) {}

  abstract calcularArea(): number;
  abstract calcularPerimetro(): number;

  // Metodo concreto — disponible en todas las subclases
  describir(): string {
    return `Forma ${this.color}: area=${this.calcularArea().toFixed(2)}, ` +
           `perimetro=${this.calcularPerimetro().toFixed(2)}`;
  }
}

class Circulo extends Forma {
  constructor(color: string, public radio: number) {
    super(color);
  }

  calcularArea(): number {
    return Math.PI * this.radio ** 2;
  }

  calcularPerimetro(): number {
    return 2 * Math.PI * this.radio;
  }
}

class Rectangulo extends Forma {
  constructor(
    color: string,
    public ancho: number,
    public alto: number
  ) {
    super(color);
  }

  calcularArea(): number {
    return this.ancho * this.alto;
  }

  calcularPerimetro(): number {
    return 2 * (this.ancho + this.alto);
  }
}

// const f = new Forma("rojo");  // ERROR: no se puede instanciar abstracta

console.log("\n=== Clases Abstractas ===");
const formas: Forma[] = [
  new Circulo("rojo", 5),
  new Rectangulo("azul", 10, 4),
  new Circulo("verde", 3)
];

formas.forEach(f => console.log(f.describir()));


// ----------------------------------------------------------------------------
// 5. IMPLEMENTS — Interfaces como contrato
// ----------------------------------------------------------------------------

interface Serializable {
  serializar(): string;
}

interface Comparable<T> {
  compararCon(otro: T): number;
}

class Estudiante implements Serializable, Comparable<Estudiante> {
  constructor(
    public nombre: string,
    public promedio: number,
    public matricula: string
  ) {}

  serializar(): string {
    return JSON.stringify({
      nombre: this.nombre,
      promedio: this.promedio,
      matricula: this.matricula
    });
  }

  compararCon(otro: Estudiante): number {
    return this.promedio - otro.promedio;
  }
}

console.log("\n=== Implements ===");
const est1 = new Estudiante("Laura", 9.2, "A001");
const est2 = new Estudiante("Pedro", 8.7, "A002");

console.log(`Serializado: ${est1.serializar()}`);
const comparacion = est1.compararCon(est2);
console.log(`${est1.nombre} vs ${est2.nombre}: ${comparacion > 0 ? "mayor" : "menor"} promedio`);


// ----------------------------------------------------------------------------
// 6. MIEMBROS ESTATICOS
// Pertenecen a la clase, no a las instancias
// ----------------------------------------------------------------------------

class GeneradorId {
  private static _siguiente: number = 1;

  static generar(): string {
    return `ID-${(GeneradorId._siguiente++).toString().padStart(4, "0")}`;
  }

  static reiniciar(): void {
    GeneradorId._siguiente = 1;
  }

  static get siguiente(): number {
    return GeneradorId._siguiente;
  }
}

console.log("\n=== Estaticos ===");
console.log(GeneradorId.generar());  // ID-0001
console.log(GeneradorId.generar());  // ID-0002
console.log(GeneradorId.generar());  // ID-0003
console.log(`Siguiente sera: ${GeneradorId.siguiente}`);


// ----------------------------------------------------------------------------
// 7. CLASE GENERICA
// ----------------------------------------------------------------------------

class Coleccion<T> {
  private items: T[] = [];

  agregar(item: T): void {
    this.items.push(item);
  }

  obtener(indice: number): T | undefined {
    return this.items[indice];
  }

  buscar(predicado: (item: T) => boolean): T | undefined {
    return this.items.find(predicado);
  }

  filtrar(predicado: (item: T) => boolean): T[] {
    return this.items.filter(predicado);
  }

  get tamano(): number {
    return this.items.length;
  }

  listar(): T[] {
    return [...this.items];
  }
}

console.log("\n=== Clase Generica ===");

const nombres = new Coleccion<string>();
nombres.agregar("Ana");
nombres.agregar("Carlos");
nombres.agregar("Maria");
nombres.agregar("Andres");

console.log(`Total: ${nombres.tamano}`);
console.log(`Buscar 'Carlos': ${nombres.buscar(n => n === "Carlos")}`);
console.log(`Filtrar 'A*': ${nombres.filtrar(n => n.startsWith("A"))}`);


// ----------------------------------------------------------------------------
// 8. EJEMPLO INTEGRADOR: Sistema de empleados
// Combina herencia, abstract, implements, static, generics
// ----------------------------------------------------------------------------

interface Imprimible {
  imprimir(): string;
}

abstract class Empleado implements Imprimible {
  static totalEmpleados: number = 0;

  constructor(
    public readonly id: number,
    public nombre: string,
    protected salarioBase: number
  ) {
    Empleado.totalEmpleados++;
  }

  abstract calcularSalario(): number;

  imprimir(): string {
    return `[${this.id}] ${this.nombre} — Salario: $${this.calcularSalario().toFixed(2)}`;
  }
}

class EmpleadoTiempoCompleto extends Empleado {
  constructor(
    id: number,
    nombre: string,
    salarioBase: number,
    private bonificacion: number
  ) {
    super(id, nombre, salarioBase);
  }

  calcularSalario(): number {
    return this.salarioBase + this.bonificacion;
  }
}

class EmpleadoPorHoras extends Empleado {
  constructor(
    id: number,
    nombre: string,
    private tarifaHora: number,
    private horasTrabajadas: number
  ) {
    super(id, nombre, 0);
  }

  calcularSalario(): number {
    return this.tarifaHora * this.horasTrabajadas;
  }
}

console.log("\n=== Sistema de Empleados ===");

const empleados: Empleado[] = [
  new EmpleadoTiempoCompleto(1, "Laura Gomez", 30000, 5000),
  new EmpleadoTiempoCompleto(2, "Pedro Ruiz", 28000, 3000),
  new EmpleadoPorHoras(3, "Sofia Martinez", 250, 160),
  new EmpleadoPorHoras(4, "Diego Torres", 300, 120)
];

empleados.forEach(e => console.log(e.imprimir()));
console.log(`\nTotal empleados registrados: ${Empleado.totalEmpleados}`);
