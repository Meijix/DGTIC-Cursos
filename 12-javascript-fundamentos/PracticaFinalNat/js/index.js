$(document).ready(function(){

	$.ajax({
		url: "https://api.themoviedb.org/3/movie/upcoming?api_key=3356865d41894a2fa9bfa84b2b5f59bb&language=es",
		success: function(respuesta) {
			console.log(respuesta);
			peliculas = $('#peliculas'); //DIV donde se cargará la lista de peliculas

			setTimeout(function () {
				$('#loader').remove(); //Se elimina la imagen de "cargando" (los engranes)

				//Para cada elemento en la lista de resultados (para cada pelicula)
				$.each(respuesta.results, function(index, elemento) {
					//La función crearMovieCard regresa el HTML con la estructura de la pelicula
					cardHTML = crearMovieCard(elemento); 
					peliculas.append(cardHTML);
				});

			}, 3000); //Tarda 3 segundos en ejecutar la función de callback
			          //Sino no se vería la imagen de los engranes, da al usuario la sensación de que se está obteniendo algo.

		},
		error: function() {
			console.log("No se ha podido obtener la información");
			$('#loader').remove();
			$('#peliculas').html('No se ha podido obtener la información');
		},
		beforeSend: function() { 
			//ANTES de hacer la petición se muestra la imagen de cargando.
			console.log('CARGANDO');
			$('#peliculas').html('<img class="mx-auto d-block" id="loader" src="images/loading.gif" />');
		},
	});	

});


function crearMovieCard(movie){
	//Llega el objeto JSON de UNA película, como la regresa la API
	console.log(movie.poster_path);
    //sabemos que el directorio donde se guardan las imágenes es: https://image.tmdb.org/t/p/w500/
    //el atributo movie.poster_path del objeto movie, sólo contiene el nombre de la imagen (NO la ruta completa)

    //NOTAR que se accede al objeto JSON movie con la notación de punto para acceder a los atributos (movie.original_title).
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