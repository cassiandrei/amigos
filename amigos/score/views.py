from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.models import Match, User
from .models import Friendship
from django.contrib import messages
from django.shortcuts import redirect
from accounts.models import *

# Create your views here.
@login_required
def list_friends(request):
    matches = Match.objects.calc_points(user=request.user)
    context = {'matches': matches}
    return render(request, 'score/list_friends.html', context)

@login_required
def addfriend(request, id):
    friend = User.objects.get(id=id)
    Friendship.objects.get_or_create(user_id=request.user.id, friend=friend)
    messages.success(request, 'Solicitação enviada com sucesso')
    return redirect('index')

@login_required
def list_solicitations(request):
    list = Friendship.objects.filter(friend=request.user)
    solicitations = []
    user_books = BookUser.objects.filter(user=request.user)
    user_music = MusicUser.objects.filter(user=request.user)
    user_games = GameUser.objects.filter(user=request.user)
    user_videos = VideoUser.objects.filter(user=request.user)
    for solicitation in list:
        itens = []
        match_books = BookUser.objects.filter(user=solicitation.user_id)
        for a in user_books:
            for b in match_books:
                if a.book.id == b.book.id:
                    itens.append(a.book.name)
        
        match_videos = VideoUser.objects.filter(user=solicitation.user_id)
        for a in user_videos:
            for b in match_videos:
                if a.video.id == b.video.id:
                    itens.append(a.video.name)
        
        match_games = GameUser.objects.filter(user=solicitation.user_id)
        for a in user_games:
            for b in match_games:
                if a.game.id == b.game.id:
                    itens.append(a.game.name)
        
        match_music = MusicUser.objects.filter(user=solicitation.user_id)
        for a in user_music:
            for b in match_music:
                if a.music.id == b.music.id:
                    itens.append(a.music.name)
        solicitations.append([User.objects.get(id=solicitation.user_id), " | ".join(itens)])

    context = {'list_friendships': solicitations}
    return render(request, 'score/friendships.html', context)

