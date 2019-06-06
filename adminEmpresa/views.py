from django.shortcuts import render
from .forms import adminForm

# Create your views here.

def vista_crear_admin(request):
    form = adminForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = adminForm()
        
    
    context = {
        'form' : form
    }

    return render(request, "administrador/registro_admin.html", context)

