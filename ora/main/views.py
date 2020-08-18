from django.shortcuts import render, redirect
from .models import Text
from .forms import TextForm


def index(request):
    texts = Text.objects.order_by('-id')[:7]
    return render(request, 'main/index.html', {'title': 'General page', 'texts': texts})


def about(request):
    return render(request, 'main/about.html')


def publish(request):
    error = ''
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'ERROR'
    form = TextForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/publish.html', context)


def login(request):
    return render(request, 'main/login.html')

