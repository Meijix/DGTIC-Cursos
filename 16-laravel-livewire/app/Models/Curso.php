<?php
/*
|==========================================================================
| Curso.php - Modelo Eloquent para la tabla 'cursos' (Modulo Livewire)
|==========================================================================
|
| Este es el mismo concepto de modelo que en el Modulo 15, pero aqui
| se usa junto con Livewire en vez de un controlador tradicional.
|
| DIFERENCIA CON EL MODULO 15:
| En el Modulo 15, el modelo tenia $fillable definido:
|   protected $fillable = ['nombre', 'objetivo', ...];
|
| Aqui NO esta definido $fillable, lo cual significa que si intentamos
| usar Curso::create([...]) obtendremos un error de Mass Assignment.
|
| SOLUCION: agregar $fillable para que create() funcione:
|   protected $fillable = ['nombre', 'objetivo', 'modalidad',
|                          'cupo', 'periodo', 'horario', 'dias', 'salon'];
|
| EL MODELO EN EL CONTEXTO DE LIVEWIRE:
| El modelo funciona exactamente igual con Livewire que con un
| controlador tradicional. Eloquent no sabe ni le importa si lo llama
| un controlador o un componente Livewire. Es la misma interfaz.
|
|   Modulo 15 (Controlador):          Modulo 16 (Livewire):
|   CursoController@store {           CursoComponent->store() {
|       Curso::create([...]);             Curso::create([...]);
|   }                                 }
|
| Eloquent es la capa de acceso a datos; quien lo invoque es irrelevante.
|
*/

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

/*
|--------------------------------------------------------------------------
| Clase Curso
|--------------------------------------------------------------------------
| Modelo basico de Eloquent. Al extender Model, hereda todos los
| metodos de consulta, creacion, actualizacion y eliminacion.
|
| NOTA IMPORTANTE:
| Este modelo esta "vacio" (sin $fillable). Para que el componente
| Livewire pueda usar Curso::create([...]), es necesario agregar:
|
|   protected $fillable = ['nombre', 'objetivo', 'modalidad',
|                          'cupo', 'periodo', 'horario', 'dias', 'salon'];
|
| Sin $fillable, Laravel lanzara una excepcion de seguridad:
|   "Add [nombre] to fillable property to allow mass assignment"
|
| CONVENCIONES APLICADAS:
| - Nombre del modelo: Curso (singular, PascalCase)
| - Tabla asociada: cursos (plural, snake_case) -> automatico por convencion
| - Clave primaria: id -> automatico por convencion
| - Timestamps: created_at y updated_at -> automatico por convencion
*/
class Curso extends Model
{
    //
}
