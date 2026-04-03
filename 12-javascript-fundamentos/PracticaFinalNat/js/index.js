// =============================================================================
// MODULO 12 - PRACTICA FINAL: PAGINA PRINCIPAL - CONSUMO DE API CON AJAX
// =============================================================================
//
// NIVEL: Avanzado
// TEMA: jQuery AJAX, manipulacion del DOM, construccion dinamica de HTML,
//       consumo de API REST (TMDB), callbacks, setTimeout
//
// CONCEPTOS CLAVE DE ESTE ARCHIVO:
// ---------------------------------
//
// 1. $(document).ready():
//    Es el equivalente de jQuery a DOMContentLoaded nativo.
//    El callback se ejecuta cuando el DOM esta listo.
//    Forma abreviada: $(function() { ... });
//
// 2. $.ajax() - PETICIONES HTTP ASINCRONAS:
//    AJAX = Asynchronous JavaScript And XML (aunque hoy se usa mas con JSON).
//    Permite hacer peticiones HTTP al servidor SIN recargar la pagina.
//
//    Parametros principales:
//    - url: La direccion del recurso (en este caso, la API de TMDB)
//    - success: Funcion que se ejecuta si la peticion fue exitosa
//    - error: Funcion que se ejecuta si hubo un error
//    - beforeSend: Funcion que se ejecuta ANTES de enviar la peticion
//
//    ALTERNATIVA MODERNA (sin jQuery):
//    fetch("url")
//      .then(response => response.json())
//      .then(data => { ... })
//      .catch(error => { ... });
//
// 3. API DE TMDB (The Movie Database):
//    Una API REST gratuita que proporciona informacion sobre peliculas.
//    - URL base: https://api.themoviedb.org/3/
//    - Requiere una API key para autenticacion
//    - Retorna datos en formato JSON
//    - Endpoint usado: /movie/upcoming (peliculas proximas)
//    - Parametro language=es: Respuesta en español
//
//    ESTRUCTURA DE LA RESPUESTA JSON:
//    {
//      page: 1,
//      results: [
//        { original_title: "...", poster_path: "/abc.jpg", overview: "..." },
//        { ... },
//      ],
//      total_results: 200,
//      total_pages: 10
//    }
//
// 4. PATRON DE CARGA (Loading Pattern):
//    beforeSend -> Mostrar indicador de carga (gif animado)
//    success    -> Quitar indicador y mostrar datos
//    error      -> Quitar indicador y mostrar mensaje de error
//    Este patron es ESENCIAL para buena experiencia de usuario (UX).
//
// 5. setTimeout():
//    Retrasa la ejecucion de una funcion por X milisegundos.
//    setTimeout(funcion, milisegundos)
//    Aqui se usa para simular un tiempo de carga y que el usuario vea
//    el gif de "cargando". En produccion real, NO se usa asi.
//
// 6. CONSTRUCCION DE HTML CON STRINGS:
//    Se construye HTML concatenando strings con +.
//    Esta tecnica funciona pero tiene desventajas:
//    - Dificil de leer y mantener
//    - Propenso a errores de sintaxis HTML
//    - Vulnerable a XSS si los datos no se sanitizan
//    ALTERNATIVAS MEJORES:
//    - Template literals (backticks con ${})
//    - document.createElement() + appendChild()
//    - Frameworks como React, Vue, Angular
//
// COMPARACION CON PYTHON (para quienes vienen del modulo 11):
// -----------------------------------------------------------
// En Python, para hacer peticiones HTTP se usa la libreria 'requests':
//   import requests
//   response = requests.get("https://api.themoviedb.org/3/movie/upcoming?api_key=...")
//   data = response.json()
//   for movie in data['results']:
//       print(movie['title'])
//
// La GRAN diferencia es que Python es SINCRONO (bloquea hasta obtener respuesta)
// y JavaScript es ASINCRONO (continua ejecutando mientras espera la respuesta).
// =============================================================================

