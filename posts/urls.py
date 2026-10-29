from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca/', views.acerca_de, name='acerca_de'),
    path("posts/", views.lista_posts, name="lista_posts"),
]