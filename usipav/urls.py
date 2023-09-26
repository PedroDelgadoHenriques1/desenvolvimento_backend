from django.urls import path

from . import views

app_name = "usipav"
urlpatterns = [
    path("", views.index, name="index"),
    path("calculadora", views.calculadora, name="calculadora"),
    path("londrina", views.londrina, name="londrina"), 
    path("filmes", views.filmes, name="filmes"),
    path("form", views._form, name="form"), 
    path("modelform", views.form_produto, name="modelform"),
    path("base", views.base, name="base"),
    path("informacao", views.informacao, name="informacao")
]
