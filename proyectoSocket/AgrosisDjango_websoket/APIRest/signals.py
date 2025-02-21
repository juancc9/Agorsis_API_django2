import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.Trazabilidad.models import Tipo_Especie
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

logger = logging.getLogger(__name__)

MY_CONSTANT = "Esta es una constante"

@receiver(post_save, sender=Tipo_Especie)
def notificar_nuevo_objeto(sender, instance, created, **kwargs):
    try:
        message = f"Señal recibida: Objeto {'creado' if created else 'actualizado'} {instance}"
        logger.info(message)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "objects_group",
            {
                "type": "nuevo_objeto",
                "message": f"Objeto {'creado' if created else 'actualizado'}: {instance}"
            }
        )
    except Exception as e:
        logger.error(f"Error al enviar el mensaje: {e}")

