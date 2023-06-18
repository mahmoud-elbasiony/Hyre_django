"""
ASGI config for Hyre project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hyre.settings')

# application = get_asgi_application()

from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from socketio_app import urls
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    'websocket':AuthMiddlewareStack( URLRouter(urls.websocket_urlpatterns))
})  

