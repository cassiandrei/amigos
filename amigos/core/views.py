# coding=utf-8
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView
from accounts.models import User


def index(request):
    return redirect('score/list')
