# coding=utf-8
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from accounts.models import User
from django.http import HttpResponseRedirect, HttpResponse
import requests
from core import facebook
from core import user_config
from django.contrib.auth import login
import json

class IndexView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'index.html'

index = IndexView.as_view()

def inicial(request):
    user = User.objects.all()
    print('oi')
    for u in user:
        print(u.name)

    return render(request, 'inicial.html')

def oauth2(request):
    if request.GET.get('code'):
        code = request.GET['code']
        dic = facebook.get_token('http://localhost:8000/oauth2/', code)
        token = dic['access_token']
        user_config.checkUser(token)
        user = User.objects.get(token_api=token)
        login(request, user)
        return redirect('index')
    else:
        return HttpResponseRedirect(facebook.url_to_login('http://localhost:8000/oauth2/'))

def index(request):
    return redirect('score/list')

