from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=255)

    def __str__(self):
        return self.name

