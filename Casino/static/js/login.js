
function entrar() {
  event.preventDefault();
  

  var modal = document.getElementById('cuadro');
  var nom = document.getElementById('nom').value
  var con = document.getElementById('con').value

  if (modal && nom === "admin" && con === "admin" ) {
      var admin = 1
      modal.style.display = "none";
      var btnAdministrar = document.getElementById('btnAdministrar');
      if (btnAdministrar) {
          btnAdministrar.disabled = false;
      }
  else if (modal && nom1 === "admin" && con1 === "admin") {
    modal.style.display = "none";
    var btnAdministrar = document.getElementById('btnAdministrar');
    if (btnAdministrar) {
      btnAdministrar.disabled = false;
    }
  }
  else if (modal) {
      var admin = 0
      modal.style.display = "none";
      var btnAdministrar = document.getElementById('btnAdministrar');
      if (btnAdministrar) {
          btnAdministrar.disabled = true;
      }
  }
}}



window.onload = function() {
    var modal = document.getElementById("cuadro");
    
    // Comprobar si el modal ya se ha mostrado anteriormente
    var modalShown = sessionStorage.getItem("modalShown");
    
    if (!modalShown) {
        // Mostrar el modal si no se ha mostrado anteriormente
        modal.style.display = "block";
        sessionStorage.setItem("modalShown", true);
    }
    const urlParams = new URLSearchParams(window.location.search);
    const nom1 = urlParams.get('nom');
    const con1 = urlParams.get('con');

    if (nom1 === 'admin' && con1 === 'admin') {
      var btnAdministrar = document.getElementById('btnAdministrar');
      if (btnAdministrar) {
        btnAdministrar.disabled = false;
      }
    }
    
}

