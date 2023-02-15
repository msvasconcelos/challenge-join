from django.db import models


class Alvo(models.Model):
    id = models.CharField(max_length=100)
    nome = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    data_expiracao = models.DateField()