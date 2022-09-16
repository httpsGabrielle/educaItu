from django.shortcuts import render
from .models import Videos, Games, Atividades

def base(request):
    return render(request, 'base.html')
    
def home(request): 
    videos = Videos.objects.all()
    return render(request, 'home.html')

def tarefas(request): 
    return render(request, 'tarefas.html')

def videos(request): 
    videos = Videos.objects.all()
    return render(request,'videosroom.html',{'videos':videos})

def games(request): 
    games = Games.objects.all()
    return render(request,'gameroom.html',{'games':games})

def atividades(request): 
    atividades = Atividades.objects.all()
    return render(request,'taskroom.html',{'atividades':atividades})