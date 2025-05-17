from django.urls import path
from . import views

urlpatterns = [
    path('',views.about1),
    path('t/',views.tabele)
]
