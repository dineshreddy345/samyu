from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def morning(request):
    return HttpResponse('<h1> hello friends good morning<h1>')
def afternoon(request):
    return HttpResponse('<h1> hello friends good afternoon<h1>')
def evening(request):
    return HttpResponse('<h1> hello friends good evening<h1>')
