# coding=utf-8
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from accounts.models import User
from django.http import HttpResponseRedirect, HttpResponse
import requests

class IndexView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'index.html'


index = IndexView.as_view()

#o botão chama essa url
#https://www.facebook.com/dialog/oauth?client_id=1625366447519489&redirect_uri=http://localhost:8000/oauth2/&scope=public_profile,email,user_about_me,user_actions.books,user_actions.music,user_actions.video,user_birthday,user_friends,user_likes

def oauth2(request):
    if request.GET.get('code'):
        code = request.GET['code']
        return HttpResponseRedirect('https://graph.facebook.com/oauth/access_token?client_id=1625366447519489&redirect_uri=http://localhost:8000/oauth2/&client_secret=d94c27f2b5cf98b53a4b53488ace6161&code=' + code)
    elif request.GET.get('access_token'):
        dic = request.GET['access_token']
        #TODO dá um jeito de converten a string dic em um dicionario de verdade
        return HttpResponse(dic)