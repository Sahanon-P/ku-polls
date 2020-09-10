from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def index(request):
    return HttpResponse("Hello World. My Laptop is blew up so I use my brother laptop instead.")
