import factory
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from books.tests.factories import BookFactory
from account.tests.factories import UserFactory

from transaction.models.transaction import Transaction


class TransactionFactory(DjangoModelFactory):
    class Meta:
        model= Transaction
       
    vendedor = SubFactory(UserFactory)
    comprador = SubFactory(UserFactory)
    book = SubFactory(BookFactory)
    
    @factory.post_generation
    def book(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            # Estamos passando uma lista de autores para o livro
            for book in extracted:
                self.book.add(book)