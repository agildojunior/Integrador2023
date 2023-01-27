from django.urls import path
from apps.core.views import cadastro, carrinho, compras, deslogar, logar, inicio, perfil 
from apps.books.views import BookListView, BookCreateView, BookDeleteView

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'), 
    path('login/', logar, name='login'),
    path('inicio/', inicio, name='inicio'), 
    path('carrinho/', carrinho, name='carrinho'), 
    path('perfil/', perfil, name='perfil'),
    path('livros/', BookListView.as_view(), name='livros'),
    path('livros/adicionar', BookCreateView.as_view(), name='adicionarLivro'),
    path('livros/<pk>', BookDeleteView.as_view(), name='excluirLivro'),
    path('compras/', compras, name='compras'), 
    path('deslogar/', deslogar, name='deslogar'), 
]
