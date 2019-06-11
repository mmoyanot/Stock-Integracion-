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

from pages.views import home_view, admin_view, quienes_somos_view

from productos.views import vista_lista_productos, vista_crear_productos, borrar

from adminEmpresa.views import vista_crear_admin

from empresa.views import vista_crear_empresa

from locales.views import vista_crear_local, vista_listar_local, redir_Productos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('quienes_somos', quienes_somos_view),

    path('lista_productos/', vista_lista_productos),
    path('crear_productos/', vista_crear_productos),
    path('delete/<list_id>', borrar, name="borrar"),

    path('crear_admin/', vista_crear_admin),
    path('crear_empresa/', vista_crear_empresa),

    path('crear_local/', vista_crear_local),
    path('select_local', vista_listar_local),

    #path('productos/<int:pk>',vista_lista_productos),
    path('<int:pk>/', redir_Productos, name='red_productos'),
    #path('red_prod/<pk>/', redirec_Productos)
    
]


