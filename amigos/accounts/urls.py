# coding=utf-8

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^alterar-dados/$', views.update_user, name='update_user'),
    url(r'^alterar-senha/$', views.update_password, name='update_password'),
    url(r'^registro/$', views.register, name='register'),
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^friend_perfil/(?P<id>\w+)/$', views.friend_perfil, name='friend_perfil'),
]
