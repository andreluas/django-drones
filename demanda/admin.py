from django.contrib import admin
from demanda.models import Demanda

class Demandas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'user', 'logradouro', 'cidade', 'uf', 'info_contato', 'status_finalizacao')
    list_display_links = ('id', 'descricao', 'user', 'logradouro', 'cidade', 'uf', 'info_contato', 'status_finalizacao')
    search_fields = ('descricao', 'user',)
    list_filter = ('descricao', 'user',)
    list_per_page = 10
    ordering = ('descricao',)

admin.site.register(Demanda, Demandas)