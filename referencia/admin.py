from django.contrib import admin
from referencia.models import Referencia

# Register your models here.
class ReferenciaAdmin(admin.ModelAdmin):
    list_display=("nombre", "cargo", "empresa")

admin.site.register(Referencia, ReferenciaAdmin)