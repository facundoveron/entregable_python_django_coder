from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "resumen", "contenido", "imagen", "estado"]

        labels = {
            "titulo": "Título del post",
            "resumen": "Resumen breve",
            "contenido": "Contenido del post",
            "imagen": "Imagen de portada",
            "estado": "Estado",
        }

        widgets = {
            "titulo": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Escribe el título del post",
            }),
            "resumen": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Un breve resumen del artículo (opcional)",
            }),
            "contenido": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 10,
                "placeholder": "Escribe el contenido del post...",
            }),
            "imagen": forms.FileInput(attrs={
                "class": "form-control",
            }),
            "estado": forms.Select(attrs={
                "class": "form-select",
            }),
        }
