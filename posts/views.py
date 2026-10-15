from django.shortcuts import render
from .models import Post

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