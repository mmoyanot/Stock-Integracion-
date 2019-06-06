"""stock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view
from productos.views import vista_lista_productos, vista_crear_productos
from adminEmpresa.views import vista_crear_admin
from empresa.views import vista_crear_empresa
from locales.views import vista_crear_local

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('lista_productos/', vista_lista_productos),
    path('crear_productos/', vista_crear_productos),
    path('crear_admin/', vista_crear_admin),
    path('crear_empresa/', vista_crear_empresa),
    path('crear_local/', vista_crear_local),
    #path('listarr', WidgetForm)
]


