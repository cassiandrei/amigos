# coding=utf-8
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from accounts.models import User
from django.http import HttpResponseRedirect, HttpResponse
import requests
from core import facebook

class IndexView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'index.html'


index = IndexView.as_view()

#o botão chama essa url
#https://www.facebook.com/dialog/oauth?client_id=1625366447519489&redirect_uri=http://localhost:8000/oauth2/&scope=public_profile,email,user_about_me,user_actions.books,user_actions.music,user_actions.video,user_birthday,user_friends,user_likes

def oauth2(request):
    if request.GET.get('code'):
        code = request.GET['code']
        dic = facebook.get_token('http://localhost:8000/oauth2/', code)
        token = dic['access_token']
        return HttpResponse(token)
    else:
        return HttpResponseRedirect(facebook.url_to_login('http://localhost:8000/oauth2/'))