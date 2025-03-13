from django.urls import path
from . import views

urlpatterns = [
    path('ln',views.machine),
    path('lr/',views.machine_1),

]
