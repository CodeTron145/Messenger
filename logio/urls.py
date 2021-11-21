from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.loginToAcc, name="login"),
    path("logout/", views.logoutFromAcc, name="logout"),
    path("signup/", views.signup, name="signup")
]
