from django.urls import path
from .views import home, MascotaList, MascotaDetail, MascotaCreate, MascotaUpdate, MascotaDelete

app_name = "mascota"

urlpatterns = [
    path("", home, name="home"),  
    path("lista/", MascotaList.as_view(), name="mascota_list"),
    path("detalle/<int:pk>/", MascotaDetail.as_view(), name="detalle_mascota"),
    path("crear/", MascotaCreate.as_view(), name="mascota_create"),
    path("actualizar/<int:pk>/", MascotaUpdate.as_view(), name="actualizar_mascota"),
    path("eliminar/<int:pk>/", MascotaDelete.as_view(), name="mascota_confirm_delete"),
]
