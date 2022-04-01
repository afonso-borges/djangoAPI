from django.contrib import admin
from cadastro.models import Cliente

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'profissao')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 15

admin.site.register(Cliente, Clientes)