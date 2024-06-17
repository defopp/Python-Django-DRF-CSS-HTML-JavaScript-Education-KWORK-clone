from django.urls import re_path

from .consumers import ChatConsumer
# from . import consumers.ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/socket-server/', ChatConsumer.as_asgi())
]