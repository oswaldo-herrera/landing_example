from django import forms
from .models import Project,ImageHeader

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