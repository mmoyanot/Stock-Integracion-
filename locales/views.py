from django.shortcuts import render
from .forms import LocalForm
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

