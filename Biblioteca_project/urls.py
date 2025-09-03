from django.urls import path, include 
from rest_framework import routers 
from . import views 

router = routers.DefaultRouter() # este elemento enrutador permite manejar múltiples rutas. 
router.register(r'v1/comuna', views.ComunaViewSet)
router.register(r'v1/nacionalidad', views.NacionalidadViewSet)
router.register(r'v1/direccion', views.DireccionViewSet)
router.register(r'v1/autor', views.AutorViewSet)
router.register(r'v1/biblioteca', views.BibliotecaViewSet)
router.register(r'v1/categoria', views.CategoriaViewSet)
router.register(r'v1/libro', views.LibroViewSet)
router.register(r'v1/lector', views.LectorViewSet)
router.register(r'v1/prestamo', views.PrestamoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
