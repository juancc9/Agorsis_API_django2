from django.db import models

class Configuracion(models.Model):
    tipo_cultivo = models.CharField(max_length=100)
    tipo_sensor = models.CharField(max_length=100)
    valor_min = models.FloatField()
    valor_max = models.FloatField()
    def __str__(self):
        return str(self.tipo_sensor) + str(self.tipo_cultivo)