from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from pathlib import Path
from .models import Message

BASE = Path(__file__).resolve().parent.parent
TEMPLATES = Path(BASE / "templates")


@login_required()
def rooms(request):
    rooms_list = Message.objects.values('room').distinct().order_by()
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'chat/rooms.html', {'users': users, 'rooms': rooms_list})


@login_required()
def room(request, room_name):
    messages = Message.objects.filter(room=room_name)
    return render(request, 'chat/room.html', {'roomname': room_name,
                                              'messages': messages})
