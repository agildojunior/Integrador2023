from django.urls import path
from core import views
from books.views import BookListView, BookCreateView

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'), 
    path('login/', views.logar, name='login'),
    path('inicio/', views.inicio, name='inicio'), 
    path('carrinho/', views.carrinho, name='carrinho'), 
    path('perfil/', views.perfil, name='perfil'), 
    path('produtos/', BookListView.as_view(), name='produtos'),
    path('adicionarLivro', BookCreateView.as_view(), name='adicionarLivro'),
    path('compras/', views.compras, name='compras'), 
    path('deslogar/', views.deslogar, name='deslogar'), 
]