// $(document).ready() asegura que el DOM esta listo antes de ejecutar codigo.
// Recibe un callback (funcion anonima) que contiene toda la logica.
$(document).ready(function(){

	// $.ajax() hace una peticion HTTP GET a la API de TMDB.
	// La configuracion se pasa como un OBJETO (entre llaves {}).
	// Cada propiedad del objeto configura un aspecto de la peticion.
	$.ajax({
		// URL de la API: endpoint 'upcoming' para peliculas proximas.
		// PARAMETROS DE LA URL (query string):
		// - api_key: Clave de autenticacion (cada desarrollador tiene la suya)
		// - language=es: Respuesta en español
		//
		// SEGURIDAD: En un proyecto real, la API key NO debe estar en el
		// codigo del frontend (es visible para cualquiera). Se deberia
		// usar un backend como intermediario (proxy) que guarde la key.
		url: "https://api.themoviedb.org/3/movie/upcoming?api_key=TU_API_KEY_AQUI&language=es",

		// CALLBACK success: Se ejecuta cuando la API responde exitosamente (HTTP 200).
		// El parametro 'respuesta' contiene el JSON ya parseado automaticamente
		// por jQuery (no necesitamos llamar a JSON.parse() manualmente).
		success: function(respuesta) {
			console.log(respuesta);

			// SELECCION DEL CONTENEDOR:
			// $('#peliculas') selecciona el div con id="peliculas" usando jQuery.
			// Equivalente nativo: document.getElementById('peliculas')
			//
			// NOTA: 'peliculas' se declara SIN var/let/const, lo que la hace
			// una VARIABLE GLOBAL implicita. Esto es una MALA PRACTICA.
			// Deberia ser: const peliculas = $('#peliculas');
			// En modo estricto ('use strict'), esto lanzaria un error.
			peliculas = $('#peliculas'); //DIV donde se cargará la lista de peliculas

			// setTimeout retrasa la ejecucion 3000ms (3 segundos).
			// PROPOSITO: Dar tiempo al usuario de ver el gif de carga.
			// EN PRODUCCION: No se agrega retraso artificial. El indicador de carga
			// se muestra el tiempo real que tarda la API en responder.
			setTimeout(function () {
				$('#loader').remove(); //Se elimina la imagen de "cargando" (los engranes)

				// $.each() itera sobre un array o objeto.
				// Equivalente nativo: respuesta.results.forEach(function(elemento, index) { ... })
				// O con for...of: for (const elemento of respuesta.results) { ... }
				//
				// Parametros del callback:
				// - index: Posicion del elemento en el array (0, 1, 2, ...)
				// - elemento: El objeto de cada pelicula (con title, poster_path, etc.)

				//Para cada elemento en la lista de resultados (para cada pelicula)
				$.each(respuesta.results, function(index, elemento) {
					// crearMovieCard() recibe un objeto pelicula y retorna un string HTML.
					// Este patron se llama "template rendering" o "renderizado de plantilla".

					//La función crearMovieCard regresa el HTML con la estructura de la pelicula
					cardHTML = crearMovieCard(elemento);

					// .append() agrega el HTML al FINAL del contenido del div.
					// Equivalente nativo: peliculas.innerHTML += cardHTML;
					// O mejor: peliculas.insertAdjacentHTML('beforeend', cardHTML);
					peliculas.append(cardHTML);
				});

			}, 3000); //Tarda 3 segundos en ejecutar la función de callback
			          //Sino no se vería la imagen de los engranes, da al usuario la sensación de que se está obteniendo algo.

		},

		// CALLBACK error: Se ejecuta si la peticion falla.
		// Causas comunes de error:
		// - Sin conexion a internet
		// - API key invalida o expirada
		// - URL incorrecta
		// - El servidor de la API esta caido
		// - Error CORS (Cross-Origin Resource Sharing)
		error: function() {
			console.log("No se ha podido obtener la información");
			$('#loader').remove();
			// .html() reemplaza TODO el contenido interno del elemento.
			// Equivalente nativo: element.innerHTML = 'No se ha podido...'
			$('#peliculas').html('No se ha podido obtener la información');
		},

		// CALLBACK beforeSend: Se ejecuta ANTES de enviar la peticion.
		// Es el lugar ideal para mostrar un indicador de carga.
		// Se ejecuta SINCRONAMENTE, antes de que la peticion salga.
		beforeSend: function() {
			//ANTES de hacer la petición se muestra la imagen de cargando.
			console.log('CARGANDO');
			// Se reemplaza el contenido del div con un gif animado de carga.
			// La imagen tiene id="loader" para poder eliminarla despues.
			$('#peliculas').html('<img class="mx-auto d-block" id="loader" src="images/loading.gif" />');
		},
	});

});


