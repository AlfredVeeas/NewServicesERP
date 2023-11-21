


jQuery(document).ready(function ($) {
  jQuery('#fichaVehiculoForm').submit(function (event) {
      event.preventDefault();

      // Utiliza FormData para serializar todos los campos, incluso aquellos vacíos
      var formData = new FormData(this);

      jQuery.ajax({
          type: 'POST',
          url: nuevaFichaURL,
          data: formData,
          processData: false,
          contentType: false,
          success: function (data) {
              console.log(data);

              if (data.redireccionar_a) {
                  console.log("Redireccionando a:", data.redireccionar_a);
                  window.location.href = data.redireccionar_a;
              } else {
                  console.error("La respuesta no contiene una URL de redirección.");
                  console.error("Mensaje de error:", data.mensaje);

                  if (data.errores_validacion) {
                      // Muestra los errores de validación en la consola
                      console.error("Errores de validación:", data.errores_validacion);
                  }
              }
          },
          error: function (data) {
              console.error("Error en la solicitud AJAX:", data);
              console.error("Mensaje de error:", data.mensaje);
          }
      });
  });

  // Llama a la función de inicialización después de que el DOM esté listo
  inicializarScripts();
});

function validarCamposVehiculos() {
  var formulario = document.getElementById("formularioVehiculos");

  // Obtener referencias a los elementos del formulario
  var campoMarca = formulario.querySelector("[name='marca']");
  var campoFechaIngreso = formulario.querySelector("[name='fechaIngreso']");
  var campoModelo = formulario.querySelector("[name='modelo']");
  var campoPatente = formulario.querySelector("[name='patente']");
  var campoChasis = formulario.querySelector("[name='chasis']");
  var campoTipoVehiculo = formulario.querySelector("[name='tipoVehiculo']");
  var campoTipoCombustible = formulario.querySelector("[name='tipoCombustible']");

  // Validar que todos los campos estén rellenados
  var camposVacios = [];
  if (campoMarca.value === "") {
    camposVacios.push("Marca de Vehículo");
  }
  if (campoFechaIngreso.value === "") {
    camposVacios.push("Fecha de Ingreso de Vehículo");
  }
  if (campoModelo.value === "") {
    camposVacios.push("Modelo del Vehículo");
  }
  // Validar que el formato de la patente sea "xx-xx-xx"
  var regex = /^[0-9]{2}-[0-9]{2}-[0-9]{2}$/;
  if (!regex.test(campoPatente.value)) {
      camposVacios.push("Patente");
  }
  if (campoChasis.value === "") {
    camposVacios.push("Chasis del Vehículo");
  }

  // Validar que el tipo de vehículo y combustible estén seleccionados
  if (campoTipoVehiculo.value === "") {
      camposVacios.push("Tipo de Vehículo");
    }
    if (campoTipoCombustible.value === "") {
      camposVacios.push("Tipo de Combustible");
    }

  // Mostrar mensaje de error si hay campos vacíos
  if (camposVacios.length > 0) {
    alert("Los siguientes campos están vacíos: " + camposVacios.join(", "));
    return false;
  }

  // Si todos los campos están rellenados, se permite enviar el formulario
  return true;
}

// Agregar evento de escucha al botón de envío
document.getElementById("GuardarFicha").addEventListener("click", validarCamposVehiculos);