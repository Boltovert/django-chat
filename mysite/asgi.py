import os
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django_asgi_app = get_asgi_application()

import chat.routing

# Эта конфигурация корневой маршрутизации указывает что при подключении к
# серверу разработки каналов "ProtocolTypeRouter" идёт проверка типа соединения
# если соединение WebSocket(ws:// or wss://) то соединение будет передано
# в AuthMiddlewareStack. AuthMiddlewareStack заполнит область подключения ссылкой
# на текущего аутентификационного пользователя, далее соединение передаётся в URLRouter
# URLRouter обрабатывает HTTP-путь соединения, чтобы направить конкретному consumer
# на основе предоставленных url шаблонов
#
application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        )
    )
})
