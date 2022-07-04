from django.db import models

class Uf(models.Model):
    uf = models.CharField(max_length=2, blank=False, null=False)

    def __str__(self):
        return self.uf

class Cidade(models.Model):
    cidade = models.CharField(max_length=255, blank=False, null=False)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %s' % (self.cidade, self.uf)