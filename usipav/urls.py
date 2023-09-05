from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("calculadora", views.calculadora, name="calculadora"),
    path("londrina", views.londrina, name="londrina"), 
    path("filmes", views.filmes, name="filmes"),
    path("form", views._form, name="form"), 
]
