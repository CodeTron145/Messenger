from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
TEMPLATES = Path(BASE / "templates")


def startPage(request):
    return render(request, "base.html")


@login_required()
def home(request):
    return render(request, "home.html")