from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    marca = models.CharField(max_length=30)

    def __str__(self):
        return self.nome