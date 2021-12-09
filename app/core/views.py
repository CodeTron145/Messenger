from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
TEMPLATES = Path(BASE / "templates")


def start(request):
    return render(request, "start.html")


@login_required()
def home(request):
    return redirect("/chat/")
