<?php
/**
 * ==========================================================================
 * MODULO 17 - PROYECTO DE EVALUACION: Modelo Customer (Cliente)
 * ==========================================================================
 *
 * PROPOSITO DE ESTE ARCHIVO:
 * El modelo Customer es la representacion en PHP de la tabla "customers"
 * en la base de datos. Es parte del patron ELOQUENT ORM de Laravel.
 *
 * QUE ES UN ORM (Object-Relational Mapping)?
 * Es una tecnica que permite interactuar con la base de datos usando
 * OBJETOS DE PHP en lugar de escribir SQL directamente:
 *
 *   SQL puro:     SELECT * FROM customers WHERE id = 5;
 *   Eloquent:     Customer::find(5);
 *
 *   SQL puro:     INSERT INTO customers (name, email) VALUES ('Ana', 'ana@mail.com');
 *   Eloquent:     Customer::create(['name' => 'Ana', 'email' => 'ana@mail.com']);
 *
 *   SQL puro:     UPDATE customers SET name = 'Ana M.' WHERE id = 5;
 *   Eloquent:     $customer->update(['name' => 'Ana M.']);
 *
 *   SQL puro:     DELETE FROM customers WHERE id = 5;
 *   Eloquent:     $customer->delete();
 *
 * CONVENCION DE NOMBRES EN LARAVEL:
 *   Modelo:     Customer (singular, PascalCase)
 *   Tabla:      customers (plural, snake_case)
 *   Migracion:  create_customers_table
 *   Factory:    CustomerFactory
 *   Seeder:     CustomerSeeder (o dentro de DatabaseSeeder)
 *
 * Laravel infiere automaticamente que el modelo Customer usa la tabla
 * "customers" (convierte a snake_case y pluraliza). Si la tabla tuviera
 * otro nombre, se especifica con $table (como se hace aqui).
 *
 * CRITERIO DE EVALUACION: Modelo bien configurado
 * - Tener $fillable definido correctamente (seguridad)
 * - Usar HasFactory para habilitar factories de testing
 * - Seguir las convenciones de nombres de Laravel
 */

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

/**
 * Modelo Eloquent para la tabla "customers".
 *
 * HERENCIA: Customer extends Model
 * Al heredar de Model, Customer obtiene automaticamente:
 * - find(), all(), create(), update(), delete()
 * - Relaciones (hasMany, belongsTo, etc.)
 * - Scopes, mutators, accessors
 * - Eventos del modelo (creating, created, updating, etc.)
 * - Conversion a JSON/Array
 * - Paginacion
 * - Y mucho mas...
 *
 * METODOS ELOQUENT MAS USADOS:
 *   Customer::all()              -> Obtener todos los registros
 *   Customer::find(5)            -> Buscar por ID (devuelve null si no existe)
 *   Customer::findOrFail(5)      -> Buscar por ID (lanza 404 si no existe)
 *   Customer::where('name', 'Ana')->get()  -> Buscar con condiciones
 *   Customer::create([...])      -> Crear nuevo registro
 *   $customer->update([...])     -> Actualizar registro existente
 *   $customer->delete()          -> Eliminar registro
 *   Customer::count()            -> Contar registros
 *   Customer::paginate(15)       -> Obtener con paginacion
 */
class Customer extends Model
{
    /**
     * Trait HasFactory: Habilita el uso de factories para testing.
     *
     * FACTORIES son generadores de datos falsos para pruebas.
     * Con este trait, puedes hacer:
     *   Customer::factory()->create()        -> Crea 1 cliente con datos falsos
     *   Customer::factory(10)->create()      -> Crea 10 clientes
     *   Customer::factory()->make()          -> Crea instancia SIN guardar en BD
     *
     * Es ESENCIAL para testing automatizado y para poblar la BD de desarrollo.
     * Ver: database/factories/CustomerFactory.php
     */
    use HasFactory;

    /**
     * Nombre explicito de la tabla en la base de datos.
     *
     * NOTA: En este caso es redundante porque Laravel infiere "customers"
     * a partir del nombre del modelo "Customer" (singularizar + snake_case).
     * Pero es una buena practica ser explicito cuando:
     * - La tabla tiene un nombre no convencional (ej: "clientes")
     * - Quieres que sea obvio para otros desarrolladores
     */
    protected $table= 'customers';

    /**
     * MASS ASSIGNMENT PROTECTION ($fillable).
     *
     * CONCEPTO DE SEGURIDAD MUY IMPORTANTE:
     * $fillable define que campos se pueden llenar "masivamente" con create() o update().
     *
     * SIN $fillable, un atacante podria enviar campos extra:
     *   POST /customers -> {name: "Ana", email: "...", is_admin: true}
     *   Customer::create($request->all())  // Peligro! Crearia un admin!
     *
     * CON $fillable, solo se permiten los campos listados:
     *   Customer::create($request->all())  // is_admin se IGNORA
     *
     * ALTERNATIVA: $guarded (campos que NO se pueden llenar masivamente)
     *   protected $guarded = ['id', 'is_admin'];  // Todo excepto estos
     *
     * CRITERIO DE EVALUACION: Seguridad del modelo
     * - SIEMPRE definir $fillable o $guarded (nunca dejar sin proteccion)
     * - Solo incluir campos que el usuario DEBE poder modificar
     */
    protected $fillable=[
        'name',
        'email',
        'phone',
        'address',
        'birthday',
    ];
}
