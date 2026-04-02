<?php
/**
 * ==========================================================================
 * MODULO 17 - PROYECTO DE EVALUACION: Migracion de la Tabla "customers"
 * ==========================================================================
 *
 * PROPOSITO DE ESTE ARCHIVO:
 * Definir la ESTRUCTURA de la tabla "customers" en la base de datos.
 * Las migraciones son como "control de versiones" para la base de datos.
 *
 * QUE ES UNA MIGRACION?
 * Es un archivo PHP que describe cambios en la estructura de la BD:
 * - Crear tablas
 * - Agregar/eliminar columnas
 * - Crear indices
 * - Modificar tipos de datos
 *
 * POR QUE USAR MIGRACIONES EN VEZ DE SQL DIRECTO?
 * 1. Version controlable: Las migraciones van en Git (el SQL no)
 * 2. Reversibles: Cada migracion tiene up() y down() (crear y destruir)
 * 3. Portables: Funcionan con MySQL, PostgreSQL, SQLite, SQL Server
 * 4. Colaborativas: Todos los desarrolladores aplican los mismos cambios
 * 5. Automatizables: Un comando aplica todas las migraciones pendientes
 *
 * COMANDOS DE MIGRACION:
 *   php artisan migrate              -> Ejecutar migraciones pendientes
 *   php artisan migrate:rollback     -> Revertir la ultima migracion
 *   php artisan migrate:fresh        -> Borrar TODO y volver a migrar
 *   php artisan migrate:status       -> Ver estado de las migraciones
 *   php artisan make:migration nombre -> Crear nueva migracion
 *
 * NOMBRE DEL ARCHIVO:
 *   2024_02_27_105309_create_customers_table.php
 *   |    |  |  |      |
 *   Ano  Mes Dia Hora  Descripcion
 *
 * La fecha asegura que las migraciones se ejecuten en ORDEN CRONOLOGICO.
 * Esto es importante porque una tabla puede depender de otra.
 *
 * CRITERIO DE EVALUACION: Migracion correcta
 * - Tipos de datos apropiados para cada campo
 * - Restricciones unique donde corresponde
 * - timestamps() para auditoria
 * - down() correctamente definido (reversibilidad)
 */

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

/**
 * Clase anonima de migracion.
 *
 * "return new class extends Migration" es una CLASE ANONIMA de PHP 8+.
 * Antes se usaban clases con nombre, pero las clases anonimas evitan
 * conflictos de nombres cuando dos migraciones crean clases similares.
 */
return new class extends Migration
{
    /**
     * Metodo up(): Se ejecuta al correr "php artisan migrate".
     *
     * BLUEPRINT ($table): Es el "plano" de la tabla.
     * Cada metodo de $table agrega una columna:
     *
     *   $table->id()                 -> Columna 'id' autoincremental (BIGINT UNSIGNED)
     *   $table->string('name')       -> VARCHAR(255) por defecto
     *   $table->string('email')      -> VARCHAR(255)
     *   ->unique()                   -> Restriccion UNIQUE (no se repite)
     *   $table->dateTime('birthday') -> Columna tipo DATETIME
     *   $table->timestamps()         -> Crea 'created_at' y 'updated_at' automaticamente
     *
     * TIPOS DE COLUMNA MAS USADOS:
     *   ->id()              : ID autoincremental
     *   ->string('col')     : Texto corto (VARCHAR, hasta 255)
     *   ->text('col')       : Texto largo (TEXT)
     *   ->integer('col')    : Numero entero
     *   ->decimal('col',8,2): Numero decimal (ej: precio)
     *   ->boolean('col')    : Verdadero/Falso
     *   ->date('col')       : Solo fecha (YYYY-MM-DD)
     *   ->dateTime('col')   : Fecha y hora
     *   ->json('col')       : Datos JSON
     *   ->timestamps()      : created_at + updated_at
     *
     * RESTRICCION unique():
     * email y phone tienen ->unique() porque:
     * - No deberian existir dos clientes con el mismo email
     * - No deberian existir dos clientes con el mismo telefono
     * - La BD RECHAZA inserciones que violen esta restriccion
     * - Es una segunda capa de validacion (la primera esta en PHP)
     */
    public function up(): void
    {
        Schema::create('customers', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('email')->unique();
            $table->string('phone')->unique();
            $table->string('address');
            $table->dateTime('birthday');
            $table->timestamps();
        });
    }

    /**
     * Metodo down(): Se ejecuta al correr "php artisan migrate:rollback".
     *
     * DEBE ser el INVERSO de up():
     * - Si up() crea una tabla, down() la elimina
     * - Si up() agrega una columna, down() la remueve
     *
     * dropIfExists() en vez de drop():
     * - drop() lanza error si la tabla no existe
     * - dropIfExists() no hace nada si la tabla no existe (mas seguro)
     *
     * CRITERIO DE EVALUACION: Reversibilidad
     * - Siempre implementar down() correctamente
     * - Permite revertir cambios sin problemas
     */
    public function down(): void
    {
        Schema::dropIfExists('customers');
    }
};
