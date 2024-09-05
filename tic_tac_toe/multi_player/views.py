from django.shortcuts import render, redirect
from django.contrib import messages
import uuid
from .models import *

def createroom(request):
    room_code = uuid.uuid4().hex[:8]
    context = {'room_code': room_code}
    if request.method == 'POST':
        room_code = request.POST.get('room_code')
        game_creator = request.POST.get('player_name')
        game = Game.objects.create(
            room_code = request.POST.get('room_code'),
            game_creator = request.POST.get('player_name')
        )
        game.save()
        return redirect('/play_multi/' + room_code + '?username='+game_creator)
    return render(request, 'createroom.html', context)

def joinroom(request):
    if request.method == "POST":
        room_code = request.POST.get('room_code')
        game_opponent = request.POST.get('player_name')

        game = Game.objects.filter(room_code = room_code).first()
        print(game)
        if game is None:
            messages.success(request, "Room code not found")
            return redirect('/joinroom/')
        
        elif game.is_over:
            messages.success(request, "Game Finished, please enter another room")
            return redirect('/joinroom/')
        
        else:
            game.game_opponent = game_opponent
            game.save()
            return redirect('/play_multi/' + room_code + '?username='+game_opponent)    
    return render(request, 'joinroom.html')

def play_multi(request, room_code):
    username = request.GET.get('username')
    game = Game.objects.filter(room_code = room_code).first()
    context = {'room_code': room_code, 'username': username, 'player1_name': game.game_creator, 'player2_name':game.game_opponent}
    return render(request, 'newmatchlogic.html', context)