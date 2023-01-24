from django.contrib import admin
from apps.account.models.user import User
from apps.account.models.adress import Adress

# Register your models here.
admin.site.register(User)
admin.site.register(Adress)
