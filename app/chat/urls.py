from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.rooms, name='rooms'),
	path('<str:room_name>/', views.room, name='room'),
]
