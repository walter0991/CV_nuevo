from django.contrib import admin

from experiencia.models import Experiencia

# Register your models here.
class ExperienciaAdmin(admin.ModelAdmin):
    list_display=("cargo", "empresa")



admin.site.register(Experiencia, ExperienciaAdmin)
