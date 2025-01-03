from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.renderPosts, name="posts"),
    path("<int:post_id>", views.post_detail, name="post_detail"),
    path("crear-portafolio", views.ProjectCreateView.as_view(), name="crear_portafolio"),
    path("imagen-header", views.ImageCreateHeader.as_view(), name="imagen_header"),
]
