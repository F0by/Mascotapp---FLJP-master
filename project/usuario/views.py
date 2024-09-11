from django.shortcuts import render
from .models import Usuario

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioCreacionUsuarioPersonalizado as RegisterForm
from .forms import UpdateUserForm
from django.contrib.auth.models import User
from core.views import login


def home(request):
    return render(request, 'core/index.html')

# TODO: Renombrar a user_login
def login(request):
    login(request)
    return render(request, 'core/login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)  
            return redirect('core:home')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

def editar_usuario(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_edit_form = UpdateUserForm(request.POST or None, instance=current_user)

    if user_edit_form.is_valid():
        user_edit_form.save()
        auth_login(request, current_user)  
        return redirect('core:home')
        
    return render(request, 'usuario/editar_usuario.html', {'form': user_edit_form})
    
# TODO: Eliminar de usuario y utilizar en /core
def sobre_mi(request):
    return render(request, 'core/sobre_mi.html')


def home(request):
    usuarios = Usuario.objects.all()
    context = {"usuarios": usuarios}
    return render(request, "usuario/index.html", context)