from django.shortcuts import render

from .models import Productos

from .forms import ProductosForm, UserlistForm
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


"""def listaCheckbox(request):
    my_form = RawListaProductosForm(request.POST or None)

    context = {
        'form' : my_form
    }

    return render(request,"productos/listarr.html", context)


    if request.method == "POST":
        my_form = RawListaProductosForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Productos.



    success_url = reverse_lazy('dashboard')
    context_object_name = 'preferences'
"""



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


def post_message(request, groupid):
    custgroup = Group.objects.get(id=groupid)
    groupusers = User.objects.filter(groups__name=custgroup.name)
 
    userlistform = UserlistForm()
 
    #This fills up the "choices"
    userlistform.fields['users'].choices = [(x.id, x) for x in User.objects.filter(groups__name=custgroup.name)]
 
    data = {"userlistform":userlistform,}
 
    return render_to_response("message/view_message.html",
                          data, context_instance=RequestContext(request))