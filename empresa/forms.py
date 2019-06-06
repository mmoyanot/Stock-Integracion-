from django import forms
from .models import empresaDatos
from django.contrib.admin.widgets import FilteredSelectMultiple

class empresaForm(forms.ModelForm):
    class Meta:
        model = empresaDatos
        fields = [
            'nombreEmpresa',
            'rutEmpresa',
        ]


