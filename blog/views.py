from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from portfolio.models import Project,ImageHeader,TextSpot,ImagenSpot,TituloSpot,SeccionUno,SeccionDos,Video
from portfolio.forms import ProjectForm,ImageHeaderForm,TextSpotForm,ImagenSpotForm,TituloSpotForm,SeccionUnoForm,SeccionDosForm,VideoForm


def renderPosts(request):
    total_posts = Post.objects.count()
    posts = Post.objects.order_by("-date")
    return render(request, "blog.html", {"posts": posts, "total_posts": total_posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_form'] = ProjectForm()
        context['image_header_form'] = ImageHeaderForm()
        context['image_spot_form'] = ImagenSpotForm()
        context['text_spot_form'] = TextSpotForm()
        context['seccion_uno_form'] = SeccionUnoForm()
        context['seccion_dos_form'] = SeccionDosForm()
        context['video_form'] = VideoForm()
        return context

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'dashboard.html'
    success_url = reverse_lazy('home')
class ImageCreateHeader(CreateView):
    model = ImageHeader
    form_class = ImageHeaderForm
    template_name = 'dashboard.html'
    success_url = reverse_lazy('home')
class ImageCreateSpot(CreateView):
    model = ImagenSpot
    form_class = ImagenSpotForm
    template_name = 'dashboard.html'
    success_url = reverse_lazy('home')
class TextCreateSpot(CreateView):
    model = TextSpot
    form_class = TextSpotForm
    template_name = 'dashboard.html'
    success_url = reverse_lazy('home')
class TituloSpotView(CreateView):
    model = TituloSpot
    form_class = TituloSpotForm
    template_name = 'dashboard.html'
    success_url = reverse_lazy('home')
class SeccionUnoView(CreateView):
    model = SeccionUno
    form_class = SeccionUnoForm
    template_name = 'dashboard.html'
    success_url = reverse_lazy('home')
class SeccionDosView(CreateView):
    model = SeccionDos
    form_class = SeccionDosForm
    template_name = 'dashboard.html'
    success_url = reverse_lazy('home')
class VideoView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'dashboard.html'
    success_url = reverse_lazy('home')