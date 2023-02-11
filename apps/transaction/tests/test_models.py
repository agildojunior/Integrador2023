from transaction.tests import test_base_transaction
from transaction.tests.factories import TransactionFactory

class TransactionTestModels(test_base_transaction.TransactionTestBase):
       
    def setUp(self):
        self.transaction = TransactionFactory()

    #TRANSACTION
    def test_transaction_create(self):
        self.assertTrue(self.transaction.comprador)
        self.assertTrue(self.transaction.vendedor)
        self.assertTrue(self.transaction.book)
        
    def test_category_fields_not_null(self):
        self.assertIsNotNone(self.transaction.comprador)
        self.assertIsNotNone(self.transaction.vendedor)
        self.assertIsNotNone(self.transaction.book)