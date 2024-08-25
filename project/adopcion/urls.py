from django.urls import path
from . import views

app_name = 'adopcion'

urlpatterns = [
    path('', views.AdopcionList.as_view(), name='adopcion_list'),
    path('detalle/<int:pk>/', views.AdopcionDetail.as_view(), name='adopcion_detail'),
    path('crear/', views.AdopcionCreate.as_view(), name='adopcion_create'),
    path('actualizar/<int:pk>/', views.AdopcionUpdate.as_view(), name='adopcion_update'),
    path('eliminar/<int:pk>/', views.AdopcionDelete.as_view(), name='adopcion_delete'),
]