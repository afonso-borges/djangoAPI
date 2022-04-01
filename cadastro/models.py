from doctest import testfile, testsource
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=35)
    email = models.EmailField(blank=False, max_length=35, )
    telefone = models.CharField(max_length=14)
    endereço_completo = models.CharField(max_length=200)
    profissao = models.CharField(max_length=35)
    curriculo_upload = models.FileField(upload_to='curriculos/%d/%m/%Y/', blank=True, null=True)

    def __str__(self):
        return self.nome