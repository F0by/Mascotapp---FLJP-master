from django.shortcuts import render
from .models import Usuario

def home(request):
    usuarios = Usuario.objects.all()
    context = {"usuarios": usuarios}
    return render(request, "usuario/index.html", context)