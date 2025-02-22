from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date
from urllib.parse import urlparse, parse_qs


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="productos")
    url = URLField(blank=True)
    date = DateField(default=date.today)

    def __str__(self) -> str:
        return self.title
class ImageHeader(models.Model):
    title = CharField(max_length=100)
    image = ImageField(upload_to="headers")
    date = DateField(default=date.today)

    def __str__(self) -> str:
        return self.title

class ImagenSpot(models.Model):
    image = ImageField(upload_to="spots")
    imagen_dos = ImageField(upload_to="spots",blank=True,null=True)
    imagen_tres = ImageField(upload_to="spots",blank=True,null=True)
    imagen_cuatro = ImageField(upload_to="spots",blank=True,null=True)
    date = DateField(default=date.today)
    title = CharField(max_length=100)
    
    def __str__(self):
        return str(self.title)

class TextSpot(models.Model):
    title = CharField(max_length=100)
    subtitle = CharField(max_length=100)
    title_boton = CharField(max_length=100)
    subtitulo_segunda_seccion = CharField(max_length=100,blank=True,null=True)
    titulo_uno = CharField(max_length=100,blank=True,null=True)
    subtitulo_uno = CharField(max_length=100,blank=True,null=True)
    titulo_dos = CharField(max_length=100,blank=True,null=True)
    subtitulo_dos = CharField(max_length=100,blank=True,null=True)
    titulo_tres = CharField(max_length=100,blank=True,null=True)
    subtitulo_tres = CharField(max_length=100,blank=True,null=True)
    

    def __str__(self):
        return str(self.title)
    
#### ya no esta en uso ###
class TituloSpot(models.Model):
    titulo = models.CharField(max_length=100,null=True,blank=True)
    subtitulo = models.CharField(max_length=100,null=True,blank=True)
    boton = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.titulo)
#### ya no esta en uso ###

class SeccionUno(models.Model):
    titulo_uno = models.CharField(max_length=100,null=True,blank=True)
    subtitulo_uno = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return str(self.titulo_uno)
class SeccionDos(models.Model):
    titulo_dos = models.CharField(max_length=100,null=True,blank=True)
    subtitulo_dos = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return str(self.titulo_dos)

class Video(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título del Video")
    embed_url = models.URLField(verbose_name="URL del Video",blank=True,null=True)
    video_file = models.FileField(upload_to="videos/", verbose_name="Archivo MP4", blank=True, null=True)


    def __str__(self):
        return self.title
    
    # def get_embed_url(self):
    #     """
    #     Convierte una URL estándar de YouTube en una URL para iframe.
    #     """
    #     parsed_url = urlparse(self.embed_url)
    #     if "youtube.com" in parsed_url.netloc:
    #         query_params = parse_qs(parsed_url.query)
    #         video_id = query_params.get("v", [None])[0]
    #         if video_id:
    #             return f"https://www.youtube.com/embed/{video_id}"
    #     return self.embed_url