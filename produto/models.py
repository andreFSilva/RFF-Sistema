from django.db import models

class Produto(models.Model):
    produto_novo = models.CharField(max_length=100, unique=True)
    produto_usado = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField('preço',max_digits=7, decimal_places=2)
    data = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.produto_novo, self.produto_usado

