import factory
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from books.models.book import Book
from books.models.category import Category
from books.models.cart import Cart

from account.tests.factories import UserFactory

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model= Category
        
    name = Faker("word")

class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    name = Faker("name")
    quantity_pages = Faker("building_number")
    status_book = Faker("random_element", elements=(
            "Novo", "Usado", "Seminovo"
        ))
    book_cover = None
    author = Faker("name")
    note = Faker("text")
    year = Faker("year")
    price = Faker("building_number")
    quantity = Faker("building_number")
    synopsis = Faker("text")
    publishing_company = Faker("name")
    category = SubFactory(CategoryFactory)
    user = SubFactory(UserFactory)
    
class CartFactory(DjangoModelFactory):
    class Meta:
        model = Cart
        
    user = SubFactory(UserFactory)
    book = SubFactory(BookFactory)
    
    @factory.post_generation
    def book(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            # Estamos passando uma lista de autores para o livro
            for book in extracted:
                self.book.add(book)