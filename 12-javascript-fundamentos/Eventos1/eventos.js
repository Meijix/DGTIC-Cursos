
//script que asigne un evento a un botón y a una imagen.
document.addEventListener("DOMContentLoaded", function() {
    function hacerClick(){
        alert("Has dado click al botón");
    }

    function pasarMouse(){
        alert("Has pasado el cursor sobre la imagen");
    }

    let botoncito = document.getElementById("boton");
    botoncito.onclick = hacerClick;

    let imagen = document.getElementById("imagen");
    imagen.onmouseover = pasarMouse;
});