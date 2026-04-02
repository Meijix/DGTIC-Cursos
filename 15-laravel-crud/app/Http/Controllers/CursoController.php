<?php
/*
|==========================================================================
| CursoController.php - Controlador de Recursos (CRUD) para Cursos
|==========================================================================
|
| ARQUITECTURA MVC (Modelo-Vista-Controlador):
| Este archivo es el CONTROLADOR, la "C" del patron MVC.
|
|   +----------+      +--------------+      +---------+      +--------+
|   | Navegador| ---> |  routes/     | ---> | Control-| ---> | Modelo |
|   | (Request)|      |  web.php     |      | ador    |      | (DB)   |
|   +----------+      +--------------+      +---------+      +--------+
|        ^                                       |
|        |                                       v
|        +------ Response <-----  Vista (Blade Template)
|
| QUE ES UN CONTROLADOR EN LARAVEL:
| - Es una clase PHP que agrupa la logica de manejo de peticiones HTTP.
| - Recibe la peticion del usuario (Request), interactua con el Modelo
|   (base de datos) y devuelve una Vista (respuesta HTML).
| - Se genera con: php artisan make:controller CursoController --resource
|   (el flag --resource genera automaticamente los 7 metodos CRUD).
|
| LOS 7 METODOS DE UN RESOURCE CONTROLLER:
| +----------+--------+------------------+----------------------------------+
| | Metodo   | HTTP   | URI              | Descripcion                      |
| +----------+--------+------------------+----------------------------------+
| | index    | GET    | /cursos          | Listar todos los registros       |
| | create   | GET    | /cursos/create   | Mostrar formulario de creacion   |
| | store    | POST   | /cursos          | Guardar nuevo registro           |
| | show     | GET    | /cursos/{id}     | Mostrar un registro especifico   |
| | edit     | GET    | /cursos/{id}/edit| Mostrar formulario de edicion    |
| | update   | PUT    | /cursos/{id}     | Actualizar registro existente    |
| | destroy  | DELETE | /cursos/{id}     | Eliminar un registro             |
| +----------+--------+------------------+----------------------------------+
|
| CICLO DE VIDA DE UNA PETICION CRUD:
|   1. El usuario hace clic en un enlace o envia un formulario
|   2. Laravel busca la ruta correspondiente en web.php
|   3. La ruta invoca el metodo del controlador apropiado
|   4. El controlador valida datos (si es necesario)
|   5. El controlador interactua con el Modelo (Eloquent)
|   6. El controlador retorna una Vista o redirecciona
|
*/

namespace App\Http\Controllers;

// Request: objeto que encapsula toda la informacion de la peticion HTTP
// (datos del formulario, headers, cookies, archivos subidos, etc.)
use Illuminate\Http\Request;

// Importamos el modelo Curso para interactuar con la tabla 'cursos' en la BD
use App\Models\Curso;

/*
|--------------------------------------------------------------------------
| Clase CursoController
|--------------------------------------------------------------------------
| Extiende de Controller (clase base de Laravel) que provee funcionalidades
| como validacion, autorizacion y manejo de middleware.
|
| Cada metodo publico corresponde a una accion CRUD que se conecta
| con una ruta definida en routes/web.php.
*/
class CursoController extends Controller
{
    /*
    |----------------------------------------------------------------------
    | INDEX - Listar todos los cursos
    |----------------------------------------------------------------------
    | Verbo HTTP: GET
    | Ruta: / (pagina principal)
    | Proposito: Obtener todos los cursos de la BD y mostrarlos en una tabla.
    |
    | CONCEPTOS CLAVE:
    | - Curso::orderBy('id'): consulta Eloquent que ordena por ID
    | - ->paginate(4): divide resultados en paginas de 4 elementos.
    |   Laravel genera automaticamente los enlaces de paginacion.
    | - compact('cursos'): crea un array ['cursos' => $cursos] para la vista.
    |   Es equivalente a: view('principal', ['cursos' => $cursos])
    | - view('principal'): busca el archivo resources/views/principal.blade.php
    */
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        // Eloquent ORM: orderBy ordena los resultados, paginate los divide en paginas
        // paginate(4) significa 4 cursos por pagina; Laravel crea los links automaticamente
        $cursos = Curso::orderBy('id')-> paginate(4);

