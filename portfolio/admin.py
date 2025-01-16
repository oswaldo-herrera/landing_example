from django.contrib import admin
from .models import Project,ImageHeader,ImagenSpot,TextSpot,TituloSpot,SeccionUno,SeccionDos,Video

admin.site.register(Project)
admin.site.register(ImageHeader)
admin.site.register(TextSpot)
admin.site.register(ImagenSpot)
admin.site.register(TituloSpot)
admin.site.register(SeccionUno)
admin.site.register(SeccionDos)
admin.site.register(Video)

