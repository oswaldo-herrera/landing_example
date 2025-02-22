from django.shortcuts import render
from .models import Project,ImageHeader,ImagenSpot,TituloSpot,TextSpot,SeccionUno,SeccionDos,Video


def home(request):
    projects = Project.objects.all()
    imgHeader = ImageHeader.objects.last()
    imgSpot = ImagenSpot.objects.last()
    txtSpot = TextSpot.objects.last()
    secc_uno = SeccionUno.objects.last()
    secc_dos = SeccionDos.objects.last()
    video = Video.objects.last()
    return render(request, "home.html", {"projects": projects, "imgHeader": imgHeader,"imgSpot":imgSpot,"txtSpot":txtSpot,"secc_uno":secc_uno,"secc_dos":secc_dos,"video":video})


def politicasPrivacidad(request):
    return render(request, "politicas.html")

def politicasCookies(request):
    return render(request, "cookies.html")