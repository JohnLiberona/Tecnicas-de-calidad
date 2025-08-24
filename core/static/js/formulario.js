document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.getElementById("registroForm");
	const urlMenu = document.body.getAttribute("data-urlForm");
	
    formulario.addEventListener("submit", function (event) {
        event.preventDefault(); // Evita el envío automático del formulario

        // Simulación de registro exitoso
        setTimeout(() => {
            alert("Registro exitoso. Serás redirigido al menú.");
            if (urlMenu) {
                window.location.href = urlMenu; // Redirige al menú
            } else {
                console.error("Error: data-url no está definido en el body.");
            }
        }, 500);  // Retraso breve para simular procesamiento
    });
});