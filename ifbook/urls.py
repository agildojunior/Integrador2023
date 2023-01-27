from django.contrib import admin
from django.urls import path, include
from apps.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ifbook/', include('apps.books.urls')),
    path('', views.inicio, name='inicio'),
]
