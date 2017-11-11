# coding=utf-8
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.models import User
from django.http import HttpResponseRedirect, HttpResponse
import requests
from core import facebook
from core import user_config
import json

class IndexView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'index.html'

index = IndexView.as_view()

def inicial(request):
    return render(request, 'inicial.html')

def oauth2(request):
    if request.GET.get('code'):
        code = request.GET['code']
        dic = facebook.get_token('http://localhost:8000/oauth2/', code)
        token = dic['access_token']
        #return HttpResponse(token)
        #user_config.checkUser(token)
        #return HttpResponse(json.dumps(facebook.get_user_info(token)))
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect(facebook.url_to_login('http://localhost:8000/oauth2/'))