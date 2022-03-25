from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Create your views here.
# Create your views here.
# Create your views here.

def home(request):
    return HttpResponse("lets get started")


def places(request):
    return HttpResponse("<h1>Places</h1>")

