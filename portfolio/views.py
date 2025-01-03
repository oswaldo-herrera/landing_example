from django.shortcuts import render
from .models import Project,ImageHeader


def home(request):
    projects = Project.objects.all()
    imgHeader = ImageHeader.objects.all()
    return render(request, "home.html", {"projects": projects, "imgHeader": imgHeader})