// =============================================================================
// FUNCION crearMovieCard: Genera el HTML de una tarjeta de pelicula.
// =============================================================================
//
// Recibe: un objeto 'movie' con la estructura de la API de TMDB.
// Retorna: un string con el HTML de una card de Bootstrap.
//
// ACCESO A PROPIEDADES DEL OBJETO JSON:
// Se usa la NOTACION DE PUNTO: movie.poster_path, movie.original_title
// Tambien se puede usar notacion de corchetes: movie["poster_path"]
// La notacion de corchetes es necesaria cuando:
// - La propiedad tiene caracteres especiales: movie["release-date"]
// - La propiedad es una variable: movie[propiedad]
//
// IMAGENES DE TMDB:
// La API no retorna la URL completa de las imagenes.
// poster_path es solo el nombre del archivo (ej: "/abc123.jpg").
// La URL base de imagenes es: https://image.tmdb.org/t/p/w500/
// w500 = ancho maximo de 500px. Otras opciones: w200, w300, w780, original.
//
// CONCATENACION DE STRINGS CON +:
// Este codigo construye HTML concatenando strings.
// Es la forma ANTIGUA de hacerlo. La forma MODERNA usa template literals:
//
// FORMA ANTIGUA (usada aqui):
//   '<h2>' + movie.title + '</h2>'
//
// FORMA MODERNA (recomendada):
//   `<h2>${movie.title}</h2>`
//
// NOTA: La funcion esta declarada FUERA de $(document).ready(), por lo que
// es una funcion GLOBAL. Esto funciona porque las function declarations
// tienen hoisting, pero es mejor practica tenerla dentro del ready
// o en un modulo separado.
function crearMovieCard(movie){
	//Llega el objeto JSON de UNA película, como la regresa la API
	console.log(movie.poster_path);
    //sabemos que el directorio donde se guardan las imágenes es: https://image.tmdb.org/t/p/w500/
    //el atributo movie.poster_path del objeto movie, sólo contiene el nombre de la imagen (NO la ruta completa)

    //NOTAR que se accede al objeto JSON movie con la notación de punto para acceder a los atributos (movie.original_title).

    // NOTA: 'var' se usa aqui en vez de 'const' o 'let'.
    // 'var' tiene alcance de FUNCION (no de bloque), lo que puede causar bugs.
    // RECOMENDACION: Usar 'const' ya que cardHTML no se reasigna despues.
	var cardHTML =
		'<!-- CARD -->'
		+'<div class="col-md-4">'
		    +'<div class="card">'
		       +'<div class="card-header">'
		          +'<img class="card-img" src="https://image.tmdb.org/t/p/w500/'+movie.poster_path+'" alt="Card image">'
		       +'</div>'
		       +'<div class="card-body">'
		          +'<h2 class="card-title">'+movie.original_title+'</h2>'
		          +'<div class="container">'
		             +'<div class="row">'
		                +'<div class="col-4 metadata">'
		                   +'<i class="fa fa-star" aria-hidden="true"></i>'
		                   +'<p>9.5/10</p>'
		                +'</div>'
		                +'<div class="col-8 metadata">Adventure. Sci-Fi</div>'
		             +'</div>'
		          +'</div>'
		          +'<p class="card-text">A team of explorers travel through wormhole in space in an attempt to ensure humanitys survival.</p>'
		       +'</div>'
		    +'</div>'
		+'</div>'
		+'<!-- CARD -->';

		return cardHTML;
}

// =============================================================================
// FLUJO COMPLETO DE LA PAGINA:
//
// 1. El navegador carga el HTML y muestra la estructura basica
// 2. Se cargan los CSS (Bootstrap + custom) y se aplican los estilos
// 3. Se carga jQuery, luego Popper, luego Bootstrap JS
// 4. Se carga index.js y se registra el callback de $(document).ready()
// 5. Cuando el DOM esta listo, se ejecuta el callback:
//    a) beforeSend: Muestra el gif de carga en #peliculas
//    b) Se envia la peticion GET a la API de TMDB
//    c) La API responde con JSON (lista de peliculas)
//    d) success: Despues de 3 segundos (setTimeout):
//       - Se elimina el gif de carga
//       - Se itera sobre cada pelicula
//       - Se genera el HTML de cada card
//       - Se agrega cada card al DOM
//    e) Si hay error: Se muestra un mensaje de error
//
// MEJORAS POSIBLES:
// 1. Usar fetch() en vez de $.ajax() (eliminar dependencia de jQuery)
// 2. Usar template literals en vez de concatenacion con +
// 3. Mostrar datos reales de la pelicula (overview, rating) en vez de hardcoded
// 4. Agregar paginacion para ver mas peliculas
// 5. Proteger la API key usando un backend como proxy
// 6. Agregar manejo de errores mas robusto (diferentes mensajes segun el error)
// =============================================================================
