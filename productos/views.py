from django.shortcuts import render

from .models import Productos

from .forms import ProductosForm
# Create your views here.


def vista_lista_productos(request):
    queryset = Productos.objects.all()
    context = {
        "object_list": queryset
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


