from django.contrib import admin
from transaction.models.transaction import Transaction, Book_Transaction

# Register your models here.
admin.site.register(Transaction)
admin.site.register(Book_Transaction)
