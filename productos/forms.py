from django import forms
from .models import Productos

from django.contrib.admin.widgets import FilteredSelectMultiple

from checkboxselectmultiple.widgets import CheckboxSelectMultiple

#from django.contrib.admin.widgets import FilteredSelectMultiple #(?)

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            'nombre',
            'descripcion',
            'precio' 
        ]
        
##################

class UserlistForm(forms.Form):
    users = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label="Notify and subscribe users to this post:")

"""class RawListaProductosForm(forms.Form):
    title = forms.MultipleChoiceField(
        required=False,
        label='Nombre',
        widget=CheckboxSelectMultiple(),
        choices=Productos.nombre
    )

    class Meta:
        model = Productos
        fields = ('nombre',)

"""





#class YourModelForm(forms.ModelForm):
 #   class Meta:
  #      model = Productos.nombre
   #     widgets = {'name_of_manytomanyfield': forms.widgets.CheckboxSelectMultiple() }
    #    """


"""MY_CHOICES = (('item_key1', 'Item title 1.1'),
              ('item_key2', 'Item title 1.2'),
              ('item_key3', 'Item title 1.3'),
              ('item_key4', 'Item title 1.4'),
              ('item_key5', 'Item title 1.5'))


class MyForm(forms.Form):

    choice_fields = forms.MultipleChoiceField(
        choices=MY_CHOICES, widget=CheckboxSelectMultiple)

    model_choice_fields = forms.ModelMultipleChoiceField(
        queryset=queryset, widget=CheckboxSelectMultiple)


class MyModelForm(forms.ModelForm):

    class Meta:
        model = MyModel
        widgets = {
            'my_fields': CheckboxSelectMultiple,
        }"""