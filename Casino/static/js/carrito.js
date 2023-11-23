const btnCart = document.querySelector('.container-cart-icon')
const containerCartProducts = document.querySelector('.container-cart-products')
const botonC = document.getElementById("boton_comprar")

btnCart.addEventListener('click', () => {
    containerCartProducts.classList.toggle('hidden-cart')
})

const cartInfo = document.querySelector('.cart-product')
const rowProduct = document.querySelector('.row-product')

const productlist = document.querySelector('.container-items')

let allproducts = []


const  valortotal = document.querySelector('.total-pagar')

const countproducts = document.querySelector('#contador-productos')


productlist.addEventListener('click', e => {

    if(e.target.classList.contains('btn-add-cart')){
        const product = e.target.parentElement

        const infoproduct = {
            quantity : 1,
            title : product.querySelector('h6').textContent,
            price : product.querySelector('p').textContent
        }

        const exits = allproducts.some(product => product.title === infoproduct.title)

        if (exits){
            const products = allproducts.map(product => {
                if (product.title === infoproduct.title){
                    product.quantity++;
                    return product
                }else{
                    return product
                }
            })
            allproducts = [...products]
            
        }else{
            allproducts = [...allproducts, infoproduct]
        }

        showHTML();
        
    }
});

rowProduct.addEventListener('click', (e) => {
    if (e.target.classList.contains('icon-close')){
        const product= e.target.parentElement
        const title = product.querySelector('p').textContent;
        console.log(title)
        allproducts = allproducts.filter(
            product => product.title !== title 
        );
        console.log(allproducts)
        showHTML()
        
    }
})


const showHTML = () => {


    

    rowProduct.innerHTML = '';

    let total = 0;
    let totalofproducts = 0;

    allproducts.forEach(product => {
        const containerProduct = document.createElement('div')
        containerProduct.classList.add('cart-product')
        
        containerProduct.innerHTML = `
        
            <div class="info-cart-product">
                <span class="cantidad-producto-carrito">${product.quantity}</span>
                <p class="titulo-producto-carrito">${product.title}</p>
                <span class="precio-producto-carrito">${product.price}</span>
            </div>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="icon-close">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
            `
        rowProduct.append(containerProduct)


        product.price = product.price.split('.').join("");

        total = total + parseInt(product.quantity * product.price.slice(1))
        totalofproducts = totalofproducts + product.quantity;

        
    })

    valortotal.innerText = `$${total}`;
    countproducts.innerText = totalofproducts;
    
}
window.onclick = function(event) {
    var cuadro = document.getElementsByClassName('container-cart-products')
    if (event.target == cuadro) {
        cuadro.style.display = "none";
    }
}
function comprado(){
    alert("La petición ha sido enviada al casino.");
    botonC.addEventListener('click', () => {
        containerCartProducts.classList.toggle('hidden-cart')
    })
    
}

// Función para traducir el texto utilizando la API de Google Cloud Translation
function traducirTexto(texto, idiomaDestino) {
    const apiKey = 'AIzaSyD1DMEtsW9Uw1TkYB8ZKDVIu4XiGphn5Fg';
  
    return $.ajax({
      url: `https://translation.googleapis.com/language/translate/v2?key=${apiKey}`,
      type: 'POST',
      data: {
        q: texto,
        target: idiomaDestino
      },
      dataType: 'json'
    });
  }
  
  // Función para actualizar el contenido de la página con la traducción
  function actualizarPagina(traduccion) {
    $('body').html(traduccion);
    
    // Vuelve a vincular las funciones JavaScript después de actualizar el contenido
    $.getScript("carrito.js");
  }
  
  // Evento clic del botón para iniciar la traducción
  $('#btnTraducir').click(function() {
    const textoPagina = $('body').html();
  
    traducirTexto(textoPagina, 'en')
      .done(function(data) {
        const traduccion = data.data.translations[0].translatedText;
        actualizarPagina(traduccion);
      })
      .fail(function(error) {
        console.error('Error:', error);
      });
  });
  