from django.shortcuts import render
from .models import Text


def index(request):
    texts = Text.objects.all()
    return render(request, 'main/index.html', {'title': 'General page', 'texts': texts})


def about(request):
    return render(request, 'main/about.html')

