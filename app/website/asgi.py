# """
# ASGI config for website project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
# """

import os
import django
from django.core.asgi import get_asgi_application

django_asgi_app = get_asgi_application()

import chat.routing
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()
application = ProtocolTypeRouter({
  "http": django_asgi_app,
  "websocket": AuthMiddlewareStack(
    URLRouter(
      chat.routing.websocket_urlpatterns
    )
  )
})

# import os
# import django
# from channels.routing import get_default_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
# django.setup()
# application = get_default_application()