        // compact() es un helper de PHP que crea un array asociativo
        // a partir del nombre de la variable: ['cursos' => $cursos]
        return view('principal', compact('cursos'));
    }

    /*
    |----------------------------------------------------------------------
    | CREATE - Mostrar formulario de creacion
    |----------------------------------------------------------------------
    | Verbo HTTP: GET
    | Ruta: /agregar
    | Proposito: Mostrar el formulario vacio para agregar un nuevo curso.
    |
    | NOTA: Este metodo solo muestra el formulario. La logica de guardado
    | esta en el metodo store(). Esta separacion es parte del patron REST:
    |   - create() = GET  -> muestra el formulario
    |   - store()  = POST -> procesa los datos del formulario
    */
    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        // Retorna la vista 'agregar' (resources/views/agregar.blade.php)
        // No necesita datos porque el formulario esta vacio
        return view('agregar');
    }

    /*
    |----------------------------------------------------------------------
    | STORE - Guardar un nuevo curso en la base de datos
    |----------------------------------------------------------------------
    | Verbo HTTP: POST
    | Ruta: /agregar
    | Proposito: Recibir datos del formulario, validarlos y guardarlos.
    |
    | FLUJO COMPLETO:
    |   1. El formulario envia datos via POST (con token CSRF)
    |   2. Laravel inyecta automaticamente el objeto $request
    |   3. Se validan los campos (si falla, redirige de vuelta con errores)
    |   4. Se crea una nueva instancia del modelo Curso
    |   5. Se asignan los valores uno por uno desde $request
    |   6. Se guarda en la BD con save()
    |   7. Se redirige a la pagina principal con un mensaje flash
    |
    | VALIDACION:
    | - $this->validate() lanza una excepcion si los datos no pasan.
    | - Laravel redirige automaticamente al formulario con los errores.
    | - En la vista se accede a los errores con @error('campo') o $errors.
    | - 'required' = el campo es obligatorio.
    | - Otras reglas comunes: 'email', 'min:3', 'max:255', 'numeric', 'unique:tabla'
    |
    | ALTERNATIVA MAS LIMPIA CON MASS ASSIGNMENT:
    |   Curso::create($request->validated());
    |   Esto funciona si $fillable esta definido en el modelo (y lo esta).
    */
    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        // PASO 1: Validar los datos del formulario
        // Si la validacion falla, Laravel redirige automaticamente al formulario
        // anterior con los mensajes de error disponibles en $errors
        $this->validate($request, [
            'nombre' => 'required',
            'objetivo' => 'required',
            'modalidad' => 'required',
            'cupo' => 'required',
            'periodo' => 'required',
            'horario' => 'required',
            'dias' => 'required',
            'salon' => 'required'
        ]);

        // PASO 2: Crear una nueva instancia del modelo (aun no se guarda en BD)
        $curso = new Curso;

        // PASO 3: Asignar cada campo manualmente desde la peticion
        // $request->nombre obtiene el valor del campo 'nombre' del formulario
        $curso->nombre = $request->nombre;
        $curso->objetivo = $request->objetivo;
        $curso->modalidad = $request->modalidad;
        $curso->cupo = $request->cupo;
        $curso->periodo = $request->periodo;
        $curso->horario = $request->horario;
        $curso->dias = $request->dias;
        $curso->salon = $request->salon;

        // PASO 4: Persistir el registro en la base de datos
        // save() ejecuta un INSERT INTO cursos (...) VALUES (...)
        $curso->save();

        // PASO 5: Redirigir a la ruta con nombre 'index'
        // ->with() agrega un mensaje "flash" a la sesion (disponible solo en la siguiente peticion)
        // En la vista se accede con: session('mensaje')
        return redirect(route('index'))->with('mensaje', 'El curso fue agregado con éxito');
    }

    /*
    |----------------------------------------------------------------------
    | SHOW - Mostrar un curso especifico (no implementado)
    |----------------------------------------------------------------------
    | Verbo HTTP: GET
    | Ruta: /cursos/{id}
    | Proposito: Mostrar los detalles de un curso individual.
    | NOTA: Este metodo viene del scaffold --resource pero no se usa aqui.
    */
    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        //
    }

    /*
    |----------------------------------------------------------------------
    | EDIT - Mostrar formulario de edicion con datos precargados
    |----------------------------------------------------------------------
    | Verbo HTTP: GET
    | Ruta: /editar/{id}
    | Proposito: Buscar un curso por su ID y mostrar el formulario con
    |            los datos actuales para que el usuario los modifique.
    |
    | PARAMETROS DE RUTA:
    | - {id} en la ruta se convierte en el parametro $id del metodo.
    | - Laravel extrae automaticamente el valor de la URL.
    | - Ejemplo: /editar/5  ->  $id = "5"
    |
    | Curso::find($id):
    | - Busca un registro por su clave primaria (id).
    | - Retorna null si no lo encuentra (considerar usar findOrFail).
    | - findOrFail($id) lanza una excepcion 404 si no existe el registro.
    */
    /**
     * Show the form for editing the specified resource.
     */
    public function edit(string $id)
    {
        // find() busca por clave primaria. Equivale a: SELECT * FROM cursos WHERE id = $id
        // MEJORA: usar findOrFail($id) para manejar IDs inexistentes con error 404
        $curso = Curso::find($id);

        // Pasa el curso encontrado a la vista 'editar' para precargar el formulario
        return view('editar', compact('curso'));
    }

    /*
    |----------------------------------------------------------------------
    | UPDATE - Actualizar un curso existente
    |----------------------------------------------------------------------
    | Verbo HTTP: POST (idealmente deberia ser PUT/PATCH)
    | Ruta: /actualizar/{id}
    | Proposito: Recibir datos editados, validarlos y actualizar el registro.
    |
    | NOTA SOBRE VERBOS HTTP:
    | - En REST puro, actualizar usa PUT o PATCH.
    | - Los formularios HTML solo soportan GET y POST.
    | - Laravel permite simular PUT/PATCH con @method('PUT') en el form.
    | - Aqui se usa POST directamente (funciona pero no sigue la convencion REST).
    |
    | ALTERNATIVA MAS LIMPIA:
    |   $curso->update($request->validated());
    |   Esto actualiza todos los campos de una vez usando mass assignment.
    */
    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        // Validar: mismas reglas que store(). Se podria extraer a un Form Request
        // para reutilizar: php artisan make:request CursoRequest
        $this->validate($request, [
            'nombre' => 'required',
            'objetivo' => 'required',
            'modalidad' => 'required',
            'cupo' => 'required',
            'periodo' => 'required',
            'horario' => 'required',
            'dias' => 'required',
            'salon' => 'required'
        ]);

        // Buscar el curso existente por su ID
        $curso = Curso::find($id);

        // Actualizar cada campo con los nuevos valores del formulario
        $curso->nombre = $request->nombre;
        $curso->objetivo = $request->objetivo;
        $curso->modalidad = $request->modalidad;
        $curso->cupo = $request->cupo;
        $curso->periodo = $request->periodo;
        $curso->horario = $request->horario;
        $curso->dias = $request->dias;
        $curso->salon = $request->salon;

        // save() detecta que el modelo ya existe (tiene ID) y ejecuta UPDATE en vez de INSERT
        $curso->save();

        // Redirigir con mensaje flash de exito
        return redirect(route('index'))->with('mensaje', 'El curso fue actualizado con éxito');
    }


    /*
    |----------------------------------------------------------------------
    | DESTROY - Eliminar un curso
    |----------------------------------------------------------------------
    | Verbo HTTP: DELETE
    | Ruta: /eliminar/{id}
    | Proposito: Eliminar permanentemente un curso de la base de datos.
    |
    | METODOS DE ELIMINACION EN ELOQUENT:
    | - Curso::destroy($id): elimina por ID sin necesidad de buscar primero.
    |   Ejecuta: DELETE FROM cursos WHERE id = $id
    | - $curso->delete(): primero buscas, luego eliminas la instancia.
    | - Soft Deletes: en vez de eliminar, marca con deleted_at (requiere
    |   SoftDeletes trait en el modelo y la columna en la migracion).
    |
    | SEGURIDAD:
    | - El formulario en la vista usa @csrf y @method('DELETE')
    | - @csrf protege contra ataques Cross-Site Request Forgery
    | - Solo peticiones DELETE son aceptadas por esta ruta
    */
    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        // destroy() es un metodo estatico que elimina por ID directamente
        // Es mas eficiente que find() + delete() porque solo hace una consulta
        Curso::destroy($id);

        // Redirige al listado con mensaje de confirmacion
        return redirect(route('index'))->with('mensaje', 'El curso fue eliminado con éxito');
    }
}
