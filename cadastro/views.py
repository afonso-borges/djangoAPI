from rest_framework import viewsets
from cadastro.models import Cliente
from cadastro.serializer import ClienteSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

class ClientesViewSet(viewsets.ModelViewSet):
    #Exibindo todos os clientes
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_clasess = [BasicAuthentication]
    permission_classes = [IsAuthenticated]