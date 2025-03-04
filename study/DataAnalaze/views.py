from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Data(requst):
    return HttpResponse("This is our Data Analaize Seciton! ")