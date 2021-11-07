from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from skills.models import Skill, Desarrollo
# Register your models here.
class SkillAdmin(admin.ModelAdmin):
    list_display=("nombre",)
    
class DesarrolloAdmin(admin.ModelAdmin):
    list_display=("link",)

admin.site.register(Skill, SkillAdmin)
admin.site.register(Desarrollo, DesarrolloAdmin)
