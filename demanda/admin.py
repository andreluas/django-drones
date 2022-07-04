from django.contrib import admin
from demanda.models import Cidade, Demanda, Uf

class Demandas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'user', 'logradouro', 'cidade', 'uf', 'info_contato', 'status_finalizacao')
    list_display_links = ('id', 'descricao', 'user', 'logradouro', 'cidade', 'uf', 'info_contato', 'status_finalizacao')
    search_fields = ('descricao', 'user',)
    list_filter = ('descricao', 'user',)
    list_per_page = 10
    ordering = ('descricao',)

class Ufs(admin.ModelAdmin):
    list_display = ('id', 'uf')

class Cidades(admin.ModelAdmin):
    list_display = ('id', 'uf', 'cidade')

admin.site.register(Demanda, Demandas)
admin.site.register(Uf, Ufs)
admin.site.register(Cidade, Cidades)