from django.urls import path
from chat.views import ChatView, RoomView

urlpatterns = [
    path('', ChatView.as_view(), name='chat'),
    path('<str:room_name>/', RoomView.as_view(), name='room'),
]
