from django.shortcuts import render, redirect
from .models import Text
from .forms import TextForm


def index(request):
    texts = Text.objects.order_by('-id')[:7]
    return render(request, 'main/index.html', {'title': 'General page', 'texts': texts})


def about(request):
    return render(request, 'main/about.html')


def publish(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
    form = TextForm()
    context = {
        'form': form,
    }
    return render(request, 'main/publish.html', context)


