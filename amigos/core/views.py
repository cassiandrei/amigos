# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import ContactForm
from accounts.models import User


class IndexView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'index.html'

index = IndexView.as_view()