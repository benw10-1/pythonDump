from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

from django.urls import path
from Room import consumer

websocket_urlPattern = [
    path("ws/session/<str:cid>/", consumer.BasicConsumer)
]

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(websocket_urlPattern)))
})