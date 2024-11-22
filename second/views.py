from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def msg(request):
    return HttpResponse("<h1><marquee>WELCOME</marquee></h1>")