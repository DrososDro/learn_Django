from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def projects(request):
    return HttpResponse("This is my page")

def project(request, pk):
    return HttpResponse(f"This is the {pk} product")