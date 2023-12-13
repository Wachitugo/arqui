function entrar() {
  var username = document.getElementById('nom').value;
  var password = document.getElementById('con').value;

  // Obtén el token CSRF de la cookie
  var csrftoken = getCookie('csrftoken');

  $.ajax({
    url: '/login/',
    method: 'POST',
    headers: {
      'X-CSRFToken': csrftoken
    },
    data: {
      username: username,
      password: password
    },
    success: function(response) {
      if (response.success) {
        alert('Inicio de sesión exitoso');
        window.location.href = '/';
        if (response.isAdmin) {  // Si el usuario es un administrador
          var adminButton = document.getElementById('adminButton');
          if (adminButton) {  // Si el botón de administración existe
            adminButton.style.display = 'block';  // Muestra el botón de administración
          }
        }
      } else {
        alert(response.error);  // Muestra el error si la respuesta no es exitosa
      }
    }
  });
}

// Función para obtener una cookie por su nombre
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
  







