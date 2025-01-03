from django.shortcuts import render, get_object_or_404
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from portfolio.models import Project,ImageHeader
from portfolio.forms import ProjectForm,ImageHeaderForm


def renderPosts(request):
    total_posts = Post.objects.count()
    posts = Post.objects.order_by("-date")
    return render(request, "blog.html", {"posts": posts, "total_posts": total_posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})

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