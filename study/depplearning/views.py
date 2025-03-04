from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def deep_lear(request):
    return HttpResponse('<h2>This is Learning zone! </h2> ')