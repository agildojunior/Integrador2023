from django.test import TestCase
from books.tests.test_base_books import BookFactory, CartFactory, CategoryFactory

class BookTestModels(TestCase):
       
    def setUp(self):
        self.book = BookFactory()
        self.category = CategoryFactory()
        self.cart = CartFactory()

    #BOOK
    def test_book_str(self):
        print(self.book)
        self.assertEqual(str(self.book), self.book.name)
    
    def test_book_create(self):
        self.assertTrue(self.book.name)
        self.assertTrue(self.book.quantity_pages)
        self.assertTrue(self.book.status_book)
        self.assertTrue(self.book.author)
        self.assertTrue(self.book.note)
        self.assertTrue(self.book.year)
        self.assertTrue(self.book.price)
        self.assertTrue(self.book.quantity)
        self.assertTrue(self.book.synopsis)
        self.assertTrue(self.book.publishing_company)
        self.assertTrue(self.book.category)
        self.assertTrue(self.book.user)
            
    def test_book_fields_not_null(self):
        self.assertIsNotNone(self.book.name)
        self.assertIsNotNone(self.book.quantity_pages)
        self.assertIsNotNone(self.book.status_book)
        self.assertIsNotNone(self.book.author)
        self.assertIsNotNone(self.book.note)
        self.assertIsNotNone(self.book.year)
        self.assertIsNotNone(self.book.price)
        self.assertIsNotNone(self.book.quantity)
        self.assertIsNotNone(self.book.synopsis)
        self.assertIsNotNone(self.book.publishing_company)
        self.assertIsNotNone(self.book.category)
        self.assertIsNotNone(self.book.user)
        
    #CATEGORY
    def test_category_str(self):
        self.assertEqual(str(self.category), self.category.name)
    
    def test_category_create(self):
        self.assertTrue(self.category.name)
        
    def test_category_fields_not_null(self):
        self.assertIsNotNone(self.category.name)
        
    #CART    
    def test_cart_create(self):
        self.assertTrue(self.cart.user)
        self.assertTrue(self.cart.book)
        
    def test_cart_fields_not_null(self):
        self.assertIsNotNone(self.cart.user)
        self.assertIsNotNone(self.cart.book)
        
    