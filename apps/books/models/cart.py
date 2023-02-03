from django.db import models
from account.models import User

class Cart(models.Model):
    user = models.OneToOneField(
        User, verbose_name="Usuário", on_delete=models.SET_NULL, null=True
    )
    quantity_books = models.CharField(verbose_name="Quantidade", max_length=255, default=0)
    book = models.ManyToManyField("Book", through='Book_Cart')

