"""
ASGI config for Tictactoe project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack
from django.conf.urls import url

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tictactoe.settings')

application = get_asgi_application()

ws_pattern = []

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(URLRouter(
        ws_pattern
    ))
})
