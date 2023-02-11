from django.test import TestCase
from account.tests.factories import UserFactory

from books.models.book import Book
from books.models.cart import Cart
from books.models.category import Category
from .factories import BookFactory, CategoryFactory


class BooksTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def create_book(self):
        user = UserFactory()
        category = CategoryFactory()
        book = Book.objects.create(
            name = "Livro Teste",
            quantity_pages = "100",
            cover_book = None,
            status_book = "Usado",
            author = "Autor Teste",
            note = "Está com a capa arranhada",
            year = "2010",
            price = "100",
            quantity = "2",
            synopsis = "Conta a história de alunos sofredores do IFRN do curso de ADS no Campus Pau dos Ferros",
            publishing_company = "IFRN",
            category = category,
            user = user,
        )
        return book
        
    def create_category(self):
        category = Category.objects.create(
           name = "Teste Categoria"
        )
        return category
    
    def create_cart(self):
        user = UserFactory()
        book = BookFactory()
        cart = Cart.objects.create(
            user = user,
            book = book
        )
        
        return cart
