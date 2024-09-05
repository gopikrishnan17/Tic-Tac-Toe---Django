from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
    # path('/ws/game_multi/<room_code>' , consumers.GameRoom.as_asgi()),
    re_path(r"ws/game_multi/(?P<room_code>\w+)$", consumers.GameRoom.as_asgi()),
    # re_path(r"ws/game_multi/.*", consumers.GameRoom.as_asgi()),

]