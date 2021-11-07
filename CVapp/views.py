from django.shortcuts import render

from sobreMi.models import SobreMi
from experiencia.models import Experiencia
from educacion.models import Educacion
from referencia.models import Referencia
from capacitacion.models import Capacitacion
from skills.models import Skill, Desarrollo

# Create your views here.
def index(request):
    sobre_mi = SobreMi.objects.all()
    experiencia = Experiencia.objects.all() 
    educacion = Educacion.objects.all()
    referencia = Referencia.objects.all()
    capacitacion = Capacitacion.objects.all()
    skill = Skill.objects.all()
    desarrollo = Desarrollo.objects.all()
    
    return render(request, "CVapp/index.html", {'sobre_mi': sobre_mi, 'experiencia': experiencia, 'educacion':educacion, 'referencia':referencia, 'capacitacion':capacitacion, 'skill': skill, 'desarrollo': desarrollo})
