from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def projects(request):
    # return HttpResponse("This is my page")
    return render(request, "projects/projects.html")


def project(request, pk):
    # return HttpResponse(f"This is the {pk} product")
    return render(request, "projects/single-project.html")
