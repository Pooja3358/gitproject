from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inform(request):
    return HttpResponse("<h1>welcome</h1><h2>to my world</h2>")