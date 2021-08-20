from django.http.response import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    if request.user.is_authenticated:
        return render(request, 'chat/room.html', {
            'room_name': room_name
        })
    else:
        return HttpResponseRedirect('/accounts/login')