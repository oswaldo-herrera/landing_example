from django import forms
from .models import Project,ImageHeader,ImagenSpot,TextSpot,TituloSpot,Video,SeccionUno,SeccionDos

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'url', 'date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
class ImageHeaderForm(forms.ModelForm):
    class Meta:
        model = ImageHeader
        fields = ['title',  'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),            
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ImagenSpotForm(forms.ModelForm):
    class Meta:
        model = ImagenSpot
        fields = ['image','imagen_dos','imagen_tres','imagen_cuatro','title']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen_dos': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagen_tres': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagen_cuatro': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            
        }

class TextSpotForm(forms.ModelForm):
    class Meta:
        model = TextSpot
        fields = ['title', 'subtitle', 'title_boton','subtitulo_segunda_seccion','titulo_uno','subtitulo_uno','titulo_dos','subtitulo_dos','titulo_tres','subtitulo_tres']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'title_boton': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo_segunda_seccion': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo_uno': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo_uno': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo_dos': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo_dos': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo_tres': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo_tres': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
class TituloSpotForm(forms.ModelForm):
    class Meta:
        model = TituloSpot
        fields = ['titulo', 'subtitulo', 'boton']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'boton': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
class SeccionUnoForm(forms.ModelForm):
    class Meta:
        model = SeccionUno
        fields = ['titulo_uno','subtitulo_uno']
        widgets = {
            'titulo_uno': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo_uno': forms.TextInput(attrs={'class': 'form-control'}),
            
            
        }
class SeccionDosForm(forms.ModelForm):
    class Meta:
        model = SeccionDos
        fields = ['titulo_dos','subtitulo_dos']
        widgets = {
            'titulo_dos': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo_dos': forms.TextInput(attrs={'class': 'form-control'}),
            
            
        }

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'embed_url', 'video_file']
        