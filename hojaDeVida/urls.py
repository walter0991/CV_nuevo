"""hojaDeVida URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from typing import Pattern
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from CVapp import views

from django.conf import settings
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG404:
    urlpatterns += Pattern('',
        (r'^static/(?P<path>.*)$', 'Django.views.static.serve',
         {'document_root': os.path.join(os.path.dirname(__file__), 'static')} ),
    )
