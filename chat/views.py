from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import ChatMessage


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    if request.user.is_authenticated:
        username = request.user.get_username()
        messages = ChatMessage.objects.filter(chatRoom=room_name)

        return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages':messages})
    else:
        return HttpResponseRedirect('/accounts/login')
