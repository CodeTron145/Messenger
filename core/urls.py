from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.start, name="start"),
    path('home/', views.home, name="home"),
    path('chat/', include('chat.urls')),
    path('', include('logio.urls')),
]