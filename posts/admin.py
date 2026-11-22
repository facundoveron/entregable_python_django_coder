from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha_creacion", "estado")
    search_fields = ("titulo", "contenido", "autor")
    list_filter = ("estado", "fecha_creacion")
    prepopulated_fields = {"slug": ("titulo",)}

admin.site.register(Post, PostAdmin)
