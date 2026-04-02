$(document).ready(function(){
	$("#boton-obtener").on("click", obtenerCatalogo);

	var listaPeliculas = $("#lista-pelis");

	function obtenerCatalogo() {
//		listaPeliculas.empty();
//		listaPeliculas.hide();		
		$.ajax({
			//url: "https://randomuser.me/api/?results=8&nat=au,fr,es&inc=gender,name,picture,email,nat",
			url: "http://api.themoviedb.org/3/discover/movie?certification_country=MX&primary_release_date.gte=2018-08-01&primary_release_date.lte=2018-09-20&language=es&total_results=3&api_key=3356865d41894a2fa9bfa84b2b5f59bb",
			success: function(respuesta) {

				setTimeout(function () {
					console.log(respuesta);
					listaPeliculas.empty();
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
						crearModal(index, elemento.overview);
			
					});
					listaPeliculas.slideDown("slow");
				}, 3000);

			},
			error: function() {
				console.log("No se ha podido obtener la información");
			},
			beforeSend: function() { 
				console.log('CARGANDO');
				listaPeliculas.empty();
				listaPeliculas.append('<div class="text-center"><img src="images/loading.gif" /></div>');
			},
		});

	}

});


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

    $('#modals').append(htmlModal);
}