const accessKey = 'cRV-LURm5GhaZBLXuTyIhPYc9VnQZev9SJJctLG8wAc'; // Reemplaza con tu clave de acceso
const imagesContainer = document.getElementById('images-container');
const loadImagesButton = document.getElementById('load-images');
let page = Math.floor(Math.random() * 100) + 1; // Página aleatoria entre 1 y 100

async function fetchImages() {
    const query = 'tattoo'; // Palabra clave para la búsqueda
    const url = `https://api.unsplash.com/search/photos?page=${page}&query=${query}&client_id=${accessKey}&per_page=12`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        displayImages(data.results);
        page = Math.floor(Math.random() * 100) + 1; // Selecciona una nueva página aleatoria
    } catch (error) {
        console.error('Error al cargar imágenes:', error);
    }
}

// Función para mostrar las imágenes en la galería
function displayImages(images) {
    images.forEach(image => {
        const imgElement = document.createElement('img');
        imgElement.src = image.urls.small; // URL de la imagen
        imgElement.alt = image.alt_description || 'Tatuaje';
        imagesContainer.appendChild(imgElement);
    });
}

// Evento para cargar más imágenes
loadImagesButton.addEventListener('click', fetchImages);
