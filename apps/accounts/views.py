from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from django.views.generic import View
from django.contrib.auth import login

from .forms import AccountCreateForm

User = get_user_model()

class LoginAccountView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/'

class LogoutAccountView(LogoutView):
    next_page = '/'

class RegisterAccountView(View):
    def get(self, request, *args, **kwargs):
        form = AccountCreateForm()
        context = {
            'form': form
        }
        return render(request, 'registration/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = AccountCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('home')