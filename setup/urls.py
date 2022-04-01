from django.contrib import admin
from django.urls import path, include
from cadastro.views import ClientesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Clientes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
