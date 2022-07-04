from django.contrib import admin
from endereco.models import Cidade, Uf

class Ufs(admin.ModelAdmin):
    list_display = ('id', 'uf')

class Cidades(admin.ModelAdmin):
    list_display = ('id', 'uf', 'cidade')

admin.site.register(Uf, Ufs)
admin.site.register(Cidade, Cidades) 