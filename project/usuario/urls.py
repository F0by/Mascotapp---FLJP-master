from django.urls import path
from . import views

app_name = "usuario"

urlpatterns = [
    path("", views.home, name="home"),
    path('editar_usuario/', views.editar_usuario, name="editar_usuario"),
]
