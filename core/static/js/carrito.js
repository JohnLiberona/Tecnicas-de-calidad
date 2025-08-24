console.log("Carrito.js cargado correctamente");

document.addEventListener("DOMContentLoaded", function () {
    // Obtener los productos almacenados en localStorage o un arreglo vacío si no hay nada
    let carrito = JSON.parse(localStorage.getItem("carrito")) || [];
    let contenedor = document.getElementById("carrito-items");
    let totalCarrito = document.getElementById("total-carrito");

    // Función para actualizar la tabla del carrito
    function actualizarTablaCarrito(carrito) {
        contenedor.innerHTML = ""; // Limpiar la tabla

        if (carrito.length === 0) {
            contenedor.innerHTML = "<tr><td colspan='4' class='text-center'>Tu carrito está vacío.</td></tr>";
        } else {
            let totalPrecio = 0;

            carrito.forEach(producto => {
                let item = document.createElement("tr");
                item.innerHTML = `
                    <td><img src="${producto.imagen}" alt="${producto.nombre}" width="80" class="img-fluid"></td>
                    <td>${producto.nombre}</td>
                    <td>${producto.categoria}</td>
                    <td>$${producto.precio}</td>
                `;
                contenedor.appendChild(item);
                totalPrecio += producto.precio * producto.cantidad;
            });

            totalCarrito.innerText = `Total: $${Math.round(totalPrecio)}`;
        }
    }

    // Actualizar la tabla del carrito al cargar la página
    actualizarTablaCarrito(carrito);
});
