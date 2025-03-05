"""
URL configuration for study project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
'''# Simple methode! improt viwes
from learning import views
# Seconde Methode! Remane use
from blog import views as blg
from About_usa import views as ab
# therd methorde! Fantion calling
from DataAnalaze.views import  Data
from depplearning.views import deep_lear'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('learning.urls')),
    path('deep/',include('depplearning.urls')),
    path('data/',include('DataAnalaze.urls')),
    path('blog/',include('blog.urls')),
    path('about/',include('About_usa.urls')),
]
