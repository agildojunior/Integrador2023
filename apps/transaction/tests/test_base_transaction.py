from django.test import TestCase
from account.tests.factories import UserFactory
from books.tests.factories import BookFactory

from transaction.models.transaction import Transaction


class TransactionTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def create_transaction(self):
        comprador = UserFactory()
        vendedor = UserFactory()
        book = BookFactory()
        transaction = Transaction.objects.create(
            comprador = comprador,
            vendedor = vendedor,
            book = book
        )
        return transaction