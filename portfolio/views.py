from django.shortcuts import render
from .models import Project,ImageHeader,ImagenSpot,TituloSpot,TextSpot,SeccionUno,SeccionDos,Video


def home(request):
    projects = Project.objects.all()
    imgHeader = ImageHeader.objects.all()
    imgSpot = ImagenSpot.objects.all()
    txtSpot = TextSpot.objects.all()
    secc_uno = SeccionUno.objects.all()
    secc_dos = SeccionDos.objects.all()
    video = Video.objects.all()
    return render(request, "home.html", {"projects": projects, "imgHeader": imgHeader,"imgSpot":imgSpot,"txtSpot":txtSpot,"secc_uno":secc_uno,"secc_dos":secc_dos,"video":video})
