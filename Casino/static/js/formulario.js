$.validator.addMethod("correito", function (value, element) {
    var pattern = /^([a-zA-Z0-9_.-])+@([a-zA-Z0-9_.-])+\.([a-zA-Z])+([a-zA-Z])+/;
    return this.optional(element) || pattern.test(value);
 }, "Por favor, escribe una dirección de correo válida");

 $.validator.addMethod("nombresito", function (value, element) {
    var pattern = /^[a-zA-Z]+$/;
    return this.optional(element) || pattern.test(value);
 }, "Por favor, escribe un nombre válido");

 $.validator.addMethod("asuntito", function (value, element) {
    var pattern = /^[a-zA-Z]+$/;
    return this.optional(element) || pattern.test(value);
 }, "Por favor, escribe un asunto válido");


 
$("#formulario").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 3,
            maxlength: 40,
            nombresito: true
        },
        email: {
            required: true,
            email: true,
            correito: true
        },
        
        subject:{
            required: true,
            minlength: 10,
            maxlength: 30,
            asuntito: true
        },

        comentario:{
            required: true,
            minlength: 30
        }
    }
})

$("#enviar").click(function(){
    if($("#formulario").valid() == false){
        return; 
    } 
    let nombre = $("nombre").val()
    let email = $("email").val()
    let subject = $("subject").val()
    let comentario = $("comentario").val()
    
})

jQuery.extend(jQuery.validator.messages, {
    required: "Este campo es obligatorio.",
    remote: "Por favor, rellena este campo.",
    email: "Por favor, escribe una dirección de correo válida",
    url: "Por favor, escribe una URL válida.",
    date: "Por favor, escribe una fecha válida.",
    dateISO: "Por favor, escribe una fecha (ISO) válida.",
    number: "Por favor, escribe un número entero válido.",
    digits: "Por favor, escribe sólo dígitos.",
    creditcard: "Por favor, escribe un número de tarjeta válido.",
    equalTo: "Por favor, escribe el mismo valor de nuevo.",
    accept: "Por favor, escribe un valor con una extensión aceptada.",
    maxlength: jQuery.validator.format("Por favor, no escribas más de {0} caracteres."),
    minlength: jQuery.validator.format("Por favor, no escribas menos de {0} caracteres."),
    rangelength: jQuery.validator.format("Por favor, escribe un valor entre {0} y {1} caracteres."),
    range: jQuery.validator.format("Por favor, escribe un valor entre {0} y {1}."),
    max: jQuery.validator.format("Por favor, escribe un valor menor o igual a {0}."),
    min: jQuery.validator.format("Por favor, escribe un valor mayor o igual a {0}.")
  });