from django.contrib import admin

from capacitacion.models import Capacitacion
# Register your models here.

class CapacitacionAdmin(admin.ModelAdmin):
    list_display = ("nombre",)

admin.site.register(Capacitacion, CapacitacionAdmin)
