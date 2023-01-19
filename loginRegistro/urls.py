from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'), 
    path('login/', views.logar, name='login'),
    path('inicio/', views.inicio, name='inicio'), 
    path('carrinho/', views.carrinho, name='carrinho'), 
    path('perfil/', views.perfil, name='perfil'), 
    path('compras/', views.compras, name='compras'), 
    path('deslogar/', views.deslogar, name='deslogar'), 
]
