from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden

def inicio(request):
    return render(request,'posts/inicio.html')

def acerca_de(request):
    return render(request,'posts/acerca.html')

def lista_posts(request):
    posts = Post.objects.all().order_by("-fecha_creacion")

    return render(request, "posts/lista_posts.html", {
        "posts": posts
    })

def detalle_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    print("Post encontrado:", post.titulo)

    return render(request, "posts/detalle_post.html", {
        "post": post
    })


@permission_required("posts.add_post")
def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            form.save()
            return redirect("posts:lista_posts")
        else:
            print(form.errors)
    else:
        form = PostForm()
    
    context = {
        "form": form,
        "titulo_pagina": "Crear post",
        "texto_boton": "Guardar"
    }
    
    return render(request, "posts/post_form.html", {
        "form": form,
        "titulo_pagina": "Crear post",
        "texto_boton": "Guardar"
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

            return redirect("posts:detalle_post", slug=post.slug)
    else:
        form = PostForm(instance=post)

    context = {
        "form": form,
        "post": post,
        "titulo_pagina": "Editar post",
        "texto_boton": "Actualizar"
    }

    return render(request, "posts/post_form.html", context)

@login_required
def eliminar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.autor != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este post.")

    if request.method == "POST":
        post.delete()
        return redirect("posts:lista_posts")
    
    context = {
        "post": post
    }

    return render(request, "posts/eliminar_post.html", context)