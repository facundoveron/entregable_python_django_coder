from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.db.models import Q
from .models import Post
from .forms import PostForm


def inicio(request):
    posts_recientes = Post.objects.filter(estado="publicado")[:3]
    return render(request, "posts/inicio.html", {"posts_recientes": posts_recientes})


def acerca_de(request):
    return render(request, "posts/acerca.html")


def lista_posts(request):
    busqueda = request.GET.get("q", "").strip()
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    if busqueda:
        posts = posts.filter(
            Q(titulo__icontains=busqueda) |
            Q(contenido__icontains=busqueda) |
            Q(resumen__icontains=busqueda)
        )
    return render(request, "posts/lista_posts.html", {
        "posts": posts,
        "busqueda": busqueda,
    })


def detalle_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # Si el post no está publicado, solo el autor puede verlo
    if post.estado != "publicado" and request.user != post.autor:
        return HttpResponseForbidden("No puedes ver este post.")
    return render(request, "posts/detalle_post.html", {"post": post})


@login_required
def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            messages.success(request, "¡Post creado exitosamente!")
            return redirect("posts:detalle_post", slug=post.slug)
    else:
        form = PostForm()

    return render(request, "posts/post_form.html", {
        "form": form,
        "titulo_pagina": "Crear nuevo post",
        "texto_boton": "Publicar",
    })


@login_required
def editar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.autor != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este post.")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post actualizado correctamente.")
            return redirect("posts:detalle_post", slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, "posts/post_form.html", {
        "form": form,
        "post": post,
        "titulo_pagina": "Editar post",
        "texto_boton": "Guardar cambios",
    })


@login_required
def eliminar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.autor != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar este post.")

    if request.method == "POST":
        titulo = post.titulo
        post.delete()
        messages.success(request, f'El post "{titulo}" fue eliminado.')
        return redirect("posts:lista_posts")

    return render(request, "posts/post_confirm_delete.html", {"post": post})


@login_required
def mis_posts(request):
    """Vista para que el autor vea todos sus posts (incluyendo borradores)."""
    posts = Post.objects.filter(autor=request.user).order_by("-fecha_creacion")
    return render(request, "posts/mis_posts.html", {"posts": posts})
