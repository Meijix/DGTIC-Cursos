$( document ).ready(function() {
  
  $.validate({
  	form: '#form-registro',
    modules : 'location, date, security, file',
    lang: 'es'
  });

  // Restrict presentation length
  $('#comentario').restrictLength($('#maxlength'));
});
