from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.LoginAccountView.as_view(), name='login'),
    path('logout/', views.LogoutAccountView.as_view(), name='logout'),
    path('registration/', views.RegisterAccountView.as_view(), name='register'),
]