from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.Trazabilidad.models import Tipo_Especie
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Si no usas `json` directamente aquí, puedes eliminar esta línea:
# import json

@receiver(post_save, sender=Tipo_Especie)
def notificar_nuevo_objeto(sender, instance, created, **kwargs):
    if created:
        print(f"Señal recibida: Nuevo objeto creado {instance}")
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "objects_group",
            {
                "type": "nuevo_objeto",
                "message": f"Nuevo objeto creado: {instance}"
            }
        )
