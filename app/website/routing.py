from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.consumers 
from django.urls import url

application = ProtocolTypeRouter({
  "websocket": AuthMiddlewareStack(
    URLRouter(
      url(r'^ws/(?P<room_name>[^/]+)/$', chat.consumers.ChatConsumer.as_asgi())
    )
  )
})