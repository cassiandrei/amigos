# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import (TemplateView, UpdateView, FormView)
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from .models import User
from .forms import UserAdminCreationForm
from django.contrib import messages
from accounts.models import BookUser, GameUser, VideoUser, MusicUser


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'


def perfil(request):
    books = []
    games = []
    videos = []
    musics = []
    for i in BookUser.objects.filter(user=request.user):
        n = BookUser.objects.filter(book_id=i.id).count()
        books.append([i.book, n-1])
    for i in GameUser.objects.filter(user=request.user):
        n = GameUser.objects.filter(game_id=i.id).count()
        games.append([i.game,n-1])
    for i in VideoUser.objects.filter(user=request.user):
        n = VideoUser.objects.filter(video_id=i.id).count()
        videos.append([i.video,n-1])
    for i in MusicUser.objects.filter(user=request.user):
        n = MusicUser.objects.filter(music_id=i.id).count()
        musics.append([i.music,n-1])
    return render(request, 'accounts/perfil/perfil.html', {'books': books,'games': games,'videos':videos,'musics':musics})


def friend_perfil(request, id):
    user = User.objects.get(id=id)
    books = []
    games = []
    videos = []
    musics = []
    for i in BookUser.objects.filter(user=user):
        n = BookUser.objects.filter(book_id=i.id).count()
        books.append([i.book, n - 1])
    for i in GameUser.objects.filter(user=user):
        n = GameUser.objects.filter(game_id=i.id).count()
        games.append([i.game, n - 1])
    for i in VideoUser.objects.filter(user=user):
        n = VideoUser.objects.filter(video_id=i.id).count()
        videos.append([i.video, n - 1])
    for i in MusicUser.objects.filter(user=user):
        n = MusicUser.objects.filter(music_id=i.id).count()
        musics.append([i.music, n - 1])
    return render(request, 'accounts/perfil/perfil.html',
                  {'books': books, 'games': games, 'videos': videos, 'musics': musics, 'user': user})


def register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso')
            return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)


index = IndexView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()
