from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter

from django.core.asgi import get_asgi_application

import os

import messenger.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SubChat.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    "websocket": URLRouter(messenger.routing.websocket_urlpatterns),
})
