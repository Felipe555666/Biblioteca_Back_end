from django.contrib import admin
from django.urls import path, include
from Biblioteca_project.views import InicioPaginaView, MenuPrincipalView, AutoresView, LectoresView, LibrosView

urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('', InicioPaginaView.as_view(), name='inicio'), # la ruta raíz que apunta a la vista de inicio
    path('menu/', MenuPrincipalView.as_view(), name='menu'), #ruta para el menú principal
    path('Biblioteca_project/libros/', LibrosView.as_view(), name='libros'),
    path('Biblioteca_project/autores/', AutoresView.as_view(), name='autores'),
    path('Biblioteca_project/lectores/', LectoresView.as_view(), name='lectores'),
    path('Biblioteca_project/', include('Biblioteca_project.urls')),
]