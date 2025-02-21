from django.urls import re_path
from apps.signaler.TrazabilidadTipoEspecie.consumers import ObjectConsumer

websocket_urlpatterns = [
    re_path(r'ws/objects/$', ObjectConsumer.as_asgi()),
]
