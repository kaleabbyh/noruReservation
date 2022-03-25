from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Create your views here.
# Create your views here.
# Create your views here.

def home(request):
    return HttpResponse("hello everyone")


def places(request):
    return HttpResponse("<h1>Places</h1>")

