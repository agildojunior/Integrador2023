from django.contrib import admin
from django.urls import path, include
from loginRegistro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('loginRegistro.urls')),
    path('', views.inicio, name='inicio'),
]
