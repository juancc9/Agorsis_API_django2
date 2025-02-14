from django.urls import re_path
from .. import consumers

websocket_urlpatterns = [
    re_path(r'ws/objects/', consumers.ObjectConsumer.as_asgi()),
]
