from django.contrib import admin

from .models import Productos 
from checkboxselectmultiple.admin import CheckboxSelectMultipleAdmin



from django.contrib import admin

#from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple


# Register your models here.
class MyAdmin(CheckboxSelectMultipleAdmin):
    pass

admin.site.register(Productos, MyAdmin)

"""class MyModelAdmin(admin.ModelAdmin):
    # ...

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'your_sortedm2m_field_name':
            kwargs['widget'] = SortedFilteredSelectMultiple()
        return super(MyModelAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)  """


class myModelAdmin(admin.ModelAdmin): 
  class Media: 
    js = ['admin/js/mselect-to-mcheckbox.js'] 
    css = { 
      'all': ('admin/css/mselect-to-mcheckbox.css') 
    }