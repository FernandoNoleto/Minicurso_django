from django.db import models

# Create your models here.

class Sabor(models.Model):
    nome = models.CharField(max_length = 255)
    descricao = models.TextField()

    def __str__(self):
        return "{}".format(self.nome)

class Bolo(models.Model):
    nome = models.CharField(max_length = 255)
    sabor = models.ForeignKey(Sabor, on_delete = models.CASCADE)
    peso = models.FloatField()
    preco = models.FloatField()
