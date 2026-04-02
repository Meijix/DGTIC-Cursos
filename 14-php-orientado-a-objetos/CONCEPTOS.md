# Modulo 14: PHP Orientado a Objetos (OOP)

## Tabla de Contenidos
1. [Que es la Programacion Orientada a Objetos](#1-que-es-la-programacion-orientada-a-objetos)
2. [Los 4 pilares de OOP](#2-los-4-pilares-de-oop)
3. [Clases y objetos](#3-clases-y-objetos)
4. [Propiedades y metodos](#4-propiedades-y-metodos)
5. [Modificadores de acceso](#5-modificadores-de-acceso-publicprivateprotected)
6. [Constructores y destructores](#6-constructores-y-destructores)
7. [Herencia](#7-herencia)
8. [$this vs self vs static](#8-this-vs-self-vs-static)
9. [Clases abstractas e interfaces](#9-clases-abstractas-e-interfaces-proximos-pasos)
10. [Errores comunes en OOP](#10-errores-comunes-en-oop)
11. [Ejercicios de practica](#11-ejercicios-de-practica)

---

## 1. Que es la Programacion Orientada a Objetos

La Programacion Orientada a Objetos (OOP) es un **paradigma de programacion** que organiza el codigo alrededor de **objetos** en vez de funciones y procedimientos.

### Por que existe OOP

Imagina que programas un sistema para una escuela. Sin OOP:

```php
// Sin OOP: variables sueltas, dificil de mantener
$alumno1_nombre = "Ana";
$alumno1_edad = 20;
$alumno1_carrera = "Ingenieria";

$alumno2_nombre = "Luis";
$alumno2_edad = 22;
$alumno2_carrera = "Medicina";

// Con 100 alumnos, tendrias 300 variables...
```

Con OOP:

```php
// Con OOP: organizado, reutilizable, escalable
class Alumno {
    public $nombre;
    public $edad;
    public $carrera;
}

$alumno1 = new Alumno();
$alumno1->nombre = "Ana";

$alumno2 = new Alumno();
$alumno2->nombre = "Luis";

// Con 100 alumnos: 100 objetos, 1 sola clase
```

### Beneficios de OOP

| Beneficio          | Descripcion                                           |
|-------------------|-------------------------------------------------------|
| Organizacion       | El codigo se agrupa logicamente en clases             |
| Reutilizacion     | Una clase se puede usar muchas veces (herencia)        |
| Mantenimiento     | Cambiar una clase afecta a todos sus objetos           |
| Escalabilidad     | Facil agregar nuevas funcionalidades                   |
| Modelado          | Representa objetos del mundo real en codigo            |

---

## 2. Los 4 pilares de OOP

```
         LOS 4 PILARES DE LA PROGRAMACION ORIENTADA A OBJETOS
    +----------------------------------------------------------+
    |                                                          |
    |   ENCAPSULAMIENTO    ABSTRACCION    HERENCIA    POLIMORFISMO
    |         |                |             |             |
    |    Proteger datos   Ocultar        Reutilizar    Misma interfaz,
    |    con private/     complejidad    codigo         diferente
    |    protected                        padre->hijo   comportamiento
    |         |                |             |             |
    |    Ej: $placas      Ej: usar      Ej: carro     Ej: cada transporte
    |    es private,      mostrar()     extends        tiene su propio
    |    se accede via    sin saber     transporte     resumen()
    |    metodos          como funciona                 |
    |                     internamente                  |
    +----------------------------------------------------------+
```

### 1. Encapsulamiento (Ejercicios 3-4)
Ocultar los datos internos y proporcionar metodos controlados para acceder a ellos.

```php
class CuentaBancaria {
    private $saldo = 0;  // No accesible desde fuera

    public function depositar($monto) {
        if ($monto > 0) {  // Validacion!
            $this->saldo += $monto;
        }
    }

    public function getSaldo() {
        return $this->saldo;
    }
}
```

### 2. Abstraccion
Mostrar solo lo esencial y ocultar la complejidad interna.

```php
// El usuario solo necesita saber QUE hace, no COMO lo hace
$cuenta->depositar(1000);  // Simple de usar
// Internamente podria validar, registrar log, enviar notificacion...
```

### 3. Herencia (Ejercicios 6-7)
Crear clases nuevas basadas en clases existentes.

```php
class Animal {
    public function respirar() { echo "Respirando..."; }
}

class Perro extends Animal {
    public function ladrar() { echo "Guau!"; }
}

$perro = new Perro();
$perro->respirar();  // Heredado de Animal
$perro->ladrar();    // Propio de Perro
```

### 4. Polimorfismo (Ejercicio 6)
Objetos diferentes responden al mismo mensaje de manera diferente.

```php
// Cada transporte genera su resumen de forma diferente
// pero todos siguen la misma estructura
$carro->resumenCarro();         // Muestra puertas
$avion->resumenAvion();         // Muestra turbinas
$barco->resumenBarco();         // Muestra calado
```

---

## 3. Clases y objetos

### La analogia del plano y la casa

```
    CLASE (Plano)                    OBJETOS (Casas construidas)
    =============                    ==========================

    +------------------+             +------------------+
    | Casa             |             | casa1            |
    |------------------|    new      |------------------|
    | $color           | ---------> | $color = "azul"  |
    | $pisos           |             | $pisos = 2       |
    | $direccion       |             | $direccion = "..." |
    |------------------|             +------------------+
    | pintar()         |
    | vender()         |    new      +------------------+
    +------------------+ ---------> | casa2            |
                                     |------------------|
                                     | $color = "rojo"  |
                                     | $pisos = 1       |
                                     | $direccion = "..." |
                                     +------------------+

    UNA clase puede generar          Cada objeto tiene sus
    MULTIPLES objetos                PROPIOS valores
```

### Definicion de una clase

```php
<?php
// La palabra clave 'class' define una nueva clase
// Por convencion, los nombres de clase empiezan con MAYUSCULA
class Carro {
    // PROPIEDADES (atributos): datos que describe al objeto
    public $color;
    public $marca;
    public $modelo;

    // METODOS: acciones que el objeto puede realizar
    public function arrancar() {
        echo "El carro $this->marca esta arrancando";
    }
}
?>
```

### Crear objetos (instanciar)

```php
<?php
// 'new' crea un objeto a partir de la clase (instanciacion)
$miCarro = new Carro();

// Asignar valores a las propiedades con ->
$miCarro->color = "rojo";
$miCarro->marca = "Toyota";

// Llamar metodos con ->
$miCarro->arrancar();  // "El carro Toyota esta arrancando"

// Crear OTRO objeto de la misma clase
$otroCarro = new Carro();
$otroCarro->color = "azul";  // Cada objeto tiene sus propios valores
?>
```

---

## 4. Propiedades y metodos

### Propiedades (que TIENE el objeto)

```php
class Persona {
    public $nombre;          // Sin valor inicial
    public $edad = 0;        // Con valor por defecto
    private $contrasena;     // Privada (solo accesible dentro de la clase)
    protected $rol = "user"; // Protegida (accesible en la clase y sus hijas)
}
```

### Metodos (que HACE el objeto)

```php
class Calculadora {
    private $resultado = 0;

    // Metodo que recibe parametros
    public function sumar($a, $b) {
        $this->resultado = $a + $b;
        return $this->resultado;  // Retorna un valor
    }

    // Metodo que usa propiedades del objeto
    public function mostrar() {
        echo "Resultado: " . $this->resultado;
    }
}

$calc = new Calculadora();
$calc->sumar(5, 3);    // $resultado = 8
$calc->mostrar();       // "Resultado: 8"
```

### $this - Referencia al objeto actual

```php
class Ejemplo {
    public $valor = 10;

    public function mostrar() {
        // $this se refiere al objeto que esta ejecutando el metodo
        echo $this->valor;

        // Sin $this, PHP busca una variable LOCAL (no la propiedad)
        // echo $valor;  // ERROR: variable local $valor no definida
    }
}

$obj1 = new Ejemplo();
$obj1->valor = 20;
$obj1->mostrar();  // 20 (porque $this = $obj1 en este caso)

$obj2 = new Ejemplo();
$obj2->mostrar();  // 10 (porque $this = $obj2, que tiene el valor por defecto)
```

---

## 5. Modificadores de acceso: public/private/protected

### Tabla de visibilidad

```
+-------------+-----------------+-----------------+-----------------+
| Modificador | Dentro de la    | En clases       | Desde codigo    |
|             | misma clase     | hijas (extends) | externo         |
+-------------+-----------------+-----------------+-----------------+
| public      |       SI        |       SI        |       SI        |
| protected   |       SI        |       SI        |       NO        |
| private     |       SI        |       NO        |       NO        |
+-------------+-----------------+-----------------+-----------------+
```

### Diagrama visual

```
    CLASE PADRE                    CLASE HIJA                CODIGO EXTERNO
    ===========                    ==========                ==============

    public $a ------acceso SI-----> $this->a ---acceso SI---> $obj->a
    protected $b ---acceso SI-----> $this->b ---acceso NO---> $obj->b (ERROR!)
    private $c -----acceso SI-----> $this->c (ERROR!) -------> $obj->c (ERROR!)
```

### Analogia del mundo real

```
    ANALOGIA: UNA EMPRESA
    ======================

    public:     La recepcion (cualquiera puede entrar)
    protected:  Las oficinas (solo empleados y sus equipos)
    private:    La caja fuerte (solo el gerente)

    class Empresa {
        public $nombre;           // Todos pueden verlo
        protected $empleados;     // Solo la empresa y filiales
        private $cuentaBancaria;  // Solo esta empresa
    }
```

### Ejemplo completo

```php
<?php
class Animal {
    public $nombre;           // Accesible desde cualquier lugar
    protected $tipo;          // Accesible en Animal y clases hijas
    private $id_interno;      // SOLO accesible en Animal

    public function setId($id) {
        $this->id_interno = $id;  // OK: estamos DENTRO de Animal
    }
}

class Perro extends Animal {
    public function mostrar() {
        echo $this->nombre;        // OK: es public
        echo $this->tipo;          // OK: es protected (somos clase hija)
        // echo $this->id_interno; // ERROR: es private de Animal
    }
}

$perro = new Perro();
$perro->nombre = "Rex";          // OK: es public
// $perro->tipo = "mamifero";    // ERROR: es protected
// $perro->id_interno = 1;       // ERROR: es private
?>
```

---

## 6. Constructores y destructores

### Constructor: __construct()

El constructor se ejecuta **automaticamente** al crear un objeto con `new`.

```php
<?php
class Usuario {
    private $nombre;
    private $email;

    // __construct() se ejecuta al hacer: new Usuario("Ana", "ana@email.com")
    public function __construct($nombre, $email) {
        $this->nombre = $nombre;
        $this->email = $email;
        echo "Usuario $nombre creado!";
    }
}

// Al ejecutar new, el constructor se llama automaticamente:
$user = new Usuario("Ana", "ana@email.com");
// Salida: "Usuario Ana creado!"

// SIN constructor, tendriamos que hacer:
// $user = new Usuario();
// $user->nombre = "Ana";   // Y esto requeriria que sean public
// $user->email = "ana@email.com";
?>
```

### Destructor: __destruct()

El destructor se ejecuta **automaticamente** cuando el objeto se destruye.

```php
<?php
class ConexionDB {
    private $conexion;

    public function __construct($servidor) {
        $this->conexion = "Conectado a $servidor";
        echo "Conexion abierta\n";
    }

    public function __destruct() {
        // Liberar recursos al destruir el objeto
        $this->conexion = null;
        echo "Conexion cerrada\n";
    }
}

$db = new ConexionDB("localhost");   // "Conexion abierta"
// ... usar la conexion ...
// Al terminar el script:              "Conexion cerrada" (automatico)
?>
```

### Ciclo de vida de un objeto

```
    new Clase()          Uso del objeto           Fin del script
        |                     |                        |
        v                     v                        v
    __construct()     $obj->metodo()              __destruct()
    Se inicializan    Se usan propiedades         Se liberan
    propiedades       y metodos                   recursos
        |                     |                        |
    NACIMIENTO            VIDA                     MUERTE
```

---

## 7. Herencia

### Herencia simple (Ejercicio 6)

```php
<?php
// CLASE PADRE (base/superclase)
class Vehiculo {
    protected $marca;
    protected $velocidad;

    public function __construct($marca, $velocidad) {
        $this->marca = $marca;
        $this->velocidad = $velocidad;
    }

    public function ficha() {
        return "Marca: $this->marca, Velocidad: $this->velocidad";
    }
}

// CLASE HIJA: hereda de Vehiculo con 'extends'
class Auto extends Vehiculo {
    private $puertas;

    public function __construct($marca, $velocidad, $puertas) {
        // parent:: llama al constructor del padre
        parent::__construct($marca, $velocidad);
        $this->puertas = $puertas;
    }

    public function fichaCompleta() {
        // parent::ficha() reutiliza el metodo del padre
        return parent::ficha() . ", Puertas: $this->puertas";
    }
}

$auto = new Auto("Toyota", 200, 4);
echo $auto->fichaCompleta();
// "Marca: Toyota, Velocidad: 200, Puertas: 4"
?>
```

### Herencia multinivel (Ejercicio 7)

```
    HERENCIA MULTINIVEL
    ===================

    Abuelo          Nivel 0 (clase base)
      |
      | extends
      v
    Padre           Nivel 1 (hereda de Abuelo)
      |
      | extends
      v
    Hijo            Nivel 2 (hereda de Padre Y de Abuelo)


    Lo que Hijo puede acceder:
    - Todo lo public/protected de Abuelo
    - Todo lo public/protected de Padre
    - Todo lo suyo propio
```

```php
<?php
class Abuelo {
    protected $apellido = "Martinez";
}

class Padre extends Abuelo {
    protected $nombre = "Jorge";

    public function nombreCompleto() {
        return $this->nombre . " " . $this->apellido;  // Accede a propiedad de Abuelo
    }
}

class Hijo extends Padre {
    private $nombre;

    public function __construct($nombre) {
        $this->nombre = $nombre;
    }

    public function presentar() {
        echo "Soy " . $this->nombre . " " . $this->apellido;  // Accede a Abuelo!
        echo "\nMi padre es " . parent::nombreCompleto();       // Accede a Padre!
    }
}

$hijo = new Hijo("Carlos");
$hijo->presentar();
// "Soy Carlos Martinez"
// "Mi padre es Jorge Martinez"
?>
```

### parent:: - Acceder a la clase padre

```php
// parent:: permite llamar metodos de la clase padre desde la hija

class Padre {
    public function saludar() {
        return "Hola desde Padre";
    }
}

class Hijo extends Padre {
    public function saludar() {
        // Llamamos al metodo del padre Y agregamos algo propio
        $saludo_padre = parent::saludar();
        return $saludo_padre . " y desde Hijo";
    }
}

$hijo = new Hijo();
echo $hijo->saludar();  // "Hola desde Padre y desde Hijo"
```

---

## 8. $this vs self vs static

| Palabra clave | Se refiere a...                          | Uso                        |
|--------------|------------------------------------------|----------------------------|
| `$this`      | El objeto ACTUAL (la instancia)          | Propiedades y metodos de instancia |
| `self`       | La clase ACTUAL (no la instancia)        | Constantes y metodos estaticos     |
| `static`     | La clase que LLAMO al metodo             | Late static binding                |
| `parent`     | La clase PADRE                           | Metodos heredados                  |

```php
<?php
class Ejemplo {
    public $valor = 10;           // Propiedad de instancia
    public static $contador = 0;   // Propiedad de CLASE (compartida)
    const PI = 3.14159;            // Constante de clase

    public function metodoInstancia() {
        echo $this->valor;        // $this-> para propiedades de instancia
    }

    public static function metodoEstatico() {
        echo self::$contador;     // self:: para propiedades de clase
        echo self::PI;            // self:: para constantes
        // echo $this->valor;     // ERROR: no hay $this en metodos estaticos
    }
}

// Uso:
$obj = new Ejemplo();
$obj->metodoInstancia();          // Necesita un objeto
Ejemplo::metodoEstatico();         // No necesita objeto (se llama con ::)
?>
```

---

## 9. Clases abstractas e interfaces (Proximos pasos)

### Clases abstractas

Una clase abstracta es una clase que **no puede ser instanciada directamente**. Sirve como plantilla para que otras clases hereden de ella.

```php
<?php
// No puedes hacer: new Figura();  (es abstracta)
abstract class Figura {
    // Metodo abstracto: OBLIGA a las clases hijas a implementarlo
    abstract public function area();

    // Metodo normal: las hijas lo heredan tal cual
    public function descripcion() {
        return "Soy una figura geometrica";
    }
}

class Circulo extends Figura {
    private $radio;

    public function __construct($radio) {
        $this->radio = $radio;
    }

    // OBLIGATORIO: implementar el metodo abstracto
    public function area() {
        return 3.14159 * $this->radio ** 2;
    }
}

class Rectangulo extends Figura {
    private $base, $altura;

    public function __construct($base, $altura) {
        $this->base = $base;
        $this->altura = $altura;
    }

    public function area() {
        return $this->base * $this->altura;
    }
}

$circulo = new Circulo(5);
echo $circulo->area();        // 78.53975
echo $circulo->descripcion(); // "Soy una figura geometrica"
?>
```

### Interfaces

Una interfaz define un **contrato**: que metodos DEBE tener una clase, sin implementarlos.

```php
<?php
// Una interfaz define QUE metodos debe tener, pero no COMO funcionan
interface Imprimible {
    public function imprimir();
}

interface Exportable {
    public function exportarPDF();
}

// Una clase puede implementar MULTIPLES interfaces (a diferencia de extends)
class Reporte implements Imprimible, Exportable {
    public function imprimir() {
        echo "Imprimiendo reporte...";
    }

    public function exportarPDF() {
        echo "Exportando a PDF...";
    }
}
?>
```

### Diferencia: abstract vs interface

| Caracteristica      | Clase abstracta            | Interface                      |
|--------------------|----------------------------|--------------------------------|
| Puede tener metodos implementados | SI              | NO (solo firmas)               |
| Puede tener propiedades           | SI              | NO (solo constantes)           |
| Herencia multiple                 | NO (solo 1 padre) | SI (multiples interfaces)    |
| Palabra clave                     | `extends`       | `implements`                   |
| Uso ideal          | Clases relacionadas (es-un) | Capacidades compartidas (puede-hacer) |

---

## 10. Errores comunes en OOP

### 1. Olvidar $this->

```php
class Ejemplo {
    public $nombre;

    public function saludar() {
        // INCORRECTO: $nombre es una variable LOCAL (no existe)
        echo "Hola " . $nombre;

        // CORRECTO: $this->nombre accede a la propiedad del objeto
        echo "Hola " . $this->nombre;
    }
}
```

### 2. Acceder a propiedad private desde fuera

```php
class Persona {
    private $edad;
}

$p = new Persona();
// $p->edad = 20;  // ERROR FATAL: Cannot access private property
// Solucion: usar un metodo setter
```

### 3. Olvidar parent::__construct()

```php
class Padre {
    protected $nombre;
    public function __construct($nombre) {
        $this->nombre = $nombre;
    }
}

class Hijo extends Padre {
    public function __construct($nombre, $extra) {
        // Si olvidas parent::__construct(), $this->nombre queda sin valor!
        parent::__construct($nombre);  // SIEMPRE llamar al padre
        // ... codigo propio
    }
}
```

### 4. Confundir clase con objeto

```php
// INCORRECTO: Carro es la clase, no un objeto
// Carro->color = "rojo";  // ERROR

// CORRECTO: crear un objeto primero
$carro = new Carro();
$carro->color = "rojo";
```

### 5. Olvidar el break en switch

```php
switch ($opcion) {
    case 'a':
        echo "Opcion A";
        // Sin break, PHP ejecuta TAMBIEN el case 'b'!
        break;  // SIEMPRE incluir break
    case 'b':
        echo "Opcion B";
        break;
}
```

---

## 11. Ejercicios de practica

### Ejercicio 1: Clase basica
Crea una clase `Libro` con propiedades publicas `$titulo`, `$autor` y `$paginas`. Crea un metodo `resumen()` que retorne un string con toda la informacion. Instancia 3 libros diferentes y muestra sus resumenes.

### Ejercicio 2: Encapsulamiento
Modifica la clase `Libro` para que todas las propiedades sean private. Crea getters y setters para cada una. En el setter de `$paginas`, valida que sea un numero positivo.

### Ejercicio 3: Constructor
Agrega un constructor a `Libro` que reciba titulo, autor y paginas. Crea los objetos pasando los datos al constructor en vez de asignarlos despues.

### Ejercicio 4: Herencia
Crea una clase padre `Empleado` con propiedades protected `$nombre`, `$departamento` y `$salario`. Crea las clases hijas `Gerente` (con propiedad `$equipo`) y `Programador` (con propiedad `$lenguaje`). Cada hija debe tener un metodo que muestre su ficha completa, reutilizando un metodo del padre.

### Ejercicio 5: Herencia multinivel
Crea una jerarquia de 3 niveles para un sistema de figuras geometricas:
- `Figura` (base): propiedad protected `$color`, metodo `descripcion()`
- `FiguraPlana` extends Figura: propiedad `$area`, metodo `calcularArea()` (abstracto)
- `Circulo` extends FiguraPlana: propiedad `$radio`, implementa `calcularArea()`

### Ejercicio 6: Sistema completo
Crea un mini sistema de inventario con:
- Clase `Producto` con propiedades private y getters/setters
- Clase `ProductoDigital` que extienda Producto y agregue `$formato`
- Clase `ProductoFisico` que extienda Producto y agregue `$peso`
- Un formulario HTML para agregar productos
- Una tabla HTML que muestre todos los productos (usando sesiones)

---

## Mapa de progresion de los ejercicios

```
    Ejercicio 1              Ejercicio 2              Ejercicio 3
    CLASES BASICAS           METODOS                  PRIVATE
    +-----------+            +-----------+             +-----------+
    | Carro     |            | Carro2    |             | Carro3    |
    |-----------|            |-----------|             |-----------|
    | +color    |            | +color    |             | -placas   |
    | +marca    |   ====>    | +modelo   |   ====>     |-----------|
    +-----------+            | +year     |             | +registrar|
    Solo datos               | -verificado|            | +mostrar  |
                             |-----------|             +-----------+
                             | +getVer() |             Encapsulamiento
                             | +setVer() |
                             | +verific()|
                             +-----------+
                             Datos + Comportamiento

    Ejercicio 4              Ejercicio 5
    ARRAYS                   CONSTRUCTOR/DESTRUCTOR
    +-----------+            +-----------+
    | Rfc       |            | token     |
    |-----------|            |-----------|
    | -datos[]  |            | -nombre   |
    |-----------|   ====>    | -token    |
    | +guardar()|            |-----------|
    | -construir|            | +__construct|
    +-----------+            | +mostrar()  |
    Datos complejos          | +__destruct |
                             +-----------+
                             Ciclo de vida

    Ejercicio 6                         Ejercicio 7
    HERENCIA                            PROTECTED + MULTINIVEL
    +-------------+                     +-----------+
    | transporte  |                     | Abuelo    |
    |-------------|                     |-----------|
    | -nombre     |                     | #nombreAb |
    | -velocidad  |                     | #apellido |
    | -combustible|                     |-----------|
    |-------------|                     | #ficha()  |
    | +crear_ficha|                     +-----------+
    +------+------+                          |
           |                                 v
    +------+------+------+             +-----------+
    |      |      |      |             | Padre     |
  carro  avion  barco  bici            |-----------|
    |      |      |      |             | #nombrePa |
  +puertas +turbinas +calado +modelo   +-----------+
                                             |
    Herencia simple                          v
    1 nivel                            +-----------+
                                       | Hijo      |
                                       |-----------|
                                       | #nombre   |
                                       +-----------+
                                       Herencia multinivel
                                       2 niveles

    Leyenda: + = public, - = private, # = protected
```

---

## Mapa de archivos del modulo

```
14-php-orientado-a-objetos/
|-- index.php                     -> Pagina principal con lista de ejercicios
|-- CONCEPTOS.md                  -> Este archivo
|-- Clases/
|   |-- ejercicio1/
|   |   |-- Carro.php             -> Clase basica con propiedades public
|   |   |-- Moto.php              -> Clase basica + formulario integrado
|   |   |-- vista.php             -> Include de ambas clases
|   |-- ejercicio2/
|   |   |-- Carro2.php            -> Metodos, constructor, getter/setter
|   |-- ejercicio3/
|   |   |-- Carro3.php            -> Propiedad private + metodos de acceso
|   |-- ejercicio4/
|   |   |-- Rfc.php               -> Atributo array + metodo private
|   |-- ejercicio5/
|   |   |-- token.php             -> Constructor + destructor + rand()
|   |   |-- archivo.php           -> Constructor + destructor + contrasena
|   |-- ejercicio6/
|   |   |-- transporte.php        -> Clase padre con propiedades comunes
|   |   |-- Carro4.php            -> Clase hija + switch + logica principal
|   |   |-- avion.php             -> Clase hija con numero_turbinas
|   |   |-- bicicleta.php         -> Clase hija con rodada y modelo
|   |   |-- barco.php             -> Clase hija con calado
|   |-- ejercicio7/
|       |-- Abuelo.php            -> Clase raiz con propiedades protected
|       |-- Padre.php             -> Clase intermedia (hereda de Abuelo)
|       |-- Hijo.php              -> Clase final (hereda de Padre y Abuelo)
|-- Vistas/
|   |-- vistaEjercicio1.php       -> Formulario color + clase inline
|   |-- vistaEjercicio2.php       -> Formulario + tabla de resultados
|   |-- vistaEjercicio3.php       -> Formulario de placas (encapsulamiento)
|   |-- vistaEjercicio4.php       -> Formulario RFC (4 campos)
|   |-- vistaEjercicio5.php       -> Formulario token (constructor/destructor)
|   |-- vistaEjercicio6.php       -> Select de transporte (herencia)
|   |-- vistaEjercicio7.php       -> Input nombre (herencia multinivel)
```
