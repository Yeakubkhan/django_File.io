from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def deep_lear(request):
    return render(request,'normal/depp/depp.html')