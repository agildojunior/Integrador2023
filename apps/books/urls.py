from django.urls import path
from core.views import cadastro, carrinho, compras, deslogar, logar, inicio, make_transaction, perfil, livrosEdit,livrosEdit2, add_book_in_cart, delete_book_in_cart, infoLivro, inicioCategoria, userEdit
from books.views import BookListView, BookCreateView, BookDeleteView

# ---para a API--- #
from .views import BookListCreate, BookRetrieveUpdateDestroy
# ---/para a API--- #

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'), 
    path('login/', logar, name='login'),
    path('inicio/', inicio, name='inicio'),
    path('inicioCategoria/<str:nome>', inicioCategoria, name='inicioCategoria'),
    path('infoLivro/<int:id>', infoLivro, name='infoLivro'),
    path('carrinho/', carrinho, name='carrinho'), 
    path('perfil/', perfil, name='perfil'),
    path('userEdit/', userEdit, name='userEdit'),
    path('livros/', BookListView.as_view(), name='livros'),
    path('livros/adicionar', BookCreateView.as_view(), name='adicionarLivro'),
    path('livros/<pk>', BookDeleteView.as_view(), name='excluirLivro'),
    path('livrosEdit/<int:id>', livrosEdit, name='livrosEdit'),
    path('livrosEdit2/<int:id>', livrosEdit2, name='livrosEdit2'),
    path('compras/', compras, name='compras'), 
    path('deslogar/', deslogar, name='deslogar'),
    path('carrinho/<id_book>', add_book_in_cart, name='adicionarCarrinho'),
    path('carrinho/excluir/<id_book>', delete_book_in_cart, name='apagarLivroCarrinho'),
    path('carrinho/comprar/', make_transaction, name='comprarLivro'),

    # ---para a API--- #
    path('', BookListCreate.as_view(), name='book-list-create'),
    path('<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-rud'),
    # ---/para a API--- #
]
