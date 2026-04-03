# Cheatsheet — PHP Orientado a Objetos (OOP)

## Clase basica

```php
class Carro {
    public $color;             // propiedad
    public $marca;

    public function arrancar() {   // metodo
        echo "El carro $this->marca arranca";
    }
}

$c = new Carro();              // instanciar objeto
$c->color = "rojo";            // asignar propiedad
$c->arrancar();                // llamar metodo
```

## Constructor y destructor

```php
class Usuario {
    private $nombre;
    private $email;

    public function __construct($nombre, $email) {
        $this->nombre = $nombre;   // se ejecuta al hacer new
        $this->email = $email;
    }

    public function __destruct() {
        // se ejecuta al destruir el objeto o al terminar el script
    }
}

$u = new Usuario("Ana", "ana@mail.com");
```

## Visibilidad (modificadores de acceso)

```
+-------------+----------------+----------------+-----------------+
| Modificador | Misma clase    | Clase hija     | Codigo externo  |
+-------------+----------------+----------------+-----------------+
| public      |      SI        |      SI        |      SI         |
| protected   |      SI        |      SI        |      NO         |
| private     |      SI        |      NO        |      NO         |
+-------------+----------------+----------------+-----------------+
```

```php
class Ejemplo {
    public $a;           // accesible desde cualquier lugar
    protected $b;        // accesible en la clase y sus hijas
    private $c;          // accesible SOLO dentro de esta clase
}
```

## Getters y setters (encapsulamiento)

```php
class CuentaBancaria {
    private $saldo = 0;

    public function getSaldo() {
        return $this->saldo;
    }

    public function depositar($monto) {
        if ($monto > 0) {
            $this->saldo += $monto;
        }
    }
}
```

## Herencia (extends)

```php
class Vehiculo {                          // clase padre
    protected $marca;
    public function __construct($marca) {
        $this->marca = $marca;
    }
    public function ficha() {
        return "Marca: $this->marca";
    }
}

class Auto extends Vehiculo {             // clase hija
    private $puertas;
    public function __construct($marca, $puertas) {
        parent::__construct($marca);      // llamar al padre
        $this->puertas = $puertas;
    }
    public function fichaCompleta() {
        return parent::ficha() . ", Puertas: $this->puertas";
    }
}
```

## $this vs self vs parent vs static

| Palabra clave | Se refiere a...                  | Accede a...                      |
|---------------|----------------------------------|----------------------------------|
| `$this`       | El objeto actual (instancia)     | `$this->propiedad`, `$this->metodo()` |
| `self`        | La clase actual                  | `self::$estatica`, `self::CONSTANTE`  |
| `parent`      | La clase padre                   | `parent::__construct()`, `parent::metodo()` |
| `static`      | La clase que llamo al metodo     | Late static binding              |

## Propiedades y metodos estaticos

```php
class Contador {
    public static $total = 0;
    const PI = 3.14159;

    public static function incrementar() {
        self::$total++;            // self:: para acceder a static
    }
}

Contador::incrementar();           // llamar sin crear objeto
echo Contador::$total;             // 1
echo Contador::PI;                 // 3.14159
```

## Clases abstractas

```php
abstract class Figura {
    abstract public function area();        // obligatorio implementar en hijas

    public function descripcion() {         // metodo normal (se hereda)
        return "Soy una figura";
    }
}

class Circulo extends Figura {
    private $radio;
    public function __construct($r) { $this->radio = $r; }

    public function area() {                // implementacion obligatoria
        return 3.14159 * $this->radio ** 2;
    }
}
// new Figura(); // ERROR: no se puede instanciar una clase abstracta
```

## Interfaces

```php
interface Imprimible {
    public function imprimir();             // solo firma, sin implementacion
}
interface Exportable {
    public function exportarPDF();
}

class Reporte implements Imprimible, Exportable {
    public function imprimir() { /* ... */ }
    public function exportarPDF() { /* ... */ }
}
```

## Referencia rapida: abstract vs interface

| Caracteristica                  | abstract class       | interface              |
|---------------------------------|----------------------|------------------------|
| Metodos implementados           | SI                   | NO (solo firmas)       |
| Propiedades                     | SI                   | NO (solo constantes)   |
| Herencia multiple               | NO (1 padre)         | SI (varias interfaces) |
| Palabra clave de uso            | `extends`            | `implements`           |
| Concepto                        | "es un" (relacion)   | "puede hacer" (contrato) |

## Type hints (sugerencias de tipo)

```php
function sumar(int $a, int $b): int {
    return $a + $b;
}

class Servicio {
    public function procesar(Usuario $user): string {
        return $user->getNombre();
    }
}
```

## Namespaces

```php
// Archivo: App/Models/Usuario.php
namespace App\Models;

class Usuario { /* ... */ }

// En otro archivo:
use App\Models\Usuario;
$u = new Usuario();
```

## Errores comunes

| Error                                      | Causa                                          | Solucion                             |
|--------------------------------------------|------------------------------------------------|--------------------------------------|
| `Undefined variable` dentro de metodo      | Usar `$nombre` en vez de `$this->nombre`       | Siempre usar `$this->` para propiedades |
| `Cannot access private property`           | Acceder a `private` desde fuera de la clase    | Crear getter/setter publico          |
| Propiedades del padre quedan en null       | Olvidar `parent::__construct()` en la hija     | Siempre llamar al constructor padre  |
| `Carro->color = "rojo"`                   | Confundir clase con objeto                     | Primero: `$c = new Carro();` luego `$c->color` |
| `Cannot instantiate abstract class`        | Intentar `new` de clase abstracta              | Instanciar la clase hija concreta    |
| Error al usar `self::` en metodo normal    | No hay `$this` en metodos estaticos            | Usar `$this->` en metodos normales, `self::` en estaticos |
