// =============================================================================
// MODULO 12 - PRACTICA FINAL: LOGICA DEL CATALOGO DE PELICULAS
// =============================================================================
//
// NIVEL: Avanzado
// TEMA: Eventos click, AJAX, generacion dinamica de HTML, modales de Bootstrap,
//       closures, funciones nombradas como callbacks, slideDown (animaciones)
//
// CONCEPTOS CLAVE DE ESTE ARCHIVO:
// ---------------------------------
//
// 1. FUNCION NOMBRADA COMO CALLBACK:
//    En vez de pasar una funcion anonima al evento click, se pasa una
//    referencia a una funcion nombrada (obtenerCatalogo).
//    .on("click", obtenerCatalogo) vs .on("click", function() { ... })
//
//    Ventajas de funciones nombradas:
//    - Mas legibles: el nombre describe lo que hace
//    - Se pueden reutilizar (llamar desde multiples eventos)
//    - Aparecen con nombre en el debugger (mas facil depurar)
//    - Se pueden remover: .off("click", obtenerCatalogo)
//
// 2. CLOSURES (CLAUSURAS):
//    obtenerCatalogo() puede acceder a 'listaPeliculas' aunque esta
//    definida fuera de la funcion. Esto es un CLOSURE: la funcion
//    "recuerda" las variables del scope donde fue creada.
//
//    Los closures son uno de los conceptos MAS IMPORTANTES de JavaScript.
//    Permiten:
//    - Encapsulamiento de datos (variables privadas)
//    - Callbacks que recuerdan su contexto
//    - Factory functions (funciones que crean funciones)
//
// 3. GENERACION DINAMICA DE MODALES:
//    La funcion crearModal() genera la estructura HTML de un modal
//    de Bootstrap para cada pelicula. Esto demuestra como JavaScript
//    puede crear componentes complejos de interfaz al vuelo.
//
//    FLUJO: Cada pelicula en la lista tiene un data-target="#modal0",
//    "#modal1", etc. Al hacer click, Bootstrap busca ese modal en el DOM
//    y lo muestra. crearModal() se asegura de que ese modal exista.
//
// 4. slideDown("slow"):
//    Es una animacion de jQuery que muestra un elemento deslizandolo
//    hacia abajo. Alternativas de jQuery: fadeIn(), show(), slideToggle().
//    En CSS moderno, se prefieren transiciones CSS o la Web Animations API.
//
// 5. SCOPE (ALCANCE) DE FUNCIONES:
//    - listaPeliculas: Declarada dentro de $(document).ready() -> scope local
//    - obtenerCatalogo: Tambien dentro de ready() -> scope local
//    - crearModal: Declarada FUERA de ready() -> scope GLOBAL
//
//    NOTA: crearModal es global, lo que significa que cualquier script
//    en la pagina puede llamarla o sobreescribirla. En una aplicacion
//    grande, esto puede causar conflictos de nombres (namespace pollution).
//    SOLUCION: Modulos ES6 (import/export) o el patron IIFE.
//
// COMPARACION AJAX: jQuery vs Fetch nativo:
// ------------------------------------------
// jQuery:                                  Fetch:
// $.ajax({                                 fetch(url)
//   url: "...",                              .then(r => r.json())
//   success: function(data) { ... },         .then(data => { ... })
//   error: function() { ... },               .catch(err => { ... })
//   beforeSend: function() { ... }         // No tiene beforeSend nativo
// })
// =============================================================================

