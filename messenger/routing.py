from django.urls import path

from messenger.consumers import MessageCreateConsumer

websocket_urlpatterns = [
    path('ws/new-message/', MessageCreateConsumer.as_asgi()),
]
