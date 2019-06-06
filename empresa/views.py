from django.shortcuts import render
from .forms import empresaForm
# Create your views here.

def vista_crear_empresa(request):
    form = empresaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = empresaForm()
    
    context = {
        'form' : form
    }

    return render(request, "empresas/crear_empresa.html", context)

