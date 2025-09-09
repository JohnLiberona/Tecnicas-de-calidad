document.addEventListener("DOMContentLoaded", function () {
    document.querySelector(".btn-finalizar").addEventListener("click", function (event) {
        event.preventDefault();

        let carrito = JSON.parse(localStorage.getItem("carrito")) || [];
        let fechaHora = document.getElementById("fecha_hora").value;
        let usuario = document.body.getAttribute("data-username") || "Usuario desconocido";
        let email = document.body.getAttribute("data-email") || "Email no disponible";
        let urlMenu = document.body.getAttribute("data-url");
        let logoURL = document.body.getAttribute("data-logo");

        if (carrito.length === 0 || !fechaHora) {
            alert("El carrito está vacío o no ha seleccionado fecha y hora.");
            return;
        }
        
        let idCompra = "ORD-" + Date.now() + "-" + Math.floor(Math.random() * 1000);
        let contenidoBoleta = `
             <div style="text-align: center;">
                <img src="${logoURL}" alt="logo" style="width: 150px; height: auto;">
                <h2>Boleta de Compra</h2>
                <p><strong>ID de Compra:</strong> ${idCompra}</p>
            </div>
            <p><strong>Cliente:</strong> ${usuario}</p>
            <p><strong>Email:</strong> ${email}</p>
            <p><strong>Fecha y Hora de cita:</strong> ${fechaHora}</p>
            <p><strong>Dirección:</strong> Av. Esq. Blanca 501, 9251863 Maipú, Región Metropolitana</p>
            <hr>
            <h3>Detalle de la compra:</h3>
            <ul>
        `;

        let total = 0;
        carrito.forEach(producto => {
            contenidoBoleta += `<li>${producto.nombre} - ${producto.categoria} - $${producto.precio}</li>`;
            total += producto.precio;
        });
        contenidoBoleta += `</ul><h3>Total: $${Math.round(total)}</h3>`;

        let ventana = window.open("", "_blank");
        ventana.document.write(`
            <html>
            <head>
                <title>Boleta de Compra</title>
                <style>
                    body { font-family: Arial, sans-serif; padding: 20px; text-align: center; }
                    h2, h3 { color: #333; }
                    ul { list-style-type: none; padding: 0; }
                    li { margin-bottom: 5px; }
                    .logo { width: 150px; height: auto; }
                </style>
            </head>
            <body>
                ${contenidoBoleta}
                <button onclick="window.print()">Imprimir Boleta</button>
            </body>
            </html>
        `);

        // Vaciar el carrito después de generar la boleta
        localStorage.removeItem("carrito");

        // Redirigir al menú después de un breve retraso
        setTimeout(() => {
            if (urlMenu) {
                window.location.href = urlMenu;
            } else {
                alert("Error: No se encontró la URL.");
            }
        }, 50);
    });
});
