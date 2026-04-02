<?php
/*
|==========================================================================
| Curso.php - Modelo Eloquent para la tabla 'cursos'
|==========================================================================
|
| ARQUITECTURA MVC - EL MODELO:
| Este archivo es el MODELO, la "M" del patron MVC.
| El modelo representa los datos de la aplicacion y la logica de negocio.
|
| QUE ES ELOQUENT ORM:
| - ORM = Object-Relational Mapping (Mapeo Objeto-Relacional)
| - Cada modelo de Eloquent corresponde a una tabla en la base de datos.
| - Cada instancia del modelo corresponde a una fila de esa tabla.
| - Cada propiedad del modelo corresponde a una columna.
|
| EJEMPLO DE MAPEO:
|   Modelo:  Curso          <-->  Tabla:    cursos
|   Objeto:  $curso         <-->  Fila:     registro con id=1
|   Prop:    $curso->nombre <-->  Columna:  nombre
|
| CONVENCIONES DE NOMBRES EN ELOQUENT:
| +-----------------------+----------------------------------------+
| | Modelo (singular)     | Tabla (plural, snake_case)             |
| +-----------------------+----------------------------------------+
| | Curso                 | cursos                                 |
| | User                  | users                                  |
| | CategoriaProducto     | categoria_productos                    |
| +-----------------------+----------------------------------------+
| Si tu tabla no sigue la convencion, usa $table para especificarla.
|
| GENERAR UN MODELO:
|   php artisan make:model Curso              -- solo el modelo
|   php artisan make:model Curso -m           -- modelo + migracion
|   php artisan make:model Curso -mcr         -- modelo + migracion + controlador resource
|
| OPERACIONES COMUNES DE ELOQUENT:
| +---------------------------------+------------------------------------------+
| | Eloquent                        | SQL equivalente                          |
| +---------------------------------+------------------------------------------+
| | Curso::all()                    | SELECT * FROM cursos                     |
| | Curso::find(1)                  | SELECT * FROM cursos WHERE id = 1        |
| | Curso::findOrFail(1)            | SELECT... (lanza 404 si no existe)       |
| | Curso::where('cupo','>',20)     | SELECT * FROM cursos WHERE cupo > 20     |
| | Curso::orderBy('nombre')->get() | SELECT * FROM cursos ORDER BY nombre     |
| | Curso::create([...])            | INSERT INTO cursos (...) VALUES (...)     |
| | $curso->save()                  | INSERT o UPDATE (detecta automaticamente)|
| | $curso->delete()                | DELETE FROM cursos WHERE id = ...         |
| | Curso::destroy(1)               | DELETE FROM cursos WHERE id = 1           |
| +---------------------------------+------------------------------------------+
|
*/

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

/*
|--------------------------------------------------------------------------
| Clase Curso
|--------------------------------------------------------------------------
| Modelo Eloquent que representa un curso en la aplicacion.
| Al extender Model, hereda todos los metodos de Eloquent para
| consultar, crear, actualizar y eliminar registros.
*/
class Curso extends Model
{
    /*
    |----------------------------------------------------------------------
    | $table - Nombre de la tabla en la base de datos
    |----------------------------------------------------------------------
    | Por convencion, Eloquent busca una tabla con el nombre plural
    | del modelo en snake_case. Como 'Curso' -> 'cursos', esta linea
    | es redundante aqui, pero es util cuando el nombre de la tabla
    | no sigue la convencion (ej: $table = 'mis_cursos_activos').
    */
    protected $table = 'cursos';

    /*
    |----------------------------------------------------------------------
    | $primaryKey - Clave primaria (comentada, usa el valor por defecto)
    |----------------------------------------------------------------------
    | Por defecto Eloquent asume que la clave primaria es 'id'.
    | Se descomenta si la clave primaria tiene otro nombre.
    | Ejemplo: protected $primaryKey = 'curso_id';
    */
    //protected $primaryKey = 'id';

    /*
    |----------------------------------------------------------------------
    | $fillable - Campos permitidos para asignacion masiva
    |----------------------------------------------------------------------
    | ASIGNACION MASIVA (Mass Assignment):
    | Cuando usamos Curso::create([...]) o $curso->fill([...]),
    | Laravel necesita saber cuales campos se pueden asignar de golpe.
    | Esto es una PROTECCION DE SEGURIDAD para evitar que un usuario
    | malicioso inyecte campos no deseados (ej: 'is_admin' => true).
    |
    | $fillable vs $guarded:
    | - $fillable (lista blanca): solo estos campos pueden asignarse masivamente
    | - $guarded (lista negra): todos excepto estos pueden asignarse
    | - Nunca uses ambos a la vez.
    |
    | EJEMPLO DE RIESGO SIN $fillable:
    |   // Si un hacker envia: POST /cursos con campo 'is_admin=1'
    |   Curso::create($request->all()); // Peligroso sin proteccion!
    |   // Con $fillable, 'is_admin' seria ignorado automaticamente
    |
    */
    protected $fillable = ['nombre', 'objetivo', 'modalidad', 'cupo', 'periodo', 'horario', 'dias', 'salon'];

    /*
    |----------------------------------------------------------------------
    | $timestamps - Marcas de tiempo automaticas (comentada)
    |----------------------------------------------------------------------
    | Por defecto Eloquent gestiona automaticamente las columnas
    | 'created_at' y 'updated_at'. Si tu tabla no las tiene,
    | descomenta esta linea: public $timestamps = false;
    |
    | Si quieres personalizar el formato:
    |   protected $dateFormat = 'Y-m-d H:i:s';
    */
    //public $timestamps = false;

    /*
    |----------------------------------------------------------------------
    | RELACIONES (no implementadas aqui, pero concepto importante)
    |----------------------------------------------------------------------
    | Eloquent soporta relaciones entre modelos:
    |
    | - hasOne:      Un curso tiene un horario  ->  $this->hasOne(Horario::class)
    | - hasMany:     Un curso tiene muchos alumnos  ->  $this->hasMany(Alumno::class)
    | - belongsTo:   Un curso pertenece a un instructor  ->  $this->belongsTo(Instructor::class)
    | - belongsToMany: Muchos a muchos (ej: cursos <-> estudiantes con tabla pivote)
    |
    | EJEMPLO:
    |   public function alumnos() {
    |       return $this->hasMany(Alumno::class);
    |   }
    |   // Uso: $curso->alumnos  (retorna coleccion de alumnos del curso)
    */
}
