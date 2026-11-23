from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Post(models.Model):
    ESTADOS = [
        ("borrador", "Borrador"),
        ("publicado", "Publicado"),
        ("archivado", "Archivado"),
    ]
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="borrador")
    imagen = models.ImageField(upload_to="posts/", null=True, blank=True)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    resumen = models.CharField(max_length=300, blank=True, help_text="Resumen breve del post (máx. 300 caracteres)")

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titulo)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.titulo

    def get_resumen(self):
        if self.resumen:
            return self.resumen
        words = self.contenido.split()
        return " ".join(words[:25]) + ("..." if len(words) > 25 else "")
