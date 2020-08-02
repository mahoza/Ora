from django.shortcuts import render
from .models import Text


def index(request):
    texts = Text.objects.order_by('-id')[:7]
    return render(request, 'main/index.html', {'title': 'General page', 'texts': texts})


def about(request):
    return render(request, 'main/about.html')


def publish(request):
    return render(request, 'main/publish.html')


