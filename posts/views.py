from django.shortcuts import render
from .models import Post
from .forms import ContactoForm
from django.http import HttpResponse

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