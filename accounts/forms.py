from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["biografia", "link_web", "avatar"]
        widgets = {
            "biografia": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Cuéntanos sobre vos...",
            }),
            "link_web": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://tu-sitio.com",
            }),
            "avatar": forms.FileInput(attrs={
                "class": "form-control",
            }),
        }


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "tu@email.com",
    }))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nombre de usuario",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"class": "form-control", "placeholder": "Contraseña"})
        self.fields["password2"].widget.attrs.update({"class": "form-control", "placeholder": "Confirmar contraseña"})

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con ese email.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
