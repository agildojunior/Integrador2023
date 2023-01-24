from django.contrib import admin
from django.urls import path, include
from apps.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.core.urls')),
    path('', views.inicio, name='inicio'),
]
