# from socketio_app.sockets import MyNamespace

# urlpatterns = [
#    ('^socket.io/',  MyNamespace.as_view('/my-namespace'))
# ]
# from django.urls import path
# from socketio_app.sockets import MyNamespace

# urlpatterns = [
#     # ...
#     path('', MyNamespace.as_view()),
#     # ...
# ]

from django.urls import re_path
from . import consumer

websocket_urlpatterns = [
    re_path('ws/socket-server/', consumer.EchoConsumer.as_asgi())
]