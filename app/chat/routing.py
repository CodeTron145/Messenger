from django.conf.urls import url, include

from . import consumers

websocket_urlpatterns = [
  url(r'^ws/(?P<room_name>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
]