from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Perfil

User = get_user_model()

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

    avatar = forms.ImageField(required=False, label="Avatar")
    link_web = forms.URLField(
        required=False,
        max_length=200,
        label="Sitio web",
    )

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ("biografia", "link_web", "avatar")