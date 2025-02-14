from django.db import models
from .Tipo_Sensor import Tipo_Sensor
from .Configuracion import Configuracion
from apps.Trazabilidad.models.Bancal import Bancal

class Sensor(models.Model):
    fk_bancal = models.ForeignKey(Bancal,on_delete=models.SET_NULL,null=True)
    fk_tipo_sensor = models.ForeignKey(Tipo_Sensor,on_delete=models.SET_NULL,null=True)
    fk_configuracion = models.ForeignKey(Configuracion,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return str(self.fk_tipo_sensor) + str(self.fk_bancal)