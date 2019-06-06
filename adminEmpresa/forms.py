from django import forms
from .models import adminDatos
from django.contrib.admin.widgets import FilteredSelectMultiple

class adminForm(forms.ModelForm):
    class Meta:
        model = adminDatos
        fields = [
            'nomAdmin',
            'rutAdmin',
            'emailAdmin',
            'passAdmin', 
        ]



