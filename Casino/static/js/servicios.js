$(document).ready(function() {
  console.log('cargado');

  // Maneja el click en el botón "Agendar hora"
  $('button').click(function() {
      $('#reservaModal').modal('show');
  });

  // Maneja el click en el botón "Aceptar"
  $(document).ready(function() {
    var reservas = [];

    // Maneja el click en el botón "Aceptar"
    $('#aceptarBtn').click(function() {
      var fechaSeleccionada = new Date($('#datePicker').val());
      var horaSeleccionada = $('#timePicker').val();
      var hora = parseInt(horaSeleccionada.split(':')[0]);
      var diaSemana = fechaSeleccionada.getDay();
      var reservaExistente = reservas.find(reserva => {
          var mismaFecha = reserva.fecha.getTime() === fechaSeleccionada.getTime();
          var mismaHora = Math.abs(parseInt(reserva.hora.split(':')[0]) - hora) < 1;
          return mismaFecha && mismaHora;
      });

      if (!fechaSeleccionada || !horaSeleccionada) {
          alert('Por favor selecciona una fecha y hora.');
      } else if (hora < 8 || hora > 19) {
          alert('Por favor selecciona una hora entre las 8 AM y las 7 PM.');
      } else if (diaSemana === 0 || diaSemana === 6) {
          alert('Por favor selecciona un día entre lunes y sábado.');
      } else if (reservaExistente) {
          alert('Esta fecha y hora ya ha sido reservada. Por favor selecciona otra.');
      } else {
          reservas.push({ fecha: fechaSeleccionada, hora: horaSeleccionada });
          $('#reservaModal').modal('hide');
          alert('Tu reserva para el ' + fechaSeleccionada + ' a las ' + horaSeleccionada + ' ha sido hecha.');
      }
  });

    // Maneja el click en el botón "Cerrar"
    $('.btn-secondary').click(function() {
        $('#reservaModal').modal('hide');
    });
});

  // Maneja el click en el botón "Cerrar"
  $('.btn-secondary').click(function() {
    $('#reservaModal').modal('hide');
});
});