# coding=utf-8

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^list$', views.list_friends, name='list'),
]
