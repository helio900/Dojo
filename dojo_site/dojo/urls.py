from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('sobre/', views.sobre, name='sobre'),  # Sobre o Dojo
    path('eventos/', views.eventos, name='eventos'),  # Eventos e Fotos
    path('contato/', views.contato, name='contato'),  # Contato e Localidade
]