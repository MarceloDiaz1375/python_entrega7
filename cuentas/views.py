from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegistroForm, PerfilForm
from django.contrib.auth.decorators import login_required
from .models import Perfil

# Create your views here.
@login_required
def editar_perfil(request):
    perfil, creado = Perfil.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect("lista_posts")
    else:
        form = PerfilForm(instance=perfil)
    return render(request, "registro/editar_perfil.html", {"form": form})

@login_required
def perfil(request):
    perfil, creado = Perfil.objects.get_or_create(user=request.user)
    return render(request, "registro/perfil.html", {"perfil": perfil})

def registro(request):
    if request.user.is_authenticated:
        return redirect('lista_posts')  # Redirige a la lista de posts si el usuario ya está autenticado
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(
                user=user,
                link_web=form.cleaned_data["link_web"],
            )
            login(request, user)  # Inicia sesión automáticamente después del registro
            messages.success(request, f'¡Bienvenido {user.username}! Ahora estás conectado.')
            return redirect('lista_posts')  # Redirige a la lista de posts después del registro
    else:
        form = RegistroForm()
    return render(request, 'cuentas/registro.html', {'form': form})