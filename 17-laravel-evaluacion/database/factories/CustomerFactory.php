<?php
/**
 * ==========================================================================
 * MODULO 17 - PROYECTO DE EVALUACION: Factory de Customer
 * ==========================================================================
 *
 * PROPOSITO DE ESTE ARCHIVO:
 * Generar datos FALSOS (pero realistas) para la tabla "customers".
 * Los factories son ESENCIALES para testing y desarrollo.
 *
 * QUE ES UN FACTORY?
 * Es una "fabrica" de modelos con datos aleatorios.
 * En vez de crear clientes manualmente uno por uno, puedes hacer:
 *
 *   Customer::factory()->create();       // Crea 1 cliente falso en la BD
 *   Customer::factory(50)->create();     // Crea 50 clientes falsos en la BD
 *   Customer::factory()->make();         // Crea 1 instancia SIN guardar
 *   Customer::factory(10)->make();       // Crea 10 instancias SIN guardar
 *
 * CUANDO SE USAN LOS FACTORIES?
 * 1. En SEEDERS: Para poblar la BD de desarrollo con datos de prueba
 *    -> php artisan db:seed
 * 2. En TESTS: Para crear datos necesarios en cada prueba
 *    -> Customer::factory()->create() dentro de un test
 * 3. En TINKER: Para experimentar desde la consola
 *    -> php artisan tinker -> Customer::factory(5)->create()
 *
 * FAKER: GENERADOR DE DATOS FALSOS
 * Laravel incluye la libreria "Faker" que genera datos realistas:
 *   $this->faker->name()          -> "Ana Garcia Lopez"
 *   $this->faker->safeEmail()     -> "ana.garcia@example.com"
 *   $this->faker->phoneNumber()   -> "+52 55 1234 5678"
 *   $this->faker->address()       -> "Calle Reforma 123, CDMX"
 *   $this->faker->date()          -> "1990-05-15"
 *
 * Faker soporta LOCALIZACION:
 *   config/app.php -> 'faker_locale' => 'es_MX'
 *   Esto genera nombres, direcciones y telefonos mexicanos.
 *
 * CRITERIO DE EVALUACION: Testing
 * - Tener un factory demuestra preparacion para testing
 * - Los factories son requisito para pruebas automatizadas
 * - Permiten probar con volumenes grandes de datos
 */

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use App\Models\Customer;

/**
 * Factory para el modelo Customer.
 *
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Customer>
 *
 * CONVENCION DE NOMBRES:
 *   Modelo:  Customer
 *   Factory: CustomerFactory
 *   Laravel conecta automaticamente CustomerFactory con Customer
 *   gracias a la convencion de nombres + el trait HasFactory en el modelo.
 */
class CustomerFactory extends Factory
{
    /**
     * Define el estado por defecto del modelo.
     *
     * METODO definition():
     * Retorna un array asociativo donde:
     * - Las CLAVES son los nombres de las columnas de la tabla
     * - Los VALORES son datos generados por Faker
     *
     * $this->faker es una instancia de la libreria Faker,
     * disponible automaticamente en todos los factories de Laravel.
     *
     * METODOS FAKER MAS UTILES:
     *   ->name()              : Nombre completo (nombre + apellidos)
     *   ->firstName()         : Solo nombre
     *   ->lastName()          : Solo apellido
     *   ->safeEmail()         : Email que NO existe realmente (dominio example.com)
     *   ->unique()->safeEmail(): Email unico (no se repite entre registros)
     *   ->phoneNumber()       : Numero de telefono con formato local
     *   ->address()           : Direccion completa
     *   ->date()              : Fecha en formato Y-m-d (2024-01-15)
     *   ->dateTimeBetween('-30 years', '-18 years') : Fecha en rango
     *   ->numberBetween(1, 100) : Numero aleatorio
     *   ->sentence()          : Una oracion
     *   ->paragraph()         : Un parrafo
     *   ->imageUrl()          : URL de imagen placeholder
     *
     * unique(): Garantiza que los valores no se repitan.
     * Es OBLIGATORIO para campos con restriccion UNIQUE en la BD
     * (como email y phone en este caso).
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'name' => $this->faker->name(),
            'email' => $this->faker->unique()->safeEmail(),
            'phone' => $this->faker->phoneNumber(),
            'address' => $this->faker->address(),
            'birthday' => $this->faker->date(),// date format: Y-m-d
        ];
    }
}
