from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.models import Match, User
from .models import Friendship
from django.contrib import messages
from django.shortcuts import redirect

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
    for solicitation in list:
        solicitations.append(User.objects.get(id=solicitation.user_id))
    context = {'list_friendships': solicitations}
    return render(request, 'score/friendships.html', context)

@login_required
def accept(request, id):
    friendship = Friendship.objects.get(user_id=id, friend=request.user)
    friendship.accept = True
    friendship.save()
    messages.success(request, 'Convite aceito com sucesso')
