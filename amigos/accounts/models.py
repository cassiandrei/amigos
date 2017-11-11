# coding=utf-8

import re

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
    email = models.EmailField('E-mail', unique=True, blank=True, null=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    # Token facebook
    token_api = models.CharField('Token', max_length=300, null=False)

    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]

# Relacoes entre amigos
class Match(models.Model):
    points = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"

# Tabelas dos gostos
class Books(models.Model):
    id_api = models.IntegerField()
    name = models.CharField('Nome', max_length=300, null=False)

class Games(models.Model):
    id_api = models.IntegerField()
    name = models.CharField('Nome', max_length=300, null=False)

class Musics(models.Model):
    id_api = models.IntegerField()
    name = models.CharField('Nome', max_length=300, null=False)

class Videos(models.Model):
    id_api = models.IntegerField()
    name = models.CharField('Nome', max_length=300, null=False)

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

