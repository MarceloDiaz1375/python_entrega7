
from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Tu nombre")
    correo = forms.EmailField(label="Tu correo electrónico")
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea
    )