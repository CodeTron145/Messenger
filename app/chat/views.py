from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
TEMPLATES = Path(BASE / "templates")

from .models import Message

@login_required()
def rooms(request):
	rooms_list = Message.objects.values('room').distinct().order_by()
	return render(request, 'chat/rooms.html', {'rooms': rooms_list})

@login_required()
def room(request, room_name):
	messages = Message.objects.filter(room=room_name)
	return render(request, 'chat/room.html', {'roomname': room_name,  
											  'messages': messages})