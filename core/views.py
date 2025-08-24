import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .forms import TattooForm, RegistroUserForm, EditarUserForm
from .models import Tattoo, Categoria, Carrito
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

def perfil(request):
    if request.method == 'POST':
        form = EditarUserForm(request.POST, instance=request.user)  # Cargamos los datos del usuario en el formulario
        if form.is_valid():
            form.save()  # Guardamos los cambios en el perfil
            return redirect('perfil')  # Redirigimos al perfil después de guardar
    else:
        form = EditarUserForm(instance=request.user)  # Cargamos los datos del usuario en el formulario
    
    return render(request, 'registration/perfil.html', {'form': form})

def menu(request):
    return render(request, 'menu.html')

def acercade(request):
    return render(request, 'acercade.html')

def carrousel(request):
    return render(request, 'Carrousel.html')

def formulario(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=='POST':
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                                password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request, "Registro exitoso, redirigiendo a pagina de inicio ... ")
        data["form"]=formulario
    return render(request, 'registration/formulario.html',data)

def galeria(request):
    return render(request, 'galeria.html')

def login_view(request):
    return render(request, 'registration/login.html')


def form_tattoo(request):
    if request.method=='POST': 
        tattooForm = TattooForm(request.POST, request.FILES)
        if tattooForm.is_valid():
            tattooForm.save()
            return redirect('listado')
    else:
        tattooForm= TattooForm()
    return render(request, 'form_tattoo.html', {'tattoo_form': tattooForm})

def eliminar(request, id):
     tattooEliminado = Tattoo.objects.get(codigo=id)   #select * from tattoo where codigo=id
     tattooEliminado.delete()
     return redirect ('listado')

def modificar(request, id):
     tattooModificado=Tattoo.objects.get(codigo=id)
     datos = {
          'form' : TattooForm(instance=tattooModificado)
     }
     if request.method=='POST':
          formulario = TattooForm(data=request.POST, instance=tattooModificado)
          if formulario.is_valid:
               formulario.save()
               return redirect('listado')
     return render(request, 'modificar.html', datos)

def crear(request):
    if request.method=="POST":
        tattooform=TattooForm(request.POST,request.FILES)
        if tattooform.is_valid():
            tattooform.save()     #similar al insert en función
            return redirect ('otra')
    else:
        tattooform=TattooForm()
    return render (request, 'form_tattoo', {'tattooform': tattooform})

def listado(request):
	# accedemos al objeto que contiene los datos de la base
	# el método all traerá todos los tatuajes que estan en la tabla, es como el  select
	tattoos= Tattoo.objects.all()
	#ahora crearemos un diccionario donde pasaremos los datos del tatuaje al template

	#ahora se agrega para enviarlo al template y se manda la variable datos que es donde queda el diccionario
	return render(request, 'listado.html',context={'datos':tattoos})


def cerrar(request):
    logout(request)
    return redirect('menu')

def registrando(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=='POST':
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                                password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request, "Registro exitoso")
            return redirect('menu')
        data["form"]=formulario
    return render(request, 'registration/formulario.html',data)

def tienda(request):
    tattoos=Tattoo.objects.all()
    categorias = Categoria.objects.filter(tattoo__isnull=False).distinct()
    return render(request, 'tienda.html', {'datos': tattoos, 'categorias': categorias})

def carrito(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Debes iniciar sesión para ver tu carrito.")
        return redirect('login')

    carrito_items = Carrito.objects.filter(usuario=request.user)
    total_precio = sum(item.tattoo.precio for item in carrito_items)

    return render(request, 'carrito.html', {'carrito': carrito_items, 'total_precio': total_precio})

def agregar_al_carrito(request, tattoo_id):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Debes iniciar sesión para agregar productos al carrito."}, status=403)

        tattoo = get_object_or_404(Tattoo, codigo=tattoo_id)

        # Asegurarse de que el producto no esté ya en el carrito
        carrito_item, created = Carrito.objects.get_or_create(usuario=request.user, tattoo=tattoo)
        if not created:
            return JsonResponse({"error": "Este producto ya está en el carrito."}, status=400)

        return JsonResponse({"message": "Producto agregado al carrito."})

    return JsonResponse({"error": "Método no permitido."}, status=405)


@csrf_exempt  # Permitir peticiones AJAX sin problema de CSRF
def eliminar_del_carrito(request, tattoo_id):
    if request.method == "POST" and request.user.is_authenticated:
        tattoo = get_object_or_404(Tattoo, codigo=tattoo_id)
        carrito_item = Carrito.objects.filter(usuario=request.user, tattoo=tattoo).first()
        
        if carrito_item:
            carrito_item.delete()
            return JsonResponse({"success": True})

    return JsonResponse({"success": False, "error": "No se pudo eliminar el producto."}, status=400)