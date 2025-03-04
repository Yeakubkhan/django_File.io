from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def machine(request):
    return HttpResponse("<h1> Amar sonar bangla ami tomay Valo basi! </h1> ")

def lear(request):
    return HttpResponse("<h4> Django is a very dificult framwork </h4> ")

def About_us(request):
    return HttpResponse("<h1> Amara apnaderke dicci django free curce </h1> <br> <h3> apnara chaile ekhoni jog dite paren </h3>")

