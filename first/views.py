from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def call(request):
    return HttpResponse("hello world")

