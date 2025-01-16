from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.renderPosts, name="posts"),
    path("<int:post_id>", views.post_detail, name="post_detail"),
    path("dashboard-forms", views.DashboardView.as_view(), name="dashboard_forms"),
    path("crear-portafolio", views.ProjectCreateView.as_view(), name="crear_portafolio"),
    path("imagen-header", views.ImageCreateHeader.as_view(), name="imagen_header"),
    path("imagen-spot", views.ImageCreateSpot.as_view(), name="imagen_spot"),
    path("text-spot", views.TextCreateSpot.as_view(), name="texto_spot"),
    path("titulo-spot", views.TituloSpotView.as_view(), name="titulo_spot"),
    path("seccion-uno", views.SeccionUnoView.as_view(), name="seccion_uno"),
    path("seccion-dos", views.SeccionDosView.as_view(), name="seccion_dos"),
    path("video-view", views.VideoView.as_view(), name="video_view"),
]
