"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Biblioteca_project.views import InicioPaginaView, MenuPrincipalView, AutoresView, LectoresView, LibrosView

urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('', InicioPaginaView.as_view(), name='inicio'), # la ruta raíz que apunta a la vista de inicio
    path('menu/', MenuPrincipalView.as_view(), name='menu'), #ruta para el menú principal
    path('menu/', include('Biblioteca_project.urls')),
    path('libros/', LibrosView.as_view(), name='libros'),
    path('autores/', AutoresView.as_view(), name='autores'),
    path('lectores/', LectoresView.as_view(), name='lectores'),
    path('api/', include('Biblioteca_project.urls')),
]