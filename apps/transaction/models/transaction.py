from django.db import models
from apps.account.models.user import User
from apps.books.models.book import Book

# Create your models here.
class Transaction(models.Model):
    STATUS_CHOICES = (
        ("1", "Compra"),
        ("2", "Venda"),
    )
    timetable = models.DateTimeField(verbose_name="Horário", auto_now_add=True)
    type = models.CharField(
        verbose_name="Tipo",
        max_length=1,
        choices=STATUS_CHOICES,
        blank=False,
        null=False,
    )
    user = models.ForeignKey(User, verbose_name="Vendedor", on_delete=models.CASCADE)
    books = models.ManyToManyField(
        Book, verbose_name="book", blank=True
    )

    def __str__(self):
        return self.type
    
    
# Tabela auxiliar para relação de N pra N livros e transações
class Book_Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    quantity_books = models.CharField(verbose_name="Quantidade", max_length=255, default=0)

