from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def about1(request):
    return render(request,'about/About.html')