from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view( request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    return render(request, "usuarios/home.html",{})

def quienes_somos_view(request, *args, **kwargs):

    return render(request, "usuarios/quienes_somos.html",{})


def admin_view( request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    return render(request, "usuarios/admin_page.html",{})

