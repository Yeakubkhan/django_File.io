from django.urls import path
from . import views

urlpatterns = [
    path('',views.machine),
    path('learn/',views.lear),
    path('about_us/',views.About_us),
]
