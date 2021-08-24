from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import ChatMessage
from django.urls import reverse
from django.views import View


class ChatView(View):
    def get(self, request):
        all_rooms = set(ChatMessage.objects.all(
        ).values_list('chatRoom', flat=True))
        my_rooms = set(ChatMessage.objects.filter(
            user=request.user.username).values_list('chatRoom', flat=True))
        return render(request, 'chat/index.html', {'rooms': all_rooms,
                      'my_rooms': my_rooms})

    def post(self, request):
        if request.POST:
            room_name = request.POST.get('room-name')
            return redirect(reverse('room', args=[room_name]))


class RoomView(View):
    def get(self, request, room_name):
        if request.user.is_authenticated:
            username = request.user.get_username()
            messages = ChatMessage.objects.filter(chatRoom=room_name)
            return render(request, 'chat/room.html', {'room_name': room_name,
                          'username': username, 'messages': messages})
        else:
            return HttpResponseRedirect('/accounts/login')
