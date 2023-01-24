from django.contrib import admin
from apps.books.models.book import Book, Book_Cart
from apps.books.models.category import Category
from apps.books.models.cart import Cart

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Book_Cart)
