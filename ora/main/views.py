from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #log the user in
            login(request, user)
            return redirect('articles:list')
    else:
        form= UserCreationForm()
    return render(request, 'main/signup.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user=form.get_user()
            login(request, user)
            return redirect('articles:list')
    else:
        form= AuthenticationForm()
    return render(request, 'main/login.html', {'form':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')


