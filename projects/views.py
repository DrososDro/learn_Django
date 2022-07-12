from django.http import HttpResponse
from django.shortcuts import render

from .models import Project

# Create your views here.
prohectsList = [
    {
        "id": "1",
        "title": "Ecommerce website",
        "description": "Fully functional ecommerce website",
    },
    {
        "id": "2",
        "title": "Portfolio website",
        "description": "This was a project where i build out my portfolio",
    },
    {
        "id": "3",
        "title": "Social Network",
        "description": "Awesome open source project i am still working",
    },
]


def projects(request):
    # return HttpResponse("This is my page")
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    # return HttpResponse(f"This is the {pk} product")
    projectObj = Project.objects.get(id=pk)
    return render(
        request,
        "projects/single-project.html",
        {"projectObj": projectObj},
    )
