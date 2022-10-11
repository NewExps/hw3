from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<h1>Alexis Sanchez</h1><h2>CSC 394</h2> <h3>Major: Computer Science</h3>")