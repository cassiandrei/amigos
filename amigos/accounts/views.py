# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import (TemplateView, UpdateView, FormView)
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from .models import User
from .forms import UserAdminCreationForm
from django.contrib import messages


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'


def perfil(request):
    return render(request, 'accounts/perfil/perfil.html')


def register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso')
            return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)


index = IndexView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()
