from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def machine(request):
    learn = "Django"
    time = " tow Hours"
    sediul = "10:30 am to 11:00 pm"
    offer={'ln':learn,'t': time, 's': sediul ,'what': 'Bacend website development!'}
    return render(request,'learning/learning.html',context=offer)
