from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


class LoginAccountView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/'

class LogoutAccountView(LogoutView):
    next_page = '/'