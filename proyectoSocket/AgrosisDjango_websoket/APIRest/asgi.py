import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from APIRest.consumers import ObjectConsumer  # Asegúrate de que esta ruta sea correcta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'APIRest.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/objects/", ObjectConsumer.as_asgi()),  # Asegúrate de que esta ruta sea correcta
        ])
    ),
})
