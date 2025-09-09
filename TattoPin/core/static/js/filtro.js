document.addEventListener("DOMContentLoaded", function () {
    const categoriaSelect = document.getElementById("categoria");
    const precioSelect = document.getElementById("orden-precio");
    const galleryItems = document.querySelectorAll(".gallery-item");

    function aplicarFiltros() {
        const categoriaSeleccionada = categoriaSelect.value.trim().toLowerCase(); 
        const ordenPrecio = precioSelect.value;

        let itemsArray = Array.from(galleryItems);

        // Filtrar por categoría usando el nombre
        itemsArray.forEach(item => {
            const categoria = item.getAttribute("data-categoria").trim().toLowerCase(); 
            if (categoriaSeleccionada === "" || categoria === categoriaSeleccionada) {
                item.style.display = "block";
            } else {
                item.style.display = "none";
            }
        });

        // Filtrar solo los visibles para ordenar
        let itemsVisibles = itemsArray.filter(item => item.style.display !== "none");

        // Ordenar por precio
        itemsVisibles.sort((a, b) => {
            const precioA = parseFloat(a.getAttribute("data-precio"));
            const precioB = parseFloat(b.getAttribute("data-precio"));
            return ordenPrecio === "asc" ? precioA - precioB : precioB - precioA;
        });

        // Reordenar los elementos en la galería
        const galleryContainer = document.querySelector(".gallery-container");
        itemsVisibles.forEach(item => galleryContainer.appendChild(item));
    }

    categoriaSelect.addEventListener("change", aplicarFiltros);
    precioSelect.addEventListener("change", aplicarFiltros);
});
