from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "imagen", "autor", "estado"]

        labels = {
            "titulo": "Titulo del post",
            "contenido": "Contenido del post",
            "imagen": "Imagen del post",
            "autor": "Autor del post",
            "estado": "Estado del post"
        }

        widgets = {
            "titulo": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Escribe el título del post",
                "required": "required"
            }),
            "contenido": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "Escribe el contenido del post",
                "required": "required"
            }),
            "imagen": forms.FileInput(attrs={
                "class": "form-control"
            }),
            "autor": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Escribe el autor del post",
                "required": "required"
            }),
            "estado": forms.Select(attrs={
                "class": "form-control",
                "required": "required"
            }),
        }