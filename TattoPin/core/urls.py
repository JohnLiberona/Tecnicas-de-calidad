from django.urls import path
from .views import menu, acercade, carrousel, perfil, formulario, cerrar, galeria, login_view, form_tattoo, eliminar, modificar, listado, carrito ,tienda, agregar_al_carrito, eliminar_del_carrito
from . import views

urlpatterns = [
    path('', menu, name='menu'),          # Ruta para la vista del menú (Página principal)
    path('acercade/', acercade, name='acercade'),  # Ruta para la vista de "acerca de"
    path('carrousel/', carrousel, name='carrousel'),  # Ruta para el carrusel
    path('galeria/', galeria, name='galeria'),  # Ruta para la galería

    path('formulario/', formulario, name='formulario'),  # Ruta para el formulario
    path('login/', login_view, name='login'),  # Ruta para el login
    path('perfil/', perfil, name='perfil'),  # Ruta para el perfil

    path('form_tattoo', form_tattoo, name='form_tattoo' ),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name='modificar'),
    path('listado/',listado, name='listado'),

    path('tienda/',tienda , name='tienda'),
    path('agregar-al-carrito/<str:tattoo_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar-del-carrito/<str:tattoo_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('cerrar/', cerrar, name="cerrar"),
    
    path('carrito/', carrito, name='carrito'),
]
