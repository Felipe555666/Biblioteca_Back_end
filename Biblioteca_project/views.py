from django.shortcuts import render
from rest_framework import viewsets 
from .serializer import ComunaSerializer, NacionalidadSerializer, DireccionSerializer, AutorSerializer, BibliotecaSerializer, CategoriaSerializer, LibroSerializer, LectorSerializer, PrestamoSerializer
from .models import Comuna, Nacionalidad, Direccion, Autor, Biblioteca, Categoria, Libro, Lector, Prestamo
from django.views.generic import TemplateView


# Create your views here.

class InicioPaginaView(TemplateView): #la vista basada en clases que renderiza la plantilla de inicio
    template_name = 'Biblioteca_project/inicio.html'

class MenuPrincipalView(TemplateView):
    template_name = 'Biblioteca_project/menu.html'

class LectoresView(TemplateView):
    template_name = 'Biblioteca_project/lectores.html'

class AutoresView(TemplateView):
    template_name = 'Biblioteca_project/autores.html'

class LibrosView(TemplateView):
    template_name = 'Biblioteca_project/libros.html'

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer 