from contextlib import redirect_stderr
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from appMain.models import Materia, Videos, Games, Atividades
from .forms import Edit_Games

@login_required(login_url='/accounts/login/')
def dashboard(request):
    return render(request, 'dashboard.html')
    
def escolas(request):
    return render(request, 'escolas.html')

def jogos(request):
    games = Games.objects.all()
    form = Edit_Games()
    if request.method == 'POST' :
        form = Edit_Games(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/dashboard/jogos/pendentes/')

    context = {'jogos':games, 'form':form}
    return render(request,'jogos-all.html', context)

def jogospendentes(request):
    games = Games.objects.all()
    form = Edit_Games()
    if request.method == 'POST' :
        form = Edit_Games(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/dashboard/jogos/pendentes/')

    context = {'jogos':games, 'form':form}
    return render(request,'jogos_pendente.html', context)

def jogosedit(request, id):
    games = Games.objects.get(id = id)
    materias = Materia.objects.all()
    form = Edit_Games(request.POST or None, instance=games)

    if form.is_valid():
        form.save()
        return redirect('/dashboard/jogos/')
    
    context = {'games':games,'materias': materias, 'form':form}
    return render(request, 'edit_games.html', context)
    