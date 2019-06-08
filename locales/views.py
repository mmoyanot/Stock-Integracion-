from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .forms import LocalForm
from .models import localDatos
# Create your views here.

def vista_crear_local(request):
    form = LocalForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LocalForm()
    
    context = {
        'form' : form
    }

    return render(request, "locales/crear_local.html", context)

def vista_listar_local(request):
    queryset = localDatos.objects.all()
    context = {
        "lista_Locales": queryset
    }
    return render(request, "locales/select_local.html", context)

def redir_Productos(request, pk):
    local = get_object_or_404(localDatos, pk=pk)
    return render(request, 'productos/lista.html', {'local': local})

