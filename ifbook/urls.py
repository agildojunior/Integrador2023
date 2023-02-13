from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ifbook/', include('books.urls')),
    path('', views.inicio, name='inicio'),
    path('api/books/', include('core.urls')), #rota da api
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
