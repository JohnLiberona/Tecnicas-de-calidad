import io
from PIL import Image
from django.test import TestCase
from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.db import IntegrityError
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Categoria, Tattoo, Carrito
from .forms import TattooForm, RegistroUserForm


def crear_imagen_falsa(nombre='test.jpg'):
    """Crea un archivo de imagen válido en memoria para las pruebas."""
    bts = io.BytesIO()
    img = Image.new("RGB", (100, 100))
    img.save(bts, 'jpeg')
    return SimpleUploadedFile(nombre, bts.getvalue(), content_type="image/jpeg")


class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.categoria = Categoria.objects.create(idCategoria=1, nombreCategoria='Realismo')
        
        self.tattoo1 = Tattoo.objects.create(
            codigo='TAT001', titulo='Leon Realista', tipo='Brazo',
            categoria=self.categoria, precio=150000, imagen=crear_imagen_falsa()
        )
        self.tattoo2 = Tattoo.objects.create(
            codigo='TAT002', titulo='Tigre Irezumi', tipo='Espalda',
            categoria=self.categoria, precio=250000, imagen=crear_imagen_falsa()
        )

    def test_creacion_tattoo(self):
        self.assertEqual(self.tattoo1.titulo, 'Leon Realista')
        self.assertEqual(self.tattoo1.categoria.nombreCategoria, 'Realismo')
        self.assertEqual(str(self.tattoo1), 'TAT001')

    def test_carrito_total_usuario(self):
        Carrito.objects.create(usuario=self.user, tattoo=self.tattoo1)
        Carrito.objects.create(usuario=self.user, tattoo=self.tattoo2)
        total_esperado = 150000 + 250000
        self.assertEqual(Carrito.total_usuario(self.user), total_esperado)

    def test_carrito_item_unico(self):
        Carrito.objects.create(usuario=self.user, tattoo=self.tattoo1)
        with self.assertRaises(IntegrityError):
            Carrito.objects.create(usuario=self.user, tattoo=self.tattoo1)


def setUp(self):
    self.user = User.objects.create_user(username='testuser', password='password123')
    
    permission = Permission.objects.get(codename='view_tattoo')
    self.user.user_permissions.add(permission)

    self.user.refresh_from_db()
    
    self.categoria = Categoria.objects.create(idCategoria=1, nombreCategoria='Realismo')
    self.tattoo = Tattoo.objects.create(
        codigo='TAT001', titulo='Leon', tipo='Brazo',
        categoria=self.categoria, precio=1000, imagen=crear_imagen_falsa()
    )

    def test_listado_muestra_tattoos(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('listado')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tattoo.titulo)

    def test_paginas_estaticas_cargan(self):
        paginas = ['menu', 'tienda', 'acercade', 'galeria']
        for pagina in paginas:
            url = reverse(pagina)
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, f"La página {pagina} falló al cargar.")

    def test_acceso_carrito_sin_login(self):
        url = reverse('carrito')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('login')))

    def test_acceso_carrito_con_login(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('carrito')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_agregar_al_carrito_ajax(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('agregar_al_carrito', kwargs={'tattoo_id': self.tattoo.codigo})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Producto agregado al carrito.')
        self.assertTrue(Carrito.objects.filter(usuario=self.user, tattoo=self.tattoo).exists())


class FormTests(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(idCategoria=1, nombreCategoria='Realismo')

    def test_tattoo_form_valido(self):
        imagen_valida = crear_imagen_falsa('form_image.jpg')
        
        form_data = {
            'codigo': 'TAT003', 'titulo': 'Serpiente', 'tipo': 'Pierna',
            'categoria': self.categoria.idCategoria, 'precio': 120000
        }
        files_data = {'imagen': imagen_valida}
        
        form = TattooForm(data=form_data, files=files_data)
        
        if not form.is_valid():
            print(form.errors.as_json())
            
        self.assertTrue(form.is_valid())

    def test_tattoo_form_invalido(self):
        form_data = {'codigo': 'TAT004', 'titulo': 'Incompleto'}
        form = TattooForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_registro_form_email_duplicado(self):
        User.objects.create_user(username='user1', password='password', email='test@example.com')
        form_data = {
            'username': 'user2', 'email': 'test@example.com', 'password': 'password'
        }
        form = RegistroUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'][0], "Este correo electrónico ya está en uso. Prueba con otro.")
