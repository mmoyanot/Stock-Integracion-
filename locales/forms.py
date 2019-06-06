from django import forms
from .models import localDatos
from django.contrib.admin.widgets import FilteredSelectMultiple

class LocalForm(forms.ModelForm):
    class Meta:
        model = localDatos
        fields = [
            'direccion_local'
        ]