// $(document).ready(): Espera a que el DOM este listo.
$(document).ready(function(){

	// Asignar el evento click al boton "Mostrar catalogo".
	// Se pasa una REFERENCIA a la funcion obtenerCatalogo (sin parentesis).
	// Con parentesis: obtenerCatalogo() -> Ejecuta la funcion INMEDIATAMENTE
	// Sin parentesis: obtenerCatalogo   -> Pasa la referencia para ejecucion futura
	//
	// Este es un error MUY COMUN entre principiantes.
	$("#boton-obtener").on("click", obtenerCatalogo);

	// Cache del selector jQuery para el contenedor de peliculas.
	// Se usa 'var' pero 'const' seria mas apropiado.
	var listaPeliculas = $("#lista-pelis");

	// FUNCION obtenerCatalogo:
	// Se declara como function declaration dentro de ready().
	// Tiene acceso a 'listaPeliculas' gracias al CLOSURE.
	function obtenerCatalogo() {
//		listaPeliculas.empty();
//		listaPeliculas.hide();
		$.ajax({
			// URL de la API de TMDB: endpoint 'discover' para descubrir peliculas.
			// Parametros del query string:
			// - certification_country=MX: Peliculas con certificacion mexicana
			// - primary_release_date.gte=2018-08-01: Estrenadas desde esta fecha
			// - primary_release_date.lte=2018-09-20: Estrenadas hasta esta fecha
			// - language=es: Respuesta en español
			// - api_key: Clave de autenticacion
			//
			// NOTA: Las fechas estan "hardcodeadas" (fijas en el codigo).
			// En una aplicacion real, el usuario podria seleccionar el rango de fechas.

			//url: "https://randomuser.me/api/?results=8&nat=au,fr,es&inc=gender,name,picture,email,nat",
			url: "http://api.themoviedb.org/3/discover/movie?certification_country=MX&primary_release_date.gte=2018-08-01&primary_release_date.lte=2018-09-20&language=es&total_results=3&api_key=3356865d41894a2fa9bfa84b2b5f59bb",

			// CALLBACK success:
			// 'respuesta' es el JSON parseado de la API.
			// Se usa setTimeout para simular un tiempo de carga (3 segundos).
			success: function(respuesta) {

				setTimeout(function () {
					console.log(respuesta);

					// .empty() limpia el contenedor (elimina el gif de carga).
					listaPeliculas.empty();

					// Iterar sobre cada pelicula en los resultados.
					// ESTRUCTURA DEL HTML GENERADO:
					// Cada pelicula se muestra como un componente "media" de Bootstrap:
					// - Imagen pequeña a la izquierda (poster, max 50px)
					// - Titulo a la derecha (como enlace al modal)
					// - Sinopsis debajo del titulo
					//
					// data-toggle="modal" data-target="#modal0":
					// Estos atributos de Bootstrap activan un modal al hacer click.
					// 'index' se usa para generar IDs unicos: modal0, modal1, modal2...
					$.each(respuesta.results, function(index, elemento) {
						listaPeliculas.append(
							'<div class="media text-muted pt-3">'
                        +  '<img style="max-width:50px;" class="mr-2 rounded" src="https://image.tmdb.org/t/p/w500' + elemento.poster_path + '"></img>'
						+  '<p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">'
						+    '<strong class="d-block text-gray-dark" data-toggle="modal" data-target="#modal'+index+'">'+elemento.title+'</strong>'
						+    elemento.overview
						+  '</p>'
                        +'</div>'
						);

						// CREAR MODAL: Para cada pelicula se genera un modal con su sinopsis.
						// Se le pasa el 'index' para generar un ID unico (modal0, modal1, etc.)
						// y el 'overview' (sinopsis) como contenido del modal.
						crearModal(index, elemento.overview);

					});

					// slideDown("slow"): Animacion de jQuery que muestra el contenedor
					// deslizandolo hacia abajo. "slow" = 600ms de duracion.
					// Opciones: "fast" (200ms), "slow" (600ms), o milisegundos (ej: 400).
					//
					// NOTA: Para que slideDown funcione, el elemento debe estar oculto.
					// En este caso funciona porque el contenedor se vacio y lleno de nuevo.
					listaPeliculas.slideDown("slow");
				}, 3000);

			},

			// CALLBACK error: Manejo basico de errores.
			// MEJORA: Mostrar un mensaje al usuario en la pagina,
			// no solo en la consola (el usuario no ve la consola).
			error: function() {
				console.log("No se ha podido obtener la información");
			},

			// CALLBACK beforeSend: Muestra indicador de carga.
			// Se limpia el contenedor y se agrega un gif animado.
			// Esto le indica al usuario que "algo esta pasando".
			beforeSend: function() {
				console.log('CARGANDO');
				listaPeliculas.empty();
				listaPeliculas.append('<div class="text-center"><img src="images/loading.gif" /></div>');
			},
		});

	}

});


