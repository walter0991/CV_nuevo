from django.contrib import admin

from sobreMi.models import SobreMi
# Register your models here.

class SobreMiAdmin(admin.ModelAdmin):
    list_display=("nombre", "apellidos", "direccion", "telefonos", "correo")



admin.site.register(SobreMi, SobreMiAdmin)