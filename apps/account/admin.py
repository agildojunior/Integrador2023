from django.contrib import admin
from account.models.user import User
from account.models.adress import Adress

# Register your models here.
admin.site.register(User)
admin.site.register(Adress)
