from django.urls import path
# ---para a API--- #
from books.views import BookListCreate, BookRetrieveUpdateDestroy
# ---/para a API--- #
urlpatterns = [
    # ---para a API--- #
    path('', BookListCreate.as_view(), name='book-list-create'),
    path('<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-rud'),
    # ---/para a API--- #
]