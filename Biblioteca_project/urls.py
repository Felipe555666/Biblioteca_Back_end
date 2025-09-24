from django.contrib import admin
from django.urls import path, include 
from rest_framework import routers 
from . import views 

router = routers.DefaultRouter()  # este elemento enrutador permite manejar múltiples rutas.
router.register(r'comuna', views.ComunaViewSet)
router.register(r'nacionalidad', views.NacionalidadViewSet)
router.register(r'direccion', views.DireccionViewSet)
router.register(r'autor', views.AutorViewSet)
router.register(r'biblioteca', views.BibliotecaViewSet)
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'libro', views.LibroViewSet)
router.register(r'lector', views.LectorViewSet)
router.register(r'prestamo', views.PrestamoViewSet)

urlpatterns = [
    path('', include(router.urls)), #incluye todas las rutas del enrutador
]
