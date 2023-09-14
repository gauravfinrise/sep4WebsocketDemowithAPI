

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import app.routing
from app.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
        app.routing.websocket_urlpatterns
        )
    )
})

# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket':URLRouter(
#         app.routing.websocket_urlpatterns
#         )
    
# })
