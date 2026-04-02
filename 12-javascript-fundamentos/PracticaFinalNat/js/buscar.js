$(document).ready(function(){

	var miLista = $("#miLista");
	var busqueda = $("#busqueda");

	$("#btn-buscar").on("click", function(){
		//verificar que la palabra no esté vacía
		if(busqueda.val() != ""){

			//Obtener la palabra a buscar
			const palabra = $('#busqueda').val();
			console.log('Palabra a buscar: ' + palabra);
			alert('Vamos a buscar: ' + palabra);
			//Usar AJAX para buscar la palabra
			$.ajax({
				type: "GET",
				url: `https://api.themoviedb.org/3/search/movie?certification_country=MX&language=es&api_key=3356865d41894a2fa9bfa84b2b5f59bb&query=${encodeURIComponent(palabra)}`,
				dataType: "json",
				success: function(data){
					console.log(data);
					$("#miLista").empty();
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
				error: function(){
					alert('Error al buscar la palabra');
				}
			});
		} else {
			alert('Debes ingresar una palabra para buscar');
		}
	});
});

