# coding=utf-8

import re

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Apelido / Usuário', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
            )
        ], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )
    name = models.CharField('Nome', max_length=100, blank=True)
    email = models.EmailField('E-mail', unique=True)
    fb_id = models.IntegerField('fb_id', unique=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)
    link = models.CharField(verbose_name='Link', max_length=300, default='')

    picture = models.CharField(verbose_name='Picture', max_length=300, default='https://openclipart.org/image/2400px/svg_to_png/211821/matt-icons_preferences-desktop-personal.png')
    cover = models.CharField(verbose_name='Cover', max_length=300, default='https://jornalismoespecializadounesp.files.wordpress.com/2014/04/capas-para-facebook-capa-facebook-777366.jpg')
    # Token facebook
    token_api = models.CharField('Token', max_length=300, null=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        unique_together = ['id', 'token_api']

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]


class MatchManager(models.Manager):
    def getcreate(self, user, match):
        try:
            match = Match.objects.get(user_id=user.id, match=match)
        except ObjectDoesNotExist:
            match = Match.objects.create(user_id=user.id, match=match)
        return match

    def calc_points(self, user):
        print("[LOG] Calculando afinidades...")
        all_users = User.objects.all()
        user_books = BookUser.objects.filter(user=user)
        user_music = MusicUser.objects.filter(user=user)
        user_games = GameUser.objects.filter(user=user)
        user_videos = VideoUser.objects.filter(user=user)
        for current_user in all_users:
            if current_user.id != user.id:
                match = self.getcreate(user=user, match=current_user)
                match.points = 0
                total_points = 0

                match_books = BookUser.objects.filter(user=current_user)
                total_points += user_books.count()
                for a in user_books:
                    for b in match_books:
                        if a.book.id == b.book.id:
                            match.points += 1
                
                match_videos = VideoUser.objects.filter(user=current_user)
                total_points += user_videos.count()
                for a in user_videos:
                    for b in match_videos:
                        if a.video.id == b.video.id:
                            match.points += 1
                
                match_games = GameUser.objects.filter(user=current_user)
                total_points += user_games.count()
                for a in user_games:
                    for b in match_games:
                        if a.game.id == b.game.id:
                            match.points += 1
                
                match_music = MusicUser.objects.filter(user=current_user)
                total_points += user_music.count()
                for a in user_music:
                    for b in match_music:
                        if a.music.id == b.music.id:
                            match.points += 1
                
                match.points = match.points * 100 // total_points
                match.save()                

        total_matches = Match.objects.filter(user_id=user.id)
        print("[LOG] Afinidades calculadas.")
        return total_matches


# Relacoes entre amigos
class Match(models.Model):
    points = models.IntegerField(default=0)
    user_id = models.IntegerField(null=False)
    match = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"
        ordering = ['-points']
        unique_together = ['user_id', 'match']

    objects = MatchManager()


# Tabelas dos gostos
class Books(models.Model):
    id_api = models.IntegerField(unique=True)
    name = models.CharField('Nome', max_length=300, null=False)

    def __str__(self):
        return self.name


class Games(models.Model):
    id_api = models.IntegerField(unique=True)
    name = models.CharField('Nome', max_length=300, null=False)
    def __str__(self):
        return self.name

class Musics(models.Model):
    id_api = models.IntegerField(unique=True)
    name = models.CharField('Nome', max_length=300, null=False)
    def __str__(self):
        return self.name

class Videos(models.Model):
    id_api = models.IntegerField(unique=True)
    name = models.CharField('Nome', max_length=300, null=False)
    def __str__(self):
        return self.name

# Relações NxN
class VideoUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)


class GameUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)


class BookUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

class MusicUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(Musics, on_delete=models.CASCADE)
