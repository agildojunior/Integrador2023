from django.urls import path
from apps.core.views import cadastro, carrinho, compras, deslogar, logar, inicio, perfil, livrosEdit ,livrosEdit2
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
    path('livrosEdit/<int:id>', livrosEdit, name='livrosEdit'),
    path('livrosEdit2/<int:id>', livrosEdit2, name='livrosEdit2'),
    path('compras/', compras, name='compras'), 
    path('deslogar/', deslogar, name='deslogar'), 
]
