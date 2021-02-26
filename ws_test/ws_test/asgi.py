import os

import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path

from chat.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ws_test.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": URLRouter([
        re_path(r"", AsgiHandler()),
    ]),
    "websocket": URLRouter([
        re_path(r"chat", ChatConsumer.as_asgi())
    ])
})
