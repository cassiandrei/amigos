# coding=utf-8

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^list$', views.list_friends, name='list'),
    url(r'^addfriend/(?P<id>\w+)$', views.addfriend, name='addfriend'),
    url(r'^friendships$', views.list_solicitations, name='list_solicitations'),
]
