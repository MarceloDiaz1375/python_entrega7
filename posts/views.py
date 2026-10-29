from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import ContactoForm, PostForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# Create your views here.
def inicio(request):
    return render(request, "posts/inicio.html")

def acerca(request):
    return render(request, "posts/acerca.html")


def lista_posts(request):
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    context = {
        "posts": posts
    }
    return render(request, "posts/lista_posts.html", context)

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            correo = form.cleaned_data["correo"]
            mensaje = form.cleaned_data["mensaje"]
            print("Nombre:", nombre)
            print("Correo:", correo)
            print("Mensaje:", mensaje)
            return HttpResponse("¡Gracias por tu mensaje! Nos pondremos en contacto contigo pronto.")
    else:
        form = ContactoForm()
    return render(request, "posts/contacto.html", {
        "form": form
    })

def detalle_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "posts/detalle_post.html", {
        "post": post,
        "puede_editar": puede_editar_post(request.user, post)
    })

@login_required
def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect("detalle_post", slug=post.slug)
    else:
        form = PostForm()

    return render(request, "posts/post_form.html", {
        "form": form,
        "title": "Crear Post",
        "text_button": "Crear"
    })

def puede_editar_post(user, post):
    return user.is_authenticated and post.autor.id == user.id

@login_required
def editar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if not puede_editar_post(request.user, post):
        raise PermissionDenied("No tienes permiso para editar este post.")
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("detalle_post", slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, "posts/post_form.html", {
        "form": form,
        "post": post,
        "title": "Editar Post",
        "text_button": "Actualizar"
    })

@login_required
def eliminar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if not puede_editar_post(request.user, post):
        raise PermissionDenied("No tienes permiso para eliminar este post.")
    if request.method == "POST":
        post.delete()
        return redirect("lista_posts")
    return render(request, "posts/post_confirm_delete.html", {
        "post": post
    })
