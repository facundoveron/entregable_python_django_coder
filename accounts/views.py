from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm, PerfilForm
from .models import Perfil


@login_required
def perfil(request):
    perfil_obj, _ = Perfil.objects.get_or_create(user=request.user)
    posts = request.user.posts.order_by("-fecha_creacion")[:5]
    return render(request, "accounts/perfil.html", {
        "perfil": perfil_obj,
        "posts_recientes": posts,
    })


@login_required
def editar_perfil(request):
    perfil_obj, _ = Perfil.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("perfil")
    else:
        form = PerfilForm(instance=perfil_obj)

    return render(request, "accounts/editar_perfil.html", {"form": form})


def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.get_or_create(user=user)
            messages.success(request, "¡Cuenta creada exitosamente! Ya podés iniciar sesión.")
            return redirect("login")
    else:
        form = RegistroUsuarioForm()

    return render(request, "accounts/registro.html", {"form": form})
