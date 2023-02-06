from django.db import models
from account.models.user import User
from books.models.book import Book

# Create your models here.
class Transaction(models.Model):
    timetable = models.DateTimeField(verbose_name="Horário", auto_now_add=True)
    vendedor = models.ForeignKey(User, related_name="Vendedor",verbose_name="Vendedor", on_delete=models.CASCADE)
    comprador = models.ForeignKey(User, related_name="Comprador", verbose_name="Comprador", on_delete=models.CASCADE)
    book = models.ManyToManyField(
        Book, through='Book_Transaction'
    )
    class Meta:
        app_label = 'transaction'
    
    
# Tabela auxiliar para relação de N pra N livros e transações
class Book_Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    quantity_books = models.CharField(verbose_name="Quantidade", max_length=255, default=0)

    class Meta:
        app_label = 'transaction'
