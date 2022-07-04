from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from endereco.models import Uf, Cidade

class Demanda(models.Model):
    STATUS = (
        ('A', 'Aberta'),
        ('F', 'Finalizada'),
    )
    descricao = models.CharField(max_length=255, blank=False, null=False)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=255, blank=False, null=False)
    info_contato = models.CharField(max_length=255, blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS, blank=False, null=False, default='A')
    user = models.ForeignKey('auth.User', related_name='demandas', on_delete=models.CASCADE)
    
    def status_finalizacao(self):
        if self.status == 'A':
            return mark_safe('<img src="/static/status_open.png" width="30" />')
        else:
            return mark_safe('<img src="/static/status_close.png" width="30" />')
    status_finalizacao.short_description = "Status de Finalização"
    status_finalizacao.allow_tags = True

    def __str__(self):
        return '%s: %s: %s: %s' % (self.descricao, self.uf, self.cidade, self.logradouro, self.info_contato, self.status)