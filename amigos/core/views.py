# coding=utf-8
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from accounts.models import User


class IndexView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'index.html'


index = IndexView.as_view()
