from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from .models import Perfil
from django.contrib.auth.decorators import login_required
from .forms import PerfilForm


@login_required
def pefil(request):
    perfil, creado = Perfil.objects.get_or_create(user=request.user)
    return render(request, "accounts/perfil.html", {"perfil": perfil})


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

    return render(request, "accounts/editar_perfil.html", {"form": form})

def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            user = form.save()
            Perfil.objects.create(user=user)
            return redirect("login")
        else:
            print(f"Formulario invalido {form.errors}")
    else:
        form = RegistroUsuarioForm()


    return render(request, "accounts/registro.html", {"form": form})
