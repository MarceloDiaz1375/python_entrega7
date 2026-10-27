
from django import forms
from .models import Post

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Tu nombre")
    correo = forms.EmailField(label="Tu correo electrónico")
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea
    )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'estado', 'imagen']
        labels = {
            'titulo': 'Título del post',
            'contenido': 'Contenido del post',
            'estado': 'Estado del post',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ingrese el título del post'}),
            'contenido': forms.Textarea(attrs={'placeholder': 'Ingrese el contenido del post'}),
        }