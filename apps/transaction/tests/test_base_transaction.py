import factory
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from books.tests.test_base_books import BookFactory
from account.tests.factories import UserFactory

from transaction.models.transaction import Transaction


class TransactionFactory(DjangoModelFactory):
    class Meta:
        model= Transaction
       
    vendedor = SubFactory(UserFactory)
    comprador = SubFactory(UserFactory)
    book = SubFactory(BookFactory)
    
    @factory.post_generation # pragma: no cover
    def book(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            # Passando uma lista de livros para tabela "livros"
            for book in extracted:
                self.book.add(book)