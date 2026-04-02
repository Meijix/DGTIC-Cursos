// =============================================================================
// MODULO 12 - PRACTICA FINAL: LOGICA DE BUSQUEDA CON API
// =============================================================================
//
// NIVEL: Avanzado
// TEMA: Busqueda dinamica, eventos click, AJAX con parametros del usuario,
//       validacion de entrada, template literals, encodeURIComponent
//
// CONCEPTOS CLAVE DE ESTE ARCHIVO:
// ---------------------------------
//
// 1. BUSQUEDA CON API:
//    Este archivo implementa el flujo completo de busqueda:
//    a) Capturar el click del boton "Buscar"
//    b) Validar que el campo no este vacio
//    c) Leer el texto del input
//    d) Hacer una peticion AJAX con la palabra buscada
//    e) Vaciar los resultados anteriores
//    f) Mostrar los nuevos resultados
//
// 2. SELECTORES DE JQUERY:
//    $("#miLista")  -> Selecciona por ID (equivale a document.getElementById)
//    $(".clase")    -> Selecciona por clase (equivale a document.getElementsByClassName)
//    $("etiqueta")  -> Selecciona por etiqueta (equivale a document.getElementsByTagName)
//
//    Los selectores de jQuery usan la misma sintaxis que CSS:
//    # para IDs, . para clases, sin prefijo para etiquetas.
//
// 3. .val() DE JQUERY:
//    Obtiene el valor actual de un elemento de formulario (input, select, textarea).
//    Equivalente nativo: document.getElementById("busqueda").value
//
// 4. .on("click", callback):
//    Asigna un evento a un elemento. Es la forma MODERNA de jQuery.
//    Equivalentes:
//    - jQuery antiguo: .click(callback)
//    - Nativo moderno: element.addEventListener("click", callback)
//
// 5. encodeURIComponent():
//    Codifica caracteres especiales para que sean seguros en una URL.
//    Ejemplo: "avengers end game" -> "avengers%20end%20game"
//    Sin esto, los espacios y caracteres especiales (ñ, acentos, &, ?, etc.)
//    podrian romper la URL o causar resultados incorrectos.
//
// 6. TEMPLATE LITERALS EN JQUERY .append():
//    A diferencia de index.js que usa concatenacion con +, este archivo
//    usa template literals (backticks ``) para construir HTML.
//    Esta es la forma MODERNA y RECOMENDADA:
//    - Mas legible (se ve como HTML real)
//    - Permite multiples lineas sin problemas
//    - Las variables se insertan con ${variable}
//
// 7. VALIDACION DE ENTRADA:
//    Antes de hacer la peticion, se verifica que el input no este vacio.
//    Esta es una validacion del LADO DEL CLIENTE (frontend).
//    IMPORTANTE: La validacion del frontend se puede saltar facilmente.
//    SIEMPRE hay que validar tambien en el backend (servidor).
//
// COMPARACION CON PYTHON:
// -----------------------
// En Python con Flask/Django, la busqueda seria:
//   @app.route('/buscar')
//   def buscar():
//       palabra = request.args.get('query')
//       response = requests.get(f"https://api.themoviedb.org/3/search/movie?query={palabra}")
//       return render_template('resultados.html', peliculas=response.json())
//
// La diferencia clave: en Python el servidor genera el HTML completo;
// aqui JavaScript en el navegador construye el HTML dinamicamente.
// =============================================================================

// $(document).ready(): Todo el codigo dentro se ejecuta cuando el DOM esta listo.
$(document).ready(function(){

	// CACHE DE SELECTORES:
	// Se guardan las referencias a elementos en variables para no buscarlos
	// en el DOM cada vez que se necesitan. Esto mejora el rendimiento.
	//
	// NOTA: Se usa 'var' (alcance de funcion). En codigo moderno deberia ser 'const'.
	// var vs const:
	//   var miLista = ...    -> Puede reasignarse, alcance de funcion
	//   const miLista = ...  -> No puede reasignarse, alcance de bloque
	var miLista = $("#miLista");
	var busqueda = $("#busqueda");

	// EVENTO CLICK EN EL BOTON DE BUSCAR:
	// .on("click", callback) es la forma recomendada en jQuery moderno.
	// Cuando el usuario hace click en #btn-buscar, se ejecuta la funcion anonima.
	//
	// NOTA: Este evento tambien podria dispararse con la tecla Enter:
	//   busqueda.on("keypress", function(e) {
	//       if (e.which === 13) { /* hacer la busqueda */ }
	//   });
	// Esto mejoraria la experiencia del usuario (UX).
	$("#btn-buscar").on("click", function(){

		// VALIDACION: Verificar que la palabra no este vacia.
		// .val() retorna el valor actual del input.
		// "" (string vacio) es un valor "falsy" en JavaScript.
		//
		// NOTA: Se usa != (comparacion debil) en vez de !== (comparacion estricta).
		// != hace conversion de tipos: null != "" es true, pero null !== "" tambien.
		// RECOMENDACION: Siempre usar === y !== para evitar bugs por conversion.
		//
		// Tambien deberia verificar espacios en blanco:
		//   if (busqueda.val().trim() !== "")
		// .trim() elimina espacios al inicio y final: "  hola  " -> "hola"

		//verificar que la palabra no esté vacía
		if(busqueda.val() != ""){

			// Leer el valor del input de busqueda.
			// NOTA: Ya se habia guardado en 'busqueda', pero aqui se vuelve a
			// seleccionar con $('#busqueda'). Seria mas eficiente usar:
			//   const palabra = busqueda.val();

			//Obtener la palabra a buscar
			const palabra = $('#busqueda').val();
			console.log('Palabra a buscar: ' + palabra);
			alert('Vamos a buscar: ' + palabra);

			// PETICION AJAX DE BUSQUEDA:
			// $.ajax() con configuracion completa.
			// - type: "GET" indica que es una peticion de lectura (no modifica datos).
			//   Los tipos mas comunes: GET (leer), POST (crear), PUT (actualizar), DELETE (eliminar).
			// - url: Endpoint de busqueda de la API de TMDB.
			// - dataType: "json" indica que esperamos JSON como respuesta.
			//   jQuery automaticamente parsea el JSON a un objeto JavaScript.

			//Usar AJAX para buscar la palabra
			$.ajax({
				type: "GET",

				// TEMPLATE LITERAL EN LA URL:
				// Se usa `...${variable}...` para insertar la palabra de busqueda.
				// encodeURIComponent(palabra) codifica caracteres especiales:
				//   "Iron Man"  -> "Iron%20Man"
				//   "avión"     -> "avi%C3%B3n"
				// Sin encodeURIComponent, caracteres como & o ? romperian la URL.
				url: `https://api.themoviedb.org/3/search/movie?certification_country=MX&language=es&api_key=3356865d41894a2fa9bfa84b2b5f59bb&query=${encodeURIComponent(palabra)}`,
				dataType: "json",

				// SUCCESS: Se ejecuta cuando la API responde correctamente.
				// 'data' contiene la respuesta JSON ya parseada:
				// { results: [ {title: "...", poster_path: "...", overview: "..."}, ... ] }
				success: function(data){
					console.log(data);

					// .empty() elimina TODO el contenido interno del elemento.
					// Es necesario para limpiar resultados de busquedas anteriores.
					// Equivalente nativo: document.getElementById("miLista").innerHTML = "";
					$("#miLista").empty();

					// $.each() itera sobre el array de resultados.
					// Para cada pelicula encontrada, genera un <li> con:
					// - Titulo de la pelicula (item.title)
					// - Imagen del poster (item.poster_path)
					// - Sinopsis (item.overview)
					//
					// TEMPLATE LITERALS: Se usan backticks (`) para crear HTML multi-linea.
					// Cada ${...} se reemplaza por el valor de la expresion.
					// Esto es MUCHO mas legible que la concatenacion con + de index.js.
					//
					// POSIBLE BUG: Si item.poster_path es null (pelicula sin imagen),
					// la URL de la imagen seria "https://image.tmdb.org/t/p/w500null"
					// lo cual mostraria una imagen rota.
					// SOLUCION: Verificar antes: item.poster_path ? url+item.poster_path : "default.jpg"
					$.each(data.results, function(index, item){
						$("#miLista").append(`
                        <li class="movie-item">
                            <h3>${item.title}</h3>
                            <img class="card-img" src="https://image.tmdb.org/t/p/w500${item.poster_path}" />
                            <p class="description">${item.overview}</p>
                        </li>
						`);

					});
				},

				// ERROR: Se ejecuta si la peticion falla (sin internet, API caida, etc.).
				// MEJORA: El callback error recibe parametros utiles:
				//   error: function(jqXHR, textStatus, errorThrown) {
				//       console.log("Status:", jqXHR.status);  // Ej: 404, 500
				//       console.log("Error:", errorThrown);     // Ej: "Not Found"
				//   }
				error: function(){
					alert('Error al buscar la palabra');
				}
			});
		} else {
			// Si el input esta vacio, se muestra una alerta al usuario.
			// MEJORA: En vez de alert(), mostrar un mensaje en la pagina:
			//   miLista.html('<li class="text-danger">Debes ingresar una palabra</li>');
			alert('Debes ingresar una palabra para buscar');
		}
	});
});

// =============================================================================
// FLUJO COMPLETO DE LA BUSQUEDA:
//
// 1. Usuario escribe "Avengers" en el input
// 2. Usuario hace click en "Buscar"
// 3. JavaScript lee el valor: "Avengers"
// 4. Se valida que no este vacio (OK)
// 5. Se codifica: encodeURIComponent("Avengers") = "Avengers"
// 6. Se construye la URL: ...&query=Avengers
// 7. Se envia la peticion GET al servidor de TMDB
// 8. TMDB responde con JSON: { results: [...] }
// 9. Se limpia la lista anterior: empty()
// 10. Se itera sobre cada resultado y se genera HTML
// 11. Se agrega cada <li> a la lista: append()
//
// EJERCICIOS SUGERIDOS:
// 1. Agrega busqueda con Enter (evento keypress, keyCode === 13)
// 2. Agrega un mensaje "Sin resultados" cuando data.results esta vacio
// 3. Maneja el caso de poster_path == null (imagen por defecto)
// 4. Agrega un indicador de carga (spinner) mientras busca
// 5. Reescribe esta funcionalidad usando fetch() en vez de $.ajax()
// =============================================================================
