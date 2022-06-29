from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from .models import ChannelSidebar




def mainpage(request):
    return render(request, 'chat/mainpage.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = RegisterForm()
    return render(request, 'chat/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('room', room_name='main')
    else:
        form = LoginForm()
    return render(request, 'chat/login.html', {'form': form})


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    sidebar_name = ChannelSidebar.objects.all()
    context = {
        'room_name': room_name,
        'sidebar_name': sidebar_name
    }
    return render(request, 'chat/room.html', context=context)

def get_chat(request):
    # chat = ChannelSidebar.objects.filter(id)
    return render(request, 'chat/room.html')
