from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(
        verbose_name="Nome", max_length=255, null=False, blank=False
    )
    username = models.CharField(verbose_name="Username", max_length=25, unique=True)
    email = models.EmailField(
        verbose_name="E-mail", max_length=255, null=False, blank=False
    )
    balance = models.CharField(verbose_name="Saldo", max_length=255)
    phone = models.CharField(
        verbose_name="Telefone", max_length=50, null=False, blank=False
    )

    is_staff = models.BooleanField(verbose_name="Administrador", default=False)
    is_active = models.BooleanField(verbose_name="Ativo", default=True)
    date_joined = models.DateTimeField(
        verbose_name="Data de Entrada", auto_now_add=True
    )

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