// =============================================================================
// FUNCION crearModal: Genera el HTML de un modal de Bootstrap.
// =============================================================================
//
// Parametros:
// - index: Numero unico para el ID del modal (0, 1, 2, ...)
// - overview: Texto de la sinopsis de la pelicula
//
// ESTRUCTURA DE UN MODAL DE BOOTSTRAP:
// .modal            -> Contenedor principal (oculto por defecto)
//   .modal-dialog   -> Dialogo centrado
//     .modal-content -> Contenido del modal
//       .modal-header -> Cabecera con titulo y boton de cerrar
//       .modal-body   -> Cuerpo con el contenido principal
//       .modal-footer -> Pie con botones de accion
//
// ATRIBUTOS IMPORTANTES:
// - id="modal0": ID unico que coincide con el data-target del trigger
// - tabindex="-1": Permite que el modal reciba foco del teclado
// - role="dialog": Accesibilidad para lectores de pantalla
// - aria-hidden="true": Indica que esta oculto para lectores de pantalla
// - data-dismiss="modal": Cierra el modal al hacer click
//
// NOTA: Esta funcion esta en el SCOPE GLOBAL (fuera de document.ready).
// Esto es necesario porque se llama desde dentro de ready().
// Aunque funciona, en una aplicacion grande seria mejor tenerla
// dentro de un modulo o namespace para evitar conflictos.
//
// VULNERABILIDAD XSS:
// El 'overview' se inserta directamente en el HTML sin sanitizar.
// Si la API retornara HTML malicioso (poco probable pero posible),
// se ejecutaria en la pagina. Para sanitizar:
//   overview = overview.replace(/</g, '&lt;').replace(/>/g, '&gt;');
// O usar .text() de jQuery en vez de construir HTML con strings.
function crearModal(index, overview){
	var htmlModal='<div class="modal fade" id="modal'+index+'" tabindex="-1" role="dialog" aria-labelledby="modal'+index+'" aria-hidden="true">'
                  +'<div class="modal-dialog" role="document">'
                  +'<div class="modal-content">'
                  +'<div class="modal-header">'
                  +'<h5 class="modal-title" id="exampleModalLabel">Sinópsis</h5>'
                  +'<button type="button" class="close" data-dismiss="modal" aria-label="Close">'
                  +'<span aria-hidden="true">&times;</span>'
                  +'</button>'
                  +'</div>'
                  +'<div class="modal-body">'
                  +overview
                  +'</div>'
                  +'<div class="modal-footer">'
                  +'<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>'
                  +'</div>'
                  +'</div>'
                  +'</div>'
                  +'</div>';

    // Se agrega el modal al div#modals del HTML.
    // Cada vez que se hace click en "Mostrar catalogo", se crean NUEVOS modales.
    // POSIBLE BUG: Si el usuario hace click multiples veces, los modales se
    // acumulan (modal0, modal0, modal0...). El ultimo siempre coincide por ID.
    // SOLUCION: Vaciar #modals al inicio de obtenerCatalogo():
    //   $('#modals').empty();
    $('#modals').append(htmlModal);
}

// =============================================================================
// FLUJO COMPLETO:
//
// 1. La pagina carga -> se registra el evento click en #boton-obtener
// 2. Usuario hace click en "Mostrar catalogo"
// 3. beforeSend: Se muestra gif de carga
// 4. Se envia peticion GET a la API de TMDB
// 5. La API responde con peliculas del periodo 2018-08 a 2018-09
// 6. Despues de 3 segundos (setTimeout):
//    a) Se vacia el contenedor de peliculas
//    b) Para cada pelicula:
//       - Se genera HTML de la pelicula y se agrega al DOM
//       - Se genera un modal con la sinopsis y se agrega al DOM
//    c) Se anima la aparicion con slideDown
// 7. Al hacer click en un titulo -> Se abre el modal con la sinopsis
//
// EJERCICIOS SUGERIDOS:
// 1. Reemplaza las fechas hardcodeadas por inputs de fecha del usuario
// 2. Agrega un boton "Cerrar catalogo" que limpie la lista
// 3. Evita que se acumulen modales al hacer click multiples veces
// 4. Agrega paginacion (boton "Ver mas") usando el parametro page de la API
// 5. Reescribe crearModal usando template literals
// =============================================================================
