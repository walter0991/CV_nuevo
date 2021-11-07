from django.contrib import admin

from educacion.models import Educacion

# Register your models here.
class EducacionAdmin(admin.ModelAdmin):
    list_display=("unidadEducativa", "titulo")
    
    
admin.site.register(Educacion, EducacionAdmin)