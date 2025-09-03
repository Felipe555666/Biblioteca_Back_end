from django.urls import path, include 
from rest_framework import routers 
from . import views 

router = routers.DefaultRouter() # este elemento enrutador permite manejar múltiples rutas. 
router.register(r'Modelo_1', views.Modelo_1_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
