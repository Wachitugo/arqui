$(document).ready(function() {
    console.log('cargado');
    // Inicializa el datepicker
    $('#datetimepicker').datetimepicker({
        format:'d.m.Y H:i',
        lang:'es'
    });
  
    // Maneja el click en el botón "Agendar hora"
    $('button').click(function() {
      $('#reservaModal').modal('show');
    });
  
    // Maneja el click en el botón "Aceptar"
    $('#aceptarBtn').click(function() {
      var fechaSeleccionada = $('#datetimepicker').datetimepicker('getDate');
      $('#reservaModal').modal('hide');
      alert('Tu reserva para el ' + fechaSeleccionada + ' ha sido hecha.');
    });
  });

  document.getElementById('aceptarBtn').addEventListener('click', function() {
    var fechaHoraReserva = document.getElementById('datetimepicker').value;
    document.getElementById('reservaModal').style.display = 'none';
    alert('Tu reserva ha sido hecha para el ' + fechaHoraReserva);
  });