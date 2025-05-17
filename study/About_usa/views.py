from django.shortcuts import render
from django.http import HttpResponse
from About_usa.models import Techarc


# Create your views here.
def about1(request):
    return render(request,'normal/about/About.html')

def tabele(request):
    teach = Techarc.objects.all()
    return render(request,'normal/t.html',{'thr':teach})