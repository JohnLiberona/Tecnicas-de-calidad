document.addEventListener("DOMContentLoaded", function () {
    const botonesAgregar = document.querySelectorAll(".btn-agregar-carrito");
    const carritoContenido = document.getElementById("carrito-contenido");
    const totalCarrito = document.getElementById("total-carrito");
    const finalizarCompraBtn = document.getElementById("finalizar-compra");

    // Cargar carrito desde localStorage
    let carrito = JSON.parse(localStorage.getItem("carrito")) || [];

    // Función para actualizar la vista del carrito
    function actualizarCarrito() {
        carritoContenido.innerHTML = ""; // Limpiar el carrito
        let total = 0;
    
        carrito.forEach(item => {
            const productoDiv = document.createElement("div");
            productoDiv.classList.add("producto-carrito");
            productoDiv.innerHTML = `
                <p>${item.nombre} - $${item.precio}</p>
                <button class="btn btn-danger btn-eliminar" data-id="${item.id}" data-categoria="${item.categoria}">Eliminar</button> 
            `;
            carritoContenido.appendChild(productoDiv);
            total += item.precio;  // Calculando el total
        });
    
        totalCarrito.textContent = Math.round(total);
        finalizarCompraBtn.disabled = carrito.length === 0;
    }

    // Lógica para agregar productos al carrito
    botonesAgregar.forEach(boton => {
        boton.addEventListener("click", function () {
            const id = String(this.dataset.id); // Convertir a string para asegurar la comparación
            const nombre = this.dataset.nombre;
            const precio = parseFloat(this.dataset.precio);
            const imagen = this.dataset.imagen;
            const categoria = this.dataset.categoria;

            // Verificar si el producto ya está en el carrito usando ID y categoría
            const productoExistente = carrito.find(item => item.id === id && item.nombre === nombre);

            if (!productoExistente) {
                carrito.push({ id, nombre, precio, imagen, categoria, cantidad: 1 });
                localStorage.setItem("carrito", JSON.stringify(carrito));
                actualizarCarrito();
            } else {
                alert("Este producto ya está en el carrito.");
            }
        });
    });

    // Lógica para eliminar productos del carrito
    carritoContenido.addEventListener("click", function (e) {
        if (e.target.classList.contains("btn-eliminar")) {
            const id = e.target.dataset.id;
    
            // Encontrar el índice del producto a eliminar usando SOLO el ID
            const indexToRemove = carrito.findIndex(item => item.id === id);
    
            if (indexToRemove > -1) {
                carrito.splice(indexToRemove, 1);
                localStorage.setItem("carrito", JSON.stringify(carrito));
                actualizarCarrito();
            }
        }
    });

    
    // Función para vaciar el carrito (eliminando todos los productos)
    function vaciarCarrito() {
        carrito = []; // Vaciar el carrito completamente
        localStorage.setItem("carrito", JSON.stringify(carrito));
        actualizarCarrito();
    }

    // Agregar un botón para vaciar el carrito
    const botonVaciar = document.createElement("button");
    botonVaciar.textContent = "Vaciar Carrito";
    botonVaciar.classList.add("btn", "btn-warning");
    botonVaciar.addEventListener("click", vaciarCarrito);
    document.getElementById("carrito-total").appendChild(botonVaciar);

    // Actualizar la vista inicial del carrito
    actualizarCarrito();
});
