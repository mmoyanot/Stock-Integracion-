from django.shortcuts import render

from .models import Productos, productosLocal

from .forms import ProductosForm, ProductosLocalForm
# Create your views here.


def vista_lista_productos(request):
    queryset1 = Productos.objects.all()
    queryset2 = productosLocal.objects.all()
    context = {
        "listaGeneral": queryset1,
        "lista_x_local": queryset2
    }
    return render(request, "productos/lista.html", context)



def vista_crear_productos(request):
    form = ProductosForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductosForm()
    
    context = {
        'form' : form
    }

    return render(request, "productos/crear_productos.html", context)





#def vista_lista_productos(request):
    #obj = Productos.objects.get(id=1)
    #context = {
     #   "nombre"      : obj.nombre,
      #  "descripcion" : obj.descripcion,
       # "precio"      : obj.precio
    #}
    #context = {
     #   'object' : obj
    #}
    #return render(request, "productos/lista.html", context)


