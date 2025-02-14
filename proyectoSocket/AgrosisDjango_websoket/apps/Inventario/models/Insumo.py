from django.db import models
from .Tipo_Insumo import Tipo_Insumo

class Insumo(models.Model):
    fk_tipo_insumo = models.ForeignKey(Tipo_Insumo, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    tipo_empacado = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    unidadMedida = models.CharField(max_length=10)

    def __str__(self):
        return self.tipo

    def save(self, *args, **kwargs):
        # Verificar si ya existe un Insumo con las mismas características
        insumo_existente = Insumo.objects.filter(
            fk_tipo_insumo=self.fk_tipo_insumo,
            precio=self.precio,
            tipo_empacado=self.tipo_empacado,
            tipo=self.tipo,
            unidadMedida=self.unidadMedida,
        ).first()
        
        if insumo_existente:
            # Si existe, solo actualizamos la cantidad
            insumo_existente.cantidad += self.cantidad
            insumo_existente.save()
        else:
            # Si no existe, creamos un nuevo registro
            super().save(*args, **kwargs)